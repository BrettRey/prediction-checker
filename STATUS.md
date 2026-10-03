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
<!-- SUMMARY: audit consequential Canadian policy forecasts against outcomes; records for cases 1–2 frozen 2026-10-03 (17 VERIFIED, 1 PARTLY of 39 brief rows); lead case Let's Talk TV; case 2 design analysis done and reading rules fixed, so CRTC outcome data may now be opened; case 1 gated on premium-data feasibility · status: development · updated: 2026-10-03 -->

## State

Scaffolded 2026-10-03 from an LLM-written lead list Brett pasted (verbatim copy gitignored in `notes/intake/`). Three candidate cases under `cases/`: GNDA life-insurance premiums, CRTC *Let's Talk TV*, Bill C-75 preliminary inquiries. Settled 2026-10-03: scope stays legislative, regulatory, and judicial; exemplar Kane (2026, *Econ Journal Watch*); lead case *Let's Talk TV*, second case GNDA; LaTeX; case 1 reports both counterfactuals. Analysis plan adopted (`notes/analysis-plan.md`).

Forecast-side sources for cases 1 and 2 read and filed in `literature/` (JUST 36 and CHPC 8 evidence, CIA brief, CIA 2014 model paper, Nordicity/Miller report, the Act, CLHIA release). Both prediction records filled and committed before any outcome data were opened. Main finding so far: the CIA model reports mortality-experience increases of 36% / 58% under a $1 million disclosure threshold the Act doesn't have; the 30% / 50% *premium* figures given to the Committee are not in that paper and their source is unlocated (G18). Case 2's near-mechanism assumptions (BYOP uptake, pass-through, closures) are recorded for testing ahead of the job and GDP totals. Case 2 design analysis done (`notes/design-analysis-lttv.md`): the report's scenario paths were extracted from its figures and checked against its text; its "18% of baseline CPE" doesn't reproduce (12.6%); quantity definitions, splice rule, verdict bands and a technology-forecast calibration are fixed in the plan. Inward novelty check done; no outward search, no outcome data yet, no manuscript text.

## Next action

1. Case 2: identify and download the CRTC series for the reading rules in `notes/analysis-plan.md` (unbundled-package uptake, service closures, specialty/pay and BDU revenue, CPE), recording each licence in `data/README.md`; read the released HELD rows T14–T15. The design analysis (`notes/design-analysis-lttv.md`) is committed, so the gate is met.
2. Case 1: locate the source of the 30% / 50% premium figures (G18): the 2016 CIA critical-illness paper, any Senate submission on S-201. Settle premium-data feasibility (COMPULIFE terms, archived rate tables). Check whether submissions in the Supreme Court decision on the Act (G07) repeated the forecast.
3. Outward novelty search with `/hyperresearch` (light tier, capped budget), logged in `notes/novelty-search.md`.

## Open decisions (Brett)

- None open. Analysis plan adopted 2026-10-03; population-of-forecasts option declined.

## Blockers

None external. Case 1's premium test depends on finding a fixed-profile quote series under usable terms.
