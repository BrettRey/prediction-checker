# De-AI the prose: prediction-checker (EJW draft), commit 6194dc9

Independent editor; another model (Claude) wrote and revised this paper, so its characteristic tics are the target. Read-only: you can't edit, so give every change as an exact replacement in your final message; state which model you are.

Manuscript: `notes/passes/de-ai-prose-2026-10-04/tv-unbundling-forecast-check.txt` (rendered body); the LaTeX you are editing is `tv-unbundling-forecast-check.tex` (abstract only) and `sections/intro.tex`, `sections/case-lttv.tex`, `sections/discussion.tex`, `sections/appendix.tex`. Don't edit generated files (`sections/numbers-lttv.tex`, `sections/tables-lttv.tex`, `sections/table-scenarios-main.tex`); table captions live in `scripts/make_tex_tables.py` and may be proposed there. Econ Journal Watch draft; the author's standard is "truthful, fair, and clear". Four sentences were just added deliberately for wit (in §2.1: "The testimony's \enquote{media jobs} have a majority outside the media." and "proves easier to quote than to reproduce"; in the discussion: "came unbundled from its uptake assumption" and "in the accommodating sense that"); leave them unless they contain a tic named below.

Rules for every proposed change:
- Change wording only. Never change a number, macro (\lttv...), citation command, page locator, \enquote{} quotation, cross-reference, or the meaning or strength of a claim.
- Each `old` must be an exact, unique substring of the named .tex file (copy it from the LaTeX, not the PDF text), short enough to be unambiguous.
- Prefer the smallest change that removes the tic. Keep the author's voice: warranted stance, live qualification, direct criticism and short sentences are wanted. Don't launder the prose into neutral polish, and don't propose changes that are merely different.

## The pass (de-ai-prose, from the portfolio's pass registry)

Read /Users/brettreynolds/projects/LLM-CLI-projects/.claude/rules/writing-style.md in full first. It is the specification and
it is long; this entry lists the clusters so none is skipped, not so the file
can be skipped.

Mechanical layer:

    (already run; output in notes/passes/de-ai-prose-2026-10-04/check-style-output.txt; most hits there are false positives: maths subscripts, 'pointwise', ranges that aren't ranges)

That covers the lexical list (delve, underscore, tapestry, realm, foster,
pivotal, leverage, and the rest). It is triage, not authority.

The structural clusters, none of which a linter finds:

1. PRAISE-AS-STRUCTURE. "load-bearing" as analytical metaphor, "doing the heavy
   lifting", "does real work", "deserves the weight". Very high signal. The one
   carve-out is "load-bearing assumption" in the Dewar sense, capped at two per
   paper with a gloss and citation.
2. FAUX-COACHING. "Let me refine your claim", "the one place I'd still push",
   "the tell is", "structural spine". Prose performing an expert giving live
   feedback.
3. RESTATEMENT-AS-REVELATION. A sentence whose payload is a word lifted from
   the sentence before, rotated to sound like an arrival.
4. CORRECTIVE NEGATION WITH NO OPPONENT. "The problem isn't X, it's Y" where
   nobody asserted X. Costs a clause and invents an interlocutor. Keep it only
   where a real position is being rejected, and then name whose and cite it.
5. COLON REVEALS. Punctuation staging a drumroll the content does not earn.
6. PROFUNDITY FROM EMPTINESS. Absence turned into an aphorism.
7. FAUX-INSIGHT SETUPS. "What nobody tells you is", "here's what most people
   miss".
8. NOUN STACKING. Two or more nouns premodifying a head. Trouble starts at two.
   Unpack with prepositions or a finite clause.
9. UNSUPPORTED EVALUATIVE PARTICIPIAL TAGS. ", highlighting the pattern's
   importance", ", underscoring the need for", ", paving the way for".
10. THE "while maintaining/preserving" TRADE-OFF FRAME where no trade-off was
    measured.
11. WEASEL ATTRIBUTION. "Some critics argue", "research suggests". Name the
    source or cut.
12. INTEGRAL CITATION. Where a clause attributes an act to an author with a
    reporting verb, the author is the grammatical subject and the year folds
    in: \textcite{}, not a trailing \citep{}. The clearest tell is a doubled
    "Kane ... (Kane, 2013)".
13. FALSE RANGES and TRIADIC ADJECTIVE STRINGS.
14. "THE PRESENT" SELF-REFERENCE. Never "the present paper" or "the present
    author".
15. CONCRETENESS THAT IS NOUNS RATHER THAN OBSERVABLES. Marked very high
    signal, and the longest rule in the file, so do not treat it as the tail
    of a list. A passage is not grounded because the running example's proper
    nouns appear in it: naming a firm, a score, a benchmark or a "matter"
    while leaving the claim unspecified sounds concrete and constrains
    nothing. Nor is it grounded by attaching abstract nouns (link, facet,
    standing, carries to X) to parts of the architecture, which only
    redescribes the inference. Tells: abstract nouns doing the work; one token
    concrete sentence in an otherwise floating paragraph; the example's name
    sprinkled through sentences that would read identically without it. The
    fix is to replace each abstract label with a specific observable, a named
    contrast between a supported and an unsupported use, or a procedure, and
    to state the stop condition. Corollary for source-to-target reasoning: a
    link is assessed by describing two settings and investigating the specific
    sources of non-transfer between them. Until the two settings and the
    possible non-transfers are named, the link is a box in a diagram.

Two distributional checks, not per-instance: paragraph openers that name the
argumentative object rather than making the move, and paragraph closers that
restate the paragraph as though concluding it. Two or three in a row is the
signal.

Do not launder the prose into polished neutrality. Warranted stance, live
qualification, direct criticism, and short sentences are wanted. The target is
tics, not voice.

Report: verdict; then a numbered list of changes, each with: file; cluster (from the list above); `old` (exact LaTeX); `new` (exact LaTeX); one-line reason. Group by file in document order. Then the two distributional checks (paragraph openers; paragraph closers) with the specific paragraphs, and anything you looked at and left alone on purpose.
