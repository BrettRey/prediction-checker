# prediction-checker

When experts tell Canadian legislators, regulators or courts what a decision will cause, and the decision goes ahead, does anyone later check? This project takes forecasts used in consequential debates, reconstructs exactly what was predicted and under what conditions, and tests them against what happened.

## The paper

*Checking a forecast put to Parliament: unbundling Canadian television, 2016–2019* (draft, `tv-unbundling-forecast-check.tex`). In April 2016 a House of Commons committee heard that the CRTC's *Let's Talk TV* rules would cost 15,130 media jobs by 2020. The figure came from Nordicity and Peter Miller's report *Canadian Television 2020* (December 2015). The paper compares the report's revenue predictions with CRTC data for 2016–2019, adds descriptive checks of uptake, payments to Canadian channels, closures and staff counts, and compares the report with what the committee was told. It doesn't test the job total or the decisions' causal effect.

The forecast record and the analysis plan were committed before any CRTC outcome file was downloaded:

- prediction record: `cases/lets-talk-tv/README.md`
- analysis plan: `notes/analysis-plan.md`
- every choice made after the outcome data was opened: `DECISIONS.md`, and table B8 of the paper, which gives the commit for each step

Each technical claim is kept apart from the public predictive argument: what a model implies under its stated conditions, and what decision-makers were told would probably happen.

## Reproducing the numbers

Requirements: Python 3 with `numpy`, `matplotlib` and `openpyxl`; `curl`, `pandoc` and `pdftotext` (poppler).

```bash
# 1. Download the public sources into data/raw/ (gitignored).
#    SEC EDGAR asks for a contact in the User-Agent.
SEC_UA="Your Name you@example.com" bash scripts/fetch_raw.sh

# 2. Run the analysis, in this order.
for s in extract_nordicity_figures cpi_canada netflix_calibration design_analysis_lttv \
         crtc_outcomes_lttv sigma_integrated_lttv closures_lttv cpe_lttv employment_lttv input_checks_lttv \
         decompose_bdu_lttv model_check_lttv figures_lttv make_tex_numbers make_tex_tables; do
  python3 scripts/$s.py
done
```

Outputs go to `data/derived/` (CSV), `figures/`, and the generated LaTeX in `sections/numbers-lttv.tex` (every number the analysis produces is a macro defined there), `sections/tables-lttv.tex` and `sections/table-scenarios-main.tex`. The table script recomputes each estimate from the displayed inputs and stops if any differs from the analysis output.

Checked on 2026-10-04: from a fresh clone and a fresh download, these steps reproduce every committed file in `data/derived/` and the generated LaTeX exactly, and the figures' PNG files byte for byte. The PDF figures differ only in embedded timestamps.

Some inputs are encoded from documents rather than downloaded. One example is the 2015 owner of each channel, taken from the CRTC's ownership charts. The scripts record these inputs with their sources, and the sources are in the paper's reference list.

## Building the manuscript

`tv-unbundling-forecast-check.tex` uses the *Econ Journal Watch* LaTeX class and builds with pdfLaTeX and biber (`make`). The class isn't redistributed here: download the template from <https://econjwatch.org/file_download/1417/EJW_latex_files_8.29.26.zip> and copy `ejw.cls`, `ejw-pdflatex.cls`, `ejw-logo.pdf` and `ejw-journaltalk-logo.png` into `ejw/`, which the Makefile puts on the TeX search path. `references.bib` is a symlink to a bibliography outside this repository, so a standalone clone can reproduce every number, table and figure but can't build the PDF without it. `scripts/plot_style.py` is a copy of the house plotting style, so the figures do build standalone.

## Layout

```
tv-unbundling-forecast-check.tex, sections/  the paper; sections/numbers-lttv.tex and the tables are generated
scripts/                     data download (fetch_raw.sh) and analysis
data/raw/                    downloaded sources (gitignored); data/derived/: analysis outputs
data/README.md               licence register for every source
figures/                     generated figures
cases/                       one folder per case: prediction record, design notes, outcomes
notes/analysis-plan.md       pre-stated plan and reading rules
notes/source-verification.md every claim from the original lead list, with its verification status
notes/novelty-search.md      the searches behind the paper's "no published comparison" statement
notes/passes/                second-model audits of the draft (numbers, inference, quotations, fairness, clarity)
notes/rereads/               source rereads
DECISIONS.md, STATUS.md      decision log and current state
```

## Other cases

`cases/gnda-life-insurance/` (actuarial forecasts of premium increases under the *Genetic Non-Discrimination Act*) and `cases/c75-preliminary-inquiries/` (forecasts about delay from restricting preliminary inquiries under Bill C-75) are candidate cases for separate papers. Their descriptions began as an unverified lead list; `notes/source-verification.md` records what has and hasn't been checked against the sources.

## Licence

Text, notes and data products: [CC BY 4.0](LICENSE), unless a source's own terms say otherwise (see `data/README.md`).
