# Analysis plan
<!-- SUMMARY: Proposed comparison grid and design analysis for cases 1–2, written before any outcome data; design analysis gates release of HELD rows · status: adopted 2026-10-03; case 2 reading rules fixed · updated: 2026-10-03 -->

Proposed and adopted 2026-10-03, before any outcome series was opened. It fixes what will be compared, so that later choices can be told apart from these. Anything decided after outcome data are opened goes in `DECISIONS.md` marked **[post hoc]**. Record row IDs refer to `source-verification.md`.

## Principles

1. **Each forecast is tested as a distribution built from the forecaster's own inputs, and also as the point figure given to legislators.** Howard says his cost estimate "should not be considered accurate to more than one significant digit" (CIA Doc. 214082, §5, PDF p. 11) and gives sensitivities (Table 3, PDF p. 14). The Nordicity report says which uptake studies it chose among: Oliver Wyman "as many as 35%", Corus "10-20%", Rogers "15%" (¶201, p. 75). Each chain is re-implemented as a script in `scripts/`, the inputs the forecasters themselves cited are propagated, and the outcome is placed against that interval as well as against the testimony's number.
2. **Design analysis before outcome data.** Gelman and Carlin (2014, *Perspectives on Psychological Science* 9(6), p. 643): "The design analysis can be performed before or after data collection and analysis." Fake-data simulation (Gelman et al. 2020, *Bayesian Workflow*, §4.1, p. 16) under "forecast true" and "forecast false", with realistic background variation, shows in advance whether the available series can tell the two apart. **Gate:** no HELD row is read and no outcome series is opened until the design analysis is committed.
3. **Every comparison in the grid is reported, not the striking one.** Gelman and Loken (2014, *American Scientist* 102(6), "The Way Forward"): "the best strategy is to move toward an analysis of all the data rather than a focus on a single comparison or small set of comparisons."
4. **Counterfactuals and baselines as a grid, not a choice.** What takes workflow beyond a single analysis is that "we are fitting many models while working on a single problem" (Gelman et al. 2020, §8, p. 42). Kane (2026, p. 486) does the same with his two baselines.
5. **A difference gets its own uncertainty.** "Observed outcomes tracked the baseline path and not the policy path" is a claim about a difference between two comparisons (Gelman and Stern 2006, *American Statistician* 60(4): 328–331), and is reported with its own interval.
6. **Full paths instead of test windows.** Each outcome is estimated over the whole period and compared with each forecaster's implied timing, so no single window has to be chosen.
7. **Where preregistration applies.** Gelman and Loken doubt it suits most applied work ("For most of our own research projects this strategy hardly seems possible"). Here the hypotheses were fixed by the forecasters years ago; only this grid is ours to fork, and committing it is cheap.

## Case 2 (lead): *Let's Talk TV*

Near mechanisms first, multiplier-derived totals last. Years 2016–2019 are the primary test; 2020 is reported separately (pandemic).

| # | Link | Forecast on record | Observable | Counterfactual needed? |
|---|---|---|---|---|
| 1 | Unbundled uptake | BYOP 5% (2016), 10% (2017), 15% (2018–2020) [T20]; Morrison "about 4%" of skinny basic [T16] | Share of BDU subscribers on the $25 basic or pick-and-pay | No: tests an input directly |
| 2 | Closures | 10% of vertically integrated Category A/B services, 25% of independent A/B services, one pay/PPV/VOD, no Category C news or sports, by 2020 [T20] | Licensed services that ceased operating, by ownership and category | Partly: compare with closures the baseline also implied, if it states any |
| 3 | Pass-through | 75% of BDU retail loss passed to Canadian services [T20] | Probably not observable directly; record as untestable unless wholesale-fee data exist | — |
| 4 | Subscribers and revenue | Baseline BDU subscribers 11.8M (2014) to 11.3M (2020) [T19]; baseline and LTTV revenue paths by year (Figs. 2–3) | BDU subscribers; BDU retail revenue; specialty and pay revenue | Observed path placed against both published paths |
| 5 | CPE | −$399M against baseline in 2020 (18%) [T05]; level $3.7B with LTTV [T19] | Canadian programming expenditure by year | Both paths |
| 6 | Employment and GDP | Table 1 paths, direct and spin-off [T02–T04] | Direct sector employment only; spin-off has no observable | Both paths; spin-off reported as untestable |

**Counterfactual grid.** (a) The report's own baseline. (b) The report's baseline corrected for its errors on technology-side quantities the policy didn't drive (OTT penetration, cord cutting), estimated from observed data. Results reported under both.

**Design analysis.** From the input ranges the report cites, how far apart are the baseline and LTTV paths in 2017–2019, relative to the spread those inputs produce? Where the bands overlap, the case can't discriminate on that quantity, and the plan says so before the data are seen.

**Data.** CRTC financial and subscriber releases and licensing decisions, identified and licensed at download (`data/README.md`). The CRTC's own *Let's Talk TV* decisions are needed first for the "intervention as enacted" rows [T13].

**Reading rules fixed by the design analysis** (2026-10-03, before any outcome data; results in `design-analysis-lttv.md`, generated by `scripts/design_analysis_lttv.py` from figure values extracted by `scripts/extract_nordicity_figures.py`):

1. **Direct input checks are primary** (rows 1–2 of the table above): they need no baseline. Uptake is read against the report's 5% / 10% / 15% and the cited range (10–35%); closures against 10% and 25%.
2. **Specialty and pay revenue is the primary model-level test.** The report's own 2016–2019 paths separate by 4.8% to 21% of baseline. At the historical volatility in the report's own 2010–2014 data (2.2% a year), the full path classifies correctly in about 99% of simulated worlds; at 5% a year, 84–90%; at 8%, 73–79%.
3. **BDU retail revenue is secondary.** The impact is 2–8% of baseline; it discriminates only if the baseline's error is near its historical 1.9% a year (about 86–89% correct), and not at 3% or more.
4. **CPE is descriptive only.** Its 2010–2014 volatility is 9% a year, at which the full path classifies correctly about 63% of the time. No conclusion about the forecast will rest on CPE.
5. **Baseline error is reported as a range, not chosen.** Results for the revenue paths are given at every annual error from 1% to 8%, since how wrong the technology-only baseline was can't be known before outcomes, and the random walk is a simple stand-in that a structural break (faster cord cutting) could exceed.
6. **Employment and GDP.** Spin-off impact has no observable and is reported as untestable; direct employment is tested only if a series with a pre-2015 level is found.

**Quantity definitions, fixed before any CRTC file is opened.** Each forecast quantity has the report's own scope; the observable must match it or the gap is recorded (Kane 2026, p. 486, on forecasts stated "in units that correspond to no publicly reported statistic").

| Quantity | Report's definition | Report's 2010–2014 values ($M) | Observable to use | If the observable doesn't match |
|---|---|---|---|---|
| Specialty and pay revenue | Advertising plus subscriber revenue of Canadian specialty services (including Category C news and sports, ¶232) and Canadian pay, PPV and VOD services; carriage fees for Canadian services only (Table 14); calendar year, else CRTC broadcast year (¶106) | 3,475; 3,748; 3,968; 4,091; 4,216 (Fig. 41) | Total revenue of Canadian discretionary and on-demand services (the CRTC's later name for specialty, pay, PPV and VOD) in CRTC aggregate financial summaries | Splice rule below |
| BDU retail revenue | Subscription revenue from TV service of cable, DTH/MDS and IPTV distributors: subscribers × TV ARPU (¶¶138, 147, 155); excludes internet and phone | 8,129; 8,571; 8,673; 8,927; 9,054 (Figs. 20, 42) | BDU revenue from broadcasting (TV) services in CRTC BDU financial summaries | Splice rule below |
| CPE | Programming services' CPE including CBC/SRC conventional (Fig. 9) plus BDU contributions to the CMF, independent funds and community channels (Fig. 8); LPIF excluded (¶187) | 3,183; 2,911; 3,165; 3,034; 3,324 (Fig. 43) | Sum of CRTC-reported CPE for the same service groups and BDU contributions | Splice rule below; CPE stays descriptive regardless |
| Unbundled uptake | "BYOP subscribers as a share of total subscribers" (Table 18): subscribers on the $25 entry-level service plus discretionary picks | none (0% in 2015) | Share of BDU TV subscribers on the entry-level service, with or without add-ons, from CRTC data | If no CRTC series: company disclosures, reported as partial coverage. If none: untestable, said so |
| Closures | Share of 2015 services shut by 2020: vertically integrated Category A/B, independent A/B, pay/PPV/VOD, Category C (¶¶232–233) | — | Services that stopped operating (no longer distributed or reporting revenue), 2016–2020, over the count operating in 2015, by ownership and category | Licence status alone isn't closure (small services were later exempted from licensing); count operation |

**Splice rule.** If a CRTC series reproduces the report's 2010–2014 values to within 2% in every year, it is used as is. Otherwise it is rescaled by the 2014 ratio of the report's value to the CRTC value, both versions are reported, and the definitional gap is described. The data vintage (release date) of every series is recorded; later revisions to 2014 move the random walk's starting point and are reported.

**What the outcome estimate is.** For each revenue quantity, the observed gap below the report's baseline is modelled as a multiple *k* of the report's own impact path, log B_t − log Y_t = k·δ_t + e_t, with e_t the baseline-error random walk of the design analysis, estimated over 2016–2019 by generalized least squares at each annual error SD. *k* = 0 is no effect; *k* = 1 is the report's forecast.

**Verdict bands, fixed now.** The forecasters' cited input range gives a band of *k*: the low-cited and high-cited scenarios of the design analysis expressed as multiples of the report's impact path (computed by the outcome script with the same scaling). With a 95% interval for *k*:

- interval includes both 0 and the low end of the band: **inconclusive**;
- interval entirely below the band: **effect smaller than the forecasters' own inputs imply** (and "no detectable effect" if it includes 0);
- interval overlaps the band: **consistent with the forecast range**, stating whether it includes *k* = 1;
- interval entirely above the band: **forecast exceeded**, i.e. revenue fell further than forecast. An outcome below the LTTV path is never reported as confirming the forecast.

Uptake and closures are read directly against the report's values and the cited ranges (uptake below 10%, 10–35%, above 35%; closures of vertically integrated A/B services below 10%, 10–26%, above 26%).

**Input checks, operational definitions** (fixed 2026-10-03 after the revenue series were opened but before the individual-service file was opened or any uptake source searched):

- *Closures.* Denominator: Canadian discretionary services (formerly Category A and B specialty; Category C and pay counted separately) that report revenue for the 2015 broadcast year in the individual-service summaries of the 2016 vintage. A service counts as closed if it reports no revenue in either 2019 or 2020 in the 2020 vintage, under its own name or a successor's. Renames and mergers are matched by licensee and service, and each match is recorded in a crosswalk file in `data/derived/`. Services that became exempt (2017 onwards) but keep filing as exempt are not closed. Ownership is classified by the 2015 owner: Bell Media, Rogers Media, Shaw Media and Québecor Média as vertically integrated; results are also shown with Corus counted as vertically integrated, since its control relationship with Shaw makes the classification arguable. If the individual summaries don't identify services or owners well enough to apply this, the check is reported as not done, not approximated.
- *Uptake.* Accepted in order: (1) a CRTC-published count or share of BDU subscribers on the entry-level service for any of 2016–2019; (2) company disclosures (annual reports, regulatory filings, earnings calls) by the large distributors, with the share of all subscribers they cover stated; (3) otherwise untestable. Pick-and-pay or small-package uptake is reported separately if found. The distribution summaries' section on companies operating only exempt systems is not uptake.

**Technology-forecast calibration (policy-independent).** The baseline's own error is the main threat, and it may be directional: if streaming took hold faster than assumed, revenue falls below the baseline with no policy effect, and the path test leans towards "F". The report's US forecasts couldn't be affected by Canadian regulation. Its Table 7 forecasts US Netflix subscribers (Trefis) of 51.0M, 54.8M, 57.0M and 58.7M for 2016–2019 (`data/derived/nordicity_2015_us_ott_forecast.csv`). The observable is Netflix's reported US paid streaming memberships at year end, from its annual reports. Rule: σ_tech = |log(observed 2018 / forecast 2018)| / √4. The main table is *read* at σ_read = max(historical SD, σ_tech), and results at every SD are still shown. If observed exceeds forecast, the write-up says the baseline was likely too optimistic about TV revenue and that the direction favours finding an effect. Table 7's composite OTT penetration is not used as the observable, because penetration definitions differ across sources (and Table 7's printed 2018–2019 rates don't match its own subscribers ÷ households).

**Post hoc addition: distributors' revenue by subscribers and revenue per subscriber** (written 2026-10-03, after the outcome series, including subscriber counts, were opened, and before this decomposition was computed). Purpose: to ask whether distributors' revenue loss came through subscriber numbers or through revenue per subscriber, since the report's channels differ on exactly that.

- *Identity.* With \(S_t\) the CRTC subscriber count and \(A_t = Y_t/(12 S_t)\) revenue per subscriber per month, and the report's baseline \(S^b_t\) (Fig. 17) and \(A^b_t = B_t/(12 S^b_t)\) (so the identity is exact; Fig. 19's ARPU is a check, expected within about 1%): \(\log(Y_t/B_t) = \log(S_t/S^b_t) + \log(A_t/A^b_t)\).
- *The report's scenario, by channel.* Unbundling lowers revenue per subscriber and leaves subscriber numbers alone (paras. 204–205). The exemption order adds cord cutting (Table 21: 1.875% of subscribers a year from 2016, printed 1.9%, against Table 5's 1.5%; para. 220) and cord shaving at $15 a month (para. 221). Closures are assigned to revenue per subscriber unless paras. 227–233 say otherwise. So \(S^L_t = S^b_t\) less cumulative incremental cord cutters (0.375% of \(S^b_t\) a year from 2016), and \(A^L_t = (B_t - I_t)/(12 S^L_t)\). Check of this reading against the report: incremental cutters × 12 × blended ARPU (\(A^b - \text{unbundling}_t/(12 S^b_t)\), about $3.64 below baseline in 2020 per para. 204) plus incremental shavers × $180 should come near the report's BDU exemption-order component (55, 104, 149, 191 for 2016–2019). If it is off by more than a few per cent, the scenario's subscriber path is reported as approximate, not tuned.
- *Alignment.* In 2012–2014, the report's actual years, CRTC subscribers sit 1.8–2.1% below the report's and CRTC revenue per subscriber 0.5–0.7% above (checked before this rule was written; 2016 subscribers differ by 0.3% between the CRTC's 2016 and 2020 editions). The decomposition is of the change in each log gap from 2014, the model's origin, and the 2012–2015 rows are printed.
- *Reading.* For each year 2016–2019, the forecast's subscriber and per-subscriber parts and the observed parts. An observed per-subscriber part at or above the baseline means unbundling's per-subscriber effect didn't appear (a second check on uptake, independent of \(k\)). An observed subscriber part beyond the scenario's means subscriber losses beyond what the report forecast in either world, which the paper attributes to no particular cause. Anything else is stated as the split it is. Descriptive, like the fee comparison: no interval, and it doesn't identify the true no-reform path.

## Case 1 (second): GNDA and life-insurance premiums

**Forecasts tested separately** (case file, sections A–B): the model (experience +36% / +58% at a $1M threshold, premium unquantified); B1 (+30% / +50%, "could", no timing); B2 ("likely", "soon after"); B3 (term life, "over time"); B4 (experience, more than a decade).

**Counterfactual grid (both, per Brett 2026-10-03).** Each answers a different question:

| Counterfactual | Question it answers | Corresponds to |
|---|---|---|
| (i) No restriction: the 2016 status quo | Did the forecast as made come true? | B1–B3 were forecasts against this world |
| (ii) CLHIA code only: no disclosure below $250,000 from 2018 | How much of any change is due to the Act? | The policy claim |

Also reported: the model's own threshold scenarios ($100k, $1M) placed on the regime ordering in the case file.

**Within-Canada contrast.** Under (ii), the Act's marginal effect falls only on amounts above $250,000. Price changes for the same profile and insurer at amounts above and below $250,000, before and after 2017–2018, isolate it from common drift (interest rates, mortality improvement, competition).

**Profiles.** Every sex × age × term × amount × smoking cell the series supports, pooled in a multilevel model rather than selected.

**Comparison jurisdiction.** A market without an equivalent restriction over the same years, to be identified and verified.

**Mechanism data.** CIA experience data [G11–G13]. B4 and the model both say experience moves slowly, so an unchanged A/E by 2023 is not evidence against the model; stated here in advance.

**Design analysis.** Simulate quote series with realistic drift and noise; ask whether a +30% / +50% step (B2), a gradual rise (B3), and no change can be told apart, with and without the above/below-$250,000 contrast.

**Feasibility gate.** No premium test without a fixed-profile quote series under usable terms. Candidates: COMPULIFE's historical product (terms to check; never committed) [G14]; archived published rate tables. If none, case 1 runs on the argument analysis alone (sections A–C of the case file: the threshold, the unlocated 30% / 50% [G18], the timing split).

**Lead to check.** Whether briefs or interventions in the Supreme Court decision on the Act [G07] repeated the premium forecast. If they did, case 1 has a forecast made to a court, as in Kane (2026).

## Scope option, not started

Two cases are two examples. A general claim about forecasts made to legislators would need a population: every quantitative forecast in one Parliament's committee evidence on, say, a dozen bills, each scored against outcomes for calibration. A first estimate is several weeks of extraction before any outcome work. Not adopted.
