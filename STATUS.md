---
slug: prediction-checker
kind: paper
title: Prediction checker (working title)
stage: development
external: none
blocked_on: []
updated: 2026-10-03
source:
- STATUS.md
- notes/project-brief.md
claim:
  provenance: not-yet-formulated
  claim_updated: 2026-10-03
---

# Prediction checker
<!-- SUMMARY: audit of a forecast put to Parliament (CRTC Let's Talk TV); full EJW draft (24 pp., 2 figures, tables A1–A8); truth/fairness round done: MTM 2017 survey reported beside the planned uptake reading (outcomes fit the report's chain only on low uptake paths), testimony criticism narrowed to three specific departures; numbers, inference, quote, negative-claims and fairness passes current after two Codex rechecks; nothing pushed · status: development (drafting for EJW) · updated: 2026-10-03 -->

## State

Scaffolded 2026-10-03 from an LLM-written lead list Brett pasted (verbatim copy gitignored in `notes/intake/`). Three candidate cases under `cases/`: GNDA life-insurance premiums, CRTC *Let's Talk TV*, Bill C-75 preliminary inquiries. Settled 2026-10-03: scope stays legislative, regulatory, and judicial; exemplar Kane (2026, *Econ Journal Watch*); lead case *Let's Talk TV*, second case GNDA; LaTeX; case 1 reports both counterfactuals. Analysis plan adopted (`notes/analysis-plan.md`).

Forecast-side sources for cases 1 and 2 read and filed in `literature/` (JUST 36 and CHPC 8 evidence, CIA brief, CIA 2014 model paper, Nordicity/Miller report, the Act, CLHIA release). Both prediction records filled and committed before any outcome data were opened. Main finding so far: the CIA model reports mortality-experience increases of 36% / 58% under a $1 million disclosure threshold the Act doesn't have; the 30% / 50% *premium* figures given to the Committee are not in that paper and their source is unlocated (G18). Case 2's near-mechanism assumptions (BYOP uptake, pass-through, closures) are recorded for testing ahead of the job and GDP totals. Case 2 design analysis done (`notes/design-analysis-lttv.md`): the report's scenario paths were extracted from its figures and checked against its text; its "18% of baseline CPE" doesn't reproduce (12.6%); quantity definitions, splice rule, verdict bands and a technology-forecast calibration are fixed in the plan. Case 2 outcomes opened after those commitments: preliminary results in `notes/results-lttv.md` (specialty/pay revenue *k* = 0.1, no detectable effect up to a baseline error of about 4% a year; BDU revenue *k* = 1.3, within the forecasters' range up to about 3%; BDU affiliation payments did not fall, so the modelled pass-through isn't visible in the aggregate, for reasons not yet established). Case 2 section drafted in LaTeX. Inward novelty check done; no outward search yet.

## Next action

1. Clarity passes on the settled text: `contribution-alignment`, `terminological-hygiene`, then `reader-pass` and `coherence-cohesion` (expensive), `figures`. Then `source-reread` (expensive) as the last truthfulness pass.
2. Still open from Elicit round 1: whether the report's baseline includes the Super Bowl simultaneous-substitution change (T10 unverified) and any 2016 CRTC local-TV measures.
3. Library-access readings before submission: Crawford and Yurukoglu 2012, Crompton 2006, Siegfried and Zimbalist 2000, Hodges 1997, full Harrington et al. 2000.
4. Before any push: payload check (`git status`, history; decide whether `notes/passes/` audit reports go public), push so the data-and-code link is live, clean-clone test of `scripts/fetch_raw.sh` (needs `SEC_UA`), Zenodo archive.
5. Submission formatting: EJW LaTeX template, Chicago author-date, mechanics passes, `/submission-gate`.
6. Case 1 (GNDA), now a separate paper: G18 source, premium-data feasibility.

## Open decisions (Brett)

- Title: the manuscript uses "A forecast put to Parliament: unbundling Canadian television, 2016–2019"; confirm or replace.
- Whether to send Nordicity/Miller and Friends of Canadian Broadcasting the factual passages for correction before submission.
- Forecasts for the prediction ledger (no base rate for economics venues).
- Data-and-code section now adds: "The analysis scripts were written with Claude Opus 5.5 and checked against the sources and against the report's printed totals." Confirm or strike.

## Blockers

None external. Case 1's premium test depends on finding a fixed-profile quote series under usable terms.
