# Level and category audit: prediction-checker (EJW draft), commit 9c49e9c

Independent auditor; another model wrote and revised this paper. Read-only; give your full report in your final message; state which model you are. Standard: truthful, fair, clear. Verify every finding against the files before reporting it, quote the manuscript text you relied on, and give its location (section and the .tex file and line).

Manuscript: `notes/passes/level-category-audit-2026-10-04/tv-unbundling-forecast-check.txt` (rendered PDF text, commit 9c49e9c); LaTeX in `tv-unbundling-forecast-check.tex` and `sections/*.tex` (numbers are macros defined in `sections/numbers-lttv.tex`); plan `notes/analysis-plan.md`; decisions `DECISIONS.md`; project rules `CLAUDE.md` (note the rule on two objects of assessment: the technical claim, what follows under the model's stated conditions, and the public predictive argument, what decision-makers were told would probably happen). The report the paper checks is `/Users/brettreynolds/projects/LLM-CLI-projects/literature/nordicity_miller_2015_canadian_television_2020.md`.

The paper is an Econ Journal Watch draft checking a commissioned forecast (Nordicity and Miller 2015) of job losses from the CRTC's 2015 television decisions, put to a House of Commons committee in 2016, against CRTC outcomes for 2016–2019. Its central quantity is a forecast scale k (0 = the report's baseline, 1 = its reform path), estimated by GLS with the baseline's error modelled as a random walk; it is explicitly not an estimate of the decisions' causal effect.

Run the pass below exactly as written. This is an audit: report findings and proposed repairs; change nothing.

## The pass (level-category-audit, from the portfolio's pass registry)

Read CLAUDE.md's "Explanation-Level Discipline" section first. Four checks:

1. IS THE TARGET DEFINED BEFORE THE MECHANISM? For each explanatory passage,
   find where the behaviour, judgment, category, model output, or social fact
   being explained is actually specified. If the mechanism arrives first, the
   passage explains something the reader cannot yet identify.

2. WHICH LEVEL IS EACH CLAIM AT, AND IS THE SHIFT MARKED? The levels:
   behavioral, algorithmic, social-practical, corpus-distributional,
   model-internal, neural or biological, institutional, normative. Sliding
   between them is legitimate and often necessary. Sliding without saying so
   is the defect. Flag each unmarked transition.

3. FILLER VERBS. Search for underlies, involves, regulates, drives, encodes,
   represents. Each is permitted only where the mechanism or the test is
   specified. Where it is not, the verb is supplying explanatory sound over a
   correlation. Quote the sentence and say what would have to be specified.

4. MEREOLOGICAL SLIPPAGE. Parts do not do what wholes do. Neurons do not
   understand, embeddings do not mean, fields do not decide, grammars do not
   judge, corpora do not know. Find every predicate attributed to the wrong
   bearer. This one is easy to miss because the sentences read naturally.

Also check the related move: a large internal map (connectome, activation
atlas, vector space, corpus inventory) offered as an explanation rather than as
a resource for testing a hypothesis. Detail is not explanation.

Report each hit with its location, which of the four it is, and the repair.
Where drift remains after the pass, say so explicitly: the checklist requires
that remaining drift be accepted by Brett rather than left unmentioned.
The CLAUDE.md section the procedure refers to:

### Explanation-Level Discipline

Before explaining a behavior, judgment, category, model output, neural finding, or social fact, identify the explanatory level being used: behavioral, algorithmic, social-practical, corpus-distributional, model-internal, neural/biological, institutional, or normative. Do not slide between levels without saying so.

- Define the target behavior/profile before proposing mechanisms or internals.
- Avoid filler verbs (`underlies`, `involves`, `regulates`, `drives`, `encodes`, `represents`) unless the mechanism or test is specified.
- Avoid mereological claims: parts do not do what wholes do. Neurons do not understand, embeddings do not mean, fields do not decide, grammars do not judge.
- Treat large internal maps (connectomes, model activations, vector spaces, corpus inventories) as resources for testing hypotheses, not as explanations by themselves.
- Use LLM critique as a sparring/checking aid, not as evidence.

---

Report: verdict; findings table (location and quoted phrase, which check, issue, severity, proposed repair); then what you checked and found clean. If drift remains that you judge acceptable, say so explicitly so the author can accept it.
