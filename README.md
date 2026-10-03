# prediction-checker

When experts tell Canadian legislators, regulators, or courts what a decision will cause, and the decision goes ahead, does anyone later check? This project picks forecasts that were used in consequential debates, reconstructs exactly what was predicted and under what conditions, and tests them against what happened.

Status: early development. Nothing here is a finding yet.

## Approach

Each case keeps two things apart: the **technical claim** (what a model implies under its stated conditions) and the **public predictive argument** (what decision-makers were told would probably happen). Prediction records are written from the primary sources and committed before any outcome data are pulled, so the test can't be bent toward the result.

## Candidate cases

| Folder | Case |
|---|---|
| `cases/gnda-life-insurance/` | Actuarial forecasts of life-insurance premium increases under the *Genetic Non-Discrimination Act* |
| `cases/lets-talk-tv/` | A 2015 economic model of job and production losses from the CRTC's *Let's Talk TV* reforms |
| `cases/c75-preliminary-inquiries/` | Competing forecasts about delay from restricting preliminary inquiries under Bill C-75 |

The case descriptions come from an unverified lead list. Every factual claim about them is tracked in `notes/source-verification.md` and none has been checked against its source yet.

## Layout

```
cases/                     one folder per case: prediction record, design notes
notes/project-brief.md     plan, assumptions, method commitments
notes/source-verification.md   every claim from the intake brief, with status
notes/novelty-search.md    the searches behind any "nobody has checked this" claim
data/                      raw/ (gitignored) and derived/; licence register
scripts/                   analysis code
main.tex                   manuscript (placeholder)
DECISIONS.md, STATUS.md    decision log and current state
```

`main.tex` builds with XeLaTeX inside Brett Reynolds's portfolio: `.house-style` and `references.bib` are symlinks to shared files outside this repository.

## Licence

Text, notes, and data products: [CC BY 4.0](LICENSE), unless a source's own terms say otherwise (see `data/README.md`).
