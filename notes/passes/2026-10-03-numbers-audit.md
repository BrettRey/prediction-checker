<!-- Saved verbatim by the parent session (Claude Opus 5.5) from codex-stdout.txt of run 2 (gpt-6-astra, xhigh, read-only); see numbers-audit-2026-10-03/MANIFEST.md. -->

**Model: GPT-6 Astra (`gpt-6-astra`), running as Codex.**

## 1. Verdict

The principal revenue estimates, confidence intervals, uptake scenarios, inflation adjustments, Netflix calibrations, expenditure shares, and employment comparisons reproduce. This is nevertheless **not a clean numbers audit**: I found two definite rounding errors, thresholds and bounds stated more precisely than their computations support, and several descriptions that misidentify a number’s denominator, forecast status, ownership classification, or source location. These findings do not overturn the principal revenue results. They do require correction, particularly in the closure comparison and the description of 2015 spending. I audited the supplied `main.txt`, whose SHA-256 matches the manifest, and made no edits.

## 2. Problems

| # | Location and quoted phrase | Printed number | What the source says | Severity | Suggested fix |
|---|---|---:|---|---|---|
| 1 | §4: “3.1 standard errors from no effect” | 3.1 | Independent GLS using A2 inputs gives \(k=1.30306784\), SE \(=0.41294090\); their ratio is **3.15557946**, rounding to **3.2**. `make_tex_numbers.py` divides the already rounded \(k=1.30\) by SE 0.4129, producing 3.1. | error | Print **3.2**. Calculate derived statistics before rounding their inputs. |
| 2 | §5: “Between 8% and 10% … stopped operating” | Upper bound 10% | `closures_summary.csv`, `corus_counted_vi=False`, `VI A/B`: 38 services, 3 closed, 1 absent. Upper bound \(4/38=10.5263158\%\), rounding to **11%**. The stored share 0.105 undergoes a second rounding. | error | For this classification, print **8%–11%**, calculated directly from counts. |
| 3 | §5: integrated “8% … 10%”; independent “6% … 33%” | Both ranges | These use only the classification **excluding Corus from VI**. With Corus included, the same file gives VI \(5/80\)–\(9/80\) = **6.25%–11.25%**, and independent \(6/85\)–\(37/85\) = **7.06%–43.53%**. `input_checks_lttv.py` explains that the available owner field cannot implement the planned 2015 classification directly. | wording | Identify the ownership classification and report the alternative, especially the independent upper bound of approximately **44%**. |
| 4 | §2.1: “Against what existed … the report’s own figure for 2015 spending”; A1: “current at the testimony” | 2015; $3,258m; 12.2% | Nordicity Fig. 43 labels the year **’15F**: this is a forecast. The manuscript itself correctly recognizes 2015 as forecast elsewhere. \(399/3258=12.2468\%\) is correct arithmetic for that forecast denominator. The later CRTC total in `cpe_lttv.csv` is $3,285.8m, giving approximately **12.1%**. | inconsistency | Say “against the report’s **forecast for 2015**.” If making an actual-spending comparison, use and identify the CRTC denominator. |
| 5 | §5: “The CRTC counted 66,000 … 0.6% and 1.6% of all subscribers” | 66,000; 0.6%; 1.6% | April release: **“more than 66,000.”** June hearing ¶12: 177,000. The percentages divide these counts by the **2016 annual subscriber total**, 11,089,600 in the derived file, rather than contemporaneous April/June totals. The arithmetic is 0.59515% and 1.59609%. | wording | Preserve **“more than 66,000.”** Identify the denominator as the 2016 subscriber total and the shares as approximations using that denominator. |
| 6 | §4: interval changes “once the error exceeds 4.1%” / “exceeds 3.1%” | 4.1%; 3.1% | `crtc_outcomes_lttv.py` searches a grid in increments of 0.001. Those are the **first grid points** meeting the condition. Continuous thresholds from A2 are **4.0488529%** and **3.0441716%**. The condition already holds at the printed grid points. | wording | State approximately **4.05%** and **3.04%**, or explicitly call 4.1% and 3.1% the first qualifying grid values. |
| 7 | §4: releases “agree on 2016 to within 0.5%” | 0.5% | Distribution workbooks, sheet `1`, row 14: \(8,779,128.838/8,734,184.814-1=\) **0.5145761%**. Channels differ by 0.0608620%. | wording | Say “differ by **about 0.5% or less**,” or give the maximum as **0.515%**. “Within 0.5%” is a slightly too-tight bound. |
| 8 | §5: distributors “pass on 75% of their losses” | 75% | Nordicity ¶207 specifies 75 cents per dollar of retail loss **associated with Canadian services**; ¶206 assigns 86% of unbundling retail loss to those services. For that calculation, the combined proportion is \(0.75\times0.86=\) **64.5%** of total retail loss. §2 supplies the 86% qualification; §5 drops it. | wording | Specify “75% of the retail loss associated with Canadian services.” |
| 9 | Abstract: “the study’s two scenarios”; §2: “It modelled two worlds” | two | Nordicity ¶ii, p. 1 explicitly introduces **three** scenarios: baseline, LTTV impact, and unbundling revisited. The audit compares the first two. | wording | Say “two of the study’s three scenarios,” or name the two being compared. |
| 10 | §6 jobs reconciliation citation | “paras. 246, 248, 250, Tables 22–23, pp. 91–92” | ¶246 is on **p. 90**; Table 22 on p. 91; ¶¶248, 250 and Table 23 on p. 92. | error | Change the inclusive page locator to **pp. 90–92**, or attach separate locators. |
| 11 | Figure 1 caption, §4, A2 and A5: “2016 release” / “2020 release” | 2016; 2020 | These identify the **data vintages**. The bibliography dates their publication to **2017** and **2021**, respectively. | wording | Use “2016 and 2020 **data vintages**,” preserving publication years in citations. |

The report’s **18%** expenditure claim is correctly reproduced as an erroneous source claim: none of the twelve displayed calculations produces 18%. Likewise, A6 correctly identifies the source’s **10-FTE** component-total discrepancy; it is not an addition error introduced by this manuscript.

## 3. Independent pipeline recomputations

I used separate, read-only Python calculations. I did not execute production scripts that write files or write on import.

| Pipeline checked | Independent calculation and result | Assessment |
|---|---|---|
| `crtc_outcomes_lttv.py`: GLS | From A2’s \(B,I,Y\), calculated \(\delta=\log[B/(B-I)]\), \(y=\log(B/Y)\), and \(P=\min(h_i,h_j)^{-1}\), \(h=(2,3,4,5)\). Specialty/pay: **k 0.1175436615**, historical σ **0.0221389705**, SE **0.1764429864**, interval **[−0.2282845919, 0.4633719149]**. Distributors: **k 1.3030678355**, σ **0.0189080213**, SE **0.4129409041**, interval **[0.4937036635, 2.1124320076]**. | All printed estimates and intervals correct; distance error #1. |
| Cited-input bands | Scaled unbundling/preponderance by \(2/3\) and \(7/3\), and high-case closures by 2.5; projected the resulting log-shortfall paths using the same \(P\). Specialty/pay: **[0.75000655, 2.53615854]**. Distributors: **[0.79746960, 2.23533235]**. | Printed bands correct. |
| Uptake scenarios | Independently scaled each year’s uptake-driven components by scenario uptake divided by **0.05, 0.10, 0.15, 0.15**. Specialty/pay k values: **0.33464284, 0.39641151, 0.55973373, 1.00000000, 0.43297049, 0.68778658**. Distributor values: **0.43493562, 0.48106546, 0.59816535, 1.00000000, 0.51902405, 0.73147059**. | All A3 values and interval classifications correct. |
| `make_tex_numbers.py` / CPI | Raw Statistics Canada vector **v41693271**, Canada/all-items: **126.6 in 2015**, **136.0 in 2019**. Specialty/pay real change: \(4195.9/4289.7\times126.6/136-1=\) **−8.947263%**; nominal **−2.186633%**. Distributors: real **−12.699315%**, nominal **−6.217274%**. | −8.9%, −2.2%, −12.7%, −6.2% correct. |
| `extract_nordicity_figures.py` / A1 | Source Figs. 8–9: \(445+2710=\) **3155**; \(668+1507+469+66=\) **2710**. \(399/3155=\) **12.646593%**. \(352/(2710-668)=\) **17.238002%**. \(399/3258=\) **12.246777%**. Recomputed every other A1 share too. | All A1 arithmetic correct; 2015 label problem #4. |
| `netflix_calibration.py` | Read the Domestic Streaming Segment paid-membership rows directly from both local 10-Ks: **43.401, 47.905, 52.810, 58.486 million**. Against **45.5, 51.0, 54.8, 57.0**, log ratios are **−0.04722984, −0.06260575, −0.03698963, 0.02573614**. Pre-stated σ \(=|\log(58.486/57)|/2=\) **1.286807%**. Pooled σ **4.672775%**; growth-based 2018 σ **4.212693%**. | All A4 calibrations and intervals reproduce. |
| `input_checks_lttv.py`: uptake | \(177000/11089600=\) **1.596090%**; \(66000/11089600=\) **0.595152%**. Raw workbook subscriber total is **11,089,627**, whose rounding does not change either printed percentage. | Arithmetic correct; qualification/base problem #5. |
| `input_checks_lttv.py`: payments | Raw CMR `U-T11`, Canadian total: **3014.1** and **3124.8** million. Monthly payments using derived subscriber totals: **$22.33321774** and **$24.67661692**. Growth **10.492886%**; real growth **2.855878%**. Total real change **−3.492878%**. Report fees: \(20.83/20.51-1=\) **1.560215%**. | 10.5%, 2.9%, −3.5%, 1.6% correct. |
| `employment_lttv.py` | Read raw staff rows, subtract exempt-channel staff, and fit a line to 2012–2015. Channel trend slope **−75.025/year**; 2019 trend **5684.695**, actual **4402.94**, gap **−1281.755**. Distributor slope **−445.669/year**; 2018 gap **−395.617**, 2019 gap **1834.112**. Vintage difference **302.2**. | 1,282 below; 396 below; 1,834 above; 302 difference all correct. All A5 cells reproduce. |
| `closures_lttv.py` | Recounted `closures_crosswalk.csv` by owner/status: excluding Corus, VI **38 = 34 operating + 3 closed + 1 absent**; independent **127 = 85 + 8 + 34**. Including Corus, VI **80 = 71 + 5 + 4**; independent **85 = 48 + 6 + 31**. | Confirms #2 and #3. |
| `model_check_lttv.py` | Specialty/pay standardized fitted steps, using unrounded historical σ: **−1.61931, 0.19883, 0.44862, 0.02441**. Offset-model k/SE: specialty/pay **0.203209/0.183620**; distributors **1.229072/0.439619**. | Printed −1.6, maximum ≤0.5, 0.20 (0.18), and 1.23 (0.44) correct. |

The other printed distances also reproduce from unrounded calculations: specialty/pay distances from zero, one and the lower band are **0.6662, 5.0014, 3.5845**; scenario distances are **1.2304, 1.5805, 2.5061, 1.7877, 3.2319**. Distributors’ distance from one is **0.7339**, and from the counted-uptake scenario **2.1023**.

## 4. Full ledger

Values below follow `main.txt` in order. Repeated values are listed again. Each table row lists its individual cells rather than replacing them with a count.

**Source shorthand**

All CSV names below mean files in `data/derived/`; row locators are keys, not physical line numbers.

| Code | File or source |
|---|---|
| **N** | `/Users/brettreynolds/projects/LLM-CLI-projects/literature/nordicity_miller_2015_canadian_television_2020.md` and companion PDF. PDF page = printed page + 4. |
| **H** | Same literature directory, `canada_commons_chpc_2016-04-12_meeting8_evidence.md`. |
| **R** | Same directory, `crtc_2015-96_lets_talk_tv_world_of_choice.md`. |
| **UA / UJ** | Same directory, `crtc_2016-04-15_66000_basic_tv_package_release.md` / `crtc_2016-09-07_hearing_transcript_bdu_renewals.md`. |
| **FC / TF** | `nordicity_2015_scenarios.csv` / `nordicity_2015_text_facts.csv`. |
| **O / MV** | `crtc_lttv_outcomes.csv` / `crtc_lttv_multiverse.csv`. |
| **UP / SC** | `uptake_crtc.csv` / `uptake_conditional_lttv.csv`; scenario paths also in `uptake_conditional_paths_lttv.csv`. |
| **DA / NF** | `design_analysis_lttv.csv` / `netflix_calibration.csv`. |
| **PAY / PS / CPI** | `payments_canadian_lttv.csv` / `payments_per_subscriber_lttv.csv` / `cpi_canada_annual.csv`. |
| **CL / EMP / MC** | `closures_summary.csv` and `closures_crosswalk.csv` / `employment_lttv.csv` and `employment_lttv_summary.csv` / `model_check_lttv.csv`. |
| **CPE / CS / CC** | `cpe_lttv.csv` / `cpe_share_candidates.csv` / `cpe_components_2020.csv`. |
| **PLAN** | `notes/analysis-plan.md`, `scripts/plan_constants.py`, and the relevant calculation script. |
| **BIB** | `references-local.bib`, central `references.bib`, and available local source headers. Bibliographic metadata marked “ok” matches these files; it is not a fresh external catalogue audit. |
| **LAYOUT** | `main.tex`, section labels, figure/table labels and rendered pagination. |
| **S / D** | CSV quantity keys `specialty_pay_revenue` / `bdu_revenue`. |

### Title, abstract and introduction

| Location | Number(s), in order | Source and locator | Verdict |
|---|---|---|---|
| Title | 2016–2019 | PLAN, primary test years | ok |
| Date | 3rd October 2026 | `main.tex`, `\today`; audit manifest/build date | ok |
| Abstract | April 2016; 15,130; 2020 | H, Morrison’s opening statement, 0900–0905 | ok |
| Abstract | two scenarios | N ¶ii, p. 1: three scenarios; two selected here | #9 |
| Abstract | 2016–2019 | PLAN; O, selected years | ok |
| Abstract | 5%; 2016; 15% | TF `table18_byop_share_pct`, 2016 and 2018–2020; N Table 18 | ok |
| Abstract | 1.6%; mid-2016 | UP, 30 June 2016; UJ ¶12 | #5, denominator qualification |
| Abstract | “most” of the job figure | TF, 2020 specialty/pay + production: 10,060/15,130 | ok |
| Abstract | “more than half” spin-off | TF `table1_employment_spin-off/total`, 2020: 8,300/15,130 | ok |
| AI disclosure | 5.5 | `DECISIONS.md`, disclosure entry; commit `c4cb1a9`; audit manifest | ok as recorded provenance |
| Introduction heading | 1 | LAYOUT | ok |
| Opening sentence | 12 April 2016; 2020; 15,130 | H, date/header and Morrison opening statement | ok |
| Citation | 2016; 0900–0905 | H, document date and surrounding time marks | ok |
| Entry package | $25 | R ¶26 | ok |
| Pagination/header | 1; 1; 2 | LAYOUT, page 1 footer and page 2 running header | ok |
| CRTC citation | 2015 | R, 19 March 2015 | ok |
| Sponsors | four other organizations | N title page: ACTRA, CMG, DGC, Friends, Unifor | ok |
| Study citation/horizon | 2015; 2020 | N title/date and forecast horizon | ok |
| Harrington citation | 1999; p. ii | `harrington_morgenstern_nelson_1999_rff_dp9918_partial.pdf`, abstract, printed ii | ok |
| Regulatory cases | 12; 25; 6 | Same abstract: 12 overestimates among 25, 6 underestimates | ok |
| Morgenstern citation | 2018; p. 285 | `morgenstern_2018_jbca_retrospective_analysis_environmental_regulation.pdf`, first page/abstract | ok |
| Simpson citations | 2014; 2014; pp. 319–320 | `simpson_2014_jbca_regulators_overestimate_costs.pdf`, pp. 319–320 | ok |
| Manski citation | 2011; p. 4 | `manski_2011_policy_analysis_incredible_certitude_pep10.pdf`, PDF page 4 | ok; PDF-page locator |
| Kane citation | 2026 | `kane_2026_after_sffa_predictions_ejw.md`, header | ok |
| “more than one baseline” | more than one | Kane, opening discussion of litigation-era and elevated later baselines | ok |
| Methods citations | 2014; 2020 | `gelman2014types.pdf`; `gelman-etal-2020-bayesian-workflow.pdf` | ok |
| Outcome definition | single number; 2016–2019; k=0; k=1 | PLAN, “What the outcome estimate is”; GLS definition | ok |
| Uptake assumptions | 5%; 2016; 15%; 2018 | TF, Table 18 rows | ok |
| Cited uptake range | 10%; 35% | N ¶201, p. 75; PLAN constants | ok |
| Counted uptake | 1.6%; June 2016 | UP, June row; UJ ¶12 | #5, denominator qualification |
| Main channel result | 0.12; 0.18; 95%; −0.23; 0.46 | MV `[S, as published, 2018 (pre-stated)]`; independent GLS | ok |
| Counted-uptake scenario | 0.33; 2016 | SC `[S, CRTC count]`; UP | ok |
| Running header | 2; 3 | LAYOUT, section/page numbers | ok |
| Distributor result | 1.30; 0.49; 2.11 | MV `[D, as published, 2018 (pre-stated)]` | ok |
| Distributor uptake scenario | 0.43; 2.1 standard errors | SC `[D, CRTC count]`; independent distance 2.1023 | ok |
| Further checks | Two | Following fee and staffing checks | ok |
| Fees comparison | 10.5%; 2015; 2019; 1.6% | PAY/PS, 2015 and 2019; TF Table 14 | ok |
| Staffing baseline | pre-2015 | EMP, trend fitted to 2012–2015 inclusive | ok as shorthand |
| Spin-off majority | more than half | TF, 8,300/15,130 = 54.8579% | ok |
| Roadmap | Section 2; Section 3; section 4; section 5; Section 6 | LAYOUT, matching sections | ok |
| CPI citation | 2026 | BIB `statcan2026cpi`; data licence/retrieval register | ok |

### Section 2

| Location | Number(s), in order | Source and locator | Verdict |
|---|---|---|---|
| Heading | 2 | LAYOUT | ok |
| Decision/package | March 2015; March 2016; $25; 2015; ¶26 | R, date and ¶26 | ok |
| Packaging deadlines | March 2016; December 2016; 2015; ¶47 | R ¶47 | ok |
| Concern quotation locator | 2015; ¶xxii; p. 5 | N, printed p. 5 | ok |
| Report/release dates | December 2015; January 2016; 2022 | N title page; `miller_2022_crtc_canadian_program_rights_market.md`, publication list, “Canadian Television 2020 … January 2016” | ok |
| Title/citation | 2020; 2015 | N title and date | ok |
| Scenario count/horizon | two; 2015; 2020 | N ¶ii, p. 1 | #9 for count; years ok |
| Baseline quotation locator | 2015; ¶ii; p. 1 | N ¶ii, printed p. 1 | ok |
| “gap between the two” | two | FC baseline and LTTV selected paths | ok |
| Headline forecast | 2020; 15,130; $1,411.1m; 6,830; 8,300 | TF, Table 1, 2020 employment/GDP rows | ok |
| Locator | 2015; ¶xliv; Table 1; p. 12 | N, printed p. 12 | ok |
| Uptake ramp | 5%; 2016; 10%; 2017; 15%; 2018 | TF, Table 18 | ok |
| Locator | 2015; Table 18; p. 76 | N, printed p. 76 | ok |
| Pass-through quote | 75% | N ¶207; qualified by the adjacent 86% clause | ok |
| Running header | 3; 4 | LAYOUT | ok |
| Canadian-service base | 86%; 2015; ¶¶206–207; p. 77 | N, printed p. 77 | ok |
| Closure assumptions | 2020; 10%; 25%; 2015; ¶¶232–233; p. 85 | N, printed p. 85; PLAN constants | ok |
| Revenue impacts | 2020; $970m; 23%; $858m; 9% | FC S/D, 2020; N ¶¶xxvi–xxvii. Ratios 23.3904%, 8.7856% | ok |
| Locator | 2015; ¶¶xxvi–xxvii | N executive summary | ok |
| Subheading | 2.1 | LAYOUT | ok |
| Hearing date | 12 April 2016 | H header | ok |
| Testimony quotation | 2020; 15,130; $400m; 18% | H, Morrison opening statement | ok as quotation |
| Locator | 2016; 0900–0905 | H | ok |
| Employment interpretation | 15,130; 8,300 | TF, Table 1, 2020 | ok |
| Expenditure claim’s stated base | 18%; 2020 | N ¶239 explicitly says 18% of baseline CPE in 2020 | ok as source’s stated claim |
| Reconstructed CPE | 2020; $3,155m; $399m; 12.6%; 18% | FC CPE 2020; CC A+B; CS. Actual ratio 12.6466%; 18% is source’s unreproduced claim | ok |
| Locator | 2015; ¶239; Figs. 8, 9, 43 | N, pp. 24, 87–88 | ok |
| Current-spending comparison | 2015; 12.2% | FC CPE 2015 = 3258, marked ’15F in N Fig. 43 | #4 |
| Candidate calculations | 12 shares; 9 denominators; two impact figures; 18% | CS: twelve rows, nine distinct denominators, numerators 399/352 | ok |
| Cross-reference | A1 | `sections/tables-lttv.tex`, CPE table | ok |
| Time since launch | one month | H, Morrison at 0920–0925; UA launch March 1 | ok |
| Morrison estimate | 4%; 2016; 0920–0925 | H, statement immediately before 0925 mark | ok |

### Section 3 and first part of Section 4

| Location | Number(s), in order | Source and locator | Verdict |
|---|---|---|---|
| Heading | 3 | LAYOUT | ok |
| Report paths | two | FC, selected baseline/LTTV paths | ok |
| Methods citations | 2014; 2020 | Local Gelman/Carlin and Bayesian Workflow sources | ok |
| Morgenstern locator | 2018; p. 286 | Local Morgenstern PDF, second page | ok |
| Kane citation/baselines | 2026; more than one | Local Kane source, opening comparison | ok |
| Design years/result | 2010–2014; about 99% | DA `[S, report, historical]`: min(0.998, 0.988) | ok |
| Running header | 4; 5 | LAYOUT | ok |
| Other design results | 86%; 9.1%; 63% | DA D: min(0.889,0.861); CPE σ 0.0906 and min(0.636,0.630) | ok |
| Estimand years/count | 2016–2019; four | PLAN and four A2 observations | ok |
| Estimand endpoints | k=0; k=1 | PLAN and GLS model | ok |
| Random-walk origin | 2014 | PLAN; N last actual year | ok |
| Interval/data count | 95%; four years | PLAN; \(k\pm1.96SE\), four observations | ok |
| Cross-reference | A2 | Matching input table | ok |
| Forecast paths | two | FC baseline/LTTV | ok |
| Input range | 10%; 35%; 2.5 times | PLAN constants; N ¶¶201, 230 | ok as selected pre-stated scaling |
| Netflix citation | 2019 | Local fiscal-2018 10-K, dated January 29, 2019 | ok |
| Netflix comparison | 57.0m; 2018; 58.5m; 1.3% | NF 2018: 57.0, 58.486; σ 0.01286807 independently | ok |
| Splice check | 2012–2014; 2%; 2017; 2021 | O/FC comparable years; PLAN tolerance; BIB vintage publication dates | ok |
| Heading/figure reference | 4; Figure 1 | LAYOUT | ok |
| Channels versus baseline | 0.8%; 4.6%; 2016; 2019 | O/FC S, 2016–2019; exact extremes 0.76609%, 4.59492% | ok |
| Channels versus forecast | 9.9%; 28.1% | O/FC S; exact extremes 9.86153%, 28.07998% | ok |
| Channel changes | 2.2%; 2015; 2019; 8.9% | O S endpoints; CPI endpoints | ok |
| Baseline period/reference | 2016–2019; A2 | FC S baseline 4172,4166,4173,4164 | ok; “flat” means approximately flat |
| Channel estimate/SE | 0.12; 0.18 | MV S, pre-stated; independent GLS | ok |
| Distances and lower band | 0.7; 5.0; 0.75; 3.6 | Independent values 0.6662,5.0014,0.7500065,3.5845 | ok |
| Interval and band | 95%; −0.23; 0.46; 0.75; 2.54 | MV/FC; independent GLS/projections | ok |
| Uptake range/reference | 10%; 35%; section 5; A3 | PLAN constants; matching references | ok |
| Counted scenario | June 2016; 1.6%; 0.33; 1.2 | UP/SC S; exact scenario distance 1.2304 | ok, with #5 qualification |
| Morrison scenario | 4%; 0.40; 1.6 | SC S Morrison; exact distance 1.5805 | ok |
| Low cited scenario | 0.56; 2.5 | SC S low end; exact distance 2.5061 | ok |
| Rising scenarios | two; 2016 | SC contains two rising paths starting in 2016 | ok |
| Running header | 4; 6 | LAYOUT | ok |

### Figures and remaining Section 4

In the figure-axis extraction, `main.txt` loses several minus signs. The corresponding existing figure images show the negative ticks correctly; this is a text-extraction issue, not a plotted-number error.

| Location | Number(s), in order | Source and locator | Verdict |
|---|---|---|---|
| Figure 1 y-axis, extracted order | 10; 5; 0; 5; 10; 15; 20 | `figures/lttv_paths`; last four are −5,−10,−15,−20 in the figure | ok; extraction issue |
| Figure 1 x-axes | 2012; 2014; 2016; 2018; 2012; 2014; 2016; 2018 | `figures_lttv.py`, `YEARS_OBS`/tick labels | ok |
| Figure 1 legend | 95% | `figures_lttv.py`, ±1.96σ√h transformed to levels | ok |
| Figure 1 caption | 1; 2012–2019; Figs. 41,42; June 2016 | LAYOUT; FC; UP | ok |
| Caption vintage selection | 2016 release; to 2015; 2020 release | O source column; figure script | #11 for “release”; splice years ok |
| Caption interval/σ | 95%; 2.2%; 1.9% | MV pre-stated S/D; figure code | ok |
| Historical/forecast division | Before 2015 | N chart ticks: ’14 actual, ’15F forecast | ok |
| Running header | 4; 7 | LAYOUT | ok |
| Figure 2 y-axis/label, extracted order | 3; 0; 1; 2; 1; 0; 1 | Figure: label defines 0/1; final tick is −1 | ok; extraction issue |
| Figure 2 x-axes | 1; 2; 3; 4; 5; 1; 2; 3; 4; 5 | `figures_lttv.py`, σ grid 0.01–0.05, percent axis | ok |
| Figure 2 legend | 95%; k=1 | Figure code, interval and forecast reference | ok |
| Figure 2 caption | 2; 95%; A4 | Figure code; matching calibration table | ok |
| Rising-to-Morrison result | 4%; 2019; 0.43; 1.8 | SC S, rising-to-Morrison; exact distance 1.7877 | ok |
| Rising-to-low result | 10%; 0.69; 3.2 | SC S, rising-to-low; exact distance 3.2319 | ok |
| Non-uptake components | zero; two | Scenario code retains exemption-order and closure components | ok as description of the implemented scenarios |
| Exemption-order citation | 2015; ¶xxiii | N executive summary | ok |
| Chronology reference | A7 | Matching table | ok |
| Distributor forecast gaps | 1.9%; 4.9% | O/FC D; exact magnitudes 1.88757%–4.88742% | ok |
| Distributor revenue/change | $8,919m; 2015; $8,364m; 2019; 6.2%; 12.7% | O D endpoints; CPI | ok |
| Distributor estimate/SE | 1.30; 0.41 | MV D pre-stated | ok |
| Distributor distances | 3.1; 0.7 | Independent distances 3.15558 and 0.73393 | #1 for 3.1; 0.7 ok |
| Distributor band/interval | 0.80; 2.24; 0.49; 2.11 | FC/MV D; independent projections | ok |
| Counted scenario/distance | 0.43; 2.1 | SC D counted; exact distance 2.10232 | ok |
| Sensitivity reference | Both intervals; figure 2 | S/D intervals and matching figure | ok |
| Channel sensitivity threshold | 4.1% | `crtc_lttv_cutoffs.csv`, S grid result; continuous 4.04885% | #6 |
| Widest calibration/upper interval | 4.7%; 0.85 | NF pooled; MV S pooled, upper 0.85 | ok |
| Distributor zero threshold | zero; 3.1% | Cutoff CSV D grid result; continuous 3.04417% | #6 |
| Channel zero inclusion | zero; A4 | Every displayed S calibration interval contains zero | ok |
| Running header | 5; 8 | LAYOUT | ok |
| Sensitivity citations | 2006; 2014 | Local Gelman/Stern; Gelman/Loken | ok |
| Pre-stated Netflix σ | 1.3% | NF `sigma_tech` | ok |
| Alternative calibrations | 2016; 4.4%; 4.7% | NF `sigma_tech_2016`, pooled | ok |
| Initial offset | 2016; 2015; 45.5m; 43.4m; 2018 | NF 2015; fiscal-2017 10-K published 2018 | ok |
| Netflix growth | 35%; 25%; 2015; 2018; 4.2% | NF: 34.75726%,25.27473%; growth σ 4.21269% | ok |
| Channel residual steps | 2014; 2016; −1.6; three; 0.5 | MC `std_innovation_2016...2019` | ok |
| Diagnostic sample size | four points | A2, four years | ok |
| Baseline gap year | 2015 | FC S, zero impact and ’15F source tick | ok |
| Channel baseline gap | $4,290m; 2.5%; $4,186m; 0.8%; 2014 | O/FC S; MC `crtc15`, `report15`, `gap15`, `gap14` | ok |
| Earlier gaps | none; 2012; 2013 | O/FC S: −0.01042%, −0.00016% using raw data | ok at the manuscript’s one-decimal-percent precision |
| Distributor standing gap | 1.3%; 1.5%; 2012; 2015 | O/FC D, 2012–2015; MC gaps | ok |
| Vintage agreement | 2016; 2020 releases; 2016; 0.5% | Raw workbook totals; MC `release_gap16` | #11 for release labels; #7 for bound |
| Offset model | 0.20; 0.18; 1.23; 0.44 | MC `k_off`, `se_k`; independent offset GLS | ok |

### Sections 5–6 and data note

| Location | Number(s), in order | Source and locator | Verdict |
|---|---|---|---|
| Heading | 5 | LAYOUT | ok |
| Uptake assumption/source estimate | 15%; 35%; 2015; ¶201; p. 75 | N ¶201/Table 18; PLAN | ok |
| April uptake | 66,000; five weeks; 2016a | UA opening paragraph | #5 for omitted “more than”; other values ok |
| June uptake | 177,000; 30 June 2016; 2016b; ¶12 | UJ ¶12 | ok |
| Shares/comparator | 0.6%; 1.6%; 5%; 2016 | UP; TF 2016 share | #5 for denominator/qualification; forecast share ok |
| Hearing date/locator | September 2016; 2016b; ¶5 | UJ date/header and ¶5 | ok |
| Baseline fee growth | 1.6%; 2015; 2019; 2015; Table 14; p. 67 | TF fee components; N printed p. 67 | ok |
| Pass-through | 75% | N ¶207’s Canadian-service loss base | #8 |
| Payments | $3,014m; 2015; $3,125m; 2019; 10.5% | PAY/PS endpoints | ok |
| Canadian share/source | 87.8%; 2019; Table U-T11 | PAY 2015 =87.82%; 2016–2019 range87.21%–88.01%; raw U-T11 | ok for “near” |
| Real payment changes | 3.5%; 2.9% | PAY/PS/CPI: −3.49288%, +2.85588% | ok |
| Running header | 6; 9 | LAYOUT | ok |
| Integrated-company offset locator | 2015; ¶227; p. 83 | N, printed p. 83 | ok |
| Wholesale code date/locator | January 2016; 2015; p. 73; n. 82 | N footnote 82: January 22, 2016 | ok |
| Both scenarios locator | both; 2015; p. 72; n. 80 | N footnote 80, maintained modelling rules | ok |
| Integrated closures | 8%; 10%; 2019–2020; 10% | CL Corus-excluded VI row; N closure assumption | #2 and #3 for observed range; years/assumption ok |
| Independent closures | 6%; 33% | CL Corus-excluded independent row | #3 |
| Descriptive CPE horizon | through 2019 | CPE 2016–2019: totals exceed each corresponding baseline | ok |
| Observable employment sectors | two; 2017; 2021 | EMP channels/distributors; BIB publication years | ok |
| Employment comparison years | 2015; 2012–2015 | EMP, baseline endpoint and trend fit | ok |
| Channel staff | 5,899; 2015; 4,403; 2019; 1,282; 800; 2019 | EMP channel rows/summary; TF channel direct impact 2019 | ok |
| Distributor staff gaps | pre-2015; 396; 2018; 1,834; 2019 | EMP distributor trend/summary | ok |
| Distributor forecast | 2,910; 2019; 2015; Table 22; p. 91 | TF distributor direct impact; N Table 22 | ok |
| Reversal | 2019; one-year | EMP 2018–2020: 26,103→27,887→25,768 | ok |
| Annual series reference | A5 | Matching table | ok |
| Vintage staff difference | two; 302; 2016 | Raw distribution staff rows: 26815.01−26512.81=302.2 | ok |
| Sensitivity years | 2018; 2019 | EMP, both comparisons shown | ok |
| Heading | 6 | LAYOUT | ok |
| Harrington locator | 1999; p. ii | Local Harrington abstract | ok |
| Distributor scenario distance | 2.1 | Independent distance 2.10232 | ok |
| Jobs reference/locator | A6; 2015; ¶246; ¶248; ¶250; Tables 22–23; pp. 91–92 | N pp.90–92 | #10 for inclusive page range |
| Headline split | 6,830; 15,130; 8,300 | TF Table 1, 2020 | ok |
| Production total | 7,180 | TF independent production, 2020 | ok |
| Running header | 6; 10 | LAYOUT | ok |
| Production split | 2,830; 4,350 | N Table 23 / TF production direct and total difference | ok |
| Broadcasting split | 7,950; 4,000; 3,950 | N ¶246 and Table 22 | ok |
| Channel/production share | 10,060; 66%; 2,880 | TF: 7180+2880=10060; /15130=66.4904% | ok |
| Spin-off majority | more than half | TF: 8300/15130 | ok |
| Morrison scenario | 4%; 0.40 | H; SC S Morrison | ok |
| Manski locator | 2011; p. 4 | Local Manski PDF page 4 | ok |
| Hypothetical “single number” / “second year” | single; second | Expository examples, not empirical statistics | ok |
| Limits heading | 6.1 | LAYOUT | ok |
| Cases/citation | one forecast; 2014 | This paper’s selected case; local Simpson source | ok |
| Uptake observation year | 2016 | UP contains only 2016 counts | ok |
| Robust-findings count | Four | Four following clauses | ok |
| Pre-policy gap | 2015; 2.5%; 0.8%; 2014 | MC S `gap15`, `gap14` | ok |
| Running header | 6; 11 | LAYOUT | ok |
| Intake provenance date | 3 October 2026 | `DECISIONS.md`, commit `346d355`, Brett-attributed provenance | ok as recorded provenance |
| Drafting model | 5.5 | `DECISIONS.md`, commit `c4cb1a9`; audit manifest | ok as recorded provenance |

### References

Identifiers such as DOI strings, dataset IDs and commit hashes are treated as whole identifiers, not decomposed into apparent numerical measurements.

| Reference/location | Numeric metadata in order | Source | Verdict |
|---|---|---|---|
| References page | 12 | LAYOUT | ok |
| CRTC choice decision | 2015; March 19; 2015-96; 2017-01-26; October 3, 2026; URL `2015/2015-96` | R header/archive URL; BIB `crtc2015worldofchoice` | ok |
| CRTC April release | 2016a; April 15; 66,000; 2017-07-20; October 3, 2026; URL `2016/04/...66-000...` | UA; `fetch_raw.sh` archive timestamp; BIB | ok; title correctly preserves “More than” |
| CRTC hearing | 2016b; September 7; September 7, 2016; volume 1; 2018-01-03; October 3, 2026; URL `2016/tb0907` | UJ; fetch script; BIB | ok |
| CRTC SFS 2016 | 2017; July 18; 2016; October 3, 2026; dataset `03a2af45-cddd-4139-824c-913b634af612` | BIB `crtc2017sfs2016`; raw workbook vintage | ok against local record |
| CRTC distribution dataset | 2019; October 28; 2013–2024; 2025-08-28; October 3, 2026; dataset `58e91edf-409e-464b-ab6c-092125abeea1` | BIB `crtc2019cmrbdu` | ok against local record; downloaded workbook additionally contains 2025 columns |
| CRTC SFS 2020 | 2021; June 17; 2020; October 3, 2026; dataset `180dfc4c-8c1a-4c31-8e29-84953476bb92` | BIB `crtc2021sfs2020`; raw workbook vintage | ok against local record |
| Gelman & Carlin | 2014; 9(6); 641–651; DOI `10.1177/1745691614551642` | `gelman2014types.pdf`, first page | ok |
| Gelman & Loken | 2014; 102(6); 460–465; DOI `10.1511/2014.111.460` | Local source/BIB | ok |
| Gelman & Stern | 2006; 60(4); 328–331; DOI `10.1198/000313006X152649` | Local PDF header/BIB | ok |
| Bayesian Workflow | 2020; November 2 | Local PDF title page: 2 Nov 2020 | ok |
| Harrington et al. | 1999; January; 99-18; 19(2); 297–322; 2000; October 3, 2026; URL `RFF-DP-99-18` | Local report title/header and BIB publication note | ok against local record |
| References page | 13 | LAYOUT | ok |
| Commons evidence | 2016; April 12; 008; 1st; 42nd; October 3, 2026; URL `42-1/...meeting-8` | H header/source URL | ok |
| Kane | 2026; 23(2); 485–508; October 3, 2026 | Local source header/retrieval note | ok |
| Manski | 2011; paper 10; 121(554); F261–F289; 2011; October 3, 2026; repository ID 58177 | Local report/BIB publication note | ok against local record |
| Miller | 2022; March 25; title 2022; 2025-06-09; October 3, 2026; URL `rp220714` | Local Miller header; BIB archival record | ok |
| Morgenstern | 2018; 9(2); 285–304; DOI `10.1017/bca.2017.17` | Local PDF first page | ok |
| Netflix fiscal 2017 | 2018; January 29; Form 10-K; December 31, 2017; October 3, 2026; SEC identifiers `1065280/000106528018000069/q4nflx201710k` | Local 10-K/BIB | ok |
| Netflix fiscal 2018 | 2019; January 29; Form 10-K; December 31, 2018; October 3, 2026; SEC identifiers `1065280/000106528019000043/form10k_q418` | Local 10-K/BIB | ok |
| Nordicity/Miller | 2015; December; title 2020; October 3, 2026; filename 2020 | N title page/retrieval record | ok |
| Simpson | 2014; 5(2); 315–332; DOI `10.1515/jbca-2014-0027` | Local PDF first page | ok |
| Statistics Canada | 2026; Table 18-10-0005-01; DOI `10.25318/1810000501-eng` | BIB/data register; raw CPI file/table identity | ok |

### Appendix A

| Location | Number(s), in order | Source and locator | Verdict |
|---|---|---|---|
| Running header | 14 | LAYOUT | ok |
| Estimation years | 2016,…,2019 | PLAN; A2 input rows | ok |
| Error distribution/summation | 0; σ²; s=2015 | PLAN; `crtc_outcomes_lttv.py`, covariance from 2014 | ok |
| Origin/covariance | 2014; σ²; t−2014; u−2014 | Same covariance construction | ok |
| GLS formula constants | Σ⁻¹; Σ⁻¹; 1; Σ⁻¹ | Standard GLS identities implemented by the script and independently recomputed | ok |
| Observations/interval | four; 95%; 1.96 | Four years; script’s normal interval constant | ok |
| Input references | A2; A3; A4 | Matching tables | ok |
| Simulation settings | 20,000; seed 20261003 | `design_analysis_lttv.py`: `NSIM`, RNG initialization | ok |
| Simulated worlds | two; k=0; k=1 | Same script’s N/F worlds; approximation described explicitly | ok |
| Classifier paths/worlds | two; two | Same script, `classify_rates` | ok |
| Historical calibration years | 2010–2014 | FC history; sample SD of annual log differences | ok |
| Netflix rationale locator | 2015; ¶137; p. 51 | N, printed p. 51 | ok |
| Calibration history/horizon | 2010–2014; 2018; h=4; 2014 | PLAN and NF rule | ok |
| Alternative endpoint years | 2016; 2017; 2016–2018; 2015 | NF calibration rows and script | ok |
| Pooled formula | e²₂₀₁₆/2; e₂₀₁₇; e₂₀₁₆; power 2; e₂₀₁₈; e₂₀₁₇; power 2; divisor 3 | `netflix_calibration.py`, three standardized random-walk increments | ok |
| Running header | 15 | LAYOUT | ok |
| Pooled horizons | 2014; h=2,3,4; e₂₀₁₅; 2015 | NF script and appendix formula | ok |
| Table-generation claim | A2–A4 | `make_tex_tables.py`, independent calculations and `check` calls | ok |

### Table A1

| Location | Number(s), in order | Source and locator | Verdict |
|---|---|---|---|
| Caption | A1; $399m; 2020; $352m; Figs. 8,9,43; 18%; ¶239; 18% | N/FC CPE 2020; CS/CC; H quotation | ok |
| All CPE baseline row | 2020; 399; 3,155; 12.6% | CS `A+B`, 399/3155 | ok |
| Programming services | 399; 2,710; 14.7% | CS `B`, 399/2710 | ok |
| Programming services | 352; 2,710; 13.0% | CS `B`, 352/2710 | ok |
| Excluding CBC/SRC | 399; 2,042; 19.5% | CS `B−C`, 399/2042 | ok |
| Excluding CBC/SRC | 352; 2,042; 17.2% | CS `B−C`, 352/2042 | ok |
| Excluding CBC/SRC, plus BDU | 399; 2,487; 16.0% | CS `B−C+A`, 399/2487 | ok |
| Specialty/pay | 399; 1,573; 25.4% | CS `D+F`, 399/1573 | ok |
| Specialty/pay | 352; 1,573; 22.4% | CS `D+F`, 352/1573 | ok |
| Specialty | 399; 1,507; 26.5% | CS `D`, 399/1507 | ok |
| LTTV total | 2020; 399; 2,756; 14.5% | CS `G`, 399/2756 | ok |
| “Current” total | 2015; 399; 3,258; 12.2% | CS `H`; N Fig.43 ’15F | #4 for status; values/arithmetic ok |
| Last actual total | 2014; 399; 3,324; 12.0% | CS `J`; N Fig.43 ’14 | ok |
| Component A | 2020; Fig.8; 445 | CC A; N Fig.8 2020 total | ok |
| Component B | 2020; Fig.9; 2,710 | CC B; N Fig.9 2020 total | ok |
| Component C | 2020; Fig.9; 668 | CC C; N Fig.9 CBC/SRC | ok |
| Component D | 2020; Fig.9; 1,507 | CC D; N Fig.9 specialty | ok |
| Component E | 2020; Fig.9; 469 | CC E; N Fig.9 private conventional | ok |
| Component F | 2020; Fig.9; 66 | CC F; N Fig.9 pay/PPV/VOD | ok |
| Component G | 2020; Fig.43; 2,756 | CC G; N Fig.43 | ok |
| Component H | 2015; Fig.43; 3,258 | CC H; N Fig.43 | ok as forecast |
| Component J | 2014; Fig.43; 3,324 | CC J; N Fig.43 | ok |
| Component N1 | 1 in identifier; 2020; Fig.43; 399 | CC N1; 352+47 | ok |
| Component N2 | 2 in identifier; 2020; Fig.43; 352 | CC N2; Fig.43 programming-services impact | ok |

### Table A2

| Location | Number(s), in order | Source and locator | Verdict |
|---|---|---|---|
| Running header | 16 | LAYOUT | ok |
| Caption | A2; four components; Figs.41,42; 2016; Figs.34–36,39,40; 2020 release; 2010–2014; A4 | FC component-source fields; N figures; O; historical inputs | #11 for release wording; others ok |
| Scaling constants | 0.10; 0.15; 0.35; 0.15; 2.5 | PLAN constants and band calculation | ok |
| Source filenames | 2015 in `nordicity_2015_scenarios.csv` | Actual filename/year | ok |
| Column years | 2016; 2017; 2018; 2019 | FC/O selected rows | ok |
| S baseline | 4,172; 4,166; 4,173; 4,164 | FC S, `baseline_level`, 2016–2019 | ok |
| S impact | 200; 490; 809; 888 | FC S, `impact_total`; sums of four components | ok |
| S unbundling | 138; 282; 436; 451 | FC S `unbundling`; N Figs.35/41 | ok |
| S preponderance | 9; 49; 122; 147 | FC S `preponderance_access`; N Figs.36/41 | ok |
| S exemption order | 53; 102; 145; 186 | FC S `exemption_order`; N Figs.39/41 | ok |
| S closures | 0; 57; 106; 104 | FC S `closures`; N Fig.41; 2016 zero inferred from matching pre-closure level | ok |
| S observed | 4,363.7; 4,299.7; 4,219.3; 4,195.9 | O S, 2016–2019; raw 2020 discretionary sheet1 row14 minus sheet10 row14, /10⁶ | ok |
| S δ | 0.0491; 0.1251; 0.2155; 0.2399 | Independently calculated from preceding B/I | ok |
| S y | −0.0449; −0.0316; −0.0110; −0.0076 | Independently calculated from preceding B/Y | ok |
| S history | 2010–2014; 3,475; 3,748; 3,968; 4,091; 4,216 | FC S historical baseline; N Fig.41 | ok |
| S volatility | 2.2% | Sample SD of four annual log changes =2.213897% | ok |
| S band | 0.75; 2.54 | Independent band 0.75000655–2.53615854 | ok |
| D baseline | 9,149; 9,280; 9,428; 9,597 | FC D `baseline_level`, 2016–2019 | ok |
| D impact | 201; 479; 748; 803 | FC D `impact_total`; component sums | ok |
| D unbundling | 146; 298; 458; 473 | FC D `unbundling`; N Figs.34/42 | ok |
| D exemption order | 55; 104; 149; 191 | FC D `exemption_order`; N Figs.40/42 | ok |
| D closures | 0; 77; 141; 139 | FC D `closures`; N Fig.42; zero from pre-closure identity | ok |
| D observed | 8,779.1; 8,581.1; 8,424.4; 8,364.2 | O D; raw distribution sheet1 row14, /1000 | ok |
| D δ | 0.0222; 0.0530; 0.0827; 0.0874 | Independent B/I calculation | ok |
| D y | 0.0413; 0.0783; 0.1126; 0.1375 | Independent B/Y calculation | ok |
| D history | 2010–2014; 8,129; 8,571; 8,673; 8,927; 9,054 | FC D history; N Fig.42 | ok |
| D volatility | 1.9% | Sample SD =1.890802% | ok |
| D band | 0.80; 2.24 | Independent band 0.79746960–2.23533235 | ok |

### Table A3

| Location | Number(s), in order | Source and locator | Verdict |
|---|---|---|---|
| Running header | 17 | LAYOUT | ok |
| Caption | A3; A2; Table18; inverse powers −1 in projection; 2016 | Scenario formula; TF shares; SC paths | ok |
| Column years | 2016; 2017; 2018; 2019 | Scenario path years | ok |
| CRTC row | 30 June 2016; 1.6%; 1.6%; 1.6%; 1.6%; 0.33; 0.43 | SC counted scenario; independently projected | ok, with #5 denominator qualification |
| Morrison row | April 2016; 4.0%; 4.0%; 4.0%; 4.0%; 0.40; 0.48 | H; SC Morrison scenario | ok |
| Low cited row | 10.0%; 10.0%; 10.0%; 10.0%; 0.56; 0.60 | SC low-end scenario | ok |
| Report row | Table18; 5.0%; 10.0%; 15.0%; 15.0%; 1.00; 1.00 | TF Table18; projection of original path | ok |
| Rising-to-Morrison row | 2016; 1.6%; 2.4%; 3.2%; 4.0%; 0.43; 0.52 | SC/path CSV, linear interpolation | ok |
| Rising-to-low row | 2016; 1.6%; 4.4%; 7.2%; 10.0%; 0.69; 0.73 | SC/path CSV, linear interpolation | ok |
| Observed row | 95%; 0.12; −0.23; 0.46; 1.30; 0.49; 2.11 | MV pre-stated S/D; independent GLS | ok |

### Table A4

| Location | Number(s), in order | Source and locator | Verdict |
|---|---|---|---|
| Running header | 18 | LAYOUT | ok |
| Caption | A4; Table7; Form10-K; A2; 0.12; 1.30; zero | N Table7; local filings; MV; interval classification rule | ok |
| Panel (a) years | 2015; 2016; 2017; 2018 | NF annual rows | ok |
| Forecast row | 45.5; 51.0; 54.8; 57.0 | N Table7, p.51; `nordicity_2015_us_ott_forecast.csv` | ok |
| Membership row | 43.401; 47.905; 52.810; 58.486 | Raw 10-K domestic paid-membership rows, thousands converted to millions | ok |
| Log-ratio row | −0.0472; −0.0626; −0.0370; 0.0257 | Independent log(observed/forecast) | ok |
| Historical-only row | 2.2%; −0.23; 0.46; 1.9%; 0.49; 2.11 | NF/MV historical calibration; independent calculation | ok |
| 2016 row | 2016; 4.4%; 4.4%; −0.57; 0.81; 4.4%; −0.59; 3.20 | NF 2016/MV S,D; independent calculation | ok |
| 2017 row | 2017; 2.1%; 2.2%; −0.23; 0.46; 2.1%; 0.39; 2.22 | NF 2017/MV S,D | ok |
| Pre-stated row | 2018; 1.3%; 2.2%; −0.23; 0.46; 1.9%; 0.49; 2.11 | NF 2018/MV S,D | ok |
| Pooled row | 2016–2018; 4.7%; 4.7%; −0.61; 0.85; 4.7%; −0.70; 3.30 | NF pooled/MV S,D | ok |
| Growth row | 2015–2016; 1.5%; 2.2%; −0.23; 0.46; 1.9%; 0.49; 2.11 | NF growth2016/MV S,D | ok |
| Growth row | 2015–2017; 0.7%; 2.2%; −0.23; 0.46; 1.9%; 0.49; 2.11 | NF growth2017/MV S,D | ok |
| Growth row | 2015–2018; 4.2%; 4.2%; −0.54; 0.78; 4.2%; −0.50; 3.11 | NF growth2018/MV S,D | ok |
| Growth-pooled row | 2015–2018; 4.0%; 4.0%; −0.51; 0.74; 4.0%; −0.41; 3.02 | NF growth-pooled/MV S,D | ok |

### Tables A5–A7

| Location | Number(s), in order | Source and locator | Verdict |
|---|---|---|---|
| A5 caption | A5; 2016; 2016 release; 2020 release; 2012–2015; Table22 | EMP construction/raw staff row labels; N Table22 | #11 for release wording; others ok |
| A5 years | 2012; 2013; 2014; 2015; 2016; 2017; 2018; 2019; 2020 | EMP year rows | ok |
| Channels staff | 6,176; 6,116; 6,198; 5,899; 5,255; 4,769; 4,705; 4,403; 3,940 | EMP channels; raw discretionary staff rows minus exemptions | ok |
| Channels trend | 2012–2015; 6,210; 6,135; 6,060; 5,985; 5,910; 5,835; 5,760; 5,685; 5,610 | EMP channel trend; independently fitted from raw counts | ok |
| Channels direct impact | 0; −180; −440; −730; −800; −870 | TF `sector_fte_specialty_and_pay_tv_services_direct`, 2015–2020; N Table22 | ok |
| Distributors staff | 28,793; 28,894; 29,086; 27,244; 26,815; 27,056; 26,103; 27,887; 25,768 | EMP distributors; raw distribution staff rows | ok |
| Distributors trend | 2012–2015; 29,173; 28,727; 28,281; 27,836; 27,390; 26,944; 26,499; 26,053; 25,607 | EMP distributor trend; independently fitted from raw counts | ok |
| Distributor direct impact | 0; −730; −1,730; −2,710; −2,910; −3,110 | TF `sector_fte_bdus_direct`, 2015–2020; N Table22 | ok |
| Running header | 19 | LAYOUT | ok |
| A6 caption | A6; 2020; Tables1,22,23; ¶246; ¶248; ¶250; 10 | N tables/paragraphs; 1900+2010+50−3950=10 | ok |
| Broadcasting total | 4,000; 3,950; 7,950 | N ¶246/Table22; TF broadcasting direct/total | ok |
| Distributors | 3,110; 1,900; 5,010 | N Table22, 2020 | ok |
| Specialty/pay | 870; 2,010; 2,880 | N Table22, 2020 | ok |
| Private conventional | 20; 50; 70 | N Table22, 2020 | ok |
| Independent production | 2,830; 4,350; 7,180 | N Table23, 2020 | ok |
| Grand total | 6,830; 8,300; 15,130 | N Table1; broadcasting+production totals | ok |
| Chronology caption | A7 | LAYOUT | ok |
| Prediction record | `5277480` | `git log/show`: freeze prediction records | ok |
| Analysis plan | `ea0564b` | Git: adopt analysis plan/lead case | ok |
| Design analysis | `08a6180` | Git: design analysis before outcome commit | ok |
| Definitions/calibration rule | `66f9c25` | Git: definitions, bands, Netflix rule | ok |
| First outcome analysis | `c2e6fa4` | Git: preliminary CRTC outcomes | ok as documented chronology |
| Input definitions | `1e61069` | Git: pre-state closure/uptake definitions | ok |
| Bounds/calibration multiverse | `40c7076` | Git: multiverse and input checks | ok |
| Growth calibrations | `187b4c5` | Git: growth-based calibration | ok |
| Direct employment | reading rule 6; `f952668` | PLAN rule6; matching employment commit | ok |
| Uptake/fees | `ecde24b`; Table14 | Git: model-implied uptake/fees comparison; N Table14 | ok |
| Flat-path correction | `cc360dd` | Git: corrected flat uptake scaling | ok |
| Rising paths | `ff1154c` | Git: rising-path addition | ok |
| Inflation comparisons | `764a690` | Git: CPI/real changes | ok |
| Model check | `3867d78` | Git: residual/offset model check | ok |

## 5. Searches for unsourced numbers

**No substantive numeric statistic was classified as wholly unsourced.** The problems above concern arithmetic, precision, source interpretation, or locators.

For reproducibility, the key source-locating commands included:

```bash
rg --files ../../../literature |
  rg '(nordicity_miller_2015|chpc_2016-04-12|crtc_2015-96|crtc_2016-04-15|crtc_2016-09-07|harrington|morgenstern|simpson|manski|kane|miller_2022|gelman)'

rg -n -C 5 '15,130|400-million|18%|4%|0900|0905|0920|0925' \
  ../../../literature/canada_commons_chpc_2016-04-12_meeting8_evidence.md

rg -n -C 3 '177,000|practices certain' \
  ../../../literature/crtc_2016-09-07_hearing_transcript_bdu_renewals.md

rg -n -C 1 'Jan.*2016|2016.*Jan|Canadian Television 2020' \
  ../../../literature/miller_2022_crtc_canadian_program_rights_market.md

pdftotext -layout -f 28 -l 28 \
  ../../../literature/nordicity_miller_2015_canadian_television_2020.pdf -

pdftotext -layout -f 16 -l 16 \
  ../../../literature/nordicity_miller_2015_canadian_television_2020.pdf -

pdftotext -layout -f 5 -l 6 \
  ../../../literature/simpson_2014_jbca_regulators_overestimate_costs.pdf -

git log --reverse --format='%h %ad %s' --date=iso-strict
```

Other Nordicity passages were located in PDF text by the literal table headings and paragraph numbers listed in the ledger; raw Excel values were read with `openpyxl` by the sheet, row and year positions reported above.
