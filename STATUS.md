---
slug: prediction-checker
kind: paper
title: 'Checking a forecast put to Parliament: unbundling Canadian television, 2016–2019'
stage: complete
external: in-review
blocked_on:
- venue-response
updated: 2026-10-04
venue: Econ Journal Watch
source:
- STATUS.md
- notes/project-brief.md
claim:
  provenance: not-yet-formulated
  claim_updated: 2026-10-03
---

# Prediction checker
<!-- SUMMARY: SUBMITTED to Econ Journal Watch 2026-10-04 (emailed to the editor with the PDF and LaTeX source bundle; initial reaction expected within about two weeks); audit of a forecast put to Parliament (CRTC Let's Talk TV); full draft in the EJW class (draft mode, 42 pp. double-spaced, pdfLaTeX; 2 figures, table 1 and tables B1–B8; tv-unbundling-forecast-check.tex); Kane-style bulleted findings, slimmer §3 with detail in Appendix A, impact-study and bundling literature added; Codex recheck 5 applied (Crawford–Yurukoglu reading corrected); post hoc σ-integrated check in two versions (verdicts hold when outcomes inform σ, depend on the prior when the prior alone sets it) and 50% intervals added, checked by Codex recheck 6; discussion closes on the measurement point (after Kane 2026); submission gate clear; last pushed 2026-10-04 after a payload check · status: in review at Econ Journal Watch · updated: 2026-10-04 -->

## State

Scaffolded 2026-10-03 from an LLM-written lead list Brett pasted (verbatim copy gitignored in `notes/intake/`). Three candidate cases under `cases/`: GNDA life-insurance premiums, CRTC *Let's Talk TV*, Bill C-75 preliminary inquiries. Settled 2026-10-03: scope stays legislative, regulatory, and judicial; exemplar Kane (2026, *Econ Journal Watch*); lead case *Let's Talk TV*, second case GNDA; LaTeX; case 1 reports both counterfactuals. Analysis plan adopted (`notes/analysis-plan.md`).

Forecast-side sources for cases 1 and 2 read and filed in `literature/` (JUST 36 and CHPC 8 evidence, CIA brief, CIA 2014 model paper, Nordicity/Miller report, the Act, CLHIA release). Both prediction records filled and committed before any outcome data were opened. Main finding so far: the CIA model reports mortality-experience increases of 36% / 58% under a $1 million disclosure threshold the Act doesn't have; the 30% / 50% *premium* figures given to the Committee are not in that paper and their source is unlocated (G18). Case 2's near-mechanism assumptions (BYOP uptake, pass-through, closures) are recorded for testing ahead of the job and GDP totals. Case 2 design analysis done (`notes/design-analysis-lttv.md`): the report's scenario paths were extracted from its figures and checked against its text; its "18% of baseline CPE" doesn't reproduce (12.6%); quantity definitions, splice rule, verdict bands and a technology-forecast calibration are fixed in the plan. Case 2 outcomes opened after those commitments: preliminary results in `notes/results-lttv.md` (specialty/pay revenue *k* = 0.1, no detectable effect up to a baseline error of about 4% a year; BDU revenue *k* = 1.3, within the forecasters' range up to about 3%; BDU affiliation payments did not fall, so the modelled pass-through isn't visible in the aggregate, for reasons not yet established). Case 2 section drafted in LaTeX. Inward novelty check done; no outward search yet.

## Next action

0. **Submitted to *Econ Journal Watch*, 2026-10-04.** Brett emailed the editor (Daniel Klein) with `submission/tv-unbundling-forecast-check.pdf` and the LaTeX source bundle `submission/tv-unbundling-forecast-check-ejw-source-2026-10-04.zip` (both gitignored). The editor acknowledged receipt the same day and expects to reply within days to a week. No manuscript ID; EJW's stated practice is an initial editorial reaction within two weeks, so check around 2026-10-18. Prediction-ledger forecasts are recorded in the portfolio ledger (`tvforecast-ejw`). Still open: Zenodo DOI (optional); copyedit-stage items ("percent" in prose, American spelling, author biography). Before the submission the gate was cleared: all five never-run passes, the three Codex prose passes (coherence-cohesion, terminological-hygiene, editorial-scar-tissue), the mechanical passes on the EJW build, and /push-bib (bibliography merged into the central file).
1. Done 2026-10-03: `contribution-alignment` and `terminological-hygiene` applied (eight-stage restructure), Codex recheck 3 of the restructure (all eight findings fixed, 24906c5), `editorial-scar-tissue` (2ece90d), abstract rewritten in NBER order (58776ac), `contribution-alignment` second run (62c911f), `reader-pass` by two model families (5fa250d; new §2 paragraph on the report's four revenue components, verdict rule in §3, tables renumbered B1–B8), closures on the plan's 2015-owner rule (44e281f; integrated 3 to 4 of 57, slightly below the report's 10%, which implies about 6), `coherence-cohesion` (cff5bbb; 14 flow edits accepted), combined Codex recheck 4 (cf6744c; clean apart from six wording fixes, applied; numbers, quote, inference, negative-claims and fairness audits current). `source-reread` (e9124df; Simpson locators and the context of Morrison's "good news" remark corrected; two optional fairness additions pending Brett). Optional additions dropped (Brett, 2026-10-04); Harrington read in full and its counts corrected to Table 3; `contribution-alignment` third run and the mechanics passes (`build-integrity`, `validate-bib`, `house-style`, `figures`, `proofread`) done and applied (5ce8df5). No factual-check emails (Brett, 2026-10-04; Friends filed no brief with the committee, so the testimony is its whole record). Pushed 2026-10-04 (5cc0c27) after a history-wide payload check and a clean-clone reproduction test; manuscript renamed `tv-unbundling-forecast-check.tex`; venue decision record gitignored. Later on 2026-10-04: intro names the report's 5% and 10% uptake and the CRTC's 1.6%; published Harrington et al. (2000) cited (14 of 28 over, 3 under); Kane-style bulleted findings in intro and discussion, §3 slimmed with detail moved to Appendix A, reason for logs stated (42d1c1e); Crompton, Siegfried–Zimbalist and Crawford–Yurukoglu added (9ae95ff); §2 sentence on what the job and GDP estimates are linked to, with the absence claim's search recorded; layout (figure 1 no longer alone on a page, caption spacing and small-caps labels); Codex recheck 5 (bc8885f; seven findings verified and applied, including a corrected reading of Crawford–Yurukoglu, whose model predicts a small fall in channels' fee revenue, not the rise observed). Pushed through 912d089 after a payload check of every unpushed commit. Brett finished his full read (2026-10-04). The five never-run submission passes are done (Codex): `level-category-audit`, `estimand-alignment-audit`, `lakoffian-metaphor`, `rhetoric-and-humour` (humour half rerun for opportunities; registry amended) and `de-ai-prose`; plus a pairwise read of each section against the introduction and conclusion. EJW formatting done (6a8288f): ejw class, unheaded introduction, named cross-references, subsection headings "The forecast" and "What the comparisons show", appendices before references, Chicago author-date via the class. Left for copyediting or Brett: "percent" in prose, American spelling, author biography, JEL codes. Next: the submission gate's remaining passes (mostly mechanical, now stale from the conversion), Zenodo archive (rest of item 5), Brett's prediction-ledger numbers, a cover note, and confirming the submission route (instructions page says email; call-for-papers page names a portal). Optional: `density-leavening` for the remaining long paragraphs.
2. Still open from Elicit round 1: whether the report's baseline includes the Super Bowl simultaneous-substitution change (T10 unverified) and any 2016 CRTC local-TV measures.
3. ~~Library-access readings~~ done 2026-10-04: Brett supplied Crawford and Yurukoglu 2012, Crompton 2006, Siegfried and Zimbalist 2000, Hodges 1997 and Harrington et al. 2000 (*JPAM*); all filed in `literature/` with `.md` companions.
4. ~~Factual-check emails~~ dropped (Brett, 2026-10-04): no emails; the paper rests on the public record.
5. Before any push: payload check (all `notes/passes/` audit reports go public, Brett 2026-10-03; raw Codex logs stay gitignored), push so the data-and-code link is live, clean-clone test of `scripts/fetch_raw.sh` (needs `SEC_UA`), Zenodo archive.
6. Submission formatting: EJW LaTeX template, Chicago author-date, mechanics passes, `/submission-gate`. At submission, log Brett's forecast in `Project-Management/prediction-ledger/ledger.jsonl` (`p_desk_survive`, `p_accept`, `expected_decision_by`; new `economics` venue class) and Claude's under its own name.
7. Case 1 (GNDA), now a separate paper: G18 source, premium-data feasibility.

## Open decisions (Brett)

- Prediction-ledger numbers, at submission.

## Blockers

None external. Case 1's premium test depends on finding a fixed-profile quote series under usable terms.
