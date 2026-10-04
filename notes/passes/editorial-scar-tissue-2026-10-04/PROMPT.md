# Editorial scar tissue: prediction-checker (EJW draft), commit 8186d12

Independent auditor; another model (Claude) wrote and revised this paper. Read-only: you can't edit, so give every proposed change as exact LaTeX in your final message; state which model you are. Standard: truthful, fair, clear. Verify every finding against the files and quote the text you relied on, with its location (section, .tex file and line).

Manuscript: `notes/passes/editorial-scar-tissue-2026-10-04/tv-unbundling-forecast-check.txt` (rendered PDF text, commit 8186d12; the paper now uses the Econ Journal Watch class, so sections are unnumbered and the introduction is unheaded); LaTeX in `tv-unbundling-forecast-check.tex` and `sections/intro.tex`, `sections/case-lttv.tex`, `sections/discussion.tex`, `sections/appendix.tex` (numbers are macros in `sections/numbers-lttv.tex`; don't edit generated files: `sections/numbers-lttv.tex`, `sections/tables-lttv.tex`, `sections/table-scenarios-main.tex`; table captions live in `scripts/make_tex_tables.py`). House writing rules: `/Users/brettreynolds/projects/LLM-CLI-projects/.claude/rules/writing-style.md`. Decision log: `DECISIONS.md`. Project rules: `CLAUDE.md` (two objects of assessment kept apart: the technical claim and the public predictive argument).

The paper checks a commissioned forecast (Nordicity and Miller 2015) of job losses from the CRTC's 2015 television decisions, put to a House of Commons committee in 2016, against CRTC outcomes for 2016–2019. It has been revised heavily today (a post hoc check that integrates over the baseline's error scale in two versions; a corrected reading of Crawford and Yurukoglu 2012; new literature; wording passes; the EJW conversion), so the places revised today are where problems are likeliest; DECISIONS.md entries dated 2026-10-04 list them.

Rules for every proposed change: change wording only; never change a number, macro (\lttv...), citation command, page locator, \enquote{} quotation, cross-reference, or the meaning or strength of a claim. Each `old` must be an exact, unique substring of the named file, copied from the LaTeX. Prefer the smallest change. Keep the author's voice and the four deliberately witty lines (\enquote{media jobs} "have a majority outside the media"; "proves easier to quote than to reproduce"; "came unbundled from its uptake assumption"; "in the accommodating sense that").

## The pass (editorial-scar-tissue, from the portfolio's pass registry)

Read for the tells listed under "Revise for the end-reader, not the
conversation" in /Users/brettreynolds/projects/LLM-CLI-projects/.claude/rules/writing-style.md. Read that section first; do
not work from this summary alone. The five tells:

1. Contrastive negation of an earlier draft's wording. "Glossematic drift is
   not Mortensen's theory; it is Ahlqvist's" is a repair of a previous error,
   visible only to whoever pointed the error out.
2. The correction promoted to the front of a sentence or paragraph, displacing
   the argument that the sentence is there to make.
3. The corrector's justification imported as new content. An aside in
   conversation ("it was common currency by then") surfacing in the text as
   "by which time it was standard in the field".
4. A clause engineered so the old misreading cannot arise, defending against a
   reading only the corrector would make.
5. Corrective negation with no opponent: "the problem isn't the data, it's the
   inference", where nobody asserted the data was the problem.

For each hit, ask the discriminating question: does this sentence serve the
paragraph's argument, or does it prove a correction was heard? Then rewrite the
passage as if drafting it fresh with the corrected fact in hand.

Expect the fix to be smaller than the discussion that produced it, and often a
deletion. "Mortensen's theory of glossematic drift" becomes "glossematic
drift", with the citation carrying attribution.

Report each hit as: location, the tell it matches, the sentence, and the
proposed fresh-draft replacement. Then apply the accepted ones.

Scar tissue accumulates wherever review has landed, so run this after
external-review-triage and after any cutting pass, not before.
Read the section of the house writing rules titled 'Revise for the end-reader, not the conversation' before anything else. The rechecks and audits that drove today's revisions are in `notes/passes/` (files dated 2026-10-04) and their outcomes in DECISIONS.md; use them to see which corrections were made, then look for sentences that exist to show a correction was heard.

Report: verdict; then findings (location and quoted text, which step of the procedure, issue, severity) each with an exact proposed replacement where a change is warranted; then what you checked and found clean.
