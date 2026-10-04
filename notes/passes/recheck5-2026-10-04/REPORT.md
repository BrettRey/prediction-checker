<!-- Saved verbatim by the parent session from Codex stdout (codex-stdout.txt, gitignored), 2026-10-04. -->

**Verdict: the numerical results pass, but the new Crawford–Yurukoglu comparison needs substantive correction.** The source does not predict an increase in the aggregate payment measure examined here. There are also two smaller substantive overstatements, several wording issues, and an overbroad sentence in the search log. None changes the two designated-scale revenue verdicts.

Model: GPT-6, running as Codex; the supplied audit manifest identifies this run as **GPT-6 Astra, xhigh**. I checked `d4bda01` read-only. The manuscript-text and diff hashes match the manifest. No files were changed.

| Location and quoted phrase | Verified issue | Severity | Fix |
|---|---|---|---|
| §5.1, [case-lttv.tex:129](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/case-lttv.tex:129): “One model predicts the direction observed”; “the opposite of the report’s assumption”; “The rise here is consistent with that mechanism” | **Different quantities are being compared.** Crawford–Yurukoglu’s 103% concerns negotiated channel-level input fees, summed across channels. Their Table 9 explains that distributors pay the à-la-carte fee “only for those that choose to subscribe.” Their discussion explicitly says: **“Total-channel affiliate-fee revenue decreases by an estimated 3.7 percent”** (p. 678). The present paper measures payments to all Canadian affiliates divided by distributor subscribers. Higher individual-channel rates do not establish higher aggregate payments per distributor subscriber. The US counterfactual and Canadian time-series comparison also differ. The caveat about not identifying the mechanism does not repair this quantity mismatch. [Source](/Users/brettreynolds/projects/LLM-CLI-projects/literature/crawford_yurukoglu_2012_aer_welfare_effects_bundling.md:384) | **Major: interpretation** | Retain the correctly attributed 103% as a theoretical result about negotiated channel fees. Remove the claimed match to the Canadian payment direction and the unqualified “opposite” comparison. Explain that the simulation also reduces aggregate affiliate-fee revenue. |
| Introduction, [intro.tex:24](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/intro.tex:24): “independent studies of sports facilities have found no significant effect on local development” | The cited page says **“no statistically significant positive correlation”**, not no significant effect of either sign. The next page discusses studies finding adverse effects, including facilities that “actually reduce per capita income.” Printed p. 103 is the correct locator; the paraphrase loses the crucial positive-direction qualification. [Source](/Users/brettreynolds/projects/LLM-CLI-projects/literature/siegfried_zimbalist_2000_jep_sports_facilities_communities.md:77) | **Moderate: attribution** | “Independent studies reviewed by Siegfried and Zimbalist found no statistically significant positive association between sports-facility construction and economic development.” |
| §3, [case-lttv.tex:41](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/case-lttv.tex:41): “treating σ as uncertain widens the intervals enough that the distributors’ interval includes zero” | This now states generally what Appendix A establishes only hypothetically. The appendix says **“As an illustration … if the historical volatility were an estimate from four independent, normal annual changes”**, then uses \(t(3)\); it adds that **“even that doesn’t carry the uncertainty of the actual calibration rule.”** The earlier main text retained “in the illustration.” [Appendix](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/appendix.tex:19) | **Moderate: lost qualification** | Restore: “In the appendix’s illustration of uncertainty in σ, the distributors’ interval includes zero.” |
| §3, [case-lttv.tex:37](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/case-lttv.tex:37): “the forecast shortfall and the baseline’s error are proportions of the baseline” | They are **log ratios**, not literal proportions. The implemented expression is `delta, y = np.log(B) - np.log(B - I), np.log(B) - np.log(Y)`. Thus \(\delta=-\log(1-I/B)\), not \(I/B\). Likewise, \(e\) represents a multiplicative baseline error through an exponential. [Script](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/scripts/model_check_lttv.py:82) | **Minor: mathematical precision** | “In logs, so that the comparison measures relative differences rather than dollar amounts …” |
| §3, [case-lttv.tex:33](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/case-lttv.tex:33): “For both revenue series it separated the two worlds in most simulations; for CPE it didn’t” | The contrast incorrectly suggests that CPE failed to classify correctly in a majority. Appendix A correctly says it **“came out at 63%.”** Independent regeneration gives 63.595% and 63.000% in the two worlds. Its discrimination was insufficient for the planned use, rather than absent in most simulations. | **Minor: misleading compression** | “Discrimination was strong for the revenue series but weak for CPE, which was therefore set aside as descriptive.” |
| Discussion’s third bullet, [discussion.tex:29](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/discussion.tex:29): “Affiliation payments … per subscriber grew faster than the report’s baseline carriage fee” | The arithmetic is correct. As a freestanding bullet, however, it drops the discussion’s explicit description **“a growth comparison of two differently defined measures”** and §5.1’s explanation that the series differ in reporters, coverage and possibly subscriber base. This wording predates the bullet conversion, but the conversion makes the missing qualification more consequential. | **Minor: summary qualification** | Append “in a comparison of differently defined measures.” |
| [novelty-search.md:38](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/notes/novelty-search.md:38): “No passage discusses re-spending” | Too broad. Report n. 22 expressly discusses **“the re-spending of labour income earned at both the direct and indirect stages.”** This is induced spending, not subscribers’ redirected savings, so it does **not** defeat the manuscript’s narrower claim. It does defeat the log’s blanket sentence. [Report](/Users/brettreynolds/projects/LLM-CLI-projects/literature/nordicity_miller_2015_canadian_television_2020.md:409) | **Minor: search documentation** | State that no passage was found modelling re-spending **of subscribers’ savings**. Record the labour-income passage as a distinct, relevant hit. |

**The calculations and numerical wording checked clean.**

I regenerated all **296 macros**, `tables-lttv.tex`, and `table-scenarios-main.tex` in memory. Each matched the committed file exactly. The table generator’s numerical consistency checks passed.

An independent calculation using successive changes in the log gaps reproduced:

| Revenue series | \(\hat k\) | Standard error | 95% interval | Cited-input band | Designated verdict |
|---|---:|---:|---:|---:|---|
| Specialty and pay | 0.11754 | 0.17644 | −0.22828 to 0.46337 | 0.75–2.54 | Smaller |
| Distributors | 1.30307 | 0.41294 | 0.49370 to 2.11243 | 0.80–2.24 | Consistent |

The following numerical statements match their macros, underlying quantities and displayed precision:

- **Abstract:** “15,130 jobs”; “1.6%”; “5%.” The first is the report’s economy-wide FTE forecast, explicitly identified as untested.
- **Introduction bullets:** the cited **10–35%** range; **5%** for 2016 and **10%** for 2017; the observed **1.6%**; and **12.6%** rather than the report’s stated **18%**. The last calculation is \(399/3155=12.6466\%\), correctly rounded.
- **Discussion bullets:** the 2015 specialty/pay gap of **2.5%**, against **0.8%** in 2014. These are comparisons with the report’s figures, not estimated policy effects.
- **§3:** designated scales **2.2%** and **1.9%**, Netflix calibration **1.3%**, and coverage figures **87%** and **93%**.
- **Appendix A:** **20,000** design simulations and seed **20261003**; classification rates **99%, 86%, 63%**; CPE historical volatility **9.1%**; the **62%** interval-widening illustration and its endpoints; and **3.8** simulated standard deviations versus **5.0** standard errors.
- **Netflix:** the file records forecast **57.0 million** and observed **58.486 million**, correctly rendered as **58.5 million**. The stated formula gives approximately **1.3%** annually.
- **New closure counts:** **3–4 of 57**, against approximately **6**; **5–9 of 80**, against **8**; and **8–42 of 108**, against **27**. The description “slightly below … a difference of two or three channels” is supported.

I also regenerated the design-classification results: no discrepancies. Independently simulated dollar-impact coverage was **86.83%** and **92.557%**; proportional-impact coverage was approximately **95.04%** and **95.02%**. The manuscript rounds these appropriately.

**The requested literature checks passed except for the two attribution issues above.**

| Source and locator | File evidence and assessment |
|---|---|
| Harrington et al. **2000, p. 297** | The published abstract says **“14 of the 28 rules”** and **“for only 3 rules were the ex ante estimates too low.”** Its quotation is exactly **“driven both by difficulties in determining the baseline and by incomplete compliance.”** The switch from the inconsistent discussion-paper summary is correct. “Total direct costs” appropriately combines the abstract’s stated subject and total-cost result. [Source](/Users/brettreynolds/projects/LLM-CLI-projects/literature/harrington_morgenstern_nelson_2000_jpam_accuracy_regulatory_cost_estimates.md:9) |
| Crompton **2006, p. 67** | Supported. The opening summary identifies commissioned studies producing inflated numbers and lists **“including local residents,” “inclusion of time-switchers and casuals,”** and **“abuse of multipliers.”** Those support the sentence about multipliers and treating spending as new. The detailed examples occur later, but p. 67 summarizes them. The manuscript does not attribute deliberate misconduct to Nordicity/Miller. [Source](/Users/brettreynolds/projects/LLM-CLI-projects/literature/crompton_2006_jtr_economic_impact_studies_political_shenanigans.md:7) |
| Siegfried and Zimbalist **2000, p. 103** | Correct page, incorrect breadth of paraphrase: retain **positive** and preferably **association**, as above. |
| Crawford and Yurukoglu **2012, p. 644** | The source does say equilibrium input costs are **“103.0 percent higher than when distributors sell bundles.”** The US setting, mandatory unbundling and contract renegotiation are accurately described. The unsupported step is transferring this result to the paper’s aggregate Canadian payment measure. |
| Simpson **2014, p. 322** | Correct: **“An unbiased estimate of the mean … would … be greater than most observations”** for the specified skewed distribution. This supports “need not show bias.” [Source](/Users/brettreynolds/projects/LLM-CLI-projects/literature/simpson_2014_jbca_regulators_overestimate_costs.md:71) |
| Simpson **pp. 319–321** | Correct range. The review reports industry overestimation in **“four of five cases,”** discusses Hodges’s industry estimates, and reports that Anderson–Sherwood generally found predicted price increases above realized changes. The manuscript’s restrained summary is supported. [Source](/Users/brettreynolds/projects/LLM-CLI-projects/literature/simpson_2014_jbca_regulators_overestimate_costs.md:43) |
| Morgenstern **2018, p. 285** | Exact support for **“a slight tendency to overestimate both costs and benefits.”** “Suggested” preserves the source’s caution. The existing counterfactual quotations also check at p. 286. [Source](/Users/brettreynolds/projects/LLM-CLI-projects/literature/morgenstern_2018_jbca_retrospective_analysis_environmental_regulation.md) |
| Miller **2022, n. 88 and n. 196** | Correct. Note 88 discusses the decisions’ consequences while declining to **“opine here on whether that policy should be seen as a success or failure.”** Note 196 acknowledges **“the mistake of predicting station closures.”** Calling this a **separate** prediction avoids conflating the local-station forecast with the forecast tested here. [Source](/Users/brettreynolds/projects/LLM-CLI-projects/literature/miller_2022_crtc_canadian_program_rights_market.md:674) |

I confirmed printed page locators from the PDFs where the Markdown did not preserve pagination.

**The gross-figures sentence is substantially supported, with a distinction worth preserving.**

Paragraph 245 explicitly links the estimates to:

> “reductions in revenue experienced by BDUs and programming services, and any reductions in financing for Canadian film and TV production.”

Thus the citation supports the mechanism described. For exactness, change **“broadcasting and production revenue”** to **“broadcasting revenue and production financing.”** [Report, para. 245](/Users/brettreynolds/projects/LLM-CLI-projects/literature/nordicity_miller_2015_canadian_television_2020.md:1796)

I repeated the recorded search and supplemented it with searches for re-spending, offsets, net losses, displacement and related terms. I found **no quantified adjustment for subscribers spending their television savings elsewhere**. Relevant distinctions are:

- Note 22 discusses re-spending **labour income**, which generates induced impacts.
- Paragraph 227 recognizes that integrated companies’ losses could be **“offset by revenue gains experienced by their OTT services”** and broadband operations. The manuscript already acknowledges this in §5.1.
- Paragraph 93 calls the GDP figures a **“net loss.”** That wording does not establish that redirected household spending was included.
- Paragraph 110’s possible replacement of Canadian customers by foreign customers concerns exports.

The manuscript’s **“I found no offset”** survives these checks. The search log needs the narrowing identified above.

On fairness: the direct/indirect/induced framework produces sector-linked economic-impact estimates. The missing household-spending adjustment establishes a limit on reading those figures as an economy-wide net loss; it does **not**, by itself, demonstrate misuse of the method or an assumption that consumers simply save the difference. The present sentence can fairly identify that limitation. It should not be developed into an allegation of erroneous multiplier application without further evidence.

**The uptake comparison and the findings lists are otherwise consistent.**

The report’s Table 18 gives:

> “BYOP subscribers as a share of total subscribers | 0% | 5% | 10% | 15% | 15% | 15%”

The columns are 2015–2020. Paragraph 201 separately reports Oliver Wyman’s **“as many as 35%,”** Corus’s **“10–20%,”** and Rogers’s **“15%.”** The report’s additional 10% uptake assumption in its *unbundling revisited* scenario concerns the separate scenario the manuscript excludes. There is no confusion between that assumption and the 2017 value in Table 18. [Report](/Users/brettreynolds/projects/LLM-CLI-projects/literature/nordicity_miller_2015_canadian_television_2020.md:1456)

The CRTC hearing states:

> “As of June 30th, 2016, 177,000 Canadians had signed up for the affordable basic service.”

Dividing by the recorded 2016 subscriber total of **11,089,600** gives **1.596%**, correctly displayed as **1.6%**. The April release supports “more than 66,000.” These remain entry-level-package counts, rather than confirmed BYOP-with-add-ons counts. The manuscript explains that distinction and the mid-year timing. [CRTC evidence](/Users/brettreynolds/projects/LLM-CLI-projects/literature/crtc_2016-09-07_hearing_transcript_bdu_renewals.md:41)

The MTM release says **“just over 1 in 10 TV subscribers”** adopted the package and separately reports **29%** adding channels or bundles. The plan accepts CRTC counts and company disclosures, followed by **“otherwise untestable”**; it does not accept surveys. The manuscript consistently labels the survey as outside those sources.

For the introduction’s four bullets:

1. The pre-stated comparison is explicitly restricted to the **designated scale**, followed by the larger-scale inconclusive result.
2. The uptake bullet preserves the timing, distinct package descriptions and survey exception.
3. The partial recalculations are explicitly **post hoc**, limited to **paths tested**, and qualified by designated scales.
4. The testimony and 12.6% claims match §2.1.

For the discussion’s five bullets, all numerical statements are correct. The subscriber comparison retains **“if the two subscriber series stay comparable.”** The payments bullet should restore its different-measures qualification. Calling these findings independent of the **baseline-error model** is otherwise accurate; it does not claim they are independent of every measurement assumption.

The sensitivity additions are supported: at the largest calibrated scale, **4.7%**, both verdicts are inconclusive. All seven uptake-scenario coefficients reproduce; only the tested rise from **1.6% to 4%** places both inside their designated intervals.

**The appendix move retained the necessary material and pointers.**

The design rates, band construction and Netflix calibration figures all have explicit Appendix A pointers in §3. The inflation-invariance statement remains in Appendix A:

> “deflating both by the same price index leaves it unchanged.”

That is correct for the paired log-ratio comparison. The estimator, covariance, interval assumptions, scenario projection and calibration formulas remain available. All section, appendix and table references resolve; there are no duplicate labels. The losses are the two qualifications identified above, not missing calculations.

**The recheck-4 repairs were correctly applied.**

The current text now says **“its release gives no fieldwork dates”**, **“the 95% interval for \(k\)”**, and **“downloads the public data files the analysis reads.”** The uptake-population criticism now asks whether Morrison meant all Canadians, households or subscribers. The replication note now reports the corrected closure counts and acknowledges that company disclosures were searched.

The “good news” correction is accurate. Vandal said that **“funding for local production across Canada has increased in the last few years.”** Morrison subsequently referred to **“the advice of Canadian Heritage officials”** and said **“If it is right, that’s good news.”** The revision correctly locates the remark in the local-production discussion. It does not present it as a concession that the numerical forecast was wrong. [Committee evidence](/Users/brettreynolds/projects/LLM-CLI-projects/literature/canada_commons_chpc_2016-04-12_meeting8_evidence.md:241)

**The new or narrowed negative claims have the following evidential status.**

| Claim added or materially reworded | Assessment |
|---|---|
| §2: “I found no offset” for redirected subscriber spending | Narrow report-content claim, supported by the recorded search and my independent search. |
| Introduction: “no significant effect on local development” | Unsupported at that breadth; correct to no significant **positive association**. |
| Introduction: “This paper doesn’t test the report’s multipliers” | Narrow, directly checkable description of scope; correct. |
| §2.1 and discussion: Morrison did not identify which population his 4% referred to | Supported by reading his and Miller’s interventions. The actual phrase is “about 4% of Canadians”; no clarification supplies the needed subscriber denominator. |
| §3: CPE did not separate the worlds “in most simulations” | Incorrect compression of the 63% result; fix as above. |
| §4.2: the release gives no fieldwork dates, sample size or margin of error | Correct for the inspected release. The repair appropriately avoids claiming this about the separate survey report. |
| §5.1: “the aggregates can’t show [the mechanism] operated” | Correct identification limitation. It does not validate the preceding claim that the model predicts the observed direction. |
| Search log: “No passage discusses re-spending” | Overbroad; distinguish labour-income re-spending from subscriber savings. |

Other negative formulations in the added lines are retained or reformatted claims: **“neither”** employment nor causal effects tested; surveys **“outside”** the plan; **“only”** one tested compatible path; testimony **“omitted”** uptake; **“not”** 18%; intervals excluding measurement and calibration uncertainty; and findings that **“don’t depend”** on the baseline-error model. Their scope remains checkable and supported, subject to the specific wording issues above. The unchanged novelty and later-uptake absence claims remain statements about recorded searches, not proof of universal absence.

The account remains generally fair to Nordicity/Miller and Morrison: it credits the report’s transparency and anticipation of low uptake, preserves evidence favourable to it, distinguishes technical forecasts from testimony, and acknowledges mitigation proposals. Correcting the new model comparison and restoring the lost qualifications would preserve that balance.
