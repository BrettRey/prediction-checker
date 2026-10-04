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
<!-- SUMMARY: audit of a forecast put to Parliament (CRTC Let's Talk TV); full EJW draft (24 pp., 2 figures, tables A1–A8); truth/fairness round done: MTM 2017 survey reported beside the planned uptake reading (outcomes fit the report's chain only on low uptake paths), testimony criticism narrowed to three specific departures; restructured after clarity passes, rechecked (Codex recheck 3) and scar-tissue pass done; numbers and quote audits current; reader-pass next; nothing pushed · status: development (drafting for EJW) · updated: 2026-10-03 -->

## State

Scaffolded 2026-10-03 from an LLM-written lead list Brett pasted (verbatim copy gitignored in `notes/intake/`). Three candidate cases under `cases/`: GNDA life-insurance premiums, CRTC *Let's Talk TV*, Bill C-75 preliminary inquiries. Settled 2026-10-03: scope stays legislative, regulatory, and judicial; exemplar Kane (2026, *Econ Journal Watch*); lead case *Let's Talk TV*, second case GNDA; LaTeX; case 1 reports both counterfactuals. Analysis plan adopted (`notes/analysis-plan.md`).

Forecast-side sources for cases 1 and 2 read and filed in `literature/` (JUST 36 and CHPC 8 evidence, CIA brief, CIA 2014 model paper, Nordicity/Miller report, the Act, CLHIA release). Both prediction records filled and committed before any outcome data were opened. Main finding so far: the CIA model reports mortality-experience increases of 36% / 58% under a $1 million disclosure threshold the Act doesn't have; the 30% / 50% *premium* figures given to the Committee are not in that paper and their source is unlocated (G18). Case 2's near-mechanism assumptions (BYOP uptake, pass-through, closures) are recorded for testing ahead of the job and GDP totals. Case 2 design analysis done (`notes/design-analysis-lttv.md`): the report's scenario paths were extracted from its figures and checked against its text; its "18% of baseline CPE" doesn't reproduce (12.6%); quantity definitions, splice rule, verdict bands and a technology-forecast calibration are fixed in the plan. Case 2 outcomes opened after those commitments: preliminary results in `notes/results-lttv.md` (specialty/pay revenue *k* = 0.1, no detectable effect up to a baseline error of about 4% a year; BDU revenue *k* = 1.3, within the forecasters' range up to about 3%; BDU affiliation payments did not fall, so the modelled pass-through isn't visible in the aggregate, for reasons not yet established). Case 2 section drafted in LaTeX. Inward novelty check done; no outward search yet.

## Next action

1. Done 2026-10-03: `contribution-alignment` and `terminological-hygiene` applied (eight-stage restructure), Codex recheck 3 of the restructure (all eight findings fixed, 24906c5), `editorial-scar-tissue` (2ece90d), abstract rewritten in NBER order (58776ac), `contribution-alignment` second run (62c911f), `reader-pass` by two model families (5fa250d; new §2 paragraph on the report's four revenue components, verdict rule in §3, tables renumbered B1–B8), closures on the plan's 2015-owner rule (44e281f; integrated 3 to 4 of 57, slightly below the report's 10%, which implies about 6), `coherence-cohesion` (cff5bbb; 14 flow edits accepted), combined Codex recheck 4 (cf6744c; clean apart from six wording fixes, applied; numbers, quote, inference, negative-claims and fairness audits current). `source-reread` (e9124df; Simpson locators and the context of Morrison's "good news" remark corrected; two optional fairness additions pending Brett). Next: Brett's call on the two additions; cheap `contribution-alignment` rerun; mechanics passes (`figures`, `build-integrity`, `house-style`, `validate-bib`, `proofread`).
2. Still open from Elicit round 1: whether the report's baseline includes the Super Bowl simultaneous-substitution change (T10 unverified) and any 2016 CRTC local-TV measures.
3. Library-access readings before submission: Crawford and Yurukoglu 2012, Crompton 2006, Siegfried and Zimbalist 2000, Hodges 1997, full Harrington et al. 2000.
4. After the clarity passes: draft the factual-check email to Peter Miller/Nordicity and Friends of Canadian Broadcasting (passages on the report, its mechanics as read here, and the testimony; corrections of fact invited, not approval), saved as a file for Brett to edit and send.
5. Before any push: payload check (all `notes/passes/` audit reports go public, Brett 2026-10-03; raw Codex logs stay gitignored), push so the data-and-code link is live, clean-clone test of `scripts/fetch_raw.sh` (needs `SEC_UA`), Zenodo archive.
6. Submission formatting: EJW LaTeX template, Chicago author-date, mechanics passes, `/submission-gate`. At submission, log Brett's forecast in `Project-Management/prediction-ledger/ledger.jsonl` (`p_desk_survive`, `p_accept`, `expected_decision_by`; new `economics` venue class) and Claude's under its own name.
7. Case 1 (GNDA), now a separate paper: G18 source, premium-data feasibility.

## Open decisions (Brett)

- Prediction-ledger numbers, at submission.

## Blockers

None external. Case 1's premium test depends on finding a fixed-profile quote series under usable terms.
