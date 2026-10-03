# Data
<!-- SUMMARY: Data layout and licence register; forecast values extracted from the Nordicity report, no outcome data yet · status: forecast-side only · updated: 2026-10-03 -->

- `raw/`: downloaded source data, **gitignored**. Never edited by hand.
- `derived/`: outputs of `../scripts/`, committed when the source licence allows.

## Licence register

Record every source at download: what it is, where from, date retrieved, licence or terms, and whether derived files may be published.

| Source | Retrieved | Licence / terms | Derived files publishable? |
|---|---|---|---|
| Nordicity and Miller, *Canadian Television 2020* (December 2015), PDF from friends.ca; values read from its bar-chart labels by `scripts/extract_nordicity_figures.py` → `derived/nordicity_2015_figure_labels.csv`, `derived/nordicity_2015_scenarios.csv` | 2026-10-03 | No licence or copyright statement in the PDF | Yes, as a cited record of the published forecast (figures, not text) |

Standing restrictions: COMPULIFE historical quotation data is a commercial product and is never committed, nor is anything that reconstructs its quotes. Check the Canadian Institute of Actuaries' terms before publishing anything derived from its experience database.
