# Targeted recheck 2: prediction-checker, after the truthful-and-fair round

Independent checker; another model wrote the text. Read-only; full report in your final message; state which model you are. Standard: truthful, fair, clear.

Manuscript: `notes/passes/recheck2-2026-10-03/main.txt` (commit dc24772); LaTeX in `main.tex`, `sections/*.tex`; macros `sections/numbers-lttv.tex`; tables `sections/tables-lttv.tex`. Reports this round answered: `notes/passes/2026-10-03-quote-audit.md`, `-negative-claims.md`, `-charitable-engagement.md`. Decision log: `DECISIONS.md` (last three entries).

Check, and only these:
1. **Survey evidence.** /Users/brettreynolds/projects/LLM-CLI-projects/literature/mtm_2017-08-17_starter_tv_pick_and_pay_press_release.md (and .pdf). Every sentence citing it: is it quoted and described accurately (what population, what measure, what date), labelled as outside the plan's accepted sources, and are its limits stated? The survey scenario's definition is in DECISIONS.md (entry citing commit 026f602); does `scripts/crtc_outcomes_lttv.py` (survey path) and `scripts/decompose_bdu_lttv.py` implement exactly that? Recompute the survey-path k for both series and the survey-path per-subscriber part, and the "67%"/"44%" shares beyond the chain.
2. **Both readings.** Abstract, introduction (uptake, channel and distributor paragraphs), results, links (uptake paragraph, fees), discussion (first two paragraphs, limits, five findings): is each reading stated with the numbers that support it, without one reading quietly treated as the true one? Is any claim stronger than its numbers (e.g., "fits", "comes closer", "far better", "lost more than it explains")?
3. **Testimony passages (fairness and accuracy).** Results section 2.1 and discussion paragraph beginning "Morrison's summary to the committee": check every quotation and paraphrase against /Users/brettreynolds/projects/LLM-CLI-projects/literature/canada_commons_chpc_2016-04-12_meeting8_evidence.md (time marks), and whether the account is fair to the whole appearance. Check the new credits to the report (para. iii, para. 111, para. 78 and n. 40) and to Miller 2022 (n. 88, n. 196: /Users/brettreynolds/projects/LLM-CLI-projects/literature/miller_2022_crtc_canadian_program_rights_market.md) against the sources.
4. **Scenario labels.** Everywhere the uptake scenarios are described: are they now consistently a partial recalculation holding the exemption-order and closure components fixed, not "the report's model run at" an uptake level?
5. **Anything new that reads as an overclaim, an unfair characterization, or a number that doesn't match its macro or source.**

Report: verdict; problems table (location and quoted phrase, issue, severity, fix); recomputations.
