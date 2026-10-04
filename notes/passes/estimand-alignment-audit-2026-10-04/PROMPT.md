# Estimand alignment audit: prediction-checker (EJW draft), commit 9c49e9c

Independent auditor; another model wrote and revised this paper. Read-only; give your full report in your final message; state which model you are. Standard: truthful, fair, clear. Verify every finding against the files before reporting it, quote the manuscript text you relied on, and give its location (section and the .tex file and line).

Manuscript: `notes/passes/estimand-alignment-audit-2026-10-04/tv-unbundling-forecast-check.txt` (rendered PDF text, commit 9c49e9c); LaTeX in `tv-unbundling-forecast-check.tex` and `sections/*.tex` (numbers are macros defined in `sections/numbers-lttv.tex`); plan `notes/analysis-plan.md`; decisions `DECISIONS.md`; project rules `CLAUDE.md` (note the rule on two objects of assessment: the technical claim, what follows under the model's stated conditions, and the public predictive argument, what decision-makers were told would probably happen). The report the paper checks is `/Users/brettreynolds/projects/LLM-CLI-projects/literature/nordicity_miller_2015_canadian_television_2020.md`.

The paper is an Econ Journal Watch draft checking a commissioned forecast (Nordicity and Miller 2015) of job losses from the CRTC's 2015 television decisions, put to a House of Commons committee in 2016, against CRTC outcomes for 2016–2019. Its central quantity is a forecast scale k (0 = the report's baseline, 1 = its reform path), estimated by GLS with the baseline's error modelled as a random walk; it is explicitly not an estimate of the decisions' causal effect.

Run the pass below exactly as written. This is an audit: report findings and proposed repairs; change nothing.

## The pass (estimand-alignment-audit, from the portfolio's pass registry)

Six checks. Work from the results tables outward to the claims, not the other
way round.

1. NAME THE TARGET QUANTITY IN WORDS. For each central claim: what quantity,
   over which population, and what would count as its true value. Do this
   before looking at any estimator. A claim whose target cannot be stated in a
   sentence is the finding.

2. COEFFICIENT VERSUS EFFECT. A regression coefficient is a coefficient.
   Calling it an effect requires the design that licenses it, named in the
   text. Check every verb attached to a number: causes, raises, drives,
   predicts, is associated with.

3. MODELLING CHOICES REPORTED AS FINDINGS. A reference level, a scale fixed
   for identifiability, a prior, a smoothing parameter, a cut-off: none of
   these is a result, and each can look like one in a table.

4. ESTIMATED, IMPORTED, OR ASSUMED. Label every parameter. A value taken from
   another study or fixed by assumption must not be described as estimated
   here, and the text must say which study or which assumption.

5. LOCAL RESULT, GENERAL CLAIM. A result holding for one variety, register,
   corpus, period, or subgroup does not carry to the others by itself. State
   the population the estimate is for and the population the claim is about,
   and say what would have to hold to get from one to the other.

6. CLAIM STRENGTH. Grade each headline claim: causal, conditional on the
   stated design, or associational. Where the design does not carry the
   wording, downgrade the wording rather than defending it.

Scope note. This pass is about the statistical target only. Whether a category
earns its projection is projectibility-audit; whether the argument slides
between explanatory levels is level-category-audit. Do not re-run those here,
and say so in the report when a finding really belongs to one of them.
Report: verdict; findings table (location and quoted phrase, which check, issue, severity, proposed repair); then what you checked and found clean. If drift remains that you judge acceptable, say so explicitly so the author can accept it.
