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
<!-- SUMMARY: audit consequential Canadian policy forecasts against outcomes; case 2 (Let's Talk TV) preliminary results in: specialty/pay revenue showed no detectable effect (k = 0.1), BDU revenue fell within the forecast range (k = 1.3), read at the pre-stated error level after the Netflix calibration (σ_tech 1.3%/yr); BDU payments to programmers didn't fall; uptake, closures, technology calibration pending; case 1 gated on premium data · status: development · updated: 2026-10-03 -->

## State

Scaffolded 2026-10-03 from an LLM-written lead list Brett pasted (verbatim copy gitignored in `notes/intake/`). Three candidate cases under `cases/`: GNDA life-insurance premiums, CRTC *Let's Talk TV*, Bill C-75 preliminary inquiries. Settled 2026-10-03: scope stays legislative, regulatory, and judicial; exemplar Kane (2026, *Econ Journal Watch*); lead case *Let's Talk TV*, second case GNDA; LaTeX; case 1 reports both counterfactuals. Analysis plan adopted (`notes/analysis-plan.md`).

Forecast-side sources for cases 1 and 2 read and filed in `literature/` (JUST 36 and CHPC 8 evidence, CIA brief, CIA 2014 model paper, Nordicity/Miller report, the Act, CLHIA release). Both prediction records filled and committed before any outcome data were opened. Main finding so far: the CIA model reports mortality-experience increases of 36% / 58% under a $1 million disclosure threshold the Act doesn't have; the 30% / 50% *premium* figures given to the Committee are not in that paper and their source is unlocated (G18). Case 2's near-mechanism assumptions (BYOP uptake, pass-through, closures) are recorded for testing ahead of the job and GDP totals. Case 2 design analysis done (`notes/design-analysis-lttv.md`): the report's scenario paths were extracted from its figures and checked against its text; its "18% of baseline CPE" doesn't reproduce (12.6%); quantity definitions, splice rule, verdict bands and a technology-forecast calibration are fixed in the plan. Case 2 outcomes opened after those commitments: preliminary results in `notes/results-lttv.md` (specialty/pay revenue *k* = 0.1, no detectable effect up to a baseline error of about 4% a year; BDU revenue *k* = 1.3, within the forecasters' range up to about 3%; BDU affiliation payments did not fall, so the modelled pass-through isn't visible in the aggregate, for reasons not yet established). Inward novelty check done; no outward search, no manuscript text.

## Next action

1. Case 2: finish the outcome checks in `notes/analysis-plan.md`: unbundled-package uptake (CRTC data or company disclosures), service closures 2016–2020 from the individual-service summaries, CPE (descriptive), and the released HELD rows T14–T15. 
2. Case 1: locate the source of the 30% / 50% premium figures (G18): the 2016 CIA critical-illness paper, any Senate submission on S-201. Settle premium-data feasibility (COMPULIFE terms, archived rate tables). Check whether submissions in the Supreme Court decision on the Act (G07) repeated the forecast.
3. Outward novelty search with `/hyperresearch` (light tier, capped budget), logged in `notes/novelty-search.md`.

## Open decisions (Brett)

- None open.

## Blockers

None external. Case 1's premium test depends on finding a fixed-profile quote series under usable terms.
