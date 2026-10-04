# Load-bearing source reread, 2026-10-03
<!-- SUMMARY: reread of the eight sources the argument leans on, against the text at 68b6ca0; two corrections applied (Simpson locators; context of Morrison's "good news" remark), two optional fairness additions for Brett · status: applied · updated: 2026-10-03 -->

Run by Claude Opus 5.5 following `passes/registry/source-reread.yaml`. `lit cites` shows every source below is cited only by this paper, so there were no sibling reading notes to start from. Sources were read from the `.md` companions in `literature/`, with the PDF for page numbers where needed. The report's numbers and all 42 quotations had already been verified by Codex in recheck 4; this pass checks attribution and context.

## Load-bearing sources and why

| Source | Role in the argument |
|---|---|
| Nordicity & Miller 2015 | The forecast checked; target of the comparison |
| Commons CHPC meeting 8 evidence (12 April 2016) | The testimony criticized; fairness to Morrison |
| Miller 2022 | Closest later work by a forecaster; bears on the novelty claim |
| Kane 2026 | The precedent whose separation of technical and public forecasts the paper adopts |
| Harrington, Morgenstern & Nelson 1999 | Supplies the ex ante/ex post result and the "quantity error" analogy |
| Simpson 2014 | Authority for "overestimates need not show bias" and for industry estimates |
| Morgenstern 2018 | Authority for the counterfactual problem |
| Manski 2011 | Authority for the point-prediction remark |

## Per source

**Kane 2026.** Attributions: checked admissions and enrolment forecasts by universities and Harvard's expert (yes: Card's simulation, the fifteen-university and thirty-three-college briefs); "separates the expert's technical estimate from the forecasts the institutions put to the Court" (yes: Card's report is treated apart from the amicus briefs, with their different counterfactuals and units, e.g. "The 33 percent figure is smaller than Card's 57 percent ... because it describes a different counterfactual"); "varies the baseline period" (yes: "Comparisons against both baselines—the litigation window, and the elevated classes of 2020 through 2023—appear throughout"). Pre-discussion verdict, from Kane's tables: post-ruling Black shares sit near the 2010–2015 baseline and about a tenth to a fifth below 2020–2023, far from the forecast 50–70% declines. Kane's interpretation (predictions "didn't come true"; a question whether schools comply) is his, and the paper doesn't adopt it.

**Harrington et al. 1999** (abstract and opening pages). "12 of the 25 rules ... while for only 6 were the ex ante estimates too low" and "The quantity errors are driven by both baseline and compliance issues" (abstract, p. ii): match. Their account: total-cost overestimates are often due to errors in the quantity of emission reductions, and per-unit cost errors run both ways for EPA and OSHA rules. The discussion's analogy ("a quantity error of the kind Harrington et al. found behind errors in regulatory cost estimates") fits: uptake is a quantity of behavioural response, not a unit price.

**Simpson 2014.** The skew argument (an unbiased estimate of a right-skewed cost distribution exceeds most outcomes) is on printed p. 322. The industry-estimate studies he reviews: Putnam, Hayes & Bartlett 1980, where industry overestimated capital costs in four of five cases (p. 319), and Anderson & Sherwood 2002, where EPA estimates were closer to actual price changes than industry estimates and ex ante estimates generally exceeded actual (p. 321). "The few studies of industry's own estimates found them above outcomes in most cases" is a fair summary of the two. **Correction:** the locator was pp. 319–320; it's 319–321, and the skew argument now carries p. 322 in both places it's cited.

**Morgenstern 2018.** "nine new case studies involving a total of 34 comparisons ... suggest a slight tendency to overestimate both costs and benefits" (abstract): matches "a later set of case studies suggested". "It is no exaggeration to say that developing a credible counterfactual is the most demanding aspect of an RA (Kopits et al. 2014)" and "these must be revisited in RAs" (p. 286): Morgenstern's own sentences, with Kopits et al. as his support. Attribution correct.

**Manski 2011.** "Point predictions are common and expressions of uncertainty are rare" (p. 1): matches. Context worth knowing, not used: Manski reports a consultant's view that "the client needs a point".

**Miller 2022.** n. 88 discusses what Let's Talk TV led to, declining to "opine here on whether that policy should be seen as a success or failure". n. 196: "I have myself made the mistake of predicting station closures" (local stations, with a link to 2016 CBC coverage). The paper's sentence ("discusses what the decisions led to, and acknowledges an error in a separate prediction of station closures") is accurate. *Optional addition for Brett (A):* n. 88 also says the large distributors have, "where they can", been "driving down service wholesale fees, and in the process, trimming the number of Canadian services offered", to the cost of "small independent services that have lost carriage, subscribers and/or revenues". That's the forecaster's own later account, and it bears on §5.1 (aggregate payments per subscriber rose) and §5.2 (independents' closures too uncertain to test). One sentence in §5.1 would give it.

**Commons evidence, meeting 8.** Morrison's opening statement and every Morrison and Miller turn reread. The quotations and the two departures stand. **Correction:** the discussion said "when a member raised officials' more reassuring view he answered, 'If it is right, that's good news'". The member (Vandal) had cited Canadian Heritage evidence that funding for local production had increased, a point about local television, not about the Let's Talk TV forecast. Now: "when a member cited officials' evidence that funding for local production had increased, he answered ...". Other context noted, no change: Morrison also said "This loss has nothing to do with technological change", which is accurate by the report's construction (the forecast is the reform scenario minus a baseline that already includes technological change); and Miller told the committee that local-TV declines were "fairly small" so far because integrated companies had kept funding local programming.

**Nordicity & Miller 2015 (framing paragraphs).** Para. iii: "designed to provide the most plausible outlooks possible given available information. None of the models developed include elements of a scenario being either worst or best case. The authors welcome a vigorous dialogue about these assumptions and their conclusions". Para. 111: "The models could be made more robust by applying weighted probability analysis ... However, there is no easy way to assign probabilities". Para. 78, n. 40: the low-uptake possibility. The paper's uses are accurate. *Optional addition for Brett (B):* the credit paragraph could add that the authors "welcome a vigorous dialogue about these assumptions" (para. iii).

## Applied

- `sections/intro.tex`, `sections/discussion.tex`: Simpson locators (322 for the skew argument; 319–321 for the industry studies).
- `sections/discussion.tex`: the "good news" remark placed in its actual context.

Rebuilt with nonstopmode, 27 pages, hairline overfulls only.

## Addendum, 2026-10-04: Harrington et al. read in full (side-agent note on the printed bibliography note)

The printed reference list carried "Only the abstract and opening pages were read". The local PDF (`literature/harrington_morgenstern_nelson_1999_rff_dp9918_partial.pdf`) is in fact the complete 44-page discussion paper; its filename and header comment said "partial" in error (header corrected). Reading the results (section IV, Table 3, p. 14) and conclusions (section VI, pp. 22–23) found that the paper's own summary is inconsistent: the abstract (p. ii) and conclusions (p. 23) say ex ante total costs were too low for "only 6" of the 25 rules, but Table 3 and its text give total costs "underestimated in just two cases" (12 overestimated, 5 accurate, 6 unable to determine); 6 is the table's count of per-unit cost underestimates. Simpson (2014, 319) reports the published 2000 version as 14 overestimates and 3 underestimates of 28 rules.

**Correction:** the introduction now cites Table 3 (p. 14): exceeded for 12 of 25 and fell short for 2, noting that the abstract gives 6; the quotation "driven by both baseline and compliance issues" keeps p. ii. The bibliography note about partial reading is removed. Alternative left to Brett: cite the published version's counts (14 and 3 of 28) through Simpson's summary instead.
