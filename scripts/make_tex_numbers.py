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
cands = {r["denominator"]: float(r["share"]) for r in rows("cpe_share_candidates.csv")}
M["lttvCPEShareFifteen"] = pct(next(v for k, v in cands.items() if k.startswith("$399M / 2015 CPE")), 1)
M["lttvCPEShareFourteen"] = pct(next(v for k, v in cands.items() if k.startswith("$399M / 2014 CPE")), 1)
M["lttvCPENCandidates"] = str(len(cands))
M["lttvCPENDenominators"] = str(len({r["denominator_musd"] for r in rows("cpe_share_candidates.csv")}))
fte_bdu = tf[("sector_fte_bdus", 2020)]
fte_spec = tf[("sector_fte_specialty_and_pay_tv_services", 2020)]
fte_prod = tf[("sector_fte_independent_production", 2020)]
M["lttvFTEBDU"] = money(fte_bdu)
M["lttvFTESpec"] = money(fte_spec)
M["lttvFTEProd"] = money(fte_prod)
M["lttvFTESpecProd"] = money(fte_spec + fte_prod)
fte_conv = tf[("sector_fte_private_conventional_tv", 2020)]
fte_bcast = tf[("sector_fte_total_broadcasting_sector", 2020)]
M["lttvFTEConv"] = money(fte_conv)
M["lttvFTEBroadcast"] = money(fte_bcast)
M["lttvFTEBroadcastComponents"] = money(fte_bdu + fte_spec + fte_conv)
# the report's two splits of the total (paras. 246, 248, 250): direct and spin-off within each sector of origin
fte_bcast_d = tf[("sector_fte_total_broadcasting_sector_direct", 2020)]
fte_prod_d = tf[("sector_fte_independent_production_direct", 2020)]
assert fte_bcast_d + fte_prod_d == tf[("table1_employment_direct", 2020)]
assert (fte_bcast - fte_bcast_d) + (fte_prod - fte_prod_d) == tf[("table1_employment_spin-off", 2020)]
M["lttvFTEBroadcastDirect"] = money(fte_bcast_d)
M["lttvFTEBroadcastSpin"] = money(fte_bcast - fte_bcast_d)
M["lttvFTEProdDirect"] = money(fte_prod_d)
M["lttvFTEProdSpin"] = money(fte_prod - fte_prod_d)
M["lttvFTEBroadcastGap"] = money(fte_bdu + fte_spec + fte_conv - fte_bcast)
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
# Stand-alone changes 2015-2019 in nominal and real terms (CPI, Statistics Canada 18-10-0005-01).
# Comparisons with the report's paths need no deflator: both sides are nominal.
cpi = {int(r["year"]): float(r["cpi_all_items_2002_100"]) for r in rows("cpi_canada_annual.csv")}
infl = cpi[2019] / cpi[2015]
M["lttvCPIGrowth"] = pct(infl - 1, 1)


def change_pair(tag, a, b):
    nom, real = b / a - 1, b / a / infl - 1
    M[f"lttv{tag}NomChange"] = pct(abs(nom), 1)
    M[f"lttv{tag}NomDir"] = "rose" if nom > 0 else "fell"
    M[f"lttv{tag}RealChange"] = pct(abs(real), 1)
    M[f"lttv{tag}RealDir"] = "rose" if real > 0 else "fell"


change_pair("SpecRev", obs[("specialty_pay_revenue", 2015)], obs[("specialty_pay_revenue", 2019)])
assert M["lttvSpecRevNomDir"] == M["lttvSpecRevRealDir"], "text states one direction for both changes"
change_pair("BDURev", obs[("bdu_revenue", 2015)], obs[("bdu_revenue", 2019)])
M["lttvExemptSixteen"] = money(obs[("specialty_pay_revenue_incl_exempt", 2016)] - obs[("specialty_pay_revenue", 2016)])

# k at the pre-stated reading and the cited band
mv = [r for r in rows("crtc_lttv_multiverse.csv") if r["prestated"] == "True"]
kse = {}
ke = rows("crtc_lttv_k_estimates.csv")
for q, tag in (("specialty_pay_revenue", "Spec"), ("bdu_revenue", "BDU")):
    r = next(r for r in mv if r["quantity"] == q)
    M[f"lttvK{tag}"] = num(float(r["k"]), 2)
    M[f"lttvK{tag}SE"] = f"{float(r['se']):.2f}"
    kse[q] = (float(r["k_full"]), float(r["se"]), float(r["sigma"]))  # unrounded, for derived numbers
    M[f"lttvK{tag}Lo"] = num(float(r["ci_lo"]))
    M[f"lttvK{tag}Hi"] = num(float(r["ci_hi"]))
    M[f"lttvSigmaRead{tag}"] = pct(float(r["sigma"]), 1)
    M[f"lttvK{tag}HiTwo"] = f"{float(r['ci_hi']):.2f}"
    M[f"lttvK{tag}LoTwo"] = f"{float(r['ci_lo']):.2f}".replace("-", "\\textminus ")
    b = next(r for r in ke if r["quantity"] == q and r["version"].startswith("as published"))
    M[f"lttvBand{tag}Lo"] = num(float(b["band_lo"]), 2)
    M[f"lttvBand{tag}Hi"] = num(float(b["band_hi"]), 2)
    # distances in standard errors at the pre-stated calibration
    k_, se_, _ = kse[q]
    M[f"lttvK{tag}SEsFromZero"] = f"{abs(k_) / se_:.1f}"
    M[f"lttvK{tag}SEsFromOne"] = f"{abs(1 - k_) / se_:.1f}"
    M[f"lttvK{tag}SEsFromBandLo"] = f"{abs(float(b['band_lo']) - k_) / se_:.1f}"
cut = {r["quantity"]: float(r["sigma_inconclusive_from"]) for r in rows("crtc_lttv_cutoffs.csv")
       if r["version"].startswith("as published")}
# Exact sigma at which each pre-stated verdict turns inconclusive (interval contains both 0 and the
# band's lower end); the grid search in crtc_outcomes_lttv.py gives the first grid point past it.
for q, tag in (("specialty_pay_revenue", "Spec"), ("bdu_revenue", "BDU")):
    k_, se_, s_ = kse[q]
    b_lo = float(next(r for r in ke if r["quantity"] == q and r["version"].startswith("as published"))["band_lo"])
    need = max(s_ * abs(k_) / (1.96 * se_), s_ * abs(b_lo - k_) / (1.96 * se_))
    assert need <= cut[q] < need + 0.0011, (q, need, cut[q])
    M[f"lttvCutoff{tag}"] = pct(need, 1)

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
change_pair("PayCan", float(pay[2015]["to_canadian_services"]), float(pay[2019]["to_canadian_services"]))
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
indc = next(r for r in cl if r["corus_counted_vi"] == "True" and r["group"] == "independent A/B")


def clos_bounds(r):  # from the counts, not the rounded shares: closed / n and (closed + not listed) / n
    n, c, a = int(r["n_2015"]), int(r["closed"]), int(r["absent"])
    return pct(c / n), pct((c + a) / n)


M["lttvClosVILo"], M["lttvClosVIHi"] = clos_bounds(vi)
M["lttvClosVICorusLo"], M["lttvClosVICorusHi"] = clos_bounds(vic)
M["lttvClosIndLo"], M["lttvClosIndHi"] = clos_bounds(ind)
M["lttvClosIndCorusLo"], M["lttvClosIndCorusHi"] = clos_bounds(indc)
cpe = {int(r["year"]): r for r in rows("cpe_lttv.csv")}
obs_cpe = [float(cpe[y]["total"]) for y in range(2016, 2020)]
# the testimony's "of what now exists": the CRTC's count of 2015 spending (the report's 2015 figure is a forecast)
M["lttvCPECRTCFifteen"] = money(float(cpe[2015]["total"]))
M["lttvCPEShareCRTCFifteen"] = pct(float(sc[("cpe", 2020)]["impact_total"]) / float(cpe[2015]["total"]), 1)
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
    M[f"lttvStaff{tag}Eighteen"] = money(emp[(sec, "staff2018")])
    M[f"lttvStaff{tag}VsTrendEighteen"] = money(abs(emp[(sec, "vs_trend2018")]))
    M[f"lttvStaff{tag}VsTrendEighteenDir"] = "below" if emp[(sec, "vs_trend2018")] < 0 else "above"
M["lttvStaffDistVintageGap"] = money(abs(emp[("vintage", "distributors_2016")]))
M["lttvPayCanIncrease"] = money(float(pay[2019]["to_canadian_services"]) - float(pay[2015]["to_canadian_services"]))

# [post hoc] Forecast at other uptake levels (crtc_outcomes_lttv.py)
cond = rows("uptake_conditional_lttv.csv")
def cget(q, lab):
    return next(r for r in cond if r["quantity"] == q and r["uptake_label"].startswith(lab))
M["lttvKPredSpecObsUptake"] = f"{float(cget('specialty_pay_revenue', 'CRTC count')['k_predicted']):.2f}"
M["lttvKPredSpecMorrison"] = f"{float(cget('specialty_pay_revenue', 'Morrison')['k_predicted']):.2f}"
M["lttvKPredSpecCitedLow"] = f"{float(cget('specialty_pay_revenue', 'low end')['k_predicted']):.2f}"
M["lttvKPredBDUObsUptake"] = f"{float(cget('bdu_revenue', 'CRTC count')['k_predicted']):.2f}"
M["lttvKPredBDUMorrison"] = f"{float(cget('bdu_revenue', 'Morrison')['k_predicted']):.2f}"
M["lttvMorrisonUptake"] = pct(PC.MORRISON_UPTAKE_ESTIMATE)
M["lttvKPredSpecRiseMorrison"] = f"{float(cget('specialty_pay_revenue', 'rising from 2016 count to Morrison')['k_predicted']):.2f}"
M["lttvKPredSpecRiseCitedLow"] = f"{float(cget('specialty_pay_revenue', 'rising from 2016 count to low end')['k_predicted']):.2f}"
for lab, ltag in (("rising from 2016 count to Morrison", "RiseMorrison"), ("rising from 2016 count to low end", "RiseCitedLow")):
    r = cget("specialty_pay_revenue", lab)
    M[f"lttvKPredSpec{ltag}Where"] = "inside" if r["inside_interval"] == "True" else (
        "below" if float(r["k_predicted"]) < float(r["ci_lo"]) else "above")
for q, tag in (("specialty_pay_revenue", "Spec"), ("bdu_revenue", "BDU")):
    for lab, ltag in (("CRTC count", "ObsUptake"), ("Morrison", "Morrison"), ("low end", "CitedLow"),
                      ("rising from 2016 count to Morrison", "RiseMorrison"), ("rising from 2016 count to low end", "RiseCitedLow")):
        k_, se_, _ = kse[q]
        M[f"lttvKPred{tag}{ltag}SEs"] = f"{abs(float(cget(q, lab)['k_predicted_full']) - k_) / se_:.1f}"
    for lab, ltag in (("CRTC count", "ObsUptake"), ("Morrison", "Morrison"), ("low end", "CitedLow")):
        r = cget(q, lab)
        M[f"lttvKPred{tag}{ltag}Where"] = "inside" if r["inside_interval"] == "True" else (
            "below" if float(r["k_predicted"]) < float(r["ci_lo"]) else "above")
# [post hoc] Payments per subscriber against the report's baseline fee path
pps = {int(r["year"]): r for r in rows("payments_per_subscriber_lttv.csv")}
M["lttvPerSubFifteen"] = f"{float(pps[2015]['observed_monthly_payment_per_subscriber']):.2f}"
M["lttvPerSubNineteen"] = f"{float(pps[2019]['observed_monthly_payment_per_subscriber']):.2f}"
M["lttvPerSubGrowth"] = pct(float(pps[2019]['observed_monthly_payment_per_subscriber']) / float(pps[2015]['observed_monthly_payment_per_subscriber']) - 1, 1)
change_pair("PerSub", float(pps[2015]['observed_monthly_payment_per_subscriber']), float(pps[2019]['observed_monthly_payment_per_subscriber']))
M["lttvBaseFeeGrowth"] = pct(float(pps[2019]['report_baseline_monthly_fee']) / float(pps[2015]['report_baseline_monthly_fee']) - 1, 1)

# [post hoc] Model check (model_check_lttv.py)
mc = {(r["quantity"], r["key"]): float(r["value"]) for r in rows("model_check_lttv.csv")}
for q, tag in (("specialty_pay_revenue", "Spec"), ("bdu_revenue", "BDU")):
    z = [mc[(q, f"std_innovation_{t}")] for t in (2016, 2017, 2018, 2019)]
    M[f"lttvInnov{tag}First"] = num(z[0], 1)
    M[f"lttvInnov{tag}LaterMax"] = f"{max(abs(v) for v in z[1:]):.1f}"
    M[f"lttvK{tag}Offset"] = f"{mc[(q, 'k_off')]:.2f}"
    M[f"lttvK{tag}OffsetSE"] = f"{mc[(q, 'se_k')]:.2f}"
    M[f"lttvGapFifteen{tag}"] = pct(abs(mc[(q, 'gap15')]), 1)
    M[f"lttvGapFourteen{tag}"] = pct(abs(mc[(q, 'gap14')]), 1)
    M[f"lttvGapFifteenLessFourteen{tag}"] = f"{100 * abs(mc[(q, 'gap15_minus_14')]):.1f}"
    actual = [mc[(q, f"gap{y}")] for y in (12, 13, 14, 15)]
    M[f"lttvGapRangeLo{tag}"] = pct(min(abs(v) for v in actual), 1)
    M[f"lttvGapRangeHi{tag}"] = pct(max(abs(v) for v in actual), 1)
    M[f"lttvGapFifteen{tag}Dir"] = "above" if mc[(q, "gap15")] > 0 else "below"
    M[f"lttvReportFifteen{tag}"] = money(mc[(q, "report15")])
    M[f"lttvCRTCFifteen{tag}"] = money(mc[(q, "crtc15")])
M["lttvReleaseGapSpec"] = pct(abs(mc[("specialty_pay_revenue", "release_gap16")]), 1)
M["lttvReleaseGapBDU"] = pct(abs(mc[("bdu_revenue", "release_gap16")]), 1)
# widest calibration for the specialty interval (figure 2)
wide = max((r for r in pub if r["quantity"] == "specialty_pay_revenue"), key=lambda r: float(r["sigma"]))
M["lttvSigmaWidest"] = pct(float(wide["sigma"]), 1)
M["lttvKSpecHiWidest"] = num(float(wide["ci_hi"]), 2)

lines = ["% Generated by scripts/make_tex_numbers.py from data/derived/. Do not edit by hand.",
         "% Every number in sections/case-lttv.tex comes from here."]
for k in sorted(M):
    lines.append(f"\\newcommand{{\\{k}}}{{{M[k]}}}")
OUT.write_text("\n".join(lines) + "\n")
print(f"{len(M)} macros -> {OUT.relative_to(ROOT)}")
