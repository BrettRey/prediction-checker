# Novelty search log
<!-- SUMMARY: Evidenced searches behind any "nobody has checked this forecast" claim; inward check done, outward not started · status: open · updated: 2026-10-03 -->

A claim that a forecast has never been publicly checked is a negative over a search space. It may appear in the manuscript only in one of two forms: the narrow claim ("source S doesn't do X", with S read), or the evidenced negative (the claim plus the exact queries below). Log every search here, including the ones that find nothing.

| Date | Where | Exact query | Scope | Result |
|---|---|---|---|---|
| 2026-10-03 | qmd `query`, `literature` collection, one call with four sub-queries: BM25 `genetic non-discrimination insurance`; BM25 `CRTC television Nordicity`; BM25 `preliminary inquiry Bill C-75`; vector `retrospective evaluation of forecasts made in legislative or regulatory debates` | as listed | Brett's portfolio literature folder (1,646 docs; 265 not yet embedded, so the vector leg is incomplete) | No hit on any of the three cases. Top results were off-topic (an ML fairness survey, Quirk et al., an AI-Act impact-assessment preprint). Goodman's *Fact, Fiction, and Forecast* appeared at low score: method-relevant on conditionals, not a prior check |
| 2026-10-03 | `grep -rIli` over `literature/*.md` (1,574 files) | `Nordicity`, `Genetic Non-Discrimination`, `preliminary inquir`, `Let's Talk TV`, `Bill S-201` | same folder, full text | Three files, all false positives: Mill's *System of Logic* (twice, "preliminary inquiry" in the ordinary sense) and Kaplow 1992 (citing Davis, *Discretionary Justice: A Preliminary Inquiry*) |
| 2026-10-03 | Full text of T14 (Nordicity 2022, CRTC) and T15 (Miller 2022, CRTC), Wayback copies | `grep -iE "Let.s Talk|LTTV|2015|Canadian Television 2020|unbundl|skinny|pick-and-pay|forecast|projection|predict|15,130|retrospect"` | the forecaster's own later CRTC work | Neither compares the 2015 forecast with outcomes. T15 lists the 2015 report (dated January 2016) in the author's publications and, in footnote 196, acknowledges "the mistake of predicting station closures" (bears on T17, the local-TV study, not the 2020 report's revenue and job figures) |
| 2026-10-03 | OpenAlex API (titles, abstracts, full text where indexed) | full-text `pick-and-pay television unbundling Canada`; `Let's Talk TV CRTC`; `a la carte cable television unbundling welfare`; `title.search:pick-and-pay`; `title.search:skinny basic`; `title.search:unbundling television`; `title.search:canadian broadcasting regulation` | scholarly literature, all years | No evaluation of *Let's Talk TV* outcomes or of the Nordicity/Miller forecast. Related: Crawford and Yurukoglu 2012 (*AER*, welfare of bundling, US); Davis and Zboralska 2017 (Netflix in Canada); Salter and Odartey-Wellington 2008. Details in `lit-search-2026-10-03.md` |
| 2026-10-03 | Web search (extended mode) | `"Canadian Television 2020" Nordicity forecast jobs "15,130" outcome OR revisited OR wrong` | open web | Copies of the report (friends.ca, Le Devoir, SlideShare) and Nordicity's site; no retrospective |
| 2026-10-03 | Web search | `Let's Talk TV pick-and-pay results evaluation specialty channel revenue impact study after 2016 academic` | open web | Trade press from 2014–2016 on expected impacts; no retrospective |

The intake brief's own "didn't locate" statements (four of them) report no queries, so they are not entered here.

## Still to search

- Outward literature and grey literature for each case: actuarial journals and CIA publications since 2017; CRTC proceedings and broadcasting-policy literature since 2016; criminal-justice evaluation reports since 2019. Planned route: `/hyperresearch`, light tier, capped budget.
- Hansard and committee evidence after each intervention, for any parliamentary return to the original forecast.
- Citing works of each forecast document (Google Scholar "cited by"; Crossref where a DOI exists).

## Leads seen but not read (HELD)

Seen on 2026-10-03 as web-search result titles while locating the CIA 2014 model paper (queries were for that document, not novelty searches, so they aren't logged above). None opened; all wait until the case 1 record is committed and the held rows are released.

- Society of Actuaries, "2018 impact genetic testing report" (soa.org research report).
- Haçarız, "Will genetic test results be monetized in life insurance?", *Risk Management and Insurance Review*, 2020.
- An item in *Scandinavian Actuarial Journal* 2022, issue 2, pp. 94–114 (IDEAS/RePEc listing; title not shown).
- "An actuarial model of arrhythmogenic right ventricular cardiomyopathy and life insurance" (Heriot-Watt research portal).
- Trade-press headlines reporting the Supreme Court outcome on the Act were visible in result lists; not read, and the outcome isn't recorded anywhere in this project until G07 is verified.
- A search engine's generated summary attributed a "12%" premium increase to Howard 2014. The paper's 12% is the valuation strain as a share of annual death claims (§5), not a premium increase; the summary is not a source.

## Negative claim about the report's content: no offset for redirected consumer spending (2026-10-04)

Claim in §2: the report links its job and GDP estimates to reductions in broadcasting revenue and production financing (para. 245), and it sets no offset for spending that subscribers who pay less redirect elsewhere. (First drafted as "these are gross figures"; the label was dropped on 2026-10-04 after recheck 5, because the report itself calls its GDP figure a "net loss" (para. 93), in the sense of a loss against its baseline.)

Search, run 2026-10-04 on `literature/nordicity_miller_2015_canadian_television_2020.md` (full text of the report): case-insensitive grep for `saving`, `save `, `consumer surplus`, `spent elsewhere`, `spend (it|the|their)`, `redirect`, `displace`, `substitut`, `net (economic|impact|effect)`, `gross`, `leakage`, `disposable`, `household spending`, `consumer spending`, `money (saved|not spent)`, `other (goods|sectors|spending)`, `upside`, `lower (bills|prices)`, `pay less`, `consumer benefit`. No passage was found that models re-spending of subscribers' savings. Hits were unrelated (simultaneous substitution; BDUs' gross revenue; "revenue leakage" from rights protection; the CRTC's "potential upsides of greater choice", quoted in n. 41) or concerned exports (para. 110: "jobs could return if foreign customers were substituted for Canadian customers"). Para. 245 defines the economic-impact estimates as "linked to 'deltas' or reductions in revenue experienced by BDUs and programming services, and any reductions in financing for Canadian film and TV production"; Table 1's note defines spin-off as "indirect and induced impacts". The claim is limited to this report's text.

Recheck 5 (Codex, 2026-10-04, `notes/passes/recheck5-2026-10-04/REPORT.md`) repeated the search with further terms and found no quantified adjustment for subscribers spending their television savings elsewhere. It also found hits the first search had worded around, each checked against the report: n. 22 defines induced impact, for Nordicity's 2013 economic-contribution study, as "the re-spending of labour income earned at both the direct and indirect stages" (induced spending, not redirected subscriber savings); para. 227 expects integrated companies' losses to be partly "offset by revenue gains experienced by their OTT services" and broadband (already reported in §5.1); para. 93 calls the GDP figure a "net loss of $328.4 million" for the unbundling-revisited scenario "(as opposed to the LTTV projected net loss of $1.4 billion)", which does not show that redirected household spending was netted out. The narrowed claim stands.
