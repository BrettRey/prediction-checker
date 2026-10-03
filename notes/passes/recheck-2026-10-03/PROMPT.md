# Targeted recheck: prediction-checker, after the numbers and inference audits

You are a second model checking work added after two audits of this paper (`notes/passes/2026-10-03-numbers-audit.md`, `notes/passes/2026-10-03-statistical-inference-audit.md`). Another model (Claude) wrote the new analysis and prose. Read-only; full report in your final message; state which model you are.

Rendered manuscript: `notes/passes/recheck-2026-10-03/main.txt` (commit a8d2717). Sources and scripts as before; the report's text is `/Users/brettreynolds/projects/LLM-CLI-projects/literature/nordicity_miller_2015_canadian_television_2020.md` (PDF beside it).

## Check these, and only these

1. **The distributor decomposition (new).** Rule: `notes/analysis-plan.md`, section "Post hoc addition: distributors' revenue by subscribers and revenue per subscriber" (committed in 4a722a0 before computing). Code: `scripts/decompose_bdu_lttv.py`; extractor additions for Figs. 17 and 19 in `scripts/extract_nordicity_figures.py`; outputs `data/derived/bdu_decomposition_lttv.csv`, `data/derived/nordicity_2015_bdu_subscribers_arpu.csv`, table A5. Verify: (a) Figs. 17 and 19 values against the report PDF; (b) the reading of the report's scenario mechanics (paras. 202–205, 215–221, 236; Tables 5, 6, 20, 21) and the reconstruction of its BDU exemption-order component; (c) the identity and the change-from-2014 alignment; (d) the counted-uptake per-subscriber part; (e) whether the code follows the committed rule, and where it goes beyond it, whether the text says so; (f) the CRTC subscriber series (2016 and 2020 editions) and its comparability with the report's.
2. **Every sentence that reports or interprets the decomposition**: abstract, introduction (the distributor paragraph), results (the paragraphs beginning "Splitting the revenue can", "By 2019, measured this way", "The split was added"), discussion (the paragraph beginning "Read as a conditional projection", and the "Five findings" list). For each: does the number match its source, and does the wording claim more than the split shows (direction, base, "mostly", "beyond", causal language)?
3. **The audit follow-ups**: coverage under a dollar-impact world (`scripts/model_check_lttv.py`, `data/derived/model_check_lttv.csv`), the t(3) illustration, the plan's 8% intervals (figure 2, `scripts/figures_lttv.py`), the distributors' counted-uptake gap in SEs under the sensitivities, the corrected residual check, and the sentences that report them (method paragraph on the interval; results paragraphs on figure 2 and the model check; limits; appendix design-analysis paragraph).
4. **New macros**: every macro in `sections/numbers-lttv.tex` whose name begins `lttvDec`, `lttvRevPerSub`, `lttvSubs`, `lttvCover`, `lttvSEInflate`, `lttvBDUGap`, `lttvK*TThree*`, `lttvK*Eight`, `lttvInnov`, `lttvTThreeWiden`, `lttvKSpecSEsFromOneDollars`: recompute each from the data.
5. **Table A8 (chronology)**: do the commits named for the new rows contain what the rows say, in that order?

## Report (final message)

1. Verdict paragraph.
2. Problems table: location and quoted phrase, printed value, what the source or recomputation gives, severity (error / overstated / wording / ok-with-note), suggested fix.
3. Your recomputations, with values.
4. Anything in the decomposition you'd want a referee to see that the paper doesn't say.
