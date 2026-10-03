# Data
<!-- SUMMARY: Data layout and licence register; forecast values extracted from the Nordicity report; CRTC outcome series for case 2 · status: case 2 outcomes in progress · updated: 2026-10-03 -->

- `raw/`: downloaded source data, **gitignored**. Never edited by hand.
- `derived/`: outputs of `../scripts/`, committed when the source licence allows.

## Licence register

Record every source at download: what it is, where from, date retrieved, licence or terms, and whether derived files may be published.

| Source | Retrieved | Licence / terms | Derived files publishable? |
|---|---|---|---|
| CRTC Statistical and Financial Summaries (2016 and 2020 vintages: discretionary and on-demand, distribution, individual discretionary) and CMR television data 2013–2024, via open.canada.ca → `raw/crtc/` | 2026-10-03 | Open Government Licence – Canada | Yes, with attribution (`derived/crtc_lttv_outcomes.csv`, `derived/crtc_lttv_k_estimates.csv`) |
| Netflix, Inc., Form 10-K for fiscal 2018, SEC EDGAR → `raw/netflix/form10k_q418.htm` (sha256 5874158b…) | 2026-10-03 | US public company filing; public record | Yes: three membership figures with citation (`derived/netflix_calibration.csv`) |
| Statistics Canada, Consumer Price Index, annual average, table 18-10-0005-01 (doi:10.25318/1810000501-eng), full-table CSV → `raw/statcan/18100005-eng.zip` (sha256 9b52900a…) | 2026-10-03 | Statistics Canada Open Licence | Yes, with attribution (`derived/cpi_canada_annual.csv`: all-items, Canada, 2010–2020) |
| Nordicity and Miller, *Canadian Television 2020* (December 2015), PDF from friends.ca; values read from its bar-chart labels by `scripts/extract_nordicity_figures.py` → `derived/nordicity_2015_figure_labels.csv`, `derived/nordicity_2015_scenarios.csv` | 2026-10-03 | No licence or copyright statement in the PDF | Yes, as a cited record of the published forecast (figures, not text) |

Standing restrictions: COMPULIFE historical quotation data is a commercial product and is never committed, nor is anything that reconstructs its quotes. Check the Canadian Institute of Actuaries' terms before publishing anything derived from its experience database.
