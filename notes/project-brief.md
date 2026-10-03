# Project brief: prediction-checker
<!-- SUMMARY: Plan for auditing consequential Canadian policy forecasts against outcomes; three candidate cases, all claims unverified · status: development · updated: 2026-10-03 -->

## The question

When experts tell legislators, regulators, or courts what a decision will cause, and the decision goes ahead, does anyone later check? For a handful of Canadian cases, this project reconstructs the forecast exactly as it was made and tests it against what happened.

The intake brief (2026-10-03, LLM-written, verbatim copy in `notes/intake/`, gitignored) proposed three candidate cases and four already-examined counterexamples. Every factual claim it makes is queued in `source-verification.md` as UNVERIFIED. This file describes the plan; it doesn't restate those claims as fact.

## What this scaffold assumes

The brief answers a question asked in a conversation that isn't on file. It refers to "your example" and "your novelty condition" and says it widened *cases* from Supreme Court litigation to parliamentary and regulatory controversies. The scaffold therefore assumes:

- **Jurisdiction:** Canada.
- **Venue of the prediction:** legislative committees, regulatory proceedings, and courts, not only courts.
- **Novelty condition:** a case qualifies only if no public retrospective already tests that specific forecast. An unsatisfactory existing check may still justify a better study, but the paper can't present the forecast as unrevisited.
- **Shape:** case studies, with one working paper as the first deliverable.

Not on file: Brett's exemplar case, and whether he wants the courts-only scope back. Record both in `DECISIONS.md` when settled.

## Candidate cases

Each has a folder under `cases/` with a prediction record to fill in before any outcome data are pulled.

1. **GNDA and life-insurance premiums** (`cases/gnda-life-insurance/`). Actuarial testimony to the Commons Justice Committee in 2016 that the bill would raise life-insurance premiums by a stated percentage (rows G01–G05). Strongest for a focused paper: an identifiable forecaster, explicit magnitudes, a professional body's model, and a clear intervention date. Feasibility hinges on a historical quotation series for fixed applicant profiles; the only route the brief names is a commercial product (G14), unconfirmed.
2. **CRTC *Let's Talk TV* and the Nordicity/Miller model** (`cases/lets-talk-tv/`). A commissioned 2015 economic model projecting job, GDP, and program-spending losses by 2020 from the reforms, presented to the Heritage Committee in 2016 (T01–T13). Strongest for a first study on public data: the report reportedly gives annual intermediate projections and its mechanisms, and CRTC financial series are public.
3. **Bill C-75 and preliminary inquiries** (`cases/c75-preliminary-inquiries/`). Ministerial and practitioner predictions about delay (C01–C06). Weaker match: the forecasts concern a proposal later narrowed, the enacted rule has no sharp numerical forecast, other reforms and COVID overlap, and a convincing design probably needs linked administrative records.

## Method commitments

- **Two objects of assessment.** (1) The technical claim: what follows under the model's stated conditions. (2) The public predictive argument: what decision-makers were told would probably happen. A changed condition can excuse a conditional projection; a foreseeable market adaptation doesn't automatically excuse a practical policy forecast. The interesting result may be that a model supported a narrow conditional claim while the testimony invited a broader inference.
- **Three questions per case**, from the brief's GNDA design and general enough for the others: did the forecast quantity show the predicted magnitude and timing; how much of any movement is attributable to the intervention; did the assumed mechanism occur.
- **Counterfactual humility.** Unchanged outcomes don't show zero effect, and outcomes moving in the predicted direction don't show the forecast was right. Each case needs a stated counterfactual.
- **Near mechanisms before headline numbers.** For *Let's Talk TV*, test packaging uptake, subscription revenue, service closures, and program spending before the multiplier-derived job and GDP figures.
- **Forecast records frozen first.** The prediction record for each case is committed before any outcome series is downloaded.

## Novelty

The brief's novelty claims are negatives with no stated search. `novelty-search.md` logs the searches actually run. The inward check (Brett's `literature/` folder) found nothing on any of the three cases. The outward search hasn't been done; `/hyperresearch` at the light tier is the planned route.

## Data leads (all unverified)

- CIA individual-life experience database, policy years 2010–2023 (G11–G13): mechanism evidence for case 1, not prices.
- COMPULIFE historical quotation software (G14): possible price route for case 1; commercial, never committed.
- CRTC financial and open-data releases; a later Nordicity model for the CRTC (T14); Miller's 2022 CRTC report (T15).
- Ontario Court of Justice statistics (C06) and national criminal-court data for case 3.
