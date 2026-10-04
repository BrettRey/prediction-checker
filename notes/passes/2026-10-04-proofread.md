# Proofread, 2026-10-04
<!-- SUMMARY: read-only proofread of main.tex and sections at ceb6cdd; no grammar errors found beyond one awkward phrase; main findings are paragraph length (systemic), four doubled-name citations, two unglossed terms · status: report · updated: 2026-10-04 -->

Run by Claude Opus 5.5 at commit ceb6cdd, following the `proofread` skill: linter (`check-style.py`, run separately as the house-style pass), `check-terms.py --follow-inputs`, and a manual audit against the skill's checklist. Report only; no source edited.

## Findings

| # | Location | Category | Severity | Current text | Suggested fix |
|---|---|---|---|---|---|
| 1 | Throughout (32 paragraphs) | quality | major (systemic) | Paragraphs over 100 words: the abstract (174, acceptable for an abstract); intro para 2 (about 140) and para 4 (about 170); §2 jobs (about 120) and chain (about 160); §2.1 testimony analysis (about 150); §3 model (about 170), interval (about 130), band (about 130); §4.3 results (about 160); §4.4 (about 115); §4.5 (about 125); §4.6 para 2 (about 175); §5.1 (about 115); §5.2 (about 125); §5.3 (about 130); discussion paras 2–5 and the limits paragraph (about 150–190); data and code (about 190). Counts approximate (macros and citations counted as single tokens) | House cap is ~60 words, max 100. The worst cases split at a natural seam without rewording: §4.6 para 2 before "Distributors' revenue shows no such change"; discussion limits paragraph before "The uptake evidence is thin"; data and code before "The case was first suggested"; §3 model paragraph before "Because the baseline's error accumulates". A full pass belongs to `density-leavening`, not here |
| 2 | §1 para 1 (intro.tex) | style (integral citation) | minor | "the consultancy Nordicity and Peter Miller, ... \citep{nordicity2015television}" (names in the sentence, then repeated in the parenthesis) | `the consultancy Nordicity and Peter Miller \citeyearpar{nordicity2015television}` |
| 3 | §1 para 2 (intro.tex) | style (integral citation) | minor | "Miller's own later work for the CRTC discusses ... \citep[n.~88, n.~196]{miller2022rights}" | `Miller's own later work for the CRTC \citeyearpar[n.~88, n.~196]{miller2022rights} discusses ...` |
| 4 | §1 literature paragraph | style (integral citation) | minor | "\textcite[322]{simpson2014overestimate} warns ...; his review notes ... \citep[319--321]{simpson2014overestimate}" renders "Simpson (2014, p. 322) ... (Simpson, 2014, pp. 319–321)" | End with `(pp.~319--321)` |
| 5 | §2 para 2 | style (integral citation) | minor | "Nordicity and Peter Miller's \textit{Canadian Television 2020}, dated December 2015, was prepared for ... \citep{nordicity2015television}" | Drop the final `\citep` (authors, title and date are in the sentence), or use `\citeyearpar` after the title |
| 6 | §4.2 survey paragraph | style (integral citation) | minor | "A survey by the Media Technology Monitor, released in August 2017, ... \citep{mtm2017starter}" renders the organization twice | `A survey by the Media Technology Monitor \citeyearpar{mtm2017starter} put adoption ...`, keeping "in August 2017" elsewhere in the sentence |
| 7 | Abstract | terminology | minor | "than any cited uptake estimate implies" (uptake is defined only two sentences later) | "than any estimate of package uptake the study cited implies" |
| 8 | §5.1 para 2 | terminology | minor | "Canadian specialty and pay, PPV and VOD services" (PPV and VOD unexpanded in the text; expanded only in table B1's note) | "Canadian specialty, pay, pay-per-view and video-on-demand services" |
| 9 | §5.2 | grammar | minor | "around the 8 the report's rate implies" | "around the 8 that the report's rate implies" |

## Checked clean

- No em-dashes; en-dash conventions consistent.
- No uncontracted forms apart from an appositive "that is" (§2) and a quotation ("If it is right").
- No throat-clearers, hackneyed adverbs or `\paragraph{}` headings; no doubled words.
- Brackets sit outside italics.
- Citation conventions are consistent: lower-case "table~\ref" for the paper's own tables, capitalized "Table" for the report's.
- Every statistic traces to a macro or to a quoted source with a locator.
- `check-terms.py` acronyms: GDP and US are free for EJW readers (venue record); FTE is expanded at its first use; CRTC, IPTV, ACTRA, BYOP, CPE, BDU and PPV are expanded; VOD isn't (finding 8).
- The other watchlist flag, "projection", occurs only inside a quotation from the report.
- Builds clean (see the build-integrity record).
