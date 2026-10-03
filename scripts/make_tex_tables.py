#!/usr/bin/env python3
"""Write sections/tables-lttv.tex: appendix tables generated from data/derived/.
Do not edit the output by hand.

Tables, in the order written (A1-A8 in the paper):
  A1 candidate denominators for the report's "18%", with the components they're built from
  A2 inputs to k: the report's paths, its impact components and the CRTC outcomes, 2016-2019
  A3 model-implied uptake scenarios, with the uptake path in each year
  A4 calibrations of the baseline's error, with the Netflix figures behind them
  A5 distributors' revenue split into subscribers and revenue per subscriber (post hoc)
  A6 annual staff series
  A7 the report's two splits of its jobs total
  A8 chronology of pre-stated and post hoc analyses

A2-A4 are recomputed here from the displayed inputs (k, intervals, scenario k,
calibration values) and checked against the analysis outputs, so a mismatch
between the tables and the analysis stops the build.
"""
import csv
import math
import re
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from plan_constants import (CITED_CLOSURES_HIGH_MULT, CITED_UPTAKE_HIGH, CITED_UPTAKE_LOW,  # noqa: E402
                            MORRISON_UPTAKE_ESTIMATE, REPORT_UPTAKE_2018)

ROOT = Path(__file__).resolve().parents[1]
DER = ROOT / "data" / "derived"
OUT = ROOT / "sections" / "tables-lttv.tex"
YEARS = [2016, 2017, 2018, 2019]
SERIES = (("specialty_pay_revenue", "Specialty and pay revenue"), ("bdu_revenue", "Distributors' revenue"))


def rows(name):
    return list(csv.DictReader(open(DER / name)))


def esc(s):
    return s.replace("$", "\\$").replace("%", "\\%").replace("&", "\\&")


def lab(s):
    """Escape a label and set year ranges with an en-dash."""
    return esc(re.sub(r"(?<=\d)-(?=\d)", "--", s))


def num(x, d=2):
    """Signed decimal with a typographic minus; no negative zero."""
    s = f"{x:.{d}f}"
    if float(s) == 0:
        s = s.lstrip("-")
    return "\\textminus " + s[1:] if s.startswith("-") else s


def intm(x):
    """Integer with thousands separator and a typographic minus; no negative zero."""
    s = f"{round(x):,.0f}"
    return "\\textminus " + s[1:] if s.startswith("-") and s != "-0" else s.lstrip("-")


def pct(x, d=1):
    return f"{100 * x:.{d}f}\\%"


def gls(y, delta, sigma):
    h = np.array([t - 2014 for t in YEARS], dtype=float)
    P = np.linalg.inv(sigma ** 2 * np.minimum.outer(h, h))
    info = delta @ P @ delta
    return (delta @ P @ y) / info, 1 / math.sqrt(info), P, info


def check(name, got, want):
    if got != want:
        sys.exit(f"make_tex_tables: {name}: recomputed {got}, analysis output {want}")


tf = {(r["fact"], int(r["year"])): float(r["value"]) for r in rows("nordicity_2015_text_facts.csv")}
fc = {(r["quantity"], int(r["year"])): r for r in rows("nordicity_2015_scenarios.csv")}
COMP = ("unbundling", "preponderance_access", "exemption_order", "closures")


def fv(q, t, k):
    v = fc[(q, t)][k]
    return float(v) if v not in ("", None) else 0.0


obs = {(r["series"], int(r["year"])): float(r["value"])
       for r in rows("crtc_lttv_outcomes.csv") if "2020 vintage" in r["source"] and int(r["year"]) in YEARS}
mv = [r for r in rows("crtc_lttv_multiverse.csv") if r["version"] == "as published"]
cal = {r["year"]: r for r in rows("netflix_calibration.csv")}
sigma_tech = float(cal["sigma_tech"]["log_ratio"])

# Inputs to k, recomputed for the checks and the tables below
inp = {}
for q, _ in SERIES:
    B = np.array([fv(q, t, "baseline_level") for t in YEARS])
    I = np.array([fv(q, t, "impact_total") for t in YEARS])
    for t, i in zip(YEARS, I):
        check(f"{q} {t} components sum to impact", round(sum(fv(q, t, c) for c in COMP), 1), round(i, 1))
    Y = np.array([obs[(q, t)] for t in YEARS])
    delta, y = np.log(B) - np.log(B - I), np.log(B) - np.log(Y)
    hist_vals = [fv(q, t, "baseline_level") for t in range(2010, 2015)]
    s_hist = float(np.std(np.diff(np.log(hist_vals)), ddof=1))

    def path(mult):
        return np.log(B) - np.log(B - np.array([sum(fv(q, t, c) * mult[c] for c in COMP) for t in YEARS]))
    lo_m, hi_m = CITED_UPTAKE_LOW / REPORT_UPTAKE_2018, CITED_UPTAKE_HIGH / REPORT_UPTAKE_2018
    d_lo = path(dict(unbundling=lo_m, preponderance_access=lo_m, exemption_order=1, closures=1))
    d_hi = path(dict(unbundling=hi_m, preponderance_access=hi_m, exemption_order=1, closures=CITED_CLOSURES_HIGH_MULT))
    k, se, P, info = gls(y, delta, max(s_hist, sigma_tech))
    pre = next(r for r in mv if r["quantity"] == q and r["calibration"] == "2018 (pre-stated)")
    check(f"{q} k at the pre-stated calibration", round(k, 2), float(pre["k"]))
    check(f"{q} interval", (round(k - 1.96 * se, 2), round(k + 1.96 * se, 2)), (float(pre["ci_lo"]), float(pre["ci_hi"])))
    band = ((delta @ P @ d_lo) / info, (delta @ P @ d_hi) / info)
    inp[q] = dict(B=B, I=I, Y=Y, delta=delta, y=y, s_hist=s_hist, hist_vals=hist_vals, k=k, se=se, P=P, info=info,
                  band=band, lo=k - 1.96 * se, hi=k + 1.96 * se)

L = ["% Generated by scripts/make_tex_tables.py from data/derived/. Do not edit by hand.", ""]

# A1: candidate denominators and the components they're built from
L += ["\\begin{table}[htbp]", "\\centering", "\\small",
      "\\caption{The report's \\$399 million reduction in Canadian programming expenditure (CPE) in 2020, and its \\$352 million "
      "programming-services part, as shares of every denominator built from the report's own figures (Figs.~8, 9, 43). "
      "The report states 18\\% of baseline CPE (para.~239); the testimony said 18\\% \\enquote{of what now exists}. "
      "Letters refer to the components in the lower panel.}",
      "\\label{tab:cpe-denominators}",
      "\\footnotesize",
      "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.34\\textwidth}lrrr}", "\\toprule",
      "Denominator & Built from & Numerator (\\$M) & Denominator (\\$M) & Share \\\\", "\\midrule"]
den_label = {  # display names; the numerator column carries the $399M/$352M distinction
    "all CPE (Figs. 8+9)": "All CPE, baseline 2020",
    "programming services only": "Programming services",
    "programming services excl. CBC/SRC": "Programming services excl. CBC/SRC",
    "excl. CBC/SRC, with BDU contributions": "Programming services excl. CBC/SRC, plus BDU contributions",
    "specialty + pay": "Specialty and pay",
    "specialty only": "Specialty",
    "$352M programming-services impact / programming services": "Programming services",
    "$352M / programming services excl. CBC/SRC": "Programming services excl. CBC/SRC",
    "$352M / specialty + pay": "Specialty and pay",
    "$399M / 2020 LTTV-scenario CPE (Fig. 43 level)": "All CPE, LTTV scenario 2020",
    "$399M / 2015 CPE (Fig. 43, current at the time of testimony)": "All CPE 2015 (report's forecast)",
    "$399M / 2014 CPE (Fig. 43, last actual year)": "All CPE 2014 (last actual year)"}
cands = rows("cpe_share_candidates.csv")
order = list(dict.fromkeys(r["denominator_musd"] for r in cands))  # each $352M share listed under its $399M counterpart
for r in sorted(cands, key=lambda r: (order.index(r["denominator_musd"]), -float(r["numerator_musd"]))):
    n, d = float(r["numerator_musd"]), float(r["denominator_musd"])
    built = r["built_from"].replace(" - ", " \\textminus{} ")
    L.append(f"{esc(den_label[r['denominator']])} & {built} & {n:,.0f} & {d:,.0f} & {100 * n / d:.1f}\\% \\\\")
L += ["\\midrule", "\\multicolumn{5}{l}{\\textit{Components} (\\$M)} \\\\"]
for r in rows("cpe_components_2020.csv"):
    L.append(f"\\multicolumn{{4}}{{l}}{{{r['letter']}\\quad {esc(r['component'])}}} & {float(r['musd']):,.0f} \\\\")
L += ["\\bottomrule", "\\end{tabular}", "\\end{table}", ""]

# A2: inputs to k
L += ["\\begin{table}[htbp]", "\\centering", "\\small",
      "\\caption{Inputs to \\(k\\), in \\$ millions: the report's forecast impact with its four components and its baseline "
      "(the decisions-scenario level plus the impact), from Figs.~41 and 42 (2016 components from Figs.~34--36, 39 and 40), and the CRTC outcome (2020 edition; channels exclude exempt services). The historical "
      "volatility is the standard deviation of annual log changes in the report's 2010--2014 values. With \\(\\sigma\\) "
      "the larger of that volatility and the calibration's value (table~\\ref{tab:calibrations}), \\(\\hat k\\) and its "
      "interval follow from the formulas in appendix~\\ref{app:methods}. The cited-input band scales the unbundling and "
      f"preponderance components by {CITED_UPTAKE_LOW:.2f}/{REPORT_UPTAKE_2018:.2f} (low) and "
      f"{CITED_UPTAKE_HIGH:.2f}/{REPORT_UPTAKE_2018:.2f} (high), and closures by {CITED_CLOSURES_HIGH_MULT} in the high case. "
      "Produced by \\texttt{scripts/crtc\\_outcomes\\_lttv.py}; data in \\texttt{data/derived/nordicity\\_2015\\_scenarios.csv} "
      "and \\texttt{data/derived/crtc\\_lttv\\_outcomes.csv}.}",
      "\\label{tab:inputs}",
      "\\begin{tabular}{lrrrr}", "\\toprule",
      " & " + " & ".join(str(t) for t in YEARS) + " \\\\", "\\midrule"]
comp_label = dict(unbundling="unbundling", preponderance_access="preponderance and access rules",
                  exemption_order="exemption order", closures="service closures")
for q, label in SERIES:
    d = inp[q]
    L.append(f"\\multicolumn{{5}}{{l}}{{\\textit{{{label}}}}} \\\\")
    L.append("Report's baseline \\(B_t\\) & " + " & ".join(f"{v:,.0f}" for v in d["B"]) + " \\\\")
    L.append("Forecast impact \\(I_t\\) & " + " & ".join(f"{v:,.0f}" for v in d["I"]) + " \\\\")
    for c in COMP:
        vals = [fc[(q, t)][c] for t in YEARS]
        L.append(f"\\quad {comp_label[c]} & " + " & ".join("--" if v in ("", None) else f"{float(v):,.0f}" for v in vals) + " \\\\")
    L.append("Observed \\(Y_t\\) & " + " & ".join(f"{v:,.1f}" for v in d["Y"]) + " \\\\")
    L.append("\\(\\delta_t=\\log B_t-\\log(B_t-I_t)\\) & " + " & ".join(num(v, 4) for v in d["delta"]) + " \\\\")
    L.append("\\(y_t=\\log B_t-\\log Y_t\\) & " + " & ".join(num(v, 4) for v in d["y"]) + " \\\\")
    L.append("Report's values 2010--2014 & \\multicolumn{4}{l}{" + ", ".join(f"{v:,.0f}" for v in d["hist_vals"]) + "} \\\\")
    L.append(f"Historical volatility & \\multicolumn{{4}}{{l}}{{{pct(d['s_hist'])}}} \\\\")
    L.append(f"Cited-input band for \\(k\\) & \\multicolumn{{4}}{{l}}{{{num(d['band'][0])} to {num(d['band'][1])}}} \\\\")
    if q != SERIES[-1][0]:
        L.append("\\addlinespace")
L += ["\\bottomrule", "\\end{tabular}", "\\end{table}", ""]

# A3: model-implied uptake scenarios
up_obs = float(next(r for r in rows("uptake_crtc.csv") if r["as_of"] == "30 June 2016")["share"])
share = {t: tf[("table18_byop_share_pct", t)] / 100 for t in YEARS}
paths = {"CRTC count, 30 June 2016": (up_obs, up_obs), "Morrison's estimate (April 2016)": (MORRISON_UPTAKE_ESTIMATE,) * 2,
         "low end of cited range": (CITED_UPTAKE_LOW,) * 2, "report's assumption": None,
         "rising from 2016 count to Morrison's estimate": (up_obs, MORRISON_UPTAKE_ESTIMATE),
         "rising from 2016 count to low end of cited range": (up_obs, CITED_UPTAKE_LOW)}
cond = {(r["quantity"], r["uptake_label"]): r for r in rows("uptake_conditional_lttv.csv")}
check("scenario labels", sorted({lb for _, lb in cond}), sorted(paths))
display = {"report's assumption": "Report's assumption (Table~18)"}
L += ["\\begin{table}[htbp]", "\\centering", "\\small",
      "\\caption{Model-implied scenarios, an exploratory comparison added after the outcome data was opened; uptake after June 2016 "
      "is assumed, and a scenario inside the interval isn't thereby confirmed. Each year's unbundling and preponderance components (table~\\ref{tab:inputs}) "
      "are multiplied by the path's uptake over the report's share for that year (Table~18), the exemption-order and "
      "closure components are unchanged, and the resulting shortfall path \\(\\delta^{u}_t\\) is projected like "
      "the band: \\(k^{u}=\\delta'\\Sigma^{-1}\\delta^{u}/\\delta'\\Sigma^{-1}\\delta\\). Rising paths are linear from the "
      "2016 count. Observed \\(k\\) and intervals at the pre-stated calibration. Produced by "
      "\\texttt{scripts/crtc\\_outcomes\\_lttv.py}; data in \\texttt{data/derived/uptake\\_conditional\\_lttv.csv}.}",
      "\\label{tab:scenarios}",
      "\\footnotesize", "\\setlength{\\tabcolsep}{4pt}",
      "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.3\\textwidth}rrrrll}", "\\toprule",
      " & \\multicolumn{4}{c}{Uptake} & \\multicolumn{2}{c}{Model-implied \\(k\\)} \\\\",
      "\\cmidrule(lr){2-5}\\cmidrule(lr){6-7}",
      "Uptake path & " + " & ".join(str(t) for t in YEARS) + " & Specialty and pay & Distributors \\\\", "\\midrule"]
for lb, p in paths.items():
    u = {t: share[t] for t in YEARS} if p is None else {t: p[0] + (p[1] - p[0]) * (t - 2016) / 3 for t in YEARS}
    cells = []
    for q, _ in SERIES:
        d = inp[q]
        f = {t: 1.0 if p is None else u[t] / share[t] for t in YEARS}
        imp = np.array([sum(fv(q, t, c) * (f[t] if c in ("unbundling", "preponderance_access") else 1) for c in COMP)
                        for t in YEARS])
        du = np.log(d["B"]) - np.log(d["B"] - imp)
        kp = (d["delta"] @ d["P"] @ du) / d["info"]
        check(f"scenario k, {q}, {lb}", round(kp, 2), float(cond[(q, lb)]["k_predicted"]))
        where = "inside" if d["lo"] <= kp <= d["hi"] else ("below" if kp < d["lo"] else "above")
        cells.append(f"{num(kp)} ({where})")
    L.append(f"{display.get(lb, lab(lb[0].upper() + lb[1:]))} & " + " & ".join(pct(u[t]) for t in YEARS) + " & " + " & ".join(cells) + " \\\\")
L.append("\\midrule")
L.append("\\multicolumn{5}{l}{Observed \\(k\\) [95\\% interval]} & "
         + " & ".join(f"{num(inp[q]['k'])} [{num(inp[q]['lo'])}, {num(inp[q]['hi'])}]" for q, _ in SERIES) + " \\\\")
L += ["\\bottomrule", "\\end{tabular}", "\\end{table}", ""]

# A4: calibrations of the baseline's error, with the Netflix figures behind them
nf = {int(y): (float(cal[y]["forecast_us_netflix_m"]), float(cal[y]["observed_us_paid_memberships_m"]))
      for y in ("2015", "2016", "2017", "2018")}
e = {y: math.log(o / f) for y, (f, o) in nf.items()}
g = {y: e[y] - e[2015] for y in (2016, 2017, 2018)}
netflix_value = {
    "none (historical SD only)": None,
    "2016": abs(e[2016]) / math.sqrt(2), "2017": abs(e[2017]) / math.sqrt(3), "2018 (pre-stated)": abs(e[2018]) / math.sqrt(4),
    "pooled 2016-2018": math.sqrt((e[2016] ** 2 / 2 + (e[2017] - e[2016]) ** 2 + (e[2018] - e[2017]) ** 2) / 3),
    "growth 2015-2016": abs(g[2016]), "growth 2015-2017": abs(g[2017]) / math.sqrt(2),
    "growth 2015-2018": abs(g[2018]) / math.sqrt(3),
    "growth pooled 2015-2018": math.sqrt((g[2016] ** 2 + (g[2017] - g[2016]) ** 2 + (g[2018] - g[2017]) ** 2) / 3)}
cal_key = {"2016": "sigma_tech_2016", "2017": "sigma_tech_2017", "2018 (pre-stated)": "sigma_tech_2018",
           "pooled 2016-2018": "sigma_tech_pooled_2016_2018", "growth 2015-2016": "sigma_growth_2015_2016",
           "growth 2015-2017": "sigma_growth_2015_2017", "growth 2015-2018": "sigma_growth_2015_2018",
           "growth pooled 2015-2018": "sigma_growth_pooled_2015_2018"}
for c, key in cal_key.items():
    check(f"Netflix calibration {c}", round(netflix_value[c], 4), float(cal[key]["log_ratio"]))
cals = list(dict.fromkeys(r["calibration"] for r in mv))
check("calibration labels", sorted(cals), sorted(netflix_value))
short = {"smaller than the forecasters' inputs imply": "smaller", "consistent with the forecast range": "consistent",
         "inconclusive": "inconclusive", "forecast exceeded": "exceeded"}
L += ["\\begin{table}[htbp]", "\\centering", "\\small",
      "\\caption{Calibrating the baseline's annual error \\(\\sigma\\). Intervals are conditional on \\(\\sigma\\) and don't "
      "carry the uncertainty in \\(\\sigma\\) itself. Panel (a): the report's forecast of US Netflix "
      "subscribers (Table~7) against Netflix's US paid memberships at year end (Form 10-K), in millions, with "
      "\\(e_t=\\log(\\text{observed}_t/\\text{forecast}_t)\\). Panel (b): the value each calibration takes from panel (a) "
      "(formulas in appendix~\\ref{app:methods}), the \\(\\sigma\\) used (the larger of that value and "
      "the series' historical volatility in table~\\ref{tab:inputs}), and the resulting interval for \\(k\\), which is "
      f"{num(inp['specialty_pay_revenue']['k'])} for specialty and pay revenue and {num(inp['bdu_revenue']['k'])} for "
      "distributors' revenue under every calibration. Verdicts: \\emph{smaller}, the interval lies below the cited-input band; "
      "\\emph{consistent}, it overlaps the band; \\emph{inconclusive}, it contains both zero and the band's lower end. "
      "Produced by \\texttt{scripts/netflix\\_calibration.py} and \\texttt{scripts/crtc\\_outcomes\\_lttv.py}; data in "
      "\\texttt{data/derived/netflix\\_calibration.csv} and \\texttt{data/derived/crtc\\_lttv\\_multiverse.csv}.}",
      "\\label{tab:calibrations}",
      "\\footnotesize",
      "(a) \\textit{The report's forecast and Netflix's count}\\par\\smallskip",
      "\\begin{tabular}{lrrrr}", "\\toprule",
      " & " + " & ".join(str(y) for y in nf) + " \\\\", "\\midrule",
      "Report's forecast & " + " & ".join(f"{f:.1f}" for f, _ in nf.values()) + " \\\\",
      "Netflix, US paid memberships & " + " & ".join(f"{o:.3f}" for _, o in nf.values()) + " \\\\",
      "\\(e_t\\) & " + " & ".join(num(e[y], 4) for y in nf) + " \\\\",
      "\\bottomrule", "\\end{tabular}", "\\par\\bigskip",
      "(b) \\textit{Results by calibration}\\par\\smallskip",
      "\\setlength{\\tabcolsep}{4pt}",
      "\\begin{tabular}{lrrllrll}", "\\toprule",
      " & & \\multicolumn{3}{c}{Specialty and pay revenue} & \\multicolumn{3}{c}{Distributors' revenue} \\\\",
      "\\cmidrule(lr){3-5}\\cmidrule(lr){6-8}",
      "Calibration & Value & \\(\\sigma\\) & Interval & Verdict & \\(\\sigma\\) & Interval & Verdict \\\\", "\\midrule"]
for c in cals:
    v = netflix_value[c]
    cells = []
    for q, _ in SERIES:
        d = inp[q]
        r = next(r for r in mv if r["quantity"] == q and r["calibration"] == c)
        s = max(d["s_hist"], v if v is not None else 0.0)
        check(f"sigma, {q}, {c}", round(s, 4), float(r["sigma"]))
        k, se, _, _ = gls(d["y"], d["delta"], s)
        check(f"interval, {q}, {c}", (round(k - 1.96 * se, 2), round(k + 1.96 * se, 2)), (float(r["ci_lo"]), float(r["ci_hi"])))
        verdict = r["verdict"].split(" (")[0]
        cells.append(f"{pct(s)} & [{num(float(r['ci_lo']))}, {num(float(r['ci_hi']))}] & {short.get(verdict, verdict)}")
    name = "None (historical s.d. only)" if v is None else lab(c)
    L.append(f"{name} & {'--' if v is None else pct(v)} & " + " & ".join(cells) + " \\\\")
L += ["\\bottomrule", "\\end{tabular}", "\\end{table}", ""]

# Decomposition of distributors' revenue (post hoc)
dec = rows("bdu_decomposition_lttv.csv")
def pcl(x):
    return num(100 * (math.exp(float(x)) - 1), 1) + "\\%"
L += ["\\begin{table}[htbp]", "\\centering", "\\small",
      "\\caption{Distributors' revenue split into subscribers and revenue per subscriber (post hoc; rule fixed before computing). "
      "Panel (a): CRTC subscriber counts (2016 edition to 2015, 2020 edition after) and revenue per subscriber per month, against "
      "the report's baseline subscribers (Fig.~17) and its revenue per subscriber, baseline revenue over 12 times subscribers "
      "(Fig.~19's ARPU shown for comparison). Panel (b): the change in each gap from 2014, when the report's figures were "
      "actuals, against the report's scenario, whose subscriber part is its added cord cutting (Tables~5, 20, 21) and whose "
      "per-subscriber part is everything else; the last column is the report's chain at the uptake the CRTC counted. "
      "Produced by \\texttt{scripts/decompose\\_bdu\\_lttv.py}; data in \\texttt{data/derived/bdu\\_decomposition\\_lttv.csv}.}",
      "\\label{tab:decomposition}", "\\footnotesize", "\\setlength{\\tabcolsep}{4pt}",
      "(a) \\textit{Levels}\\par\\smallskip",
      "\\begin{tabular}{lrrrrr}", "\\toprule",
      " & \\multicolumn{2}{c}{Subscribers (thousands)} & \\multicolumn{3}{c}{Revenue per subscriber (\\$ a month)} \\\\",
      "\\cmidrule(lr){2-3}\\cmidrule(lr){4-6}",
      "Year & CRTC & Report & CRTC & Report & Fig.~19 \\\\", "\\midrule"]
for r in dec:
    L.append(f"{r['year']} & {float(r['crtc_subscribers_k']):,.0f} & {float(r['report_subscribers_k']):,.0f} & "
             f"{float(r['crtc_rev_per_sub']):.2f} & {float(r['report_rev_per_sub']):.2f} & {float(r['report_fig19_arpu']):.2f} \\\\")
L += ["\\bottomrule", "\\end{tabular}", "\\par\\bigskip",
      "(b) \\textit{Change in the gap from 2014, against the report's paths}\\par\\smallskip",
      "\\begin{tabular}{lrrrrr}", "\\toprule",
      " & \\multicolumn{2}{c}{Observed} & \\multicolumn{2}{c}{Report's scenario} & At counted uptake \\\\",
      "\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-6}",
      "Year & Subscribers & Per subscriber & Subscribers & Per subscriber & Per subscriber \\\\", "\\midrule"]
for r in dec:
    if int(r["year"]) < 2015:
        continue
    fcs = pcl(r["fc_sub_part"]) if int(r["year"]) >= 2016 else "--"
    fcp = pcl(r["fc_per_part"]) if int(r["year"]) >= 2016 else "--"
    fcu = pcl(r["fc_counted_uptake_per_part"]) if int(r["year"]) >= 2016 else "--"
    L.append(f"{r['year']} & {pcl(r['obs_sub_change_from_2014'])} & {pcl(r['obs_per_change_from_2014'])} & {fcs} & {fcp} & {fcu} \\\\")
L += ["\\bottomrule", "\\end{tabular}", "\\end{table}", ""]

# A5: annual staff series
emp = rows("employment_lttv.csv")
years = sorted({int(r["year"]) for r in emp})
L += ["\\begin{table}[htbp]", "\\centering", "\\small",
      "\\caption{Staff counts from the CRTC's financial summaries (channels: discretionary and on-demand services, exempt "
      "services excluded from 2016; distributors: cable, satellite and IPTV, reported as FTEs in the 2016 edition and as a "
      "staff count in the 2020 edition), the 2012--2015 linear trend, and the report's direct FTE impact for each sector "
      "(Table~22). Staff counts aren't the report's modelled FTEs. Produced by \\texttt{scripts/employment\\_lttv.py}.}",
      "\\label{tab:staff}",
      "\\footnotesize", "\\setlength{\\tabcolsep}{2.5pt}",
      "\\begin{tabular}{l" + "r" * len(years) + "}", "\\toprule",
      " & " + " & ".join(str(y) for y in years) + " \\\\", "\\midrule"]
for sector, label in (("channels", "Channels"), ("distributors", "Distributors")):
    rs = {int(r["year"]): r for r in emp if r["sector"] == sector}
    L.append(f"{label}: staff & " + " & ".join(f"{float(rs[y]['staff']):,.0f}" for y in years) + " \\\\")
    L.append("\\quad 2012--2015 trend & " + " & ".join(f"{float(rs[y]['pre2015_trend']):,.0f}" for y in years) + " \\\\")
    L.append("\\quad Report's direct impact & " + " & ".join(
        intm(float(rs[y]["forecast_direct_impact"])) if rs[y]["forecast_direct_impact"] not in ("", None) else ""
        for y in years) + " \\\\")
L += ["\\bottomrule", "\\end{tabular}", "\\end{table}", ""]

# A6: the report's two splits of its jobs total


def fte(key):
    return tf[(key, 2020)]


bd, bt = fte("sector_fte_total_broadcasting_sector_direct"), fte("sector_fte_total_broadcasting_sector")
prd, prt = fte("sector_fte_independent_production_direct"), fte("sector_fte_independent_production")
check("direct FTEs sum to Table 1", bd + prd, fte("table1_employment_direct"))
check("spin-off FTEs sum to Table 1", (bt - bd) + (prt - prd), fte("table1_employment_spin-off"))
comp = [("Distributors", "bdus"), ("Specialty and pay services", "specialty_and_pay_tv_services"),
        ("Private conventional stations", "private_conventional_tv")]
L += ["\\begin{table}[htbp]", "\\centering", "\\small",
      "\\caption{The report's FTE losses in 2020, by the sector whose lost revenue or spending gives rise to them and by kind "
      "of effect (Tables~1, 22, 23; paras.~246, 248, 250). Direct FTEs are jobs within that sector; spin-off FTEs are "
      "jobs in other sectors of the economy. The headline split (direct and spin-off) and the sector split (broadcasting "
      "and production) cross-classify the same total. Broadcasting's printed components sum to 10 more spin-off FTEs "
      "than its printed total, a rounding difference in the report.}",
      "\\label{tab:jobs-reconciliation}",
      "\\begin{tabular}{lrrr}", "\\toprule",
      "Sector & Direct & Spin-off & Total \\\\", "\\midrule"]
L.append(f"Broadcasting (printed total) & {bd:,.0f} & {bt - bd:,.0f} & {bt:,.0f} \\\\")
for label, key in comp:
    d, t = fte(f"sector_fte_{key}_direct"), fte(f"sector_fte_{key}")
    L.append(f"\\quad {label} & {d:,.0f} & {t - d:,.0f} & {t:,.0f} \\\\")
L.append(f"Independent production & {prd:,.0f} & {prt - prd:,.0f} & {prt:,.0f} \\\\")
L.append("\\midrule")
L.append(f"Total & {bd + prd:,.0f} & {(bt - bd) + (prt - prd):,.0f} & {bt + prt:,.0f} \\\\")
L += ["\\bottomrule", "\\end{tabular}", "\\end{table}", ""]

# A7: chronology (commit hashes from the repository's history)
chron = [
    ("Prediction record frozen", "pre-stated", "5277480"),
    ("Analysis plan; lead case", "pre-stated", "ea0564b"),
    ("Design analysis and reading rules", "pre-stated", "08a6180"),
    ("Quantity definitions, splice rule, verdict bands, Netflix calibration rule", "pre-stated", "66f9c25"),
    ("Outcome data first opened; exempt services removed; series rescaled to the report's 2014 (sensitivity); affiliation payments as a pass-through observable", "post hoc", "c2e6fa4"),
    ("Closure and uptake definitions (before those sources were opened)", "pre-stated for those sources", "1e61069"),
    ("Closures reported as bounds; multiverse over calibrations", "post hoc", "40c7076"),
    ("Growth-based calibrations", "post hoc", "187b4c5"),
    ("Direct employment (reading rule 6; the 2012--2015 trend comparator chosen then)", "rule pre-stated, comparator post hoc", "f952668"),
    ("Model-implied uptake scenarios; fees per subscriber against Table~14", "post hoc", "ecde24b"),
    ("Uptake scenarios held flat per year", "post hoc, correction", "cc360dd"),
    ("Rising uptake paths", "post hoc", "ff1154c"),
    ("Changes stated after inflation (descriptive)", "post hoc", "764a690"),
    ("Model check and offset model", "post hoc", "3867d78"),
    ("Rule for splitting distributors' revenue into subscribers and revenue per subscriber", "post hoc, fixed before computing", "4a722a0"),
    ("That split; corrected residual check; coverage check; sensitivity range to 8\\%", "post hoc", "2bbb326"),
]
L += ["\\begin{table}[htbp]", "\\centering", "\\small",
      "\\caption{Order of the analyses. Commit identifiers refer to the replication repository, listed in the order the commits were made.}",
      "\\label{tab:chronology}",
      "\\begin{tabular}{p{0.47\\textwidth}p{0.25\\textwidth}l}", "\\toprule",
      "Step & Status & Commit \\\\", "\\midrule"]
for step, status, h in chron:
    L.append(f"{step} & {status} & \\texttt{{{h}}} \\\\")
L += ["\\bottomrule", "\\end{tabular}", "\\end{table}", ""]

OUT.write_text("\n".join(L) + "\n")
print(f"wrote {OUT.relative_to(ROOT)}")
