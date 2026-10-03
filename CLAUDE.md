# CLAUDE.md: prediction-checker
<!-- SUMMARY: Agent guidance for prediction-checker; project rules only, portfolio rules by pointer · status: development · updated: 2026-10-03 -->

## Role

Editor / research collaborator. Deep analytic work is welcome here.

## What this is

A research project that takes consequential predictions made to Canadian legislators, regulators, or courts, reconstructs exactly what was forecast, and checks it against what later happened. `notes/project-brief.md` is the plan; `STATUS.md` has the next action; `cases/` holds one folder per candidate case.

## Rules for this project

- **Nothing in the intake brief is a fact yet.** Every quote, figure, date, and attribution from the 2026-10-03 brief sits in `notes/source-verification.md` as UNVERIFIED until someone has read the primary source and recorded the locator. Several rows attribute quoted predictions to named, living people; treat them with that care.
- **Novelty is a negative claim.** "Nobody has checked this forecast" needs an evidenced search: the exact queries, where they were run, and when. Record them in `notes/novelty-search.md` before the claim appears anywhere else.
- **Two objects of assessment, kept apart.** (1) The technical claim: what follows under the model's stated conditions. (2) The public predictive argument: what decision-makers were told would probably happen. A case write-up that collapses them is wrong whichever way the result falls.
- **Fix the forecast before looking at outcomes.** For each case, write the prediction record (forecaster, date, venue, quantity, magnitude, horizon, stated conditions, baseline) in the case folder and commit it before pulling any outcome series. Anything decided after seeing outcome data is marked **[post hoc]** in `DECISIONS.md`.
- **Numbers come from files.** Every value in the manuscript traces to a file in `data/derived/` or a script in `scripts/`. No figure from memory or from the brief.
- **Data licensing.** `data/raw/` is gitignored. COMPULIFE historical quotation data is a commercial product: never commit it or anything that reconstructs it. Check the Canadian Institute of Actuaries' terms before redistributing anything derived from its experience database. CRTC open data and House of Commons evidence are public; record each source's licence in `data/README.md` at download.
- **Sources.** Put retrieved reports, briefs, and papers in `literature/` at the portfolio root with `.md` companions (`lit` resolves them). The verbatim intake brief in `notes/intake/` is gitignored raw agent output: use it as a lead list, never cite it.
- **Routing.** Public-document reading and candidate scripts can go to `ocx`; run and check scripts locally before any result counts. Quotation and citation fidelity stays on a model that reads the primary source.

## Portfolio rules

House style, writing style, source grounding, bibliography workflow, and dispatch live in `../../../.claude/rules/` and load automatically in a session opened inside the portfolio. Don't copy them here.

## Build

`make` (XeLaTeX + biber). `.house-style` and `references.bib` are symlinks into the portfolio, so the manuscript builds only inside it.
