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
