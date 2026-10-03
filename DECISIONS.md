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

## Forecast verification and prediction records (cases 1–2)

2026-10-03 — Post-intervention material is HELD until each case's prediction record is committed: retrospectives (G08, X01–X04), outcome claims and data sources (G10–G14, T14–T15), and implementation evidence (G09). Legal-history rows (G07, T10) are left UNVERIFIED rather than held, since they describe changed conditions, not outcomes. Reason: the record has to be fixed before anyone sees what happened.

2026-10-03 — Locator convention: committee evidence by committee, meeting, speaker, and bracketing five-minute time marks, e.g. JUST 36, Howard, (1220)–(1225); Nordicity report by paragraph and printed page (PDF page − 4); CIA brief by PDF page and point; CIA model paper by section and PDF page. Reason: time marks and paragraph numbers survive format changes; the two-column committee PDFs garble under text extraction.

2026-10-03 — Committee transcripts stored in `literature/` as the official PDF plus a `.md` built from the HTML DocumentViewer page (pandoc plain, trimmed to the evidence, time marks kept). Each `.md` starts with retrieval URL, date, and SHA-256. Reason: `lit convert` on the two-column PDF loses speaker order and time marks.

2026-10-03 — G05 marked PARTLY: the CIA brief has the "All else being equal" qualification and the large-policy exemption (proposed s. 4(3), 200 × AWE), but never names adverse selection; it describes the incentive (point 2). Reason: the brief's claim overstated the source's wording.

2026-10-03 — Case 1 prediction record kept as one row per statement (CIA brief; Howard; Frank attributing to the CIA; Boudreau; Frank's own coverage forecast; Howard on the U.K.), with the 2014 CIA model paper recorded separately as the technical claim. Reason: the statements disagree on quantity (premiums vs mortality experience), timing ("soon after" vs "over time" vs "more than a decade"), and modality ("could" vs "likely"); merging them would hide the split the project exists to test.

2026-10-03 — Rows not in the brief (G15–G19, T16–T20) added under separate headings marked "read from source, not from the brief", so their provenance stays distinct from the LLM lead list.

2026-10-03 — The 2014 CIA model paper (Doc. 214082) was retrieved from the Wayback Machine (snapshot 2021-11-29); its cia-ica.ca URL returned HTTP 410. Finding: the paper reports mortality-experience increases of 36% / 58% under a $1 million disclosure threshold and does not quantify the premium increase; the 30% / 50% premium figures used in testimony are unlocated (row G18). Not resolved; the 2016 CIA critical-illness paper and any Senate submission are the next places to look.

2026-10-03 — The CLHIA's voluntary $250,000 commitment (announced at JUST 36; press release 2017-01-11, effective 2018-01-01) recorded as a competing intervention in case 1. Proposed consequence, pending Brett: the counterfactual is "industry code only", not "no restriction". Raised by Brett's question on 2026-10-03 whether the pledge took effect; answer so far: scheduled, overtaken on paper by the Act's assent on 2017-05-04, implementation not established.

2026-10-03 — Morrison's skinny-basic uptake estimate (T16, about 4%) recorded beside the report's BYOP assumption (T20, 5% in 2016 rising to 15%), since the project brief says to test near mechanisms before multiplier-derived totals.

2026-10-03 — Correction to the case 1 record, made before any outcome data were opened (so not [post hoc]): the model's threshold is the amount above which insurers may still require disclosure, so the enacted Act (no threshold) is at least as severe as the model's $1 million headline, not close to its $100,000 scenario. The record now orders the regimes ($100k scenario < CIA amendment ~$190k < CLHIA code $250k < $1M headline < Act) and states that flat premiums would count against the model's headline unless only the CLHIA code was operative. Also removed a memory-sourced reference to the Quebec reference from the legal-status row; only G07 (unverified) remains.

## Scope, exemplar, lead case, and analysis design (2026-10-03, after the freeze)

2026-10-03 — Scope kept: forecasts made to legislative committees, regulators, and courts, not Supreme Court litigation only. Decision owner: Brett.

2026-10-03 — Exemplar: Kane, "After SFFA v. Harvard: Predictions that Didn't Come True", *Econ Journal Watch* 23(2): 485–508 (September 2026), proposed by Brett and filed in `literature/`. The identification with the brief's "your example" is an inference: the brief says its leads "weren't predictions made exclusively in Supreme Court litigation", and its three set-aside cases are all Supreme Court of Canada rulings. Design features adopted from it are listed in `notes/project-brief.md`.

2026-10-03 — Manuscript stays in LaTeX. Decision owner: Brett.

2026-10-03 — Lead case *Let's Talk TV*, second case GNDA. Decision owner: Brett (delegated 2026-10-03); chosen by Claude Opus 5.5. Reason: *Let's Talk TV* can be tested before any identification question arises (the model's own inputs, such as unbundled uptake and closures, are directly observable; both scenario paths are published by year; four pre-pandemic years; administrative data). GNDA's forecast quantity has no confirmed data source, its counterfactual splits between the Act and the CLHIA code with compliance unknown, and the 30% / 50% derivation is unlocated. GNDA stays in the paper because its main finding so far (the technical claim against the public argument, row G18) needs no outcome data; its premium test waits on a feasibility check.

2026-10-03 — Case 1 uses both counterfactuals, reported side by side: (i) no restriction, the 2016 status quo, which tests the forecast as made; (ii) CLHIA code only, which isolates the Act's contribution. Decision owner: Brett ("why not both?"). The above/below-$250,000 contrast follows from (ii).

2026-10-03 — Test windows replaced by full-path estimates compared with each forecaster's implied timing. Made before any outcome data were opened, so not [post hoc]. Supersedes the window proposal in the case 1 file.

2026-10-03 — Analysis plan proposed in `notes/analysis-plan.md`: forecasts tested as distributions built from the forecasters' own cited inputs as well as the testimony's point figures; every cell of a fixed comparison grid reported; differences between comparisons given their own uncertainty. A design analysis by fake-data simulation for each case gates the release of HELD rows and the opening of any outcome series. Sources for the method: Gelman and Carlin 2014; Gelman and Loken 2014; Gelman and Stern 2006; Gelman et al. 2020 (all in `literature/`).

2026-10-03 — Corpus-awareness adjudication: `papers/queue/difference-in-differences-for-corpus-linguistics/` stays **deferred**, now with a concrete use (case 1's above/below-$250,000 contrast is a difference-in-differences design). Read it before writing the case 1 design analysis, then adopt or distinguish.
