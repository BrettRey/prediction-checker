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
<!-- SUMMARY: audit consequential Canadian policy forecasts against outcomes; prediction records for cases 1–2 filled from primary sources and frozen 2026-10-03 (16 VERIFIED, 1 PARTLY of 39 brief rows; post-intervention rows held), novelty search inward-only · status: development · updated: 2026-10-03 -->

## State

Scaffolded 2026-10-03 from an LLM-written lead list Brett pasted (verbatim copy gitignored in `notes/intake/`). Three candidate cases under `cases/`: GNDA life-insurance premiums, CRTC *Let's Talk TV*, Bill C-75 preliminary inquiries.

Forecast-side sources for cases 1 and 2 read and filed in `literature/` (JUST 36 and CHPC 8 evidence, CIA brief, CIA 2014 model paper, Nordicity/Miller report, the Act, CLHIA release). Both prediction records filled and committed before any outcome data were opened. Main finding so far: the CIA model reports mortality-experience increases of 36% / 58% under a $1 million disclosure threshold the Act doesn't have; the 30% / 50% *premium* figures given to the Committee are not in that paper and their source is unlocated (G18). Case 2's near-mechanism assumptions (BYOP uptake, pass-through, closures) are recorded for testing ahead of the job and GDP totals. Inward novelty check done; no outward search, no outcome data, no manuscript text.

## Next action

1. Locate the source of the 30% / 50% premium figures (G18): the 2016 CIA critical-illness model paper, any CIA submission to the Senate on S-201.
2. Read the CRTC's own *Let's Talk TV* decisions (T13) and the S-201 bill text as debated, for the "intervention as enacted" rows.
3. Release the HELD rows and start on outcomes, case by case, now that the records are committed.
4. Outward novelty search with `/hyperresearch` (light tier, capped budget), logged in `notes/novelty-search.md`.

## Open decisions (Brett)

- Scope: the brief widened *cases* from Supreme Court litigation to legislative and regulatory forecasts. Keep that, or return to courts only?
- Exemplar: the brief measures its leads against "your example", which isn't on file. Add it to `notes/project-brief.md`.
- First case for the paper: GNDA (stronger paper, data access uncertain) or *Let's Talk TV* (public data, more reconstruction).
- Manuscript format: LaTeX scaffold for now; Quarto is the portfolio default for a numbers-heavy paper.
- Case 1 design, proposed in the case file: counterfactual "industry code only" (CLHIA's $250,000 commitment from 2018) rather than "no restriction"; test windows fixed before quote data are opened.

## Blockers

None external. Case 1 has a feasibility question (historical premium quotes) to settle before it can be the lead case.
