# Novelty search log
<!-- SUMMARY: Evidenced searches behind any "nobody has checked this forecast" claim; inward check done, outward not started · status: open · updated: 2026-10-03 -->

A claim that a forecast has never been publicly checked is a negative over a search space. It may appear in the manuscript only in one of two forms: the narrow claim ("source S doesn't do X", with S read), or the evidenced negative (the claim plus the exact queries below). Log every search here, including the ones that find nothing.

| Date | Where | Exact query | Scope | Result |
|---|---|---|---|---|
| 2026-10-03 | qmd `query`, `literature` collection, one call with four sub-queries: BM25 `genetic non-discrimination insurance`; BM25 `CRTC television Nordicity`; BM25 `preliminary inquiry Bill C-75`; vector `retrospective evaluation of forecasts made in legislative or regulatory debates` | as listed | Brett's portfolio literature folder (1,646 docs; 265 not yet embedded, so the vector leg is incomplete) | No hit on any of the three cases. Top results were off-topic (an ML fairness survey, Quirk et al., an AI-Act impact-assessment preprint). Goodman's *Fact, Fiction, and Forecast* appeared at low score: method-relevant on conditionals, not a prior check |
| 2026-10-03 | `grep -rIli` over `literature/*.md` (1,574 files) | `Nordicity`, `Genetic Non-Discrimination`, `preliminary inquir`, `Let's Talk TV`, `Bill S-201` | same folder, full text | Three files, all false positives: Mill's *System of Logic* (twice, "preliminary inquiry" in the ordinary sense) and Kaplow 1992 (citing Davis, *Discretionary Justice: A Preliminary Inquiry*) |

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
