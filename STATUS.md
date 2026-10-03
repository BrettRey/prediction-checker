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
<!-- SUMMARY: audit of a forecast put to Parliament (CRTC Let's Talk TV); full EJW draft assembled (intro, method, results, links incl. employment, discussion; 9 pp.), venue record approved; GNDA split off as a later paper; nothing pushed · status: development (drafting for EJW) · updated: 2026-10-03 -->

## State

Scaffolded 2026-10-03 from an LLM-written lead list Brett pasted (verbatim copy gitignored in `notes/intake/`). Three candidate cases under `cases/`: GNDA life-insurance premiums, CRTC *Let's Talk TV*, Bill C-75 preliminary inquiries. Settled 2026-10-03: scope stays legislative, regulatory, and judicial; exemplar Kane (2026, *Econ Journal Watch*); lead case *Let's Talk TV*, second case GNDA; LaTeX; case 1 reports both counterfactuals. Analysis plan adopted (`notes/analysis-plan.md`).

Forecast-side sources for cases 1 and 2 read and filed in `literature/` (JUST 36 and CHPC 8 evidence, CIA brief, CIA 2014 model paper, Nordicity/Miller report, the Act, CLHIA release). Both prediction records filled and committed before any outcome data were opened. Main finding so far: the CIA model reports mortality-experience increases of 36% / 58% under a $1 million disclosure threshold the Act doesn't have; the 30% / 50% *premium* figures given to the Committee are not in that paper and their source is unlocated (G18). Case 2's near-mechanism assumptions (BYOP uptake, pass-through, closures) are recorded for testing ahead of the job and GDP totals. Case 2 design analysis done (`notes/design-analysis-lttv.md`): the report's scenario paths were extracted from its figures and checked against its text; its "18% of baseline CPE" doesn't reproduce (12.6%); quantity definitions, splice rule, verdict bands and a technology-forecast calibration are fixed in the plan. Case 2 outcomes opened after those commitments: preliminary results in `notes/results-lttv.md` (specialty/pay revenue *k* = 0.1, no detectable effect up to a baseline error of about 4% a year; BDU revenue *k* = 1.3, within the forecasters' range up to about 3%; BDU affiliation payments did not fall, so the modelled pass-through isn't visible in the aggregate, for reasons not yet established). Case 2 section drafted in LaTeX. Inward novelty check done; no outward search yet.

## Next action

1. Act on the page-one cold read; then a full reader pass and a review board with an outsider persona.
2. Read the library-access sources before submission: Crawford and Yurukoglu 2012 (bundling), Crompton 2006 and Siegfried and Zimbalist 2000 (impact-study critiques), Hodges 1997, full Harrington et al. 2000. Then `/hyperresearch` (light tier) as the deeper novelty sweep.
3. Before any push: payload check (`git status`, history), then push so the data-and-code statement's repository link is live; run `scripts/fetch_raw.sh` in a clean clone to test replication.
4. Submission formatting: EJW LaTeX template, Chicago author-date, `/submission-gate`.
5. Case 1 (GNDA), now a separate paper: G18 source, premium-data feasibility.

## Open decisions (Brett)

- Title: working title "Fifteen thousand jobs: checking a forecast put to Parliament on unbundling Canadian television".
- AI disclosure wording: `\aidisclosure{Claude Opus 5.5}` renders "The large language models Claude Opus 5.5 served..."; the ChatGPT lead list is noted in the data-and-code section. Confirm the model list and how to handle the singular.
- Forecasts for the prediction ledger (no base rate for economics venues).

## Blockers

None external. Case 1's premium test depends on finding a fixed-profile quote series under usable terms.
