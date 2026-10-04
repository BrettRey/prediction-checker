# Targeted recheck 3: prediction-checker, after the restructure

Independent checker; another model wrote and restructured this paper. Read-only; full report in your final message; state which model you are. Standard: truthful, fair, clear.

The paper was restructured today (commits 1b65504 through c449a34) following two clarity reports (`notes/passes/2026-10-03-contribution-alignment.md`, `notes/passes/2026-10-03-terminological-hygiene.md`): a controlled vocabulary (report baseline / reform scenario / reform path; forecast scale k, estimate k-hat, scenario coefficient k^u; partial recalculation; designated error scale; cited-input band; BYOP uptake vs the CRTC's entry-level share vs the survey's starter-package adoption), a new section order, a main-text scenario table, a shorter introduction and a reorganized discussion.

- Before: `notes/passes/recheck3-2026-10-03/main-before-restructure.txt` (commit 043df99). After: `notes/passes/recheck3-2026-10-03/main.txt` (commit c449a34). LaTeX in `main.tex`, `sections/*.tex`, `sections/table-scenarios-main.tex`; macros `sections/numbers-lttv.tex`. Diff with `git diff 043df99 c449a34 -- main.tex sections/`.

Check, and only these:
1. **Nothing got stronger in the move.** Compare each claim in the new abstract, introduction, section 4 and discussion with the corresponding claim before. Flag any sentence that now claims more (scope, certainty, causation, "only", "established") than the body supports, and any qualification that was dropped where it still matters.
2. **Quotations intact.** Every \enquote{} in the new text against its source (/Users/brettreynolds/projects/LLM-CLI-projects/literature/ for the report, the committee evidence, the CRTC documents, MTM; see the earlier quote audit for locators). Any quotation altered, truncated differently, or moved under a wrong locator?
3. **Numbers matched to quantities.** Every number in the new prose and the new main-text table: does it describe the right quantity (e.g., k-hat vs k^u; shortfall vs nominal decline; entry-level share vs BYOP uptake; designated error scale vs Netflix-derived scale)? Recompute the main-text scenario table from `data/derived/uptake_conditional_lttv.csv`.
4. **Vocabulary applied without changing meaning.** Spot-check the controlled terms across text, tables (sections/tables-lttv.tex) and figure labels (scripts/figures_lttv.py). Any place where substituting the new term changed what is claimed, or where old and new terms now coexist confusingly?
5. **Deliberate drops.** These were cut from the main text on purpose and remain in appendix tables: secondary scenario values (flat 4%, flat 10%, rise to 10%), Morrison's derived k 0.40, the 2,880 specialty-and-pay FTEs, exact coverage figures and the t(3) widening (now in appendix A). Is anything else missing that a reader needs, or that the body still refers to?
6. **Internal consistency and cross-references.** Same bounded conclusion in abstract, introduction, section 4 and discussion? Every \ref resolves to the right object? The roadmap matches the section titles?

Report: verdict; problems table (location and quoted phrase, issue, severity, fix).
