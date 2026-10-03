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
<!-- SUMMARY: audit consequential Canadian policy forecasts against outcomes; scaffolded 2026-10-03, 0/39 intake claims verified, novelty search inward-only · status: development · updated: 2026-10-03 -->

## State

Scaffolded 2026-10-03 from an LLM-written lead list Brett pasted (verbatim copy gitignored in `notes/intake/`). Three candidate cases under `cases/`: GNDA life-insurance premiums, CRTC *Let's Talk TV*, Bill C-75 preliminary inquiries. Every claim from the brief is queued in `notes/source-verification.md`; none verified. Inward novelty check done (`notes/novelty-search.md`): nothing in `literature/` on any case. No outward search, no data, no manuscript text.

## Next action

1. Verify the forecast documents for cases 1 and 2: the JUST meeting-36 evidence and the CIA brief (G01–G05), and the Nordicity/Miller report and CHPC meeting-8 evidence (T01–T12). Save each to `literature/` with an `.md` companion.
2. Fill each case's prediction record from those sources and commit it before touching outcome data.
3. Outward novelty search with `/hyperresearch` (light tier, capped budget), logged in `notes/novelty-search.md`.

## Open decisions (Brett)

- Scope: the brief widened *cases* from Supreme Court litigation to legislative and regulatory forecasts. Keep that, or return to courts only?
- Exemplar: the brief measures its leads against "your example", which isn't on file. Add it to `notes/project-brief.md`.
- First case for the paper: GNDA (stronger paper, data access uncertain) or *Let's Talk TV* (public data, more reconstruction).
- Manuscript format: LaTeX scaffold for now; Quarto is the portfolio default for a numbers-heavy paper.

## Blockers

None external. Case 1 has a feasibility question (historical premium quotes) to settle before it can be the lead case.
