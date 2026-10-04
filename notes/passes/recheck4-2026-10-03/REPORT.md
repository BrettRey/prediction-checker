<!-- Saved verbatim by the parent session from codex-stdout.txt (Codex gpt-6-astra, xhigh, read-only), 2026-10-03. -->

**Verdict: the numerical results and closures reclassification pass. The manuscript needs several wording and documentation corrections, but none changes the reported estimates or verdicts.**

Model: GPT-6, running as Codex; the supplied audit manifest identifies this run as `gpt-6-astra`, xhigh. I checked commit `f29f3eb` read-only. No files were changed.

| Location and quoted phrase | Issue | Severity | Fix |
|---|---|---|---|
| §4.2, [case-lttv.tex:71](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/case-lttv.tex:71): “This one … gives no fieldwork dates, sample size or margin of error” | The inspected source is MTM’s **press release**, which announces a separate report. The release omits those details; that does not establish that the survey report omits them. This unnecessarily weakens evidence favourable to the forecasters. | Moderate: source scope/fairness | “The available press release gives no fieldwork dates, sample size or margin of error.” |
| Introduction, [intro.tex:14](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/intro.tex:14): “at the scales the plan set”; “at those scales” | The plan sets both designated scales and a sensitivity range of 1–8%. The findings stated here hold at the designated scales, not throughout that range. The abstract and §4 are clearer. | Minor: qualification ambiguity | Use “at the plan’s designated error scale for each series,” and “at those designated scales.” |
| §2.1, [case-lttv.tex:28](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/case-lttv.tex:28), repeated in [discussion.tex:15](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/discussion.tex:15): “‘4% of Canadians’ doesn’t specify a denominator” | It names Canadians as the denominator. What it fails to establish is whether Morrison meant all Canadians, households, or existing television subscribers—the population needed for comparison with BYOP uptake. | Minor: precision/fairness | “He didn’t specify whether this meant 4% of existing television subscribers.” |
| §4.3, [case-lttv.tex:77](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/case-lttv.tex:77): “the 95% interval for \(\hat k\)” | The confidence interval is for \(k\), constructed around \(\hat k\). The equations and calculations use the correct quantity. | Minor: statistical notation | Replace with “the 95% interval for \(k\).” |
| Data and code, [discussion.tex:27](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/discussion.tex:27): “a script that downloads every public source used” | [fetch_raw.sh](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/scripts/fetch_raw.sh) does not download the ownership charts, CRTC 2016-110, or the MTM release, among other cited sources. Numerical reproduction works because the relevant classifications and assumptions are already encoded. The source-download claim is broader than the script. | Moderate: reproducibility description | Narrow the claim to the raw inputs downloaded by the script, or add retrieval of the sources supporting the manually encoded inputs. |
| Supporting replication note, [results-lttv-inputs.md:30](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/notes/results-lttv-inputs.md:30): “the bounds sit around the report’s 10%”; the plan’s rule “couldn’t be applied directly”; “two versions shown” | These statements survived the reclassification, although the table now contains all three versions and the plan’s result is below 10%. The note also says company disclosures have not been searched, contradicted by `DECISIONS.md:122`. Its legacy 8–10% range rounds an already rounded bound; the exact upper bound rounds to 11%. | Minor: stale documentation | Correct the text and percentage calculation in [input_checks_lttv.py:103](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/scripts/input_checks_lttv.py:103), then regenerate the note. The manuscript’s percentages are already correct. |

**Numbers and inference checked clean.**

I regenerated all **284 macros**, `tables-lttv.tex`, and `table-scenarios-main.tex` in memory. All matched the committed files exactly. I also reran the outcome, closures, payment/input-check, CPE, and model-check scripts with their writes intercepted in memory; their generated outputs matched.

An independent calculation using changes in the log gaps reproduced:

| Quantity | \(\hat k\) | Standard error | 95% interval | Cited-input band | Designated verdict |
|---|---:|---:|---:|---:|---|
| Specialty/pay revenue | 0.11754 | 0.17644 | −0.22828 to 0.46337 | 0.75–2.54 | Smaller |
| Distributors’ revenue | 1.30307 | 0.41294 | 0.49370 to 2.11243 | 0.80–2.24 | Consistent |

The following descriptions are correct:

- \(k\) scales the report’s **log shortfall**, rather than measuring a causal policy effect.
- The band’s scenario values are what \(\hat k\) would equal if revenue followed those paths exactly. They are projections, not probability bounds.
- The ordered verdict rule in §3 and table B4 matches `crtc_outcomes_lttv.py`.
- “Compatible” is explicitly a comparison of the scenario coefficient with the interval. It does not establish the uptake path’s truth.
- All seven scenario coefficients reproduce. At the designated scales, only the tested path rising from 1.6% to 4% keeps both coefficients inside their intervals.
- The counted-uptake distributor gap is **2.102 SEs**; the survey-path specialty/pay gap is **3.665 SEs**, correctly reported as 2.1 and 3.7.
- The proportional-impact assumption and its difference from the dollar-impact simulation are accurately disclosed. Reproduced coverage is **86.83% and 92.56%** under dollar impacts, versus **95.04% and 95.02%** under proportional impacts. The manuscript’s 87%, 93%, and 95% are correct.
- The illustrative \(t_3\) distributor interval is approximately **−0.01 to 2.62**, as stated.

The abstract’s sentence **“Under the largest error scales some calibrations give, both verdicts become inconclusive” is exactly supported**:

| Calibration | Specialty/pay | Distributors |
|---|---|---|
| 2016 level, approximately 4.4% | Inconclusive | Inconclusive |
| Pooled 2016–2018, approximately 4.7% | Inconclusive | Inconclusive |
| Growth 2015–2018, approximately 4.2% | Inconclusive | Inconclusive |
| Pooled growth, approximately 4.0% | Smaller | Inconclusive |

“Inconclusive” here does **not** mean that the specialty/pay interval includes \(k=1\): the plan’s rule requires it to contain zero and the band’s lower endpoint. The manuscript correctly distinguishes this from inclusion of \(k=1\) at the 8% sensitivity scale.

Every numerical claim in the abstract, introduction, and discussion checked against its intended quantity. This includes 15,130 economy-wide FTEs; 1.6% entry-level uptake versus the report’s 5% BYOP assumption; the cited 10–35% uptake range; 12.6% rather than 18%; payment growth of 10.5% versus 1.6%; and the 2015/2014 revenue discrepancies of 2.5%/0.8%. The introduction’s 12-of-25 and 6-of-25 figures match Harrington et al.’s abstract.

**The closures reclassification is correct and fairly presented.**

All 19 marked rows match service entries in the specified charts:

| Chart | Matched operating services |
|---|---|
| **32h — six** | BC News 1; Crime + Investigation; Deja View; DTOUR; H2; MovieTime |
| **32i — thirteen** | Action; BBC Canada; DIY Network; Food Network Canada; fyi; HGTV Canada; History Television; Lifetime; NatGeo Wild; National Geographic Channel; Showcase; Slice; The Independent Film Channel Canada |

The CSV’s spelling variants and former names resolve correctly. No additional denominator service appears in these charts as a Shaw Media service. Reality TV and Fox Sports World Canada are marked no longer operating; Quest is marked not yet operating. None appears in the 2015-revenue denominator.

Shaw’s fiscal-2015 filing independently states that Shaw Media operated **19 specialty channels**. CRTC 2016-110 is dated **23 March 2016** and approves the transfer. Thus “the 19 specialty channels Shaw Media operated before its transfer to Corus, approved in March 2016” is supported.

Recomputed bounds, before rounding:

| Classification | Group | Denominator | Closed | Absent | Closure bounds |
|---|---|---:|---:|---:|---:|
| Plan: 2015 owner | Integrated | 57 | 3 | 1 | 5.26–7.02% |
| Plan: 2015 owner | Independent | 108 | 8 | 34 | 7.41–38.89% |
| Corus counted as integrated | Integrated | 80 | 5 | 4 | 6.25–11.25% |
| Corus counted as integrated | Independent | 85 | 6 | 31 | 7.06–43.53% |
| Legacy 2016-owner field, Corus excluded | Integrated | 38 | 3 | 1 | 7.89–10.53% |
| Legacy 2016-owner field, Corus excluded | Independent | 127 | 8 | 34 | 6.30–33.07% |

All 19 reassigned Shaw services are operating in the crosswalk’s endpoint classification; their reassignment increases the integrated denominator without increasing its closure numerator.

The interpretation is faithful to the three governing documents:

- **Plan, line 69:** explicitly makes Shaw Media integrated under 2015 ownership and requires an additional result counting Corus as integrated.
- **Report, n. 31:** explicitly lists Shaw/Corus together, quoting the CRTC.
- **CRTC 2016-110:** explicitly states their common effective control, while acknowledging separate management and boards.

Leading with the plan’s result and immediately reporting the result under the report’s grouping is fair. The manuscript does not conceal that the conclusion about integrated closures changes with classification. The contradictory wording is confined to the stale replication note identified above.

**The new factual explanations are supported, with the press-release qualification noted above.**

- **Four components:** unbundling, preponderance/access, exemption order, and closures match the report’s figures and discussion.
- **Preponderance:** the received-versus-offered distinction and the modelled Canadian wholesale-fee share declining from 86% to 50% among BYOP subscribers match paras. 210–213.
- **Uptake dependence:** scaling unbundling and preponderance while describing the other components as separately specified but partly dependent on them accurately reflects paras. 220 and 234. Calling the recalculations *partial* is necessary and correctly retained.
- **Pass-through:** paras. 206–207 support 86% of retail losses attributed to Canadian services, then 75% of that amount passed through.
- **Payments:** para. 180 and Table 14 support the report-side definition. Raw CMR U-T11 identifies affiliation payments reported by BDUs and distinguishes Canadian affiliates. The manuscript correctly warns that the resulting series and the report’s fee measure differ.
- **Wholesale code:** n. 80 supports the quoted description and its retention in the modelling; n. 82 gives the scheduled January 2016 commencement. The manuscript’s “scheduled” wording is appropriate.
- **Band construction:** para. 201 supplies Corus’s 10–20% and Oliver Wyman’s “as many as 35%”; para. 230 supplies Bell’s approximately 25% and Oliver Wyman’s 26% closure estimates. The **2.5 multiplier is the analysis’s approximation**, motivated by approximately 25% versus the report’s 10%, not a multiplier literally supplied by those sources. The text describes the band as constructed rather than probabilistic.
- **Companies and terminology:** the English-language integrated-company list matches n. 31. “Category A and B specialty channels” is supported. The licensing-exemption distinction is valid; exempt operation need not mean closure. The historical CRTC record explicitly distinguishes operating exempt services from licensing them. [CRTC 2018-29](https://crtc.gc.ca/eng/archive/2018/2018-29.htm)
- **ACTRA and table B1:** ACTRA’s expansion is correct; the CBC/SRC, CMF, PPV, and VOD note contains no factual error. [ACTRA](https://www.actra.ca/)
- **CPE:** observed 2016–2019 spending spans **$3,203.6–$3,427.1 million**; the corresponding baseline spans **$3,121–$3,140 million**. The rounded ranges and “above” comparison in §5.2 are correct.

**Quotation checking found no misquotation.**

I checked all 42 `\enquote{}` occurrences, including repeated quotations and the author’s own labels. Source quotations match after normalizing typography and PDF line breaks; the staff labels match the original spreadsheets.

In particular:

| Quotation | Verified locator |
|---|---|
| “materially increase cord cutting and cord shaving” | Report para. xxiii, printed p. 6 |
| “governs the commercial relationship between BDUs and programmers” | Report n. 80, printed p. 72 |
| “just over 1 in 10” and its longer version | MTM release, 17 August 2017, first highlight |
| “as many as 35% … skinny-basic/BYOP option” | Report para. 201, p. 75 |
| “relatively unattractive … very few Canadians opt for it” | Report para. 78, n. 40, p. 34 |
| “there is no easy way to assign probabilities …” | Report para. 111, p. 43 |
| Morrison’s jobs, spending, and mitigation quotations | Committee evidence, 0900–0905 |
| Morrison’s approximately 4% quotation | Committee evidence, 0920–0925 |
| “If it is right, that’s good news” | Committee evidence, 0915–0920 |

The Harrington, Morgenstern, Manski, regulatory-policy, hearing, and remaining report quotations also checked clean.

**Negative and absence claims were checked as follows.** Repetitions are grouped; this inventory includes the source-facing claims and the substantive methodological negatives.

| Claim and location | Finding |
|---|---|
| Conclusions are “not necessarily” those of the commissioning groups — §1 | Exact support in the report’s preamble. |
| Recorded searches “found no published comparison” — §1 | Supported by the dated queries in `notes/novelty-search.md`. Appropriately reports search results rather than universal absence. |
| Overestimates “need not show bias”; nothing here establishes general stakeholder bias — §§1, 6.1 | Supported by Simpson and the single-case scope. |
| Price “no more than $25,” excluding equipment — §2 | Supported by CRTC 2015-96, para. 26. |
| The report’s 18% concerns projected baseline spending, not current spending — §2.1 | Supported by para. 239 and the committee wording. |
| The report’s figures “don’t reproduce” 18%; “none” of the tested shares gives it — §§1, 2.1, 6 | Correct for the explicitly identified 12 calculations over nine denominators. |
| Morrison omitted the uptake assumption and did not connect his 4% estimate to the jobs figure — abstract, §§1, 2.1, 6 | Supported by reading all Morrison/Miller interventions in the supplied committee evidence. |
| Morrison “didn’t specify” a denominator — §§2.1, 6 | Needs the narrower wording in the problems table. |
| “I found no later CRTC count” / “no official count … after 2016” — §§4.2, 6 | A recorded search supports this for the study’s 2017–2019 period. The detailed record is in **`DECISIONS.md:122`**, not the novelty log. It does not establish universal absence through 2026. |
| Surveys are not accepted uptake sources under the plan — §4.2 | Directly checkable and correct. |
| The survey gives no fieldwork dates, sample size, or margin of error — §4.2 | Only established for the press release; correction required. |
| Entry-level counts/survey adoption may not measure BYOP uptake — §§4.2, 6.1 | Properly qualified and supported by the differing definitions. |
| Outcome series alone cannot identify baseline error or a causal effect — §3 | Correct identification limitation of the stated model. |
| The band “isn’t a probability interval” — §3 | Correct by construction. |
| The decomposition does not observe prices or identify causes; part remains “unexplained” — §4.4 | Correct when “unexplained” means the residual against the specified partial recalculation. |
| Estimates do not move with \(\sigma\); no reported specialty/pay interval excludes zero — §4.5 | Verified computationally. |
| Distributors show no corresponding residual pattern or new 2015 divergence — §4.6 | Supported by the reported residuals and 2012–2015 discrepancies; the text appropriately avoids identifying a cause. |
| 2015 has no forecast impact; earlier specialty/pay discrepancies are negligible — §4.6 | Verified against forecast and outcome files. |
| Revisions between the two CRTC editions cannot explain the gap — §4.6 | Supported for the specific editions and comparison examined. |
| Payment measures differ; aggregates cannot identify counterfactual fees, causes, or pass-through — §§5.1, 6.1 | Supported by the definitions and missing counterfactual. |
| The wholesale code cannot explain the scenario difference unless its effect exceeds the assumption — §5.1 | Supported by its inclusion in both modelled scenarios. |
| The summaries cannot distinguish absent independent services that closed from those operating under exemption — §§5.2, 6.1 | Correct limitation of these files; the bounds preserve the ambiguity. |
| The report does not publish the employment baseline path — §5.3 | Supported: its employment tables provide impacts, not the required baseline levels. |
| The chain does not imply the observed staff/revenue mismatch; that mismatch cannot test employment — §§5.3, 6 | Fairly qualified by the unlike measures and unlike benchmarks. |
| Staff counts are not the report’s modelled FTE estimates — §5.3, table B6 | Correct; both spreadsheet labels and the vintage discrepancy were verified. |
| “No easy way” to assign probabilities — §6 | Accurate quotation of para. 111, not an independently asserted literature-wide impossibility. |
| Jobs totals, causal effects, production/spin-off employment, and the third scenario are not tested — throughout | Accurate statements of the analysis’s scope. |
| Intervals omit measurement uncertainty and uncertainty in \(\sigma\) — §§3, 6.1, appendix A | Correct description of the implemented intervals. |
| A headline alone would leave the intermediate predictions unavailable — §6 | Narrow, conditional claim consistent with the information the calculation requires. |
| The initial ChatGPT lead list supplied no reported calculations — Data and code | Consistent with the recorded provenance; distinct from the later models’ documented analysis work. |

The account is generally fair to Nordicity/Miller and Morrison. It credits the report’s transparency, uncertainty statement, anticipation of low uptake, and later self-correction; retains the survey evidence favourable to the forecast; acknowledges Morrison’s mitigation proposals and reassuring qualification; and avoids treating rounded spending or “direct result” as separate errors.

The abstract, §§4–5, and discussion now agree on the substantive findings. The introduction needs the more explicit **designated-scale** qualifier identified above. There is no numerical basis for reversing either principal revenue verdict, rejecting the 19-service mapping, or restoring the old unqualified statement that integrated closures came out close to the report.
