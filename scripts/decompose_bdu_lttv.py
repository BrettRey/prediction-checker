#!/usr/bin/env python3
"""[post hoc] Distributors' revenue split into subscribers and revenue per
subscriber, against the report's own paths. Rule fixed in notes/analysis-plan.md
("Post hoc addition: distributors' revenue by subscribers and revenue per
subscriber", commit 4a722a0) before this was computed.

Identity: log(Y/B) = log(S/S_b) + log(A/A_b), with A = Y / (12 S) and the
report's A_b = B / (12 S_b), so it holds exactly.

The report's scenario by channel: unbundling and closures act on revenue per
subscriber (paras. 204-205, 236); the exemption order adds cord cutting at 125%
of the baseline rate from 2016 (para. 216, Tables 5 and 21: 1.875% against
1.5% of subscribers a year) and cord shaving at 125% of the baseline rate
(Tables 6 and 21) worth $15 a month each (para. 221). So the scenario's
subscriber path is S_L = S_b less cumulative incremental cord cutters, and
everything else is per subscriber. The reading is checked against the report's
own BDU exemption-order component before it's used.

Observed gaps are measured as the change from 2014, the model's origin, because
the CRTC and the report differ by stable amounts in 2012-2014; those rows are
reported too.

Outputs: data/derived/bdu_decomposition_lttv.csv, notes/results-lttv-bdu-decomposition.md
"""
import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DER = ROOT / "data" / "derived"
YEARS = list(range(2012, 2020))
TEST = [2016, 2017, 2018, 2019]
CUT_BASE, CUT_FACTOR = 0.015, 1.25                      # Table 5; para. 216 and Table 20
SHAVE_BASE = {2016: 0.04, 2017: 0.03, 2018: 0.02, 2019: 0.01}  # Table 6
SHAVE_DISCOUNT = 15.0                                    # $ a month, para. 221


def rows(name):
    return list(csv.DictReader(open(DER / name)))


fc = {int(r["year"]): r for r in rows("nordicity_2015_scenarios.csv") if r["quantity"] == "bdu_revenue"}
sa = {int(r["year"]): r for r in rows("nordicity_2015_bdu_subscribers_arpu.csv")}
obs = {}
for r in rows("crtc_lttv_outcomes.csv"):
    obs.setdefault((r["series"], int(r["year"])), float(r["value"]))  # 2016 edition to 2015
for r in rows("crtc_lttv_outcomes.csv"):
    if "2020 vintage" in r["source"]:
        obs[(r["series"], int(r["year"]))] = float(r["value"])


def f(r, k):
    return float(r[k]) if r[k] not in ("", None) else 0.0


B = {t: f(fc[t], "baseline_level") for t in YEARS}                    # $M
I = {t: f(fc[t], "impact_total") for t in YEARS}
Sb = {t: float(sa[t]["baseline_subscribers_thousands"]) for t in YEARS}  # thousands
ARPU19 = {t: float(sa[t]["baseline_monthly_arpu"]) for t in YEARS}
Ab = {t: 1000 * B[t] / (12 * Sb[t]) for t in YEARS}                   # $ a month per subscriber
Y = {t: obs[("bdu_revenue", t)] for t in YEARS}
S = {t: obs[("bdu_subscribers_thousands", t)] for t in YEARS}
A = {t: 1000 * Y[t] / (12 * S[t]) for t in YEARS}

# The scenario's subscriber path and the check against the report's exemption-order component
cut, shave, check = {}, {}, {}
cum_cut = cum_shave = 0.0
for t in YEARS:
    if t >= 2016:
        cum_cut += CUT_BASE * (CUT_FACTOR - 1) * Sb[t]
        cum_shave += SHAVE_BASE[t] * (CUT_FACTOR - 1) * Sb[t]
    cut[t], shave[t] = cum_cut, cum_shave
    blended = Ab[t] - 1000 * f(fc[t], "unbundling") / (12 * Sb[t])  # the rule's A_b; Fig. 19's ARPU gives much the same
    check[t] = 12 * (cum_cut * blended + cum_shave * SHAVE_DISCOUNT) / 1000   # $M
SL = {t: Sb[t] - cut[t] for t in YEARS}
AL = {t: 1000 * (B[t] - I[t]) / (12 * SL[t]) for t in YEARS}
# Beyond the rule, labelled as such in the text: the report's chain at the uptake the CRTC
# counted (unbundling scaled, exemption order and closures unchanged, as in table A3), whose
# subscriber path is the same S_L because the exemption order doesn't depend on uptake.
Iu = {int(r["year"]): float(r["impact"]) for r in rows("uptake_conditional_paths_lttv.csv")
      if r["quantity"] == "bdu_revenue" and r["uptake_label"] == "CRTC count, 30 June 2016"}
AU = {t: 1000 * (B[t] - Iu[t]) / (12 * SL[t]) for t in TEST}
# [post hoc] the same at the survey path (DECISIONS.md, commit 026f602)
Is_ = {int(r["year"]): float(r["impact"]) for r in rows("uptake_conditional_paths_lttv.csv")
       if r["quantity"] == "bdu_revenue" and r["uptake_label"].startswith("survey path")}
AS = {t: 1000 * (B[t] - Is_[t]) / (12 * SL[t]) for t in TEST}

out = []
for t in YEARS:
    o_sub, o_per = math.log(S[t] / Sb[t]), math.log(A[t] / Ab[t])
    out.append(dict(
        year=t, crtc_subscribers_k=round(S[t], 1), report_subscribers_k=Sb[t],
        crtc_rev_per_sub=round(A[t], 2), report_rev_per_sub=round(Ab[t], 2), report_fig19_arpu=ARPU19[t],
        obs_sub_gap=round(o_sub, 4), obs_per_gap=round(o_per, 4),
        obs_sub_change_from_2014=round(o_sub - math.log(S[2014] / Sb[2014]), 4),
        obs_per_change_from_2014=round(o_per - math.log(A[2014] / Ab[2014]), 4),
        fc_sub_part=round(math.log(SL[t] / Sb[t]), 4), fc_per_part=round(math.log(AL[t] / Ab[t]), 4),
        fc_total=round(math.log((B[t] - I[t]) / B[t]), 4),
        fc_counted_uptake_per_part=round(math.log(AU[t] / Ab[t]), 4) if t in AU else "",
        fc_survey_path_per_part=round(math.log(AS[t] / Ab[t]), 4) if t in AS else "",
        report_exemption_component=f(fc[t], "exemption_order"), reconstructed_exemption_component=round(check[t], 1)))
    r = out[-1]
    assert abs(r["fc_sub_part"] + r["fc_per_part"] - r["fc_total"]) < 2e-4
    assert abs(o_sub + o_per - math.log(Y[t] / B[t])) < 1e-9

with open(DER / "bdu_decomposition_lttv.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(out[0]))
    w.writeheader()
    w.writerows(out)


def pc(x):
    return f"{100 * (math.exp(x) - 1):+.1f}%"


L = ["# Results: distributors' revenue by subscribers and revenue per subscriber [post hoc]",
     "<!-- SUMMARY: Generated by scripts/decompose_bdu_lttv.py; CRTC subscribers and revenue per subscriber against the report's baseline and scenario · status: generated · updated: 2026-10-03 -->",
     "", "Generated by `scripts/decompose_bdu_lttv.py`; do not edit by hand. Rule: `notes/analysis-plan.md` (post hoc addition, commit 4a722a0).", "",
     "## Check of the scenario reading against the report", "",
     "| Year | Report's exemption-order component ($M) | Reconstructed from cutters and shavers ($M) | Ratio |", "|---|---|---|---|"]
for r in out:
    if r["year"] in TEST:
        L.append(f"| {r['year']} | {r['report_exemption_component']:.0f} | {r['reconstructed_exemption_component']:.0f} | "
                 f"{r['reconstructed_exemption_component'] / r['report_exemption_component']:.2f} |")
L += ["", "## Levels and gaps", "",
      "| Year | CRTC subs (k) | Report subs (k) | Subs gap | CRTC rev/sub ($) | Report rev/sub ($) | Fig. 19 ARPU | Rev/sub gap |",
      "|---|---|---|---|---|---|---|---|"]
for r in out:
    L.append(f"| {r['year']} | {r['crtc_subscribers_k']:,.0f} | {r['report_subscribers_k']:,.0f} | {pc(r['obs_sub_gap'])} | "
             f"{r['crtc_rev_per_sub']:.2f} | {r['report_rev_per_sub']:.2f} | {r['report_fig19_arpu']:.2f} | {pc(r['obs_per_gap'])} |")
L += ["", "## Decomposition, change from 2014 (observed) against the report's scenario", "",
      "| Year | Observed: subscribers | Observed: revenue per subscriber | Forecast: subscribers | Forecast: revenue per subscriber | Chain at counted uptake: per subscriber | Chain at survey path: per subscriber |",
      "|---|---|---|---|---|---|---|"]
for r in out:
    if r["year"] >= 2015:
        L.append(f"| {r['year']} | {pc(r['obs_sub_change_from_2014'])} | {pc(r['obs_per_change_from_2014'])} | "
                 f"{pc(r['fc_sub_part']) if r['year'] >= 2016 else '--'} | {pc(r['fc_per_part']) if r['year'] >= 2016 else '--'} | "
                 f"{pc(r['fc_counted_uptake_per_part']) if r['year'] >= 2016 else '--'} | "
                 f"{pc(r['fc_survey_path_per_part']) if r['year'] >= 2016 else '--'} |")
(ROOT / "notes" / "results-lttv-bdu-decomposition.md").write_text("\n".join(L) + "\n")
print("\n".join(L[5:]))
