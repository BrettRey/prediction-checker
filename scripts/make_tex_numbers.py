#!/usr/bin/env python3
"""Write sections/numbers-lttv.tex: every number the case 2 text uses, as a
LaTeX macro computed from data/derived/. The manuscript types no numbers of
its own for this case; rerun this script after any upstream script.
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import plan_constants as PC  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DER = ROOT / "data" / "derived"
OUT = ROOT / "sections" / "numbers-lttv.tex"


def rows(name):
    return list(csv.DictReader(open(DER / name)))


def money(x):            # $M, thousands separator, no decimals
    return f"{x:,.0f}"


def pct(x, d=0):         # x is a share (0.12) -> "12\%"
    return f"{100 * x:.{d}f}\\%"


def num(x, d=1):         # signed number for math-free text
    s = f"{x:.{d}f}"
    return s.replace("-", "\\textminus ") if s.startswith("-") else s


M = {}

# Forecast (extracted from the report)
sc = {(r["quantity"], int(r["year"])): r for r in rows("nordicity_2015_scenarios.csv")}
tf = {(r["fact"], int(r["year"])): float(r["value"]) for r in rows("nordicity_2015_text_facts.csv")}
M["lttvJobsTotal"] = money(tf[("table1_employment_total", 2020)])
M["lttvJobsDirect"] = money(tf[("table1_employment_direct", 2020)])
M["lttvJobsSpinoff"] = money(tf[("table1_employment_spin-off", 2020)])
M["lttvGDPTotal"] = f"{tf[('table1_gdp_total', 2020)]:,.1f}"
M["lttvByopSixteen"] = pct(tf[("table18_byop_share_pct", 2016)] / 100)
M["lttvByopSeventeen"] = pct(tf[("table18_byop_share_pct", 2017)] / 100)
M["lttvByopEighteen"] = pct(tf[("table18_byop_share_pct", 2018)] / 100)
M["lttvCPEShareStated"] = pct(tf[("cpe_share_stated_pct", 2020)] / 100)
fte_bdu = tf[("sector_fte_bdus", 2020)]
fte_spec = tf[("sector_fte_specialty_and_pay_tv_services", 2020)]
fte_prod = tf[("sector_fte_independent_production", 2020)]
M["lttvFTEBDU"] = money(fte_bdu)
M["lttvFTESpec"] = money(fte_spec)
M["lttvFTEProd"] = money(fte_prod)
M["lttvFTESpecProd"] = money(fte_spec + fte_prod)
M["lttvFTESpecProdShare"] = pct((fte_spec + fte_prod) / tf[("table1_employment_total", 2020)])
for q, tag in (("specialty_pay_revenue", "Spec"), ("bdu_revenue", "BDU"), ("cpe", "CPE")):
    r = sc[(q, 2020)]
    M[f"lttv{tag}ImpactTwenty"] = money(float(r["impact_total"]))
    M[f"lttv{tag}BaselineTwenty"] = money(float(r["baseline_level"]))
    M[f"lttv{tag}ShareTwenty"] = pct(float(r["impact_total"]) / float(r["baseline_level"]), 1 if q == "cpe" else 0)
    for yr, w in ((2016, "Sixteen"), (2019, "Nineteen")):
        M[f"lttv{tag}ShareOfBaseline{w}"] = pct(float(sc[(q, yr)]["impact_share_of_baseline"]), 1)

# Outcomes: observed against the report's paths
obs = {(r["series"], int(r["year"])): float(r["value"]) for r in rows("crtc_lttv_outcomes.csv")}
for q, tag in (("specialty_pay_revenue", "Spec"), ("bdu_revenue", "BDU")):
    vsb = [obs[(q, y)] / float(sc[(q, y)]["baseline_level"]) - 1 for y in range(2016, 2020)]
    vsl = [obs[(q, y)] / float(sc[(q, y)]["lttv_level"]) - 1 for y in range(2016, 2020)]
    # magnitudes only; the text states the direction (checked here)
    assert all(v > 0 for v in vsb) or all(v < 0 for v in vsb), (q, vsb)
    assert all(v > 0 for v in vsl) or all(v < 0 for v in vsl), (q, vsl)
    M[f"lttv{tag}VsBaselineMin"] = pct(min(abs(v) for v in vsb), 1)
    M[f"lttv{tag}VsBaselineMax"] = pct(max(abs(v) for v in vsb), 1)
    M[f"lttv{tag}VsLTTVMin"] = pct(min(abs(v) for v in vsl), 1)
    M[f"lttv{tag}VsLTTVMax"] = pct(max(abs(v) for v in vsl), 1)
    M[f"lttv{tag}AboveBaseline"] = "above" if vsb[0] > 0 else "below"
    M[f"lttv{tag}AboveLTTV"] = "above" if vsl[0] > 0 else "below"
M["lttvBDURevFifteen"] = money(obs[("bdu_revenue", 2015)])
M["lttvBDURevNineteen"] = money(obs[("bdu_revenue", 2019)])
M["lttvBDURevDrop"] = money(obs[("bdu_revenue", 2015)] - obs[("bdu_revenue", 2019)])
M["lttvExemptSixteen"] = money(obs[("specialty_pay_revenue_incl_exempt", 2016)] - obs[("specialty_pay_revenue", 2016)])

# k at the pre-stated reading and the cited band
mv = [r for r in rows("crtc_lttv_multiverse.csv") if r["prestated"] == "True"]
ke = rows("crtc_lttv_k_estimates.csv")
for q, tag in (("specialty_pay_revenue", "Spec"), ("bdu_revenue", "BDU")):
    r = next(r for r in mv if r["quantity"] == q)
    M[f"lttvK{tag}"] = num(float(r["k"]))
    M[f"lttvK{tag}Lo"] = num(float(r["ci_lo"]))
    M[f"lttvK{tag}Hi"] = num(float(r["ci_hi"]))
    M[f"lttvSigmaRead{tag}"] = pct(float(r["sigma"]), 1)
    b = next(r for r in ke if r["quantity"] == q and r["version"].startswith("as published"))
    M[f"lttvBand{tag}Lo"] = num(float(b["band_lo"]))
    M[f"lttvBand{tag}Hi"] = num(float(b["band_hi"]))
cut = {r["quantity"]: float(r["sigma_inconclusive_from"]) for r in rows("crtc_lttv_cutoffs.csv")
       if r["version"].startswith("as published")}
M["lttvCutoffSpec"] = pct(cut["specialty_pay_revenue"], 1)
M["lttvCutoffBDU"] = pct(cut["bdu_revenue"], 1)

# Multiverse counts by calibration choice (series as published)
pub = [r for r in rows("crtc_lttv_multiverse.csv") if r["version"] == "as published"]
cals = list(dict.fromkeys(r["calibration"] for r in pub))
M["lttvNCalibrations"] = str(len(cals))
for q, tag in (("specialty_pay_revenue", "Spec"), ("bdu_revenue", "BDU")):
    inc = sum(1 for r in pub if r["quantity"] == q and r["verdict"].startswith("inconclusive"))
    M[f"lttvNInconclusive{tag}"] = str(inc)

# Technology calibration (Netflix)
nc = {r["year"]: r for r in rows("netflix_calibration.csv")}
M["lttvNetflixFcFifteen"] = f"{float(nc['2015']['forecast_us_netflix_m']):.1f}"
M["lttvNetflixObsFifteen"] = f"{float(nc['2015']['observed_us_paid_memberships_m']):.1f}"
M["lttvNetflixFcEighteen"] = f"{float(nc['2018']['forecast_us_netflix_m']):.1f}"
M["lttvNetflixObsEighteen"] = f"{float(nc['2018']['observed_us_paid_memberships_m']):.1f}"
fcg = float(nc["2018"]["forecast_us_netflix_m"]) / float(nc["2015"]["forecast_us_netflix_m"]) - 1
obg = float(nc["2018"]["observed_us_paid_memberships_m"]) / float(nc["2015"]["observed_us_paid_memberships_m"]) - 1
M["lttvNetflixFcGrowth"] = pct(fcg)
M["lttvNetflixObsGrowth"] = pct(obg)
M["lttvSigmaTech"] = pct(float(nc["sigma_tech"]["log_ratio"]), 1)
M["lttvSigmaTechSixteen"] = pct(float(nc["sigma_tech_2016"]["log_ratio"]), 1)
M["lttvSigmaTechPooled"] = pct(float(nc["sigma_tech_pooled_2016_2018"]["log_ratio"]), 1)
M["lttvSigmaGrowthEighteen"] = pct(float(nc["sigma_growth_2015_2018"]["log_ratio"]), 1)
M["lttvSigmaGrowthPooled"] = pct(float(nc["sigma_growth_pooled_2015_2018"]["log_ratio"]), 1)

# Design analysis (report's inputs, historical SD, full path)
da = rows("design_analysis_lttv.csv")
for q, tag in (("specialty_pay_revenue", "Spec"), ("bdu_revenue", "BDU"), ("cpe", "CPE")):
    r = next(r for r in da if r["quantity"] == q and r["scenario"] == "report" and r["sigma_label"] == "historical")
    M[f"lttvHistSD{tag}"] = pct(float(r["sigma"]), 1)
    M[f"lttvDesignCorrect{tag}"] = pct(min(float(r["correct_N_path"]), float(r["correct_F_path"])))

# Mechanisms, uptake, closures, CPE
pay = {int(r["year"]): r for r in rows("payments_canadian_lttv.csv")}
M["lttvPayCanFifteen"] = money(float(pay[2015]["to_canadian_services"]))
M["lttvPayCanNineteen"] = money(float(pay[2019]["to_canadian_services"]))
M["lttvPayShareFifteen"] = pct(float(pay[2015]["canadian_share"]), 1)
M["lttvPayShareNineteen"] = pct(float(pay[2019]["canadian_share"]), 1)
up = rows("uptake_crtc.csv")
M["lttvUptakeAprilN"] = money(float(up[0]["entry_level_subscribers"]))
M["lttvUptakeAprilShare"] = pct(float(up[0]["share"]), 1)
M["lttvUptakeJuneN"] = money(float(up[1]["entry_level_subscribers"]))
M["lttvUptakeJuneShare"] = pct(float(up[1]["share"]), 1)
cl = rows("closures_summary.csv")
vi = next(r for r in cl if r["corus_counted_vi"] == "False" and r["group"] == "VI A/B")
vic = next(r for r in cl if r["corus_counted_vi"] == "True" and r["group"] == "VI A/B")
ind = next(r for r in cl if r["corus_counted_vi"] == "False" and r["group"] == "independent A/B")
M["lttvClosVILo"] = pct(float(vi["share_closed_lower"]))
M["lttvClosVIHi"] = pct(float(vi["share_closed_upper"]))
M["lttvClosVICorusLo"] = pct(float(vic["share_closed_lower"]))
M["lttvClosVICorusHi"] = pct(float(vic["share_closed_upper"]))
M["lttvClosIndLo"] = pct(float(ind["share_closed_lower"]))
M["lttvClosIndHi"] = pct(float(ind["share_closed_upper"]))
cpe = {int(r["year"]): r for r in rows("cpe_lttv.csv")}
obs_cpe = [float(cpe[y]["total"]) for y in range(2016, 2020)]
base_cpe = [float(cpe[y]["report_baseline"]) for y in range(2016, 2020)]
M["lttvCPEObsMin"] = money(min(obs_cpe))
M["lttvCPEObsMax"] = money(max(obs_cpe))
M["lttvCPEBaseMin"] = money(min(base_cpe))
M["lttvCPEBaseMax"] = money(max(base_cpe))

# Plan constants and report assumptions (scripts/plan_constants.py)
M["lttvCitedUptakeLow"] = pct(PC.CITED_UPTAKE_LOW)
M["lttvCitedUptakeHigh"] = pct(PC.CITED_UPTAKE_HIGH)
M["lttvCitedClosuresMult"] = f"{PC.CITED_CLOSURES_HIGH_MULT:g}"
M["lttvSpliceTol"] = pct(PC.SPLICE_TOLERANCE)
M["lttvReportPassThrough"] = pct(PC.REPORT_PASS_THROUGH)
M["lttvReportCanShare"] = pct(PC.REPORT_CANADIAN_SHARE)
M["lttvReportClosuresVI"] = pct(PC.REPORT_CLOSURES_VI)
M["lttvReportClosuresIndep"] = pct(PC.REPORT_CLOSURES_INDEP)
# The report's pass-through rule applied to the observed 2015-2019 fall in BDU revenue
bdu_drop = obs[("bdu_revenue", 2015)] - obs[("bdu_revenue", 2019)]
M["lttvPassImplied"] = money(bdu_drop * PC.REPORT_CANADIAN_SHARE * PC.REPORT_PASS_THROUGH)
bdu_short19 = float(sc[("bdu_revenue", 2019)]["baseline_level"]) - obs[("bdu_revenue", 2019)]
M["lttvBDUShortfallNineteen"] = money(bdu_short19)
M["lttvPassImpliedBaseline"] = money(bdu_short19 * PC.REPORT_CANADIAN_SHARE * PC.REPORT_PASS_THROUGH)
# Direct employment (scripts/employment_lttv.py)
emp = {(r["sector"], r["key"]): float(r["value"]) for r in rows("employment_lttv_summary.csv")}
for sec, tag in (("channels", "Chan"), ("distributors", "Dist")):
    M[f"lttvStaff{tag}Fifteen"] = money(emp[(sec, "staff2015")])
    M[f"lttvStaff{tag}Nineteen"] = money(emp[(sec, "staff2019")])
    M[f"lttvStaff{tag}Change"] = money(abs(emp[(sec, "change")]))
    M[f"lttvStaff{tag}VsTrend"] = money(abs(emp[(sec, "vs_trend")]))
    M[f"lttvStaff{tag}VsTrendDir"] = "below" if emp[(sec, "vs_trend")] < 0 else "above"
    M[f"lttvStaff{tag}Forecast"] = money(abs(emp[(sec, "forecast2019")]))
M["lttvStaffDistVintageGap"] = money(abs(emp[("vintage", "distributors_2016")]))
M["lttvPayCanIncrease"] = money(float(pay[2019]["to_canadian_services"]) - float(pay[2015]["to_canadian_services"]))

lines = ["% Generated by scripts/make_tex_numbers.py from data/derived/. Do not edit by hand.",
         "% Every number in sections/case-lttv.tex comes from here."]
for k in sorted(M):
    lines.append(f"\\newcommand{{\\{k}}}{{{M[k]}}}")
OUT.write_text("\n".join(lines) + "\n")
print(f"{len(M)} macros -> {OUT.relative_to(ROOT)}")
