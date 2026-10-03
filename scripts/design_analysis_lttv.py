#!/usr/bin/env python3
"""Design analysis for case 2 (Let's Talk TV), run before any outcome data.

Question: if we observe the actual 2016-2019 values of a quantity the report
forecast, could we tell a world where the forecast effect happened from a world
where it didn't? The answer depends on how far apart the report's two paths are
(baseline vs LTTV) relative to how wrong the baseline itself could plausibly be.

Generative model, for one quantity, years t = 2016..2019 (h = t - 2014 years
past the last actual in the report):
  counterfactual  C_t = B_t * exp(e_t),  e_t = sum of h iid N(0, sigma^2) steps
  world N (no policy effect):        Y_t = C_t
  world F (forecast effect occurs):  Y_t = C_t - k * I_t
where B_t is the report's baseline path, I_t its forecast impact, and k scales
the impact to the inputs the forecasters themselves cited (k = 1 is the report).
Administrative series are treated as measured without error.

For each sigma and k, simulate many paths in each world, then classify each
path by the likelihood ratio of the full 2016-2019 path (random-walk
covariance sigma^2 * min(h_i, h_j)) between "B_t" and "B_t - I_t" (the report's
own two paths). Report the share classified correctly in each world, and the
same for a single-year comparison (2018).

sigma grid: the historical estimate from the report's own 2010-2014 data, and
fixed values from 1% to 8% a year. The baseline's real forecast error is
unknown before outcomes are seen; the grid shows where discrimination fails.

Input scenarios for k (impact scale), from the record (case file, T20):
  unbundled uptake: report 15% by 2018; cited studies 10-20% (Corus), 15%
    (Rogers), "as many as 35%" (Oliver Wyman) -> unbundling and preponderance
    components scale by s/0.15
  closures: report 10% of vertically integrated A/B services; Bell suggested
    about 25% of its services, Oliver Wyman 26% unviable -> high = 2.5x
  low closures (0.5x), the exemption-order range (0 to 2x of its component),
  and the pass-through range are NOT cited by the report; they are this
  project's sensitivity choices and are labelled as such.

Outputs
  data/derived/design_analysis_lttv.csv
  notes/design-analysis-lttv.md   (tables generated from the CSV)
  figures/design_lttv_paths.png
"""
import csv
import math
from pathlib import Path

import numpy as np

from plan_constants import (CITED_CLOSURES_HIGH_MULT, CITED_UPTAKE_HIGH, CITED_UPTAKE_LOW,
                            REPORT_UPTAKE_2018)

ROOT = Path(__file__).resolve().parents[1]
SCEN = ROOT / "data" / "derived" / "nordicity_2015_scenarios.csv"
OUT_CSV = ROOT / "data" / "derived" / "design_analysis_lttv.csv"
OUT_MD = ROOT / "notes" / "design-analysis-lttv.md"
OUT_FIG = ROOT / "figures" / "design_lttv_paths.png"

YEARS = [2016, 2017, 2018, 2019]
QUANTS = {
    "specialty_pay_revenue": "Specialty and pay revenue",
    "bdu_revenue": "BDU retail revenue",
    "cpe": "Canadian programming expenditure",
}
SIGMAS = [0.01, 0.02, 0.03, 0.05, 0.08]
NSIM = 20000
RNG = np.random.default_rng(20261003)

# Impact-scale scenarios: multipliers per component. "cited" = from sources the
# report itself names; "project" = this project's sensitivity choice.
SCENARIOS = {
    "report": dict(unbundling=1, preponderance_access=1, exemption_order=1, closures=1,
                   basis="report's own inputs"),
    "low_cited": dict(unbundling=CITED_UPTAKE_LOW / REPORT_UPTAKE_2018, preponderance_access=CITED_UPTAKE_LOW / REPORT_UPTAKE_2018, exemption_order=1, closures=1,
                      basis="uptake 10% (Corus low end); other inputs as report"),
    "high_cited": dict(unbundling=CITED_UPTAKE_HIGH / REPORT_UPTAKE_2018, preponderance_access=CITED_UPTAKE_HIGH / REPORT_UPTAKE_2018, exemption_order=1, closures=CITED_CLOSURES_HIGH_MULT,
                       basis="uptake 35% (Oliver Wyman); closures 2.5x (Bell, Oliver Wyman)"),
    "low_project": dict(unbundling=CITED_UPTAKE_LOW / REPORT_UPTAKE_2018, preponderance_access=CITED_UPTAKE_LOW / REPORT_UPTAKE_2018, exemption_order=0, closures=0.5,
                        basis="project choice: uptake 10%, no OTT acceleration, half the closures"),
}


def load():
    rows = list(csv.DictReader(open(SCEN)))
    data = {}
    for r in rows:
        q, yr = r["quantity"], int(r["year"])
        num = lambda k: float(r[k]) if r.get(k) not in (None, "") else 0.0
        data[(q, yr)] = dict(
            B=num("baseline_level"), L=num("lttv_level"), I=num("impact_total"),
            unbundling=num("unbundling"), preponderance_access=num("preponderance_access"),
            exemption_order=num("exemption_order"), closures=num("closures"),
            programming_services_cpe=num("programming_services_cpe"),
            bdu_contributions=num("bdu_contributions"),
        )
    return data


def scaled_impact(data, q, yr, sc):
    d = data[(q, yr)]
    if q == "cpe":
        # CPE impacts are derived from the revenue impacts; scale each part by the
        # ratio of scaled to report impact in the revenue it comes from
        # (programming services <- specialty/pay revenue, BDU contributions <- BDU revenue).
        r_sp = scaled_impact(data, "specialty_pay_revenue", yr, sc) / max(data[("specialty_pay_revenue", yr)]["I"], 1e-9)
        r_bdu = scaled_impact(data, "bdu_revenue", yr, sc) / max(data[("bdu_revenue", yr)]["I"], 1e-9)
        return d["programming_services_cpe"] * r_sp + d["bdu_contributions"] * r_bdu
    return sum(d[k] * sc[k] for k in ("unbundling", "preponderance_access", "exemption_order", "closures"))


def historical_sigma(data, q):
    lv = [data[(q, y)]["B"] for y in range(2010, 2015)]
    g = np.diff(np.log(lv))
    return float(np.std(g, ddof=1)), [round(float(x), 4) for x in g]


def classify_rates(B, I_true, I_test, sigma):
    """Share correct in each world, full path and 2018 alone.
    B: baseline path; I_true: impact in world F; I_test: impact defining the
    report's LTTV path used by the classifier."""
    h = np.array([y - 2014 for y in YEARS], dtype=float)
    cov = sigma ** 2 * np.minimum.outer(h, h)
    prec = np.linalg.inv(cov)
    mu_N = np.log(B)
    mu_F = np.log(np.maximum(B - I_test, 1e-9))
    steps = RNG.normal(0, sigma, size=(NSIM, len(YEARS) + 2))  # 2015..2019 from 2014
    e = np.cumsum(steps, axis=1)[:, [h_ - 1 for h_ in h.astype(int)]]
    out = {}
    for world, I in (("N", np.zeros_like(B)), ("F", I_true)):
        y = np.log(np.maximum(B * np.exp(e) - I, 1e-9))
        dN, dF = y - mu_N, y - mu_F
        llr = -0.5 * (np.einsum("ij,jk,ik->i", dF, prec, dF) - np.einsum("ij,jk,ik->i", dN, prec, dN))
        call_F = llr > 0
        j = YEARS.index(2018)
        call_F_2018 = np.abs(y[:, j] - mu_F[j]) < np.abs(y[:, j] - mu_N[j])
        out[world] = (float(np.mean(call_F if world == "F" else ~call_F)),
                      float(np.mean(call_F_2018 if world == "F" else ~call_F_2018)))
    return out


def main():
    data = load()
    rows = []
    hist = {}
    for q in QUANTS:
        s_hat, growth = historical_sigma(data, q)
        hist[q] = (s_hat, growth)
        B = np.array([data[(q, y)]["B"] for y in YEARS])
        I_rep = np.array([data[(q, y)]["I"] for y in YEARS])
        for sname, sc in SCENARIOS.items():
            I_true = np.array([scaled_impact(data, q, y, sc) for y in YEARS])
            for sig_label, sigma in [("historical", s_hat)] + [(f"{s:.2f}", s) for s in SIGMAS]:
                res = classify_rates(B, I_true, I_rep, sigma)
                eff2018 = math.log(B[2]) - math.log(B[2] - I_true[2])
                sd2018 = sigma * math.sqrt(2018 - 2014)
                rows.append(dict(
                    quantity=q, scenario=sname, scenario_basis=sc["basis"],
                    sigma_label=sig_label, sigma=round(sigma, 4),
                    effect_2018_log=round(eff2018, 4), baseline_error_sd_2018=round(sd2018, 4),
                    effect_over_sd_2018=round(eff2018 / sd2018, 2),
                    correct_N_path=round(res["N"][0], 3), correct_F_path=round(res["F"][0], 3),
                    correct_N_2018=round(res["N"][1], 3), correct_F_2018=round(res["F"][1], 3),
                ))
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    write_md(data, rows, hist)
    plot(data, hist)


def write_md(data, rows, hist):
    L = []
    L.append("# Design analysis: case 2 (*Let's Talk TV*)")
    L.append("<!-- SUMMARY: Fake-data design analysis for the Nordicity/Miller forecast, run before any CRTC outcome data; "
             "generated by scripts/design_analysis_lttv.py · status: generated · updated: 2026-10-03 -->")
    L.append("")
    L.append("Generated by `scripts/design_analysis_lttv.py` from `data/derived/nordicity_2015_scenarios.csv` "
             "(itself extracted from the report's figures by `scripts/extract_nordicity_figures.py`). "
             "No outcome data were used. Do not edit by hand; rerun the script.")
    L.append("")
    L.append("## The report's two paths, 2016–2019 ($M)")
    L.append("")
    L.append("| Quantity | Year | Baseline | LTTV | Impact | Impact as share of baseline |")
    L.append("|---|---|---|---|---|---|")
    for q, name in QUANTS.items():
        for y in YEARS:
            d = data[(q, y)]
            L.append(f"| {name} | {y} | {d['B']:,.0f} | {d['L']:,.0f} | {d['I']:,.0f} | {d['I'] / d['B']:.1%} |")
    L.append("")
    L.append("## Historical volatility in the report's own data")
    L.append("")
    L.append("Standard deviation of annual log growth, 2010–2014 (four changes; a crude estimate).")
    L.append("")
    L.append("| Quantity | Annual log growth 2011–2014 | SD |")
    L.append("|---|---|---|")
    for q, name in QUANTS.items():
        s, g = hist[q]
        L.append(f"| {name} | {', '.join(f'{x:+.3f}' for x in g)} | {s:.3f} |")
    L.append("")
    L.append("## Can the outcome discriminate?")
    L.append("")
    L.append("Share of simulated worlds classified correctly by the full 2016–2019 path, "
             "in a world without the policy effect (N) and a world where the report's own impact occurs (F). "
             "0.5 is a coin toss. Scenario: report's inputs.")
    L.append("")
    L.append("| Quantity | Baseline error SD per year | Effect / error SD, 2018 | Correct if N (path) | Correct if F (path) | Correct if N (2018 only) | Correct if F (2018 only) |")
    L.append("|---|---|---|---|---|---|---|")
    for q, name in QUANTS.items():
        for r in rows:
            if r["quantity"] == q and r["scenario"] == "report":
                lab = f"{r['sigma']:.3f} (historical)" if r["sigma_label"] == "historical" else f"{r['sigma']:.2f}"
                L.append(f"| {name} | {lab} | {r['effect_over_sd_2018']:.1f} | {r['correct_N_path']:.2f} | "
                         f"{r['correct_F_path']:.2f} | {r['correct_N_2018']:.2f} | {r['correct_F_2018']:.2f} |")
    L.append("")
    L.append("## Sensitivity to the forecasters' own input ranges")
    L.append("")
    L.append("Size of the 2018 effect (log points) if the true impact followed other inputs, and that effect "
             "divided by the baseline's 2018 error SD at 3% and 5% a year. Ratios below about 2 mean the outcome "
             "could not separate that effect from baseline error. Scenarios marked 'project choice' use ranges the "
             "report does not cite.")
    L.append("")
    L.append("| Quantity | Scenario | Basis | Effect 2018 | Effect / SD at 3% | Effect / SD at 5% |")
    L.append("|---|---|---|---|---|---|")
    for q, name in QUANTS.items():
        for sname in SCENARIOS:
            r3 = next(r for r in rows if r["quantity"] == q and r["scenario"] == sname and r["sigma_label"] == "0.03")
            r5 = next(r for r in rows if r["quantity"] == q and r["scenario"] == sname and r["sigma_label"] == "0.05")
            L.append(f"| {name} | {sname} | {r3['scenario_basis']} | {r3['effect_2018_log']:.3f} | "
                     f"{r3['effect_over_sd_2018']:.1f} | {r5['effect_over_sd_2018']:.1f} |")
    L.append("")
    OUT_MD.write_text("\n".join(L) + "\n")


def plot(data, hist):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.4))
    for ax, (q, name) in zip(axes, QUANTS.items()):
        yrs = list(range(2010, 2021))
        B = np.array([data[(q, y)]["B"] for y in yrs])
        Lv = np.array([data[(q, y)]["L"] for y in yrs])
        s = hist[q][0]
        h = np.array([max(y - 2014, 0) for y in yrs])
        lo, hi = B * np.exp(-1.96 * s * np.sqrt(h)), B * np.exp(1.96 * s * np.sqrt(h))
        ax.fill_between(yrs, lo, hi, color="0.85", lw=0, label="baseline ±1.96 × historical SD")
        ax.plot(yrs[:5], B[:5], color="black", lw=1.5, label="actual (as reported)")
        ax.plot(yrs[4:], B[4:], color="black", lw=1, ls="--", label="baseline forecast")
        ax.plot(yrs[4:], Lv[4:], color="#b2182b", lw=1.5, label="LTTV forecast")
        ax.axvspan(2015.5, 2019.5, color="#2166ac", alpha=0.06, lw=0)
        ax.set_title(name, fontsize=10)
        ax.set_xticks([2010, 2014, 2016, 2018, 2020])
        ax.tick_params(labelsize=8)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("$M", fontsize=9)
    axes[0].legend(fontsize=7, frameon=False, loc="lower left")
    fig.tight_layout()
    OUT_FIG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_FIG, dpi=200)


if __name__ == "__main__":
    main()
