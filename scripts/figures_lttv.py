#!/usr/bin/env python3
"""Figures for case 2, from data/derived/ (no recomputation of the analysis
beyond rescaling: the standard error of k is proportional to sigma, because
the covariance is sigma^2 times a fixed matrix).

Figure 1 (figures/lttv_paths): each revenue series relative to the report's
  no-reform baseline, 2012-2019, with the report's forecast path, the report's
  chain at the uptake the CRTC counted (model-implied, post hoc), and the 95%
  range of the no-reform outcome at the pre-stated sigma. Both panels share
  one percentage scale.
Figure 2 (figures/lttv_k_sigma): k and its 95% interval as a function of the
  assumed annual baseline error sigma, with the calibrations marked and the
  band implied by the forecasters' cited inputs shaded.
"""
import csv
import math
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".house-style"))
from plot_style import COLORS, add_grid, save_figure, setup  # noqa: E402

DER = ROOT / "data" / "derived"
FIG = ROOT / "figures"
TEXT = {"secondary": "#C74F41", "tertiary": "#3D825D", "accent": "#4B7AA1"}  # WCAG AA text variants (style guide)
SERIES = (("specialty_pay_revenue", "Specialty and pay services' revenue"), ("bdu_revenue", "Distributors' revenue"))
YEARS_OBS = list(range(2012, 2020))
YEARS_FC = list(range(2014, 2020))


def rows(name):
    return list(csv.DictReader(open(DER / name)))


fc = {(r["quantity"], int(r["year"])): r for r in rows("nordicity_2015_scenarios.csv")}
obs = {}
for r in rows("crtc_lttv_outcomes.csv"):
    obs.setdefault((r["series"], int(r["year"])), float(r["value"]))
for r in rows("crtc_lttv_outcomes.csv"):
    if "2020 vintage" in r["source"]:
        obs[(r["series"], int(r["year"]))] = float(r["value"])
pre = {r["quantity"]: r for r in rows("crtc_lttv_multiverse.csv") if r["prestated"] == "True"}
mv = [r for r in rows("crtc_lttv_multiverse.csv") if r["version"] == "as published"]
paths = [r for r in rows("uptake_conditional_paths_lttv.csv") if r["uptake_label"] == "CRTC count, 30 June 2016"]
band = {r["quantity"]: (float(r["band_lo"]), float(r["band_hi"])) for r in rows("crtc_lttv_k_estimates.csv")
        if r["version"].startswith("as published")}

setup()
plt.rcParams.update({"mathtext.fontset": "custom", "mathtext.rm": "EB Garamond",
                     "mathtext.it": "EB Garamond:italic", "mathtext.bf": "EB Garamond:bold"})
FIG.mkdir(exist_ok=True)

# Figure 1
fig, axes = plt.subplots(1, 2, figsize=(6.5, 3.1), sharey=True)
for ax, (q, title) in zip(axes, SERIES):
    B = {t: float(fc[(q, t)]["baseline_level"]) for t in range(2012, 2020)}
    s = float(pre[q]["sigma"])
    h = np.array([t - 2014 for t in YEARS_FC], dtype=float)
    ax.fill_between(YEARS_FC, 100 * (np.exp(-1.96 * s * np.sqrt(h)) - 1), 100 * (np.exp(1.96 * s * np.sqrt(h)) - 1),
                    color=COLORS["light"], lw=0, label="95% range, no-reform outcome")
    ax.axhline(0, color=COLORS["dark"], lw=0.8, label="Report's no-reform baseline")
    ax.plot(YEARS_FC, [-100 * float(fc[(q, t)]["impact_total"]) / B[t] for t in YEARS_FC],
            color=TEXT["secondary"], lw=1.4, label="Report's forecast")
    sc = {int(r["year"]): -100 * float(r["impact"]) / float(r["baseline"]) for r in paths if r["quantity"] == q}
    ax.plot([2015] + sorted(sc), [0.0] + [sc[t] for t in sorted(sc)], color=TEXT["tertiary"], lw=1.4, ls="--",
            label="Report's model at counted uptake")
    ax.plot(YEARS_OBS, [100 * (obs[(q, t)] / B[t] - 1) for t in YEARS_OBS], color=COLORS["primary"], lw=1.6,
            marker="o", ms=3.5, label="CRTC outcome")
    ax.axvline(2015.5, color=COLORS["dark"], lw=0.5, ls=":")
    ax.set_title(title, fontsize=10)
    ax.set_xticks(YEARS_OBS)
    ax.set_xticklabels([f"{t}" if t % 2 == 0 else "" for t in YEARS_OBS])
    ax.set_xlim(2011.7, 2019.3)
    add_grid(ax, axis="y")
axes[0].set_ylabel("Difference from the report's\nno-reform baseline (%)")
axes[0].text(2015.6, axes[0].get_ylim()[1] * 0.92, "rules in force", fontsize=8, color=COLORS["dark"])
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", ncol=3, fontsize=8, frameon=False, bbox_to_anchor=(0.5, -0.02))
fig.tight_layout(rect=(0, 0.12, 1, 1))
save_figure(fig, FIG / "lttv_paths")
plt.close(fig)

# Figure 2
fig, axes = plt.subplots(1, 2, figsize=(6.5, 3.0), sharey=True, sharex=True)
grid = np.linspace(0.01, 0.05, 81)
for ax, (q, title) in zip(axes, SERIES):
    k, se_pre, s_pre = float(pre[q]["k"]), float(pre[q]["se"]), float(pre[q]["sigma"])
    for r in (r for r in mv if r["quantity"] == q):  # SE proportional to sigma: check against every calibration
        assert math.isclose(se_pre * float(r["sigma"]) / s_pre, float(r["se"]), abs_tol=0.002), r
    lo, hi = band[q]
    ax.axhspan(lo, hi, color=COLORS["light"], lw=0, label="Band from the forecasters' inputs")
    ax.fill_between(100 * grid, k - 1.96 * se_pre * grid / s_pre, k + 1.96 * se_pre * grid / s_pre,
                    color=COLORS["accent"], alpha=0.35, lw=0, label="95% interval for $k$")
    ax.axhline(k, color=COLORS["primary"], lw=1.4, label="Estimate of $k$")
    ax.axhline(0, color=COLORS["dark"], lw=0.8)
    ax.axhline(1, color=TEXT["secondary"], lw=0.8, ls="--", label="Forecast ($k=1$)")
    used = sorted({round(100 * float(r["sigma"]), 1) for r in mv if r["quantity"] == q})
    for u in used:
        ax.axvline(u, color=COLORS["dark"], lw=0.4, ls=":")
    ax.axvline(100 * s_pre, color=COLORS["dark"], lw=1.0)
    ax.text(100 * s_pre + 0.05, 3.25, "pre-stated", fontsize=7.5, color=COLORS["dark"])
    ax.set_title(title, fontsize=10)
    ax.set_xlim(1, 5)
    ax.set_xlabel("Assumed annual baseline error, σ (%)")
axes[0].set_ylim(-1, 3.5)
axes[0].set_ylabel("$k$ (0 = no effect, 1 = forecast)")
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", ncol=4, fontsize=8, frameon=False, bbox_to_anchor=(0.5, -0.02))
fig.tight_layout(rect=(0, 0.1, 1, 1))
save_figure(fig, FIG / "lttv_k_sigma")
plt.close(fig)
