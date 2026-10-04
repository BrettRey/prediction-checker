# Terminological hygiene: prediction-checker (EJW draft), commit 8186d12

Independent auditor; another model (Claude) wrote and revised this paper. Read-only: you can't edit, so give every proposed change as exact LaTeX in your final message; state which model you are. Standard: truthful, fair, clear. Verify every finding against the files and quote the text you relied on, with its location (section, .tex file and line).

Manuscript: `notes/passes/terminological-hygiene-2026-10-04/tv-unbundling-forecast-check.txt` (rendered PDF text, commit 8186d12; the paper now uses the Econ Journal Watch class, so sections are unnumbered and the introduction is unheaded); LaTeX in `tv-unbundling-forecast-check.tex` and `sections/intro.tex`, `sections/case-lttv.tex`, `sections/discussion.tex`, `sections/appendix.tex` (numbers are macros in `sections/numbers-lttv.tex`; don't edit generated files: `sections/numbers-lttv.tex`, `sections/tables-lttv.tex`, `sections/table-scenarios-main.tex`; table captions live in `scripts/make_tex_tables.py`). House writing rules: `/Users/brettreynolds/projects/LLM-CLI-projects/.claude/rules/writing-style.md`. Decision log: `DECISIONS.md`. Project rules: `CLAUDE.md` (two objects of assessment kept apart: the technical claim and the public predictive argument).

The paper checks a commissioned forecast (Nordicity and Miller 2015) of job losses from the CRTC's 2015 television decisions, put to a House of Commons committee in 2016, against CRTC outcomes for 2016–2019. It has been revised heavily today (a post hoc check that integrates over the baseline's error scale in two versions; a corrected reading of Crawford and Yurukoglu 2012; new literature; wording passes; the EJW conversion), so the places revised today are where problems are likeliest; DECISIONS.md entries dated 2026-10-04 list them.

Rules for every proposed change: change wording only; never change a number, macro (\lttv...), citation command, page locator, \enquote{} quotation, cross-reference, or the meaning or strength of a claim. Each `old` must be an exact, unique substring of the named file, copied from the LaTeX. Prefer the smallest change. Keep the author's voice and the four deliberately witty lines (\enquote{media jobs} "have a majority outside the media"; "proves easier to quote than to reproduce"; "came unbundled from its uptake assumption"; "in the accommodating sense that").

## The pass (terminological-hygiene, from the portfolio's pass registry)

Mechanical layer first, then the judgment layer. The mechanical layer is
already written:

    (already run; output given below)

That covers the gloss subset only. It is triage, not authority, and passing it
is not passing this pass.

The judgment layer:

1. LIST THE PAPER'S LOCAL CONTRASTS. Every paper of Brett's runs on a handful
   of distinctions it introduces and then depends on. Find them: they are
   usually stated once, early, in a sentence of the form "I use X for A and
   reserve Y for B". Write them down as pairs.

2. TRACE EACH TERM. For each side of each pair, collect every occurrence. Ask
   at each one whether the contrast is still being honoured, or whether the
   word has slid into standing for the pair as a whole. The failure is
   gradual, and it concentrates in later sections written after the
   distinction stopped feeling new.

3. CHECK THE CANON TERMS. These are portfolio-wide and non-negotiable, so a
   violation is a defect rather than a judgment call. Category not word class.
   Determinative is the category, determiner the function. Non-count not mass.
   Predicator not predicate. Irrealis not subjunctive. The perfect is secondary
   tense, not aspect. Projectibility is the frame; HPC is one world-side
   commitment, not the frame. Stabilizer is not controller. See canon/entries/
   for the full set and the regexes that find them drifting.

4. CHECK IMPORTED TERMS. A term borrowed from a cited author must be used in
   that author's sense or the divergence must be marked. This is where
   attribution errors originate.

Report: the contrast list, each drift with its location, and the proposed
repair. Prefer repairing the drifted use over redefining the term, since
redefinition invalidates every earlier use.
The mechanical layer has been run; its output is in `notes/passes/terminological-hygiene-2026-10-04/check-terms-gate.txt`. For step 3, the portfolio canon entries are in `/Users/brettreynolds/projects/LLM-CLI-projects/canon/entries/`; most concern linguistics and may not apply to this economics paper, so say which apply.

Report: verdict; then findings (location and quoted text, which step of the procedure, issue, severity) each with an exact proposed replacement where a change is warranted; then what you checked and found clean.
