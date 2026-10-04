<!-- Saved verbatim by the parent session from Codex stdout (codex-stdout.txt, gitignored), 2026-10-04 (second run; the first stopped at a usage limit). -->

**Verdict:** Local cleanup is warranted. The clearest remaining tics are noun stacks, abstract descriptions of calculations, and one redundant restatement. The criticism, qualifications and deliberate wit should remain.

**Model:** Codex, based on GPT-6. I read the full style specification. Every `old` below is an exact, unique substring at `6194dc9`. No files changed. Numbers, commands, quotations, locators and cross-references remain unchanged.

1. **File:** [sections/case-lttv.tex:20](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/case-lttv.tex:20)  
   **Cluster:** 15 — concreteness.
   
   **old**
   ```latex
   Unbundling and the preponderance change act through BYOP subscribers and so scale with uptake; the report sets the exemption order and closures separately, though it values them partly from the other two
   ```
   **new**
   ```latex
   The modelled revenue losses from unbundling and the preponderance change scale with BYOP uptake; the report sets the losses from the exemption order and closures separately, though it calculates them partly from the other two
   ```
   **Reason:** Names the quantities being scaled and calculated; the policy changes themselves aren't those quantities.

2. **File:** [sections/case-lttv.tex:59](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/case-lttv.tex:59), figure 1 caption  
   **Cluster:** 8 — noun stacking.
   
   **old**
   ```latex
   and the exemption-order and closure dollar components fixed
   ```
   **new**
   ```latex
   and the dollar components for the exemption order and closures fixed
   ```
   **Reason:** Makes the relation between the dollar components and their sources explicit.

3. **File:** [sections/case-lttv.tex:71](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/case-lttv.tex:71)  
   **Cluster:** 15 — concreteness.
   
   **old**
   ```latex
   reported beside the planned reading
   ```
   **new**
   ```latex
   reported beside the uptake evidence allowed by the plan
   ```
   **Reason:** Specifies what the survey is being reported beside; “reading” leaves that relation unnamed.

4. **File:** [sections/case-lttv.tex:77](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/case-lttv.tex:77)  
   **Cluster:** 8 — noun stacking.
   
   **old**
   ```latex
   hold the exemption-order and closure dollar components fixed
   ```
   **new**
   ```latex
   hold the dollar components for the exemption order and closures fixed
   ```
   **Reason:** Unpacks the same compressed modifier sequence in the account of the recalculation.

5. **File:** [sections/discussion.tex:7](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/discussion.tex:7)  
   **Cluster:** 3 — restatement-as-revelation.
   
   **old**
   ```latex
   These comparisons set outcomes against the report's paths. They don't estimate the decisions' effect, and they don't test the total employment forecast.
   ```
   **new**
   ```latex
   These comparisons don't estimate the decisions' effect, and they don't test the total employment forecast.
   ```
   **Reason:** Removes a summary of the comparison just described while retaining both substantive limits.

6. **File:** [sections/discussion.tex:15](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/discussion.tex:15)  
   **Cluster:** 15 — concreteness.
   
   **old**
   ```latex
   His appearance also presented the losses as open to policy, citing the authors' proposals to reduce them
   ```
   **new**
   ```latex
   He also said policy changes could reduce the losses, citing the authors' proposals to reduce them
   ```
   **Reason:** Replaces “open to policy” with the claim Morrison made and gives the reporting verb its human subject.

7. **File:** [sections/appendix.tex:11](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/appendix.tex:11)  
   **Cluster:** 8 — noun stacking.
   
   **old**
   ```latex
   the report's forecast shortfall path
   ```
   **new**
   ```latex
   the report's path of forecast shortfalls
   ```
   **Reason:** Unpacks the three-noun sequence without changing the mathematical object.

8. **File:** [sections/appendix.tex:19](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/appendix.tex:19)  
   **Cluster:** 8 — noun stacking.
   
   **old**
   ```latex
   the log shortfall path recomputed
   ```
   **new**
   ```latex
   the path of log shortfalls recomputed
   ```
   **Reason:** Makes clear that the path consists of shortfalls measured in logs.

9. **File:** [sections/appendix.tex:19](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/appendix.tex:19)  
   **Cluster:** 8 — noun stacking.
   
   **old**
   ```latex
   the exemption-order and closure dollar components held fixed
   ```
   **new**
   ```latex
   the dollar components for the exemption order and closures held fixed
   ```
   **Reason:** Unpacks the recurring component description in the estimator's definition.

10. **File:** [sections/appendix.tex:22](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/appendix.tex:22)  
    **Cluster:** 15 — concreteness.
    
    **old**
    ```latex
    The band projects onto
    ```
    **new**
    ```latex
    To construct the band, I project onto
    ```
    **Reason:** States the operation used to construct the band instead of making the resulting band perform it.

11. **File:** [sections/appendix.tex:22](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/appendix.tex:22)  
    **Cluster:** 15 — concreteness.
    
    **old**
    ```latex
    which keeps the report's ramp
    ```
    **new**
    ```latex
    which preserves the report's proportional increases in uptake
    ```
    **Reason:** Specifies what remains unchanged when the uptake path is rescaled.

The following caption changes are grouped under their source file, in **document order**: table 1, then B2 and B3. The fragments are copied from the Python source, including its string boundaries.

12. **File:** [scripts/make_tex_tables.py:459](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/scripts/make_tex_tables.py:459), table 1  
    **Cluster:** 8 — noun stacking.
    
    **old**
    ```text
    the exemption-order and closure dollar components are held fixed
    ```
    **new**
    ```text
    the dollar components for the exemption order and closures are held fixed
    ```
    **Reason:** Applies the same unpacking to the main table's caption.

13. **File:** [scripts/make_tex_tables.py:164](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/scripts/make_tex_tables.py:164), table B2  
    **Cluster:** 15 — concreteness.
    
    **old**
    ```text
    The cited-input band scales
    ```
    **new**
    ```text
    To construct the cited-input band, I scale
    ```
    **Reason:** Identifies the calculation that produces the band instead of assigning the calculation to its result.

14. **File:** [scripts/make_tex_tables.py:212](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/scripts/make_tex_tables.py:212), table B3  
    **Cluster:** 8 — noun stacking.
    
    **old**
    ```text
    the exemption-order and "
      "closure dollar components
    ```
    **new**
    ```text
    the dollar components for the exemption order and "
      "closures
    ```
    **Reason:** Unpacks the component description while preserving the source's adjacent string literals.

15. **File:** [scripts/make_tex_tables.py:215](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/scripts/make_tex_tables.py:215), table B3  
    **Cluster:** 15 — concreteness.
    
    **old**
    ```text
    which scales the report's ramp
    ```
    **new**
    ```text
    which scales the report's year-by-year uptake shares
    ```
    **Reason:** Names the values being scaled rather than their metaphorical shape.

**Distributional check — paragraph openers.** Three concentrations deserve inspection, but none warrants a further replacement:

- **Introduction, paragraphs beginning “The number came…”, “This paper compares…” and “The report's main input…”**: successive provenance, scope and definition moves. Each supplies information immediately.
- **§3, consecutive paragraphs beginning “The 95\% interval…”, “The scale…”, “The plan's verdicts…” and “The outcome series alone…”**: the strongest repeated cadence. These define distinct parts of the method; varying them for rhythm would obscure useful signposting.
- **§5.1, “The report also assumed…”, “The report's fee is…” and “The aggregates can't say…”**: another three-paragraph run, but the movement from prediction to comparability to inferential limits is clear.

**Distributional check — paragraph closers.** I found no run of two or three empty seals. Change 5 removes the clearest local repetition. The introduction's “The public argument is what the committee was told” completes a needed definition. The §4.2 closer identifies what the survey puts in doubt. The final “A committee hearing such a forecast can ask for both” adds an action to the preceding conditions. Keep these.

**Examined and deliberately retained:**

- **All four deliberate jokes.** Each refers to a demonstrated discrepancy or qualification. None relies on an empty revelation.
- **“The report deserves credit…”**: warranted appraisal supported by the following particulars, rather than praise used as an engineering metaphor.
- **The causal-effect, employment and comparability qualifications.** These delimit the analysis; treating them as phantom-opponent negations would weaken the paper.
- **Colons introducing definitions, evidence and lists**, including “The uptake evidence is thin:”. Their payloads justify them.
- **“Chain” and “link” where the steps are specified.** Uptake, revenue, payments, programming expenditure and jobs are connected through stated assumptions; the examples aren't merely decorative proper nouns.
- **The citations, numerical ranges and substantive participial clauses.** The existing citations identify sources; the ranges have common scales; clauses about allowing for baseline error and leaving verdicts unchanged describe analytical conditions or results.
- **The abstract and introduction:** no replacement met the threshold of removing a tic without merely restyling the prose.

No further changes were warranted under clusters 1, 2, 4–7 or 9–14.
