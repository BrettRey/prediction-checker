# Coherence and cohesion: prediction-checker (EJW draft), commit 8186d12

Independent auditor; another model (Claude) wrote and revised this paper. Read-only: you can't edit, so give every proposed change as exact LaTeX in your final message; state which model you are. Standard: truthful, fair, clear. Verify every finding against the files and quote the text you relied on, with its location (section, .tex file and line).

Manuscript: `notes/passes/coherence-cohesion-2026-10-04/tv-unbundling-forecast-check.txt` (rendered PDF text, commit 8186d12; the paper now uses the Econ Journal Watch class, so sections are unnumbered and the introduction is unheaded); LaTeX in `tv-unbundling-forecast-check.tex` and `sections/intro.tex`, `sections/case-lttv.tex`, `sections/discussion.tex`, `sections/appendix.tex` (numbers are macros in `sections/numbers-lttv.tex`; don't edit generated files: `sections/numbers-lttv.tex`, `sections/tables-lttv.tex`, `sections/table-scenarios-main.tex`; table captions live in `scripts/make_tex_tables.py`). House writing rules: `/Users/brettreynolds/projects/LLM-CLI-projects/.claude/rules/writing-style.md`. Decision log: `DECISIONS.md`. Project rules: `CLAUDE.md` (two objects of assessment kept apart: the technical claim and the public predictive argument).

The paper checks a commissioned forecast (Nordicity and Miller 2015) of job losses from the CRTC's 2015 television decisions, put to a House of Commons committee in 2016, against CRTC outcomes for 2016–2019. It has been revised heavily today (a post hoc check that integrates over the baseline's error scale in two versions; a corrected reading of Crawford and Yurukoglu 2012; new literature; wording passes; the EJW conversion), so the places revised today are where problems are likeliest; DECISIONS.md entries dated 2026-10-04 list them.

Rules for every proposed change: change wording only; never change a number, macro (\lttv...), citation command, page locator, \enquote{} quotation, cross-reference, or the meaning or strength of a claim. Each `old` must be an exact, unique substring of the named file, copied from the LaTeX. Prefer the smallest change. Keep the author's voice and the four deliberately witty lines (\enquote{media jobs} "have a majority outside the media"; "proves easier to quote than to reproduce"; "came unbundled from its uptake assumption"; "in the accommodating sense that").

## The pass (coherence-cohesion, from the portfolio's pass registry)

1. MAP THE SPINE FIRST. Before editing anything, write one line per section
   saying what question it answers and what it establishes. Then read the list.
   A section whose line you cannot write is the finding, and it is a bigger
   one than any transition.

2. THE SLIDING THREE-PARAGRAPH WINDOW. This is the method that has worked
   here: read paragraphs 1-2-3 and edit 1; read 2-3-4 and edit 2; and so on.
   Each edit is made with its successors in view, which is what catches a
   transition that assumes a paragraph that moved. Fanning out one subagent
   per section is the usual shape for a long manuscript; ask Brett which
   models before dispatching.

3. WHAT TO REPAIR.
   - Transitions where the section changes question, evidence type, or
     explanatory level without marking it. This overlaps level-category-audit
     deliberately: that pass asks whether the shift is legitimate, this one
     asks whether the reader is told.
   - Ambiguous antecedents and vague demonstratives. "This shows" where three
     things precede it. The commonest single hit.
   - Duplicated verdicts: the same conclusion delivered in two places with
     different wording, so the reader cannot tell if they are one claim or two.
   - Announcing openers: "In this section I will" doing work the section's
     first substantive sentence should do.

4. DELIVER EDITS FOR APPROVAL, NOT APPLIED. The house practice for this pass
   is CriticMarkup into Roughdraft so Brett accepts or rejects each one. Flow
   edits are where an agent most easily changes meaning while thinking it is
   changing rhythm.

Do not rewrite. If a passage needs rewriting, say so and stop; that is a
different decision and it belongs upstream.
The procedure's step 2 mentions fanning out subagents; you are the single reader for the whole manuscript. Step 4's CriticMarkup isn't available: give each proposed edit as file, `old`, `new`, and one-line reason, so the author can accept or reject each one.

Report: verdict; then findings (location and quoted text, which step of the procedure, issue, severity) each with an exact proposed replacement where a change is warranted; then what you checked and found clean.
