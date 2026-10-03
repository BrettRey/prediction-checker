#!/usr/bin/env python3
"""Case 2 outcomes: CRTC series against the Nordicity/Miller forecast.

Follows notes/analysis-plan.md (case 2), committed before any CRTC file was
opened. Choices made after the data were seen are marked [post hoc] here and in
DECISIONS.md.

Inputs (data/raw/crtc/, gitignored; Open Government Licence - Canada):
  sfs2016_discretionary_ondemand.xlsx  2012-2016, vintage published with 2016 summaries
  sfs2020_discretionary_ondemand.xlsx  2016-2020, vintage published with 2020 summaries
  sfs2016_distribution.xlsx, sfs2020_distribution.xlsx  BDU summaries, same vintages
  data/derived/nordicity_2015_scenarios.csv  the forecast (extracted from the report)

Outputs
  data/derived/crtc_lttv_outcomes.csv    observed series used
  data/derived/crtc_lttv_k_estimates.csv k by quantity, series version and sigma
  notes/results-lttv.md                  generated tables (do not edit by hand)
"""
import csv
import math
import warnings
from pathlib import Path

import numpy as np
import openpyxl

from plan_constants import (CITED_CLOSURES_HIGH_MULT, CITED_UPTAKE_HIGH, CITED_UPTAKE_LOW,
                            MORRISON_UPTAKE_ESTIMATE, REPORT_UPTAKE_2018, SPLICE_TOLERANCE)

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "crtc"
DER = ROOT / "data" / "derived"
YEARS = [2016, 2017, 2018, 2019]
SIGMAS = [0.01, 0.02, 0.03, 0.05, 0.08]


def sheet_series(path, sheet, label):
    """Year -> value for the row whose first non-empty cell is `label`."""
    ws = openpyxl.load_workbook(path, read_only=True, data_only=True)[sheet]
    rows = list(ws.iter_rows(values_only=True))
    years = None
    for r in rows:
        cells = list(r)
        if years is None and any(str(c).strip().isdigit() and len(str(c).strip()) == 4 for c in cells if c is not None):
            years = {i: int(str(c).strip()) for i, c in enumerate(cells)
                     if c is not None and str(c).strip().isdigit() and len(str(c).strip()) == 4}
            continue
        first = next((c for c in cells if c is not None), None)
        if years and isinstance(first, str) and first.strip() == label:
            out = {}
            for i, yr in years.items():
                v = cells[i] if i < len(cells) else None
                if isinstance(v, str):
                    v = v.replace(",", "").strip()
                    v = float(v) if v.replace(".", "").replace("-", "").isdigit() else None
                if v is not None:
                    out[yr] = float(v)
            return out
    raise KeyError(f"{path.name}[{sheet}]: no row '{label}'")


def observed():
    d16, d20 = RAW / "sfs2016_discretionary_ondemand.xlsx", RAW / "sfs2020_discretionary_ondemand.xlsx"
    b16, b20 = RAW / "sfs2016_distribution.xlsx", RAW / "sfs2020_distribution.xlsx"
    # Discretionary and on-demand, total revenue ($). 2012-2015 from the 2016
    # vintage, 2016-2020 from the 2020 vintage (latest revisions).
    dod = {**sheet_series(d16, "1", "Total Revenue"), **sheet_series(d20, "1", "Total Revenue")}
    # [post hoc] Exempt services began filing in 2016 (units 228 -> 307); remove
    # them so the scope matches 2012-2015. Sheet 10 of the 2020 vintage.
    exempt = sheet_series(d20, "10", "Total Revenue")
    dod_ex = {y: v - exempt.get(y, 0.0) for y, v in dod.items()}
    # BDU basic and non-basic, total revenue ($000).
    bdu = {**sheet_series(b16, "1", "Total Revenue"), **sheet_series(b20, "1", "Total Revenue")}
    # [post hoc] BDU affiliation payments ($000): wholesale fees paid to programmers.
    aff = {**sheet_series(b16, "1", "Affiliation Payments"), **sheet_series(b20, "1", "Affiliation Payments")}
    subs = {**sheet_series(b16, "1", "Subscribers"), **sheet_series(b20, "1", "Total Subscribers")}
    to_m = lambda s, f: {y: v / f for y, v in s.items()}
    return dict(
        specialty_pay_revenue=to_m(dod_ex, 1e6),
        specialty_pay_revenue_incl_exempt=to_m(dod, 1e6),
        bdu_revenue=to_m(bdu, 1e3),
        bdu_affiliation_payments=to_m(aff, 1e3),
        bdu_subscribers_thousands=to_m(subs, 1e3),
    )


def forecast():
    rows = list(csv.DictReader(open(DER / "nordicity_2015_scenarios.csv")))
    f = {}
    for r in rows:
        f[(r["quantity"], int(r["year"]))] = dict(
            B=float(r["baseline_level"]), L=float(r["lttv_level"]), I=float(r["impact_total"]),
            **{k: float(r[k]) if r[k] not in ("", None) else 0.0
               for k in ("unbundling", "preponderance_access", "exemption_order", "closures")})
    return f


def scen_impact(fc, q, yr, mult):
    d = fc[(q, yr)]
    return sum(d[k] * mult[k] for k in ("unbundling", "preponderance_access", "exemption_order", "closures"))


# Same input scenarios as scripts/design_analysis_lttv.py (cited ranges).
LOW = dict(unbundling=CITED_UPTAKE_LOW / REPORT_UPTAKE_2018, preponderance_access=CITED_UPTAKE_LOW / REPORT_UPTAKE_2018,
           exemption_order=1, closures=1)
HIGH = dict(unbundling=CITED_UPTAKE_HIGH / REPORT_UPTAKE_2018, preponderance_access=CITED_UPTAKE_HIGH / REPORT_UPTAKE_2018,
            exemption_order=1, closures=CITED_CLOSURES_HIGH_MULT)


def gls_k(y, delta, sigma):
    h = np.array([t - 2014 for t in YEARS], dtype=float)
    P = np.linalg.inv(sigma ** 2 * np.minimum.outer(h, h))
    info = delta @ P @ delta
    k = (delta @ P @ y) / info
    return k, 1 / math.sqrt(info), P, info


def verdict(lo, hi, band_lo, band_hi):
    if lo <= 0 <= hi and lo <= band_lo <= hi:
        return "inconclusive"
    if hi < band_lo:
        return "smaller than the forecasters' inputs imply" + (" (no detectable effect)" if lo <= 0 <= hi else "")
    if lo > band_hi:
        return "forecast exceeded"
    return "consistent with the forecast range" + (" (includes k = 1)" if lo <= 1 <= hi else " (excludes k = 1)")


def main():
    obs = observed()
    fc = forecast()
    report_hist = {q: {y: fc[(q, y)]["B"] for y in (2012, 2013, 2014)} for q in ("specialty_pay_revenue", "bdu_revenue")}

    # Splice rule (plan): within 2% of the report's values in every comparable year.
    splice = {}
    for q in ("specialty_pay_revenue", "bdu_revenue"):
        devs = {y: obs[q][y] / report_hist[q][y] - 1 for y in report_hist[q]}
        splice[q] = dict(devs=devs, pass_=all(abs(v) <= SPLICE_TOLERANCE for v in devs.values()),
                         ratio2014=report_hist[q][2014] / obs[q][2014])

    est = []
    for q in ("specialty_pay_revenue", "bdu_revenue"):
        B = np.array([fc[(q, t)]["B"] for t in YEARS])
        I = np.array([fc[(q, t)]["I"] for t in YEARS])
        delta = np.log(B) - np.log(B - I)
        d_lo = np.log(B) - np.log(B - np.array([scen_impact(fc, q, t, LOW) for t in YEARS]))
        d_hi = np.log(B) - np.log(B - np.array([scen_impact(fc, q, t, HIGH) for t in YEARS]))
        versions = {"as published (splice rule)": np.array([obs[q][t] for t in YEARS]),
                    "rescaled to report's 2014 [sensitivity]": np.array([obs[q][t] for t in YEARS]) * splice[q]["ratio2014"]}
        for vname, Y in versions.items():
            y = np.log(B) - np.log(Y)
            for sig in SIGMAS:
                k, se, P, info = gls_k(y, delta, sig)
                band_lo = (delta @ P @ d_lo) / info
                band_hi = (delta @ P @ d_hi) / info
                lo, hi = k - 1.96 * se, k + 1.96 * se
                est.append(dict(quantity=q, version=vname, sigma=sig, k=round(k, 2), se=round(se, 2),
                                ci_lo=round(lo, 2), ci_hi=round(hi, 2),
                                band_lo=round(band_lo, 2), band_hi=round(band_hi, 2),
                                verdict=verdict(lo, hi, band_lo, band_hi)))

    # Smallest annual baseline-error SD at which each verdict becomes inconclusive
    # (k and the band don't depend on sigma; the interval widens in proportion).
    cutoffs = {}
    for q in ("specialty_pay_revenue", "bdu_revenue"):
        B = np.array([fc[(q, t)]["B"] for t in YEARS])
        I = np.array([fc[(q, t)]["I"] for t in YEARS])
        delta = np.log(B) - np.log(B - I)
        d_lo = np.log(B) - np.log(B - np.array([scen_impact(fc, q, t, LOW) for t in YEARS]))
        d_hi = np.log(B) - np.log(B - np.array([scen_impact(fc, q, t, HIGH) for t in YEARS]))
        for vname, scale in (("as published (splice rule)", 1.0), ("rescaled to report's 2014 [sensitivity]", splice[q]["ratio2014"])):
            Y = np.array([obs[q][t] for t in YEARS]) * scale
            y = np.log(B) - np.log(Y)
            for sig in np.arange(0.001, 0.2001, 0.001):
                k, se, P, info = gls_k(y, delta, sig)
                v = verdict(k - 1.96 * se, k + 1.96 * se, (delta @ P @ d_lo) / info, (delta @ P @ d_hi) / info)
                if v == "inconclusive":
                    cutoffs[(q, vname)] = round(float(sig), 3)
                    break

    # Reading at sigma_read = max(historical SD from the report's 2010-2014 data,
    # sigma_tech from the Netflix calibration), as fixed in the plan.
    cal = {r["year"]: r for r in csv.DictReader(open(DER / "netflix_calibration.csv"))}
    sigma_tech = float(cal["sigma_tech"]["log_ratio"])
    reading = {}
    for q in ("specialty_pay_revenue", "bdu_revenue"):
        hist = np.diff(np.log([fc[(q, y)]["B"] for y in range(2010, 2015)]))
        s_hist = float(np.std(hist, ddof=1))
        s_read = max(s_hist, sigma_tech)
        B = np.array([fc[(q, t)]["B"] for t in YEARS])
        I = np.array([fc[(q, t)]["I"] for t in YEARS])
        delta = np.log(B) - np.log(B - I)
        d_lo = np.log(B) - np.log(B - np.array([scen_impact(fc, q, t, LOW) for t in YEARS]))
        d_hi = np.log(B) - np.log(B - np.array([scen_impact(fc, q, t, HIGH) for t in YEARS]))
        for vname, scale in (("as published (splice rule)", 1.0), ("rescaled to report's 2014 [sensitivity]", splice[q]["ratio2014"])):
            y = np.log(B) - np.log(np.array([obs[q][t] for t in YEARS]) * scale)
            k, se, P, info = gls_k(y, delta, s_read)
            bl, bh = (delta @ P @ d_lo) / info, (delta @ P @ d_hi) / info
            reading[(q, vname)] = dict(s_hist=s_hist, s_read=s_read, k=k, lo=k - 1.96 * se, hi=k + 1.96 * se,
                                       bl=bl, bh=bh, verdict=verdict(k - 1.96 * se, k + 1.96 * se, bl, bh))

    # [post hoc] Multiverse: every combination of calibration choice and series
    # version, each read at max(historical SD, calibration SD). The pre-stated
    # reading (2018 calibration, series as published) is one cell, flagged.
    cal_choices = {"none (historical SD only)": 0.0,
                   "2016": float(cal["sigma_tech_2016"]["log_ratio"]),
                   "2017": float(cal["sigma_tech_2017"]["log_ratio"]),
                   "2018 (pre-stated)": sigma_tech,
                   "pooled 2016-2018": float(cal["sigma_tech_pooled_2016_2018"]["log_ratio"]),
                   "growth 2015-2016": float(cal["sigma_growth_2015_2016"]["log_ratio"]),
                   "growth 2015-2017": float(cal["sigma_growth_2015_2017"]["log_ratio"]),
                   "growth 2015-2018": float(cal["sigma_growth_2015_2018"]["log_ratio"]),
                   "growth pooled 2015-2018": float(cal["sigma_growth_pooled_2015_2018"]["log_ratio"])}
    multiverse = []
    for q in ("specialty_pay_revenue", "bdu_revenue"):
        hist = np.diff(np.log([fc[(q, y)]["B"] for y in range(2010, 2015)]))
        s_hist = float(np.std(hist, ddof=1))
        B = np.array([fc[(q, t)]["B"] for t in YEARS])
        I = np.array([fc[(q, t)]["I"] for t in YEARS])
        delta = np.log(B) - np.log(B - I)
        d_lo = np.log(B) - np.log(B - np.array([scen_impact(fc, q, t, LOW) for t in YEARS]))
        d_hi = np.log(B) - np.log(B - np.array([scen_impact(fc, q, t, HIGH) for t in YEARS]))
        versions = {"as published": np.array([obs[q][t] for t in YEARS]),
                    "rescaled to report's 2014": np.array([obs[q][t] for t in YEARS]) * splice[q]["ratio2014"]}
        if q == "specialty_pay_revenue":
            versions["incl. exempt services"] = np.array([obs["specialty_pay_revenue_incl_exempt"][t] for t in YEARS])
        for vname, Y in versions.items():
            y = np.log(B) - np.log(Y)
            for cname, sc in cal_choices.items():
                s_read = max(s_hist, sc)
                k, se, P, info = gls_k(y, delta, s_read)
                bl, bh = (delta @ P @ d_lo) / info, (delta @ P @ d_hi) / info
                multiverse.append(dict(quantity=q, version=vname, calibration=cname, sigma=round(s_read, 4),
                                       k=round(k, 2), ci_lo=round(k - 1.96 * se, 2), ci_hi=round(k + 1.96 * se, 2),
                                       verdict=verdict(k - 1.96 * se, k + 1.96 * se, bl, bh),
                                       prestated=(vname == "as published" and cname == "2018 (pre-stated)")))
    # [post hoc] Uptake-conditional forecast: the report's chain with the
    # unbundling and preponderance components scaled to other uptake levels
    # (exemption-order and closure components don't depend on uptake). The
    # only CRTC count is mid-2016, so later uptake is assumed equal to it.
    up_obs = float(next(r for r in csv.DictReader(open(DER / "uptake_crtc.csv")) if r["as_of"] == "30 June 2016")["share"])
    uptake_levels = {"CRTC count, 30 June 2016": up_obs, "Morrison's estimate (April 2016)": MORRISON_UPTAKE_ESTIMATE,
                     "low end of cited range": CITED_UPTAKE_LOW, "report's assumption": REPORT_UPTAKE_2018}
    conditional = []
    for q in ("specialty_pay_revenue", "bdu_revenue"):
        B = np.array([fc[(q, t)]["B"] for t in YEARS])
        I = np.array([fc[(q, t)]["I"] for t in YEARS])
        delta = np.log(B) - np.log(B - I)
        s_read = reading[(q, "as published (splice rule)")]["s_read"]
        k_obs = reading[(q, "as published (splice rule)")]
        _, _, P, info = gls_k(np.zeros(len(YEARS)), delta, s_read)
        for lab, u in uptake_levels.items():
            m = dict(unbundling=u / REPORT_UPTAKE_2018, preponderance_access=u / REPORT_UPTAKE_2018,
                     exemption_order=1, closures=1)
            du = np.log(B) - np.log(B - np.array([scen_impact(fc, q, t, m) for t in YEARS]))
            k_pred = (delta @ P @ du) / info
            conditional.append(dict(quantity=q, uptake_label=lab, uptake=round(u, 4), k_predicted=round(k_pred, 2),
                                    k_observed=round(k_obs["k"], 2), ci_lo=round(k_obs["lo"], 2), ci_hi=round(k_obs["hi"], 2),
                                    inside_interval=bool(k_obs["lo"] <= k_pred <= k_obs["hi"])))
    with open(DER / "uptake_conditional_lttv.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(conditional[0]))
        w.writeheader()
        w.writerows(conditional)

    with open(DER / "crtc_lttv_cutoffs.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["quantity", "version", "sigma_inconclusive_from"])
        for (q, vname), c in cutoffs.items():
            w.writerow([q, vname, c])
    with open(DER / "crtc_lttv_multiverse.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(multiverse[0]))
        w.writeheader()
        w.writerows(multiverse)

    with open(DER / "crtc_lttv_outcomes.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["series", "year", "value", "unit", "source"])
        units = dict(specialty_pay_revenue="$M", specialty_pay_revenue_incl_exempt="$M", bdu_revenue="$M",
                     bdu_affiliation_payments="$M", bdu_subscribers_thousands="thousands")
        for s, d in obs.items():
            for y in sorted(d):
                src = "CRTC SFS 2016 vintage" if y < 2016 else "CRTC SFS 2020 vintage"
                w.writerow([s, y, round(d[y], 1), units[s], src])
    with open(DER / "crtc_lttv_k_estimates.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(est[0]))
        w.writeheader()
        w.writerows(est)
    write_md(obs, fc, splice, est, cutoffs, reading, cal, sigma_tech, multiverse, conditional)


def write_md(obs, fc, splice, est, cutoffs, reading, cal, sigma_tech, multiverse, conditional):
    cal_choices_order = list(dict.fromkeys(r['calibration'] for r in multiverse))
    L = ["# Results: case 2 (*Let's Talk TV*) against CRTC data",
         "<!-- SUMMARY: Generated by scripts/crtc_outcomes_lttv.py; observed CRTC series against the report's two paths, "
         "with k estimates and pre-stated verdicts · status: generated; read at the pre-stated error level · updated: 2026-10-03 -->",
         "",
         "Generated by `scripts/crtc_outcomes_lttv.py`. Do not edit by hand. Rules: `notes/analysis-plan.md` (committed before the data were opened). "
         "Choices made after seeing the data are marked [post hoc]. CRTC data: Open Government Licence – Canada; broadcast years ending 31 August.",
         "",
         "## Splice check (pre-stated rule: within 2% of the report's values)",
         "",
         "| Quantity | 2012 | 2013 | 2014 | Rule |",
         "|---|---|---|---|---|"]
    names = dict(specialty_pay_revenue="Specialty and pay revenue (discretionary and on-demand, excl. exempt)",
                 bdu_revenue="BDU total revenue (basic and non-basic)")
    for q, s in splice.items():
        dv = s["devs"]
        L.append(f"| {names[q]} | {dv[2012]:+.1%} | {dv[2013]:+.1%} | {dv[2014]:+.1%} | {'pass: used as published' if s['pass_'] else 'fail: rescaled'} |")
    L.append("")
    L.append("2010–2011 are not in these vintages, so the rule was checked on 2012–2014 only.")
    L.append("")
    L.append("## Observed against the report's paths ($M)")
    L.append("")
    L.append("| Quantity | Year | Report baseline | Report LTTV | Observed | Observed vs baseline | Observed vs LTTV |")
    L.append("|---|---|---|---|---|---|---|")
    for q in ("specialty_pay_revenue", "bdu_revenue"):
        for t in YEARS:
            B, Lv, Y = fc[(q, t)]["B"], fc[(q, t)]["L"], obs[q][t]
            L.append(f"| {names[q]} | {t} | {B:,.0f} | {Lv:,.0f} | {Y:,.0f} | {Y / B - 1:+.1%} | {Y / Lv - 1:+.1%} |")
    L.append("")
    L.append("Unadjusted discretionary and on-demand total (incl. exempt services) [post hoc comparison]: "
             + "; ".join(f"{t}: {obs['specialty_pay_revenue_incl_exempt'][t]:,.0f}" for t in YEARS) + ".")
    L.append("")
    L.append("## Scale of the forecast effect, *k* (0 = none, 1 = the report's forecast)")
    L.append("")
    L.append("GLS over 2016–2019 with random-walk baseline error at each annual SD. Band: the forecasters' cited input range "
             "(uptake 10–35%, closures up to 2.5×) as multiples of the report's impact path.")
    L.append("")
    L.append("| Quantity | Series | Baseline error SD | *k* | 95% interval | Cited band | Verdict |")
    L.append("|---|---|---|---|---|---|---|")
    for r in est:
        L.append(f"| {names[r['quantity']]} | {r['version']} | {r['sigma']:.2f} | {r['k']:.1f} | "
                 f"[{r['ci_lo']:.1f}, {r['ci_hi']:.1f}] | [{r['band_lo']:.1f}, {r['band_hi']:.1f}] | {r['verdict']} |")
    L.append("")
    L.append("## Reading at the pre-stated error level")
    L.append("")
    L.append("Technology calibration (`scripts/netflix_calibration.py`): the report forecast US Netflix subscribers of "
             + ", ".join(f"{cal[str(y)]['forecast_us_netflix_m']}M ({y})" for y in (2016, 2017, 2018))
             + "; Netflix's 10-K for 2018 reports US paid memberships at year end of "
             + ", ".join(f"{float(cal[str(y)]['observed_us_paid_memberships_m']):.1f}M" for y in (2016, 2017, 2018))
             + f". By the pre-stated rule, sigma_tech = |log(observed 2018 / forecast 2018)| / 2 = {sigma_tech:.1%} a year, "
             "and the table is read at the larger of that and the quantity's historical SD.")
    L.append("")
    L.append("| Quantity | Series | Historical SD | SD read at | *k* | 95% interval | Cited band | Verdict |")
    L.append("|---|---|---|---|---|---|---|---|")
    for (q, vname), r in reading.items():
        L.append(f"| {names[q]} | {vname} | {r['s_hist']:.1%} | {r['s_read']:.1%} | {r['k']:.1f} | "
                 f"[{r['lo']:.1f}, {r['hi']:.1f}] | [{r['bl']:.1f}, {r['bh']:.1f}] | {r['verdict']} |")
    L.append("")
    ratio18 = float(cal["2018"]["log_ratio"])
    if ratio18 > 0:
        L.append("Netflix's 2018 US memberships exceeded the report's forecast, so on the pre-stated reading the report's "
                 "technology-only baseline was, if anything, too optimistic about TV revenue: the direction favours finding "
                 "a policy effect, which strengthens the specialty and pay result and weakens the BDU one.")
    L.append("Not part of the rule, recorded for the write-up: the forecast's 2016 and 2017 errors had the opposite sign "
             "(observed below forecast), and the report's Trefis series may count all memberships rather than paid ones.")
    L.append("")
    L.append("## The forecast at other uptake levels [post hoc]")
    L.append("")
    L.append("The report's chain with its unbundling and preponderance components scaled to other uptake levels "
             "(the exemption-order and closure components don't depend on uptake), expressed as *k* and set against the "
             "observed *k* and its 95% interval at the pre-stated error level. The only CRTC count is for 30 June 2016; "
             "later uptake is assumed to stay at each level.")
    L.append("")
    L.append("| Quantity | Uptake | Share of subscribers | Forecast *k* at that uptake | Observed *k* [95% interval] | Inside interval |")
    L.append("|---|---|---|---|---|---|")
    for r in conditional:
        short = {"specialty_pay_revenue": "Specialty and pay revenue", "bdu_revenue": "BDU total revenue"}[r["quantity"]]
        L.append(f"| {short} | {r['uptake_label']} | {r['uptake']:.1%} | {r['k_predicted']:.2f} | "
                 f"{r['k_observed']:.1f} [{r['ci_lo']:.1f}, {r['ci_hi']:.1f}] | {'yes' if r['inside_interval'] else 'no'} |")
    L.append("")
    L.append("## Multiverse [post hoc]")
    L.append("")
    L.append("The pre-stated rule calibrates on 2018 alone, measuring error from 2014. The same formula on 2016 or 2017, or a "
             "pooled random-walk estimate, gives other error levels. Table 7's 2015 base (45.5M) was already above Netflix's "
             "actual 2015 count (43.4M, 10-K for 2017), so the growth-based rows measure error from 2015 instead. Every "
             "combination with each series version, read at the larger of the historical SD and the calibration SD (the "
             "pre-stated cell in bold):")
    L.append("")
    L.append("| Quantity | Series | Calibration | SD read at | *k* | 95% interval | Verdict |")
    L.append("|---|---|---|---|---|---|---|")
    for r in multiverse:
        b0, b1 = ("**", "**") if r["prestated"] else ("", "")
        short = {"specialty_pay_revenue": "Specialty and pay revenue", "bdu_revenue": "BDU total revenue"}[r["quantity"]]
        L.append(f"| {b0}{short}{b1} | {r['version']} | {r['calibration']} | {r['sigma']:.1%} | {r['k']:.1f} | "
                 f"[{r['ci_lo']:.1f}, {r['ci_hi']:.1f}] | {b0}{r['verdict']}{b1} |")
    L.append("")
    L.append("By calibration choice (series as published; the other versions change the verdict only where noted):")
    L.append("")
    L.append("| Calibration | SD read at (specialty/pay) | Specialty and pay revenue | BDU total revenue |")
    L.append("|---|---|---|---|")
    for cname in cal_choices_order:
        cells = {q: [r for r in multiverse if r["quantity"] == q and r["calibration"] == cname] for q in ("specialty_pay_revenue", "bdu_revenue")}
        out = []
        for q in ("specialty_pay_revenue", "bdu_revenue"):
            pub = next(r for r in cells[q] if r["version"] == "as published")
            others = {r["verdict"].split(" (")[0] for r in cells[q]}
            txt = pub["verdict"].split(" (")[0]
            if len(others) > 1:
                txt += " (varies by series version)"
            out.append(txt)
        sd = next(r for r in cells["specialty_pay_revenue"] if r["version"] == "as published")["sigma"]
        L.append(f"| {cname} | {sd:.1%} | {out[0]} | {out[1]} |")
    L.append("")
    L.append("**Sensitivity.** Each verdict holds up to the annual baseline-error SD below and becomes inconclusive at it:")
    L.append("")
    for (q, vname), c in cutoffs.items():
        L.append(f"- {names[q]}, {vname}: inconclusive from {c:.1%} a year")
    L.append("")
    L.append("These are tests of the report's scenario paths. That the policy had no effect on specialty and pay revenue is a "
             "counterfactual claim, and holds only if the report's technology-only baseline was about right; the Netflix "
             "calibration is evidence on that, not proof.")
    L.append("")
    L.append("## Pass-through [post hoc observable]")
    L.append("")
    L.append("The report assumes BDUs pass 75% of their retail revenue loss to Canadian services as lower wholesale fees (¶207). "
             "BDU affiliation payments ($M), the wholesale fees BDUs pay programmers, did not fall: the modelled pass-through is "
             "not visible in the aggregate. That doesn't show why. Rising fees on a shrinking subscriber base, payments to "
             "services outside the report's scope, and the CRTC Wholesale Code (in force January 2016; ¶197 item 3) are all "
             "consistent with it.")
    L.append("")
    L.append("| Year | " + " | ".join(str(y) for y in range(2012, 2021)) + " |")
    L.append("|---|" + "---|" * 9)
    L.append("| Affiliation payments | " + " | ".join(f"{obs['bdu_affiliation_payments'].get(y, float('nan')):,.0f}" for y in range(2012, 2021)) + " |")
    L.append("| BDU total revenue | " + " | ".join(f"{obs['bdu_revenue'].get(y, float('nan')):,.0f}" for y in range(2012, 2021)) + " |")
    L.append("| BDU subscribers (000s) | " + " | ".join(f"{obs['bdu_subscribers_thousands'].get(y, float('nan')):,.0f}" for y in range(2012, 2021)) + " |")
    L.append("")
    (ROOT / "notes" / "results-lttv.md").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
