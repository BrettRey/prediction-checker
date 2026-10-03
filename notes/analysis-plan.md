# Analysis plan
<!-- SUMMARY: Proposed comparison grid and design analysis for cases 1–2, written before any outcome data; design analysis gates release of HELD rows · status: proposed · updated: 2026-10-03 -->

Proposed 2026-10-03, before any outcome series was opened. It fixes what will be compared, so that later choices can be told apart from these. Anything decided after outcome data are opened goes in `DECISIONS.md` marked **[post hoc]**. Record row IDs refer to `source-verification.md`.

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
