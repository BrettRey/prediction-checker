# DECISIONS
<!-- SUMMARY: dated log of setup and design choices for prediction-checker; setup entries only so far · status: development · updated: 2026-10-03 -->

Format: `YYYY-MM-DD — Decision. Reason.` Choices made after seeing outcome data are marked **[post hoc]**.

## Setup

2026-10-03 — Project placed at `papers/development/prediction-checker/`, slug from Brett's name for it. Source and data work before a paper is shaped, which is what `development/` holds. `main.tex` carries a working title only.

2026-10-03 — The pasted brief is kept verbatim in `notes/intake/` and gitignored. It is LLM-written (every link carries `utm_source=chatgpt.com`; model unknown), so it counts as raw agent output under the portfolio's publishing rule. `notes/project-brief.md` is a distillation that points at the verification table rather than restating claims.

2026-10-03 — Every checkable claim in the brief (39) queued as UNVERIFIED in `notes/source-verification.md`, with tracking parameters stripped from the pointers. Several attribute quoted predictions to named, living people, so nothing is restated as fact anywhere else until verified.

2026-10-03 — The brief's four "didn't locate a retrospective study" statements report no queries; recorded as unverified negatives. `notes/novelty-search.md` logs searches actually run.

2026-10-03 — Scope assumed from the brief, pending Brett: Canada; forecasts made to legislative committees, regulators, and courts; a case qualifies only if no public retrospective already tests that forecast. Brett's exemplar case and his view on the courts-only question aren't on file.

2026-10-03 — Method commitments carried from the brief into `CLAUDE.md`: technical claim and public predictive argument assessed separately; each case's prediction record committed before outcome data are pulled.

2026-10-03 — Public GitHub repo under `BrettRey/`, CC BY 4.0 (portfolio default for open papers). `data/raw/` gitignored; COMPULIFE data never committed; CIA terms checked before publishing derived files. Decision owner: Brett (standing default for new projects, `~/.claude/CLAUDE.md`); assisting: Claude Opus 5.5; status: executed 2026-10-03, payload enumerated before push (27 files, verbatim brief excluded); record: this file.

2026-10-03 — `.house-style` and `references.bib` are symlinks into the portfolio (template snapshot replaced), so the repo builds only inside the portfolio.

2026-10-03 — Dropped the template's `.agent/workflows/` (its multi-agent review recipe still calls the deprecated Gemini CLI), empty `docs/plans/`, and `.house-style-version` (meaningless once `.house-style` is a symlink). Dispatch guidance lives in the portfolio rules.

## Corpus-awareness adjudication (setup)

Inward searches: qmd and full-text grep over `literature/` (queries in `notes/novelty-search.md`); `grep -i 'forecast|predict|policy|legislat|audit|accountab|conditional'` over `Project-Management/intellectual-map.md`; `grep -i 'forecast|legislat|parliament|regulat'` over `papers/CLAIMS.md` (no hits); `find -iname '*predict*'` from the portfolio root to depth 4.

2026-10-03 — `Project-Management/prediction-ledger/`: **deliberately distinguished**. Same word, different object: it scores Brett's own probabilistic forecasts of venue decisions with Brier scores; this project audits other people's magnitude forecasts of policy effects. Its never-retro-forecast rule is the same discipline as freezing prediction records here.

2026-10-03 — `papers/queue/difference-in-differences-for-corpus-linguistics/`: **deferred**. Method neighbour for case 3's design (offence groups that lost preliminary-inquiry eligibility versus groups that kept it), and for any comparison-jurisdiction design in case 1.

2026-10-03 — `papers/retarget/kinds-as-projectibility-profiles/` and Goodman, *Fact, Fiction, and Forecast* (in `literature/`): **deferred**. Possible bearing on the gap between a model's conditional result and the unconditional inference offered to legislators. A prompt to look, not yet a connection.

2026-10-03 — `papers/queue/effective-without-warrant/`: **deferred**. A forecast can shape a legislative outcome whether or not it was warranted; whether that is the same effective/warranted split is unexamined.
