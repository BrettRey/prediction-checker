#!/usr/bin/env python3
"""[post hoc] Model check for the k estimates (case 2), added after the
outcome data was opened. Nothing here replaces the pre-stated reading.

1. Standardized one-step innovations of the baseline's error under the fitted
   k-only model at the pre-stated sigma: e_t = y_t - k delta_t, steps
   2014->2016 (variance 2 sigma^2), then yearly (sigma^2). After fitting k
   they're correlated, with covariance I - H (see 5 below), not independent N(0, 1).
2. An offset model, y_t = a + k delta_t + e_t, fitted by GLS under the same
   covariance, as a sensitivity: a one-time level gap between the report's
   baseline and the CRTC series would show up in a, not in k.
3. The report's own 2015 figure (marked '15F, itself a forecast; the report is
   dated December 2015 and its last actual year is 2014) against the CRTC's
   2015 count, measured against the same gap in 2012-2014, when the report's
   figures were actuals. 2015 carries no forecast impact, so a change in the
   gap from 2014 is baseline error observable without a counterfactual; a gap
   present in the actual years too is a standing difference between the two
   series, not a forecast miss.
4. Agreement between the CRTC's 2016 and 2020 releases for 2016, to check that
   the series' change of release isn't the source of any level gap.
5. (After the inference audit, notes/passes/2026-10-03-statistical-inference-audit.md.)
   The fitted innovations' correct reference: after fitting k their covariance
   is I - H, so each is also given divided by sqrt(1 - H_ii). The coverage of
   the interval for k = 1 when the forecast impact applies in dollars to the
   drifted baseline (the design simulation's version) and when it applies
   proportionally (the estimation model's). The distributors' counted-uptake
   gap in standard errors under the reported sensitivities. An illustration of
   sigma uncertainty: the interval with t(3) in place of 1.96, as if the
   historical volatility were estimated from its four changes.

Outputs: data/derived/model_check_lttv.csv, notes/results-lttv-modelcheck.md
"""
import csv
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crtc_outcomes_lttv import RAW, sheet_series  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DER = ROOT / "data" / "derived"
YEARS = [2016, 2017, 2018, 2019]
H = np.array([t - 2014 for t in YEARS], dtype=float)
SERIES = (("specialty_pay_revenue", "Specialty and pay revenue"), ("bdu_revenue", "Distributors' revenue"))


def rows(name):
    return list(csv.DictReader(open(DER / name)))


fc = {(r["quantity"], int(r["year"])): r for r in rows("nordicity_2015_scenarios.csv")}
obs = {}
for r in rows("crtc_lttv_outcomes.csv"):
    obs.setdefault((r["series"], int(r["year"])), float(r["value"]))  # first row: 2016 vintage to 2015, 2020 after
for r in rows("crtc_lttv_outcomes.csv"):
    if "2020 vintage" in r["source"]:
        obs[(r["series"], int(r["year"]))] = float(r["value"])
pre = {r["quantity"]: r for r in rows("crtc_lttv_multiverse.csv") if r["prestated"] == "True"}
mvall = rows("crtc_lttv_multiverse.csv")
paths_u = {(r["quantity"], int(r["year"])): float(r["impact"]) for r in rows("uptake_conditional_paths_lttv.csv")
           if r["uptake_label"] == "CRTC count, 30 June 2016"}
sigma_tech = float(next(r for r in rows("netflix_calibration.csv") if r["year"] == "sigma_tech")["log_ratio"])
T_DIFF = np.array([[1 / np.sqrt(2), 0, 0, 0], [-1, 1, 0, 0], [0, -1, 1, 0], [0, 0, -1, 1]])  # T'T = C^-1
T3 = 3.182446  # t quantile, 0.975, 3 degrees of freedom
rng = np.random.default_rng(20261003)
NSIM = 100_000

# CRTC 2016 in both releases (totals; exempt services are in both totals)
d16 = sheet_series(RAW / "sfs2016_discretionary_ondemand.xlsx", "1", "Total Revenue")
d20 = sheet_series(RAW / "sfs2020_discretionary_ondemand.xlsx", "1", "Total Revenue")
b16 = sheet_series(RAW / "sfs2016_distribution.xlsx", "1", "Total Revenue")
b20 = sheet_series(RAW / "sfs2020_distribution.xlsx", "1", "Total Revenue")
release_gap = {"specialty_pay_revenue": d20[2016] / d16[2016] - 1, "bdu_revenue": b20[2016] / b16[2016] - 1}

out, summary = [], {}
for q, label in SERIES:
    B = np.array([float(fc[(q, t)]["baseline_level"]) for t in YEARS])
    I = np.array([float(fc[(q, t)]["impact_total"]) for t in YEARS])
    Y = np.array([obs[(q, t)] for t in YEARS])
    delta, y = np.log(B) - np.log(B - I), np.log(B) - np.log(Y)
    hist = [float(fc[(q, t)]["baseline_level"]) for t in range(2010, 2015)]
    s = float(np.std(np.diff(np.log(hist)), ddof=1))  # exact historical volatility, which sets the pre-stated sigma
    assert s > sigma_tech and round(s, 4) == float(pre[q]["sigma"]), (q, s, pre[q]["sigma"])
    P = np.linalg.inv(s ** 2 * np.minimum.outer(H, H))
    k = (delta @ P @ y) / (delta @ P @ delta)
    assert round(k, 2) == float(pre[q]["k"]), (q, k, pre[q]["k"])
    e = y - k * delta
    step_h = np.diff(np.concatenate([[0.0], H]))
    z = np.diff(np.concatenate([[0.0], e])) / (s * np.sqrt(step_h))
    C = np.minimum.outer(H, H)
    assert np.allclose(T_DIFF.T @ T_DIFF, np.linalg.inv(C))
    x = T_DIFF @ delta
    Hm = np.outer(x, x) / (x @ x)
    var_z = np.diag(np.eye(len(YEARS)) - Hm)
    z_adj = z / np.sqrt(var_z)
    se = s / np.sqrt(delta @ np.linalg.inv(C) @ delta)
    # coverage of k = 1 under the two ways the forecast impact can meet the baseline's error
    eps = np.cumsum(rng.normal(0, s, size=(NSIM, 5)), axis=1)[:, [1, 2, 3, 4]]  # e at h = 2, 3, 4, 5
    Ci = np.linalg.inv(C)
    cover = {}
    for world, Ysim in (("dollars", B * np.exp(-eps) - I), ("proportional", (B - I) * np.exp(-eps))):
        ys = np.log(B) - np.log(Ysim)
        ks = (ys @ Ci @ delta) / (delta @ Ci @ delta)
        cover[world] = (float(np.mean(np.abs(ks - 1) <= 1.96 * se)), float(np.std(ks) / se))
    # distributors' counted-uptake gap in standard errors under the reported sensitivities
    du = np.log(B) - np.log(B - np.array([paths_u[(q, t)] for t in YEARS]))
    ku = (du @ Ci @ delta) / (delta @ Ci @ delta)
    def mv(version, cal):
        r = next(r for r in mvall if r["quantity"] == q and r["version"] == version and r["calibration"] == cal)
        return float(r["k_full"]), float(r["se"])
    gap_ses = {}
    for name, (kk, ss) in (("2017", mv("as published", "2017")), ("pooled", mv("as published", "pooled 2016-2018")),
                           ("rescaled", mv("rescaled to report's 2014", "2018 (pre-stated)"))):
        gap_ses[name] = (kk - ku) / ss
    X = np.column_stack([np.ones(len(YEARS)), delta])
    V = np.linalg.inv(X.T @ P @ X)
    a_off, k_off = V @ X.T @ P @ y
    se_a, se_k = np.sqrt(np.diag(V))
    ku_off = (V @ X.T @ P @ du)[1]  # the scenario projected in the offset model
    gap_ses["offset"] = (k_off - ku_off) / se_k
    gap_ses["prestated"] = (k - ku) / se
    sigma_enter = s * abs(k - ku) / (1.96 * se)  # sigma at which the counted-uptake scenario enters the interval
    gaps = {t: obs[(q, t)] / float(fc[(q, t)]["baseline_level"]) - 1 for t in range(2012, 2016)}
    gap15 = gaps[2015]
    assert float(fc[(q, 2015)]["impact_total"]) == 0
    summary[q] = dict(sigma=s, k=k, z=z, z_adj=z_adj, e=e, a_off=a_off, se_a=se_a, k_off=k_off, se_k=se_k, gap15=gap15,
                      gap12=gaps[2012], gap13=gaps[2013], gap14=gaps[2014], gap15_minus_14=gaps[2015] - gaps[2014],
                      report15=float(fc[(q, 2015)]["baseline_level"]), crtc15=obs[(q, 2015)], release_gap16=release_gap[q],
                      se=se, cover_dollars=cover["dollars"][0], sd_ratio_dollars=cover["dollars"][1],
                      cover_proportional=cover["proportional"][0], t3_lo=k - T3 * se, t3_hi=k + T3 * se,
                      ku=ku, sigma_enter=sigma_enter, **{f"gap_ses_{n}": v for n, v in gap_ses.items()})
    for t, et, zt, za, vz in zip(YEARS, e, z, z_adj, var_z):
        out.append(dict(quantity=q, key=f"residual_{t}", value=round(float(et), 4)))
        out.append(dict(quantity=q, key=f"std_innovation_{t}", value=round(float(zt), 2)))
        out.append(dict(quantity=q, key=f"std_innovation_var_{t}", value=round(float(vz), 4)))
        out.append(dict(quantity=q, key=f"std_innovation_adj_{t}", value=round(float(za), 4)))
    for key in ("sigma", "k", "a_off", "se_a", "k_off", "se_k", "gap12", "gap13", "gap14", "gap15", "gap15_minus_14",
                "report15", "crtc15", "release_gap16", "se", "cover_dollars", "sd_ratio_dollars", "cover_proportional",
                "t3_lo", "t3_hi", "ku", "sigma_enter", "gap_ses_2017", "gap_ses_pooled", "gap_ses_rescaled",
                "gap_ses_offset", "gap_ses_prestated"):
        out.append(dict(quantity=q, key=key, value=round(float(summary[q][key]), 4)))

with open(DER / "model_check_lttv.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["quantity", "key", "value"])
    w.writeheader()
    w.writerows(out)

L = ["# Results: case 2, model check [post hoc]",
     "<!-- SUMMARY: Generated by scripts/model_check_lttv.py; residual innovations, offset model, 2015 baseline gap, release agreement · status: generated · updated: 2026-10-03 -->",
     "", "Generated by `scripts/model_check_lttv.py`; do not edit by hand. Added after the outcome data was opened; "
     "the pre-stated reading is unchanged.", "",
     "| Series | sigma | k (pre-stated) | Std. innovations 2016-2019, divided by their SD under the fit | Offset a (SE) | k with offset (SE) | CRTC vs report, 2012-2015 | 2015 gap less 2014 gap | 2016: 2020 vs 2016 release |",
     "|---|---|---|---|---|---|---|---|---|"]
for q, label in SERIES:
    d = summary[q]
    L.append(f"| {label} | {d['sigma']:.4f} | {d['k']:.2f} | {', '.join(f'{v:+.2f}' for v in d['z_adj'])} | "
             f"{d['a_off']:+.3f} ({d['se_a']:.3f}) | {d['k_off']:.2f} ({d['se_k']:.2f}) | "
             f"{d['gap12']:+.1%}, {d['gap13']:+.1%}, {d['gap14']:+.1%}, {d['gap15']:+.1%} | {100 * d['gap15_minus_14']:+.1f} points | "
             f"{d['release_gap16']:+.2%} |")
for q, label in SERIES:
    d = summary[q]
    L.append(f"- {label}: coverage of k = 1 by the 95% interval when the impact applies in dollars to the drifted baseline "
             f"{d['cover_dollars']:.1%} (SD of k-hat {d['sd_ratio_dollars']:.2f} times the SE), proportionally {d['cover_proportional']:.1%}; "
             f"interval with t(3) {d['t3_lo']:+.2f} to {d['t3_hi']:+.2f}; counted-uptake scenario k {d['ku']:.2f}, "
             f"gap in SEs: pre-stated {d['gap_ses_prestated']:+.2f}, 2017 {d['gap_ses_2017']:+.2f}, pooled {d['gap_ses_pooled']:+.2f}, "
             f"rescaled {d['gap_ses_rescaled']:+.2f}, offset {d['gap_ses_offset']:+.2f}.")
L += ["", "A first innovation far from zero followed by small ones is the pattern of a one-time level gap; with four "
      "points it is also consistent with a random walk whose later steps happened to be small."]
(ROOT / "notes" / "results-lttv-modelcheck.md").write_text("\n".join(L) + "\n")
print("\n".join(L[6:]))
