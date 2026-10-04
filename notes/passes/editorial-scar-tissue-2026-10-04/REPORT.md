<!-- Saved verbatim by the parent session from Codex stdout (codex-stdout.txt, gitignored), 2026-10-04. -->

**Verdict: two minor instances of editorial scar tissue; no major problem on this pass.** Most qualifications added during revision serve the reader and should stay.

Model: GPT-6, running as Codex; the supplied manifest identifies this audit as **GPT-6 Astra, xhigh**. I checked commit `8186d12` read-only. No files were changed.

**1. The Crawford–Yurukoglu correction is stated twice.**

Location: “Payments, closures and staff counts” → “Payments to Canadian channels,” [sections/case-lttv.tex:133](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/case-lttv.tex:133).

Procedure: **tell 1**, contrastive negation of earlier wording; also **tell 4**, reinforcement against the old misreading. Severity: **minor**.

**Old — exact sentence:**

```latex
That model predicts a small fall, not the rise observed here, and the aggregates can't show which mechanism operated.
```

The preceding sentence already states the corrected result: `but by only 3.7\% once contracts between channels and distributors are renegotiated`. The paragraph also opens:

> The aggregates can't say what fees would have been without the decisions, or why affiliation payments per subscriber rose.

Thus the predicted fall and observed rise are already explicit. Repeating their opposition reads as reassurance that the former interpretation has been withdrawn. The revision history confirms that connection: [DECISIONS.md:229](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/DECISIONS.md:229) records that the earlier description, `"predicts the direction observed"`, was wrong.

Retain the return from the theoretical example to the limits of the Canadian evidence; remove the repeated correction.

**New:**

```latex
The aggregates can't show which mechanism operated.
```

The preceding numerical result, observed direction and identification limit all remain.

**2. The cut-posterior parenthesis answers the superseded label.**

Location: Appendix A, “Estimation details” → “Integrating over the error scale (post hoc),” [sections/appendix.tex:41](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/appendix.tex:41).

Procedure: **tells 1 and 4**. Severity: **minor**.

**Sentence:**

```latex
In the version specified first, \(\sigma\)'s posterior combines its prior with \(p(y\mid\sigma)\); in the prior-only version, computed after it, the likelihood term is dropped, so the outcomes don't update \(\sigma\) and its prior weights the mixture (a cut posterior, not the ordinary posterior under this model).
```

The sentence already explains the distinction operationally: the first calculation updates the scale; the second prevents that update and weights the mixture by the prior. Naming the latter a *cut posterior* completes the explanation. The additional denial repeats the correction to the former blanket use of “posterior,” documented in [the recheck-6 triage, line 8](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/notes/passes/2026-10-04-recheck6.md:8).

**Old — smallest unique substring:**

```latex
(a cut posterior, not the ordinary posterior under this model)
```

**New:**

```latex
(a cut posterior)
```

The definition and chronology remain intact.

**Checked and found clean on this pass**

- **The two objects of assessment remain distinct.** The unheaded introduction says, “It tests neither the total employment forecast nor the decisions' causal effect” ([intro.tex:9](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/intro.tex:9)). This limitation establishes the paper’s scope; it does useful work.
- **The corrected literature wording reads as fresh exposition.** “No statistically significant positive association” ([intro.tex:21](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/intro.tex:21)) incorporates the correction without recounting it. Likewise, “only weakly for CPE” ([case-lttv.tex:35](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/case-lttv.tex:35)) states the revised assessment directly.
- **The error-scale qualifications are substantive.** “The pre-stated intervals also treat the error scale as known (the post hoc integrated checks relax that)” ([discussion.tex:23](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/discussion.tex:23)) distinguishes calculations actually reported. The chronology and differing results of the two integrated versions also warrant their space.
- **The measurement cautions prevent plausible reader errors.** “With or without added channels” distinguishes the CRTC counts from BYOP uptake ([case-lttv.tex:71](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/case-lttv.tex:71)); “a comparison on that single scale, not year by year” defines compatibility ([case-lttv.tex:79](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/case-lttv.tex:79)). Neither merely answers an earlier draft.
- **The figure qualification is useful locally.** “It isn't a probability interval” distinguishes the cited-input band from the plotted uncertainty intervals ([case-lttv.tex:105](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/case-lttv.tex:105)).
- **All four designated witty lines remain untouched**, in [case-lttv.tex:28](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/case-lttv.tex:28), [discussion.tex:9](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/discussion.tex:9) and [discussion.tex:17](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/discussion.tex:17).

I checked the rendered manuscript, the named LaTeX sources, captions, and the revision decisions and audit records. Both `old` strings occur exactly once in their named files. Applying these replacements in memory preserved every number, macro, citation, locator, quotation and cross-reference. This was a wording audit, not a new numerical or source-verification audit.
