# Statistical inference audit: prediction-checker (EJW draft)

You are an independent reviewer. Another model (Claude) designed the analysis, wrote the scripts and wrote the prose. Your job is to judge whether the paper's inference is valid for the dependence structure and design it actually has, and whether each inferential claim in the text survives. You are read-only; put your full report in your final message. State at the top which model you are.

## What to read

- Rendered manuscript: `notes/passes/statistical-inference-audit-2026-10-03/main.txt` (from commit 3046dc3). LaTeX in `main.tex` and `sections/*.tex`; numbers are macros from `sections/numbers-lttv.tex`; appendix tables in `sections/tables-lttv.tex`.
- Pre-stated analysis plan: `notes/analysis-plan.md` (and `scripts/plan_constants.py`). Decision log with dates and [post hoc] labels: `DECISIONS.md`. Chronology: table A7 in the manuscript.
- Analysis code: `scripts/crtc_outcomes_lttv.py` (k, intervals, bands, cutoffs, multiverse, uptake scenarios), `scripts/design_analysis_lttv.py` (pre-outcome simulation), `scripts/netflix_calibration.py` (sigma calibrations), `scripts/model_check_lttv.py` (post hoc model check), `scripts/employment_lttv.py`, `scripts/input_checks_lttv.py`, `scripts/closures_lttv.py`, `scripts/figures_lttv.py`.
- Outputs: `data/derived/*.csv`, `notes/results-lttv*.md`, `notes/design-analysis-lttv.md`.

## The design in brief (verify it yourself; don't take this summary as given)

Four annual observations (2016-2019) per revenue series, two series (specialty and pay channels; distributors). y_t = log B_t - log Y_t, delta_t = log B_t - log(B_t - I_t), model y_t = k delta_t + e_t with e_t a random walk from 2014 with variance sigma^2 per year. k is estimated by GLS with sigma fixed by an external calibration (a US Netflix subscriber forecast in the same report, against Netflix's counts), floored at the series' 2010-2014 historical volatility. 95% interval = k_hat +/- 1.96 SE. Verdicts compare the interval with a band of k implied by the forecasters' cited inputs. Nine calibrations are shown; model-implied uptake scenarios, an offset model and real-terms changes were added after the outcome data was opened.

## The checks (adapted from the registry's eight to this design)

1. DEPENDENCE UNIT. The residual dependence here is serial (within a series, across years) and possibly across the two series (both are television revenues in the same market, and distributors' payments are channels' revenue). Is the random-walk covariance a defensible model for the baseline error? Does any claim in the text combine or compare the two series in a way that needs their cross-correlation?
2. FEW OBSERVATIONS. Four points per series. What does the paper's inference assume that four points can't check? Is the decision to fix sigma rather than estimate it stated and justified, and are the consequences (no degrees-of-freedom correction, normal critical value) stated?
3. TWO-STEP UNCERTAINTY. sigma comes from one external comparison (essentially one or a few Netflix forecast errors), then is treated as known. How much does the interval understate uncertainty because sigma is itself uncertain? The paper shows nine calibrations and a figure of the interval against sigma: is that an adequate substitute for propagating sigma uncertainty, and does the text say what it does and doesn't cover? Similarly, B_t, I_t and the band come from chart labels: is any uncertainty there relevant?
4. RESAMPLING AND SIMULATION. The design analysis simulated 20,000 paths per world and classified them by likelihood ratio. Is the classification rule and the "classified correctly" summary (the smaller of the two worlds' shares) sound? Is the simulation's data-generating process consistent with the estimation model (note the paper's statement about the sign of e and the additive impact)?
5. MULTIPLICITY. Count the inferential statements actually made: two series, nine calibrations, two series versions, six uptake scenarios per series compared with an interval, the offset model, the staffing and fee comparisons. Is any claim made as though it were the single test, when it is one of many? Does the text say which reading was pre-stated?
6. POST-SELECTION. Which specifications, thresholds or comparisons were chosen after seeing outcomes (use DECISIONS.md and table A7)? For each, is the reported interval or verdict presented with that status, and does any conclusion rest on a post hoc choice? Pay attention to the uptake scenarios, the exempt-services adjustment, the growth calibrations, the offset model, and the "standard errors from the estimate" distances added today.
7. DISTANCES IN STANDARD ERRORS. The text now reports distances like "2.1 standard errors below the estimate" between k_hat and a model-implied scenario k. A scenario k is computed from the report's chain, not estimated. Is "standard errors" the right yardstick, and is the interpretation in the text (e.g., that some of the distributors' loss came from outside the model's channel) warranted at that distance, given sigma calibration and the multiplicity above?
8. ARITHMETIC. Recompute k, SE, intervals, bands, cutoffs and the offset-model fit from the derived CSVs; check the design-analysis shares against `data/derived/design_analysis_lttv.csv`.

Also check the employment and fee comparisons, which carry no intervals: does the text draw inferential conclusions from them that would need one?

## Report format (final message, Markdown)

1. Verdict paragraph.
2. One entry per reported interval, test, verdict or inferential claim in the text: location and quoted phrase; the dependence unit; the level the paper used; verdict (valid / valid with caveat / overstated / invalid); consequence for the claim; suggested wording if it needs downgrading. A claim whose interval doesn't survive gets downgraded wording, not a defence.
3. Findings on checks 1-8, each with evidence (file and line, or your recomputation).
4. Your recomputations, with values.
5. What the paper should add, if anything, and what it should cut.
