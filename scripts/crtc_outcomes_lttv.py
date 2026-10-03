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
LOW = dict(unbundling=10 / 15, preponderance_access=10 / 15, exemption_order=1, closures=1)
HIGH = dict(unbundling=35 / 15, preponderance_access=35 / 15, exemption_order=1, closures=2.5)


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
        splice[q] = dict(devs=devs, pass_=all(abs(v) <= 0.02 for v in devs.values()),
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
    write_md(obs, fc, splice, est)


def write_md(obs, fc, splice, est):
    L = ["# Results: case 2 (*Let's Talk TV*) against CRTC data",
         "<!-- SUMMARY: Generated by scripts/crtc_outcomes_lttv.py; observed CRTC series against the report's two paths, "
         "with k estimates and pre-stated verdicts · status: generated, preliminary (technology calibration pending) · updated: 2026-10-03 -->",
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
        L.append(f"| {names[r['quantity']]} | {r['version']} | {r['sigma']:.2f} | {r['k']:.2f} | "
                 f"[{r['ci_lo']:.2f}, {r['ci_hi']:.2f}] | [{r['band_lo']:.2f}, {r['band_hi']:.2f}] | {r['verdict']} |")
    L.append("")
    L.append("## Pass-through [post hoc observable]")
    L.append("")
    L.append("The report assumes BDUs pass 75% of their retail revenue loss to Canadian services as lower wholesale fees (¶207). "
             "BDU affiliation payments ($M), the wholesale fees BDUs pay programmers:")
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
