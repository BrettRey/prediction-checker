<!-- Saved verbatim by the parent session (Claude Opus 5.5) from notes/passes/round-clarity-2026-10-03/codex-stdout-terminological-hygiene.txt (gpt-6-astra, xhigh, read-only). -->

I’m **GPT-6, working through Codex**. This is an independent, read-only review of `043df99` and the supplied `main.txt`. I changed no files.

The main terminology problem is **compression of distinctions the paper otherwise understands**. The detailed qualifications are often sound, but summaries turn partial recalculations into “the report’s mechanism,” proxy measures into “uptake,” and a fitted coefficient into an observed shortfall. Those changes can strengthen the apparent findings.

Locations below use source lines at `043df99`:

- **M** — [main.tex](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/main.tex)
- **I** — [sections/intro.tex](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/intro.tex)
- **C** — [sections/case-lttv.tex](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/case-lttv.tex)
- **D** — [sections/discussion.tex](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/discussion.tex)
- **A** — [sections/appendix.tex](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/appendix.tex)
- **T** — [sections/tables-lttv.tex](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/sections/tables-lttv.tex)
- **F** — [scripts/figures_lttv.py](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/scripts/figures_lttv.py), for labels inside figures.

The live LaTeX already contains concurrent acronym repairs. The findings below concern the requested snapshot.

**1. Local terms, first-use definitions, and contrasts**

| Term or contrast | First use and definition supplied | Trace and assessment |
|---|---|---|
| **\(k\)** | I18: “the observed shortfall below … baseline … as a multiple of its forecast impact.” | Repeated at C35; formally specified at A10–18. The opening definition sounds like a ratio of observed losses. The actual quantity is a coefficient in a statistical model, estimated by a weighted projection. |
| **\(\hat k\)** | C55 introduces the notation with the numerical result, without explicitly distinguishing it from \(k\). A18 supplies the estimator. | The introduction uses \(k\) for estimates; results alternate between \(k\) and \(\hat k\); Table A3 calls the estimate “Observed \(k\).” Distinguish parameter, estimate, and projected scenario coefficient. |
| **Scenario \(k\), \(k^u\)** | C57 calls it “projected \(k\).” T85 defines \(k^u\) as a projection of the recalculated log-shortfall path. | This is neither an observed estimate nor necessarily a full path proportional to the original forecast. The notation is most precise in Table A3. |
| **Report baseline / no-reform baseline / no-reform path** | I18 supplies these as near-synonyms. C10 gives the substantive definition: technological and behavioural change with the pre-existing regulatory regime retained. | Mostly stable. D21 changes to “technology-only baseline,” a source-derived label that sounds narrower. The baseline is a forecast, not the observed pre-reform level or an identified counterfactual. |
| **Forecast path / LTTV scenario / decisions scenario** | M26 uses “forecast path” before distinguishing it from the baseline, which is also forecast. C10 describes the decisions overlaid on the baseline. | The same reform scenario appears as “forecast,” “its scenario,” “LTTV scenario,” and “decisions-scenario.” LTTV is not expanded as an acronym in the running text. |
| **Impact** | I10 uses “economic-impact study”; I18 uses “forecast impact.” C10 explains that headline numbers are gaps between scenarios. | Later denotes dollar shortfalls \(I_t\), log shortfalls \(\delta_t\), signed employment changes, and broader economic consequences. The context usually resolves this, but tables need units and sign conventions. |
| **Shortfall** | I18: below the report baseline. A10 precisely defines the signed log shortfall \(y_t\). | Usually careful. The distributor decomposition concerns the **change from 2014 in a baseline-relative gap**, a further qualification that must remain attached. |
| **Gap** | C10: difference between the report’s two scenarios. | Also means outcome–baseline difference, report–CRTC measurement difference, and estimate–scenario distance in standard errors. These are legitimate uses if the two quantities are named. Several compressed uses omit them. |
| **Loss / decline / missing growth** | M26 uses “channel losses”; C12 describes the report’s forecast losses. | “Loss” can mean either a counterfactual shortfall or an actual reduction over time. C65 carefully distinguishes missing growth from nominal change; the abstract does not. |
| **Chain / mechanism** | I10 says assumptions are stated “link by link”; I22 first says “the report’s chain.” C12 describes the sequence from package choice to revenue, programming and employment. | Appropriate for the report’s proposed causal relationships. Later also denotes the author’s limited numerical recalculation. D9 makes the strongest slide from numerical compatibility to the mechanism fitting. |
| **Model** | C16: the report’s economic model. C35 introduces the paper’s statistical model. | Bare “the model” subsequently alternates between these. C80’s model check concerns the statistical error model; C59’s model concerns Nordicity’s model. |
| **Partial recalculation / model-implied scenario** | I22 describes holding exemption-order and closure components fixed; Figure 1 calls this a “partial recalculation.” C57 calls the outputs “model-implied scenarios.” | C59 explicitly says this is an approximation, not a rerun. That qualification is weakened by the stronger label and later “chain” language. |
| **Scenario / path** | M26 refers to the report’s three scenarios. I20 gives annual uptake values; I22 introduces a survey path. | “Scenario” sometimes denotes an assumption set, sometimes a numerical revenue path. “Uptake path” should denote the assumed sequence of subscriber shares; “revenue path” its calculated output. |
| **Uptake** | M26: uptake “of an entry-level package.” I20: subscribers taking entry-level service **with chosen channels**. | The referent changes immediately. Elsewhere it covers CRTC basic-package subscriptions, MTM starter-package adoption, prospective willingness, and Morrison’s unspecified “Canadians.” |
| **Entry-level package / service** | I8: a $25 package; C8 specifies the maximum price and exclusion of equipment. | These are harmless synonyms for the basic offering. Neither term by itself entails buying discretionary additions. |
| **Skinny basic / starter package** | “Starter packages” appears at I20 without an explicit equivalence; “skinny-basic” appears inside the quotation at C87. | Both refer to the entry-level offering in the relevant sources. Their relation to BYOP needs stating. |
| **BYOP** | C87, inside “skinny-basic/BYOP option”; no expansion in the snapshot. | The report expands it as **Build Your Own Package** and models basic service plus discretionary spending. It is not simply another name for basic-package adoption. |
| **Pick-and-pay** | Appears in the MTM reference title; the body describes individual-channel purchases without using the label. | No substantive running-text drift to repair. If introduced, distinguish buying individual channels from choosing a starter package. |
| **Band / cited-input band / forecasters’ inputs** | C39: a band constructed by the author from inputs cited by the report, explicitly not published by the report. | Good provenance statement. Later descriptions obscure both that provenance and the construction. It is neither a confidence interval nor the envelope of Table A3’s uptake scenarios. |
| **Calibration / error scale / \(\sigma\)** | I22 mentions an error scale and “widest calibration.” C37 explains external calibration. Figure 1 introduces \(\sigma\); A12 defines its statistical role. | “Calibration” alternates between a rule and its resulting value. “Error” often substitutes for its annual standard deviation. The Netflix-derived value is sometimes presented as though it were the final \(\sigma\). |
| **Baseline’s error / \(e_t\)** | C35: positive when the baseline overstates the no-decisions outcome; a random walk from 2014. | A24 and Table A4 reuse \(e_t\) for **Netflix observed/forecast**, reversing the sign convention and changing the underlying quantity. |
| **Pre-stated / planned / post hoc / added after seeing outcomes** | M26 distinguishes the initial plan from later analyses. | Generally candid. However, “pre-stated reading” can mean a rule, rather than a result known in advance. Table A8 also distinguishes commitments before all outcomes, before particular sources, and before a new computation. These are different statuses. |
| **Consistent / compatible / inconsistent** | M26 uses consistent/inconsistent; I22 switches to compatible. | No separate meanings are established. Table A4 additionally uses “consistent” as a classification label whose stated definition overlaps with “inconclusive.” |
| **Channels / specialty and pay services** | M26: “specialty and pay channels.” | “Channels” later abbreviates the outcome sector. Table A6 reveals that the CRTC series is discretionary **and on-demand** services. C63 also uses “channels” to mean causal routes. |
| **Programming services / Canadian services** | C14 uses both in describing pass-through. | Broader than specialty and pay services in Table A1, which includes conventional television. “Canadian” concerns the service, not a claim that all its programming is Canadian. No first-use scope definition is supplied. |
| **Distributors / BDUs** | I8 gives cable, satellite and IPTV distributors. C63 first uses BDUs inside a quotation. | Same institutional class; BDU is unexpanded in the snapshot. The revenue series concerns broadcasting services, not all telecommunications revenue. |
| **Edition / release / vintage** | Figure 1 uses “2016 edition” and “2020 edition.” “Released” also dates the report and MTM publication. | No substantive edition/vintage drift in the rendered paper: “vintage” is not used there. Edition year and publication year are nevertheless easily confused. MTM release date is not a survey fieldwork date. |
| **Direct / spin-off** | I8 quotes “direct result”; I26 uses “direct FTE loss”; I28 introduces spin-off employment. C12 and C22 explain the sector distinction. | The paper correctly distinguishes causal attribution in “direct result” from the input–output category “direct.” Spin-off’s inclusion of indirect and induced effects is not stated. |
| **FTE / staff count** | I26 uses FTE unexpanded; C12 expands it. | The later qualification is good, but the introduction compares unlike measures before explaining that. The distributor series is itself assembled from differently labelled staffing measures. |
| **CPE / ARPU / preponderance / exemption order** | CPE is expanded in Table A1; ARPU appears unexpanded in Table A5; technical preponderance appears in Table A2; exemption-order components appear in I22 before explanation. | These need scope definitions, not merely acronym expansion. Details below. |

**2. Drifts that could mislead a reader**

**A. \(k\) is introduced as a quantity it is not.**  
At I18 and C35, “observed shortfall … as a multiple” implies a direct shortfall ratio. Yet the channel observations lie above the baseline throughout, while \(\hat k\) is positive. The paper explains why at C35, but this explanation repairs the reader’s interpretation of the earlier definition.

The formal account is coherent: \(k\) is the coefficient of the forecast log-shortfall path under the assumed error model; \(\hat k\) is its estimate. Use that distinction from the outset. Also qualify “\(k=0\) is the no-reform path”: with nonzero \(e_t\), it denotes the no-reform **benchmark**, not a realised path exactly equal to \(B_t\).

**B. The report’s mechanism becomes the partial recalculation.**  
The explicit limitation at C59 is valuable: two components are held fixed although the report derives them partly from other components. Nevertheless, I22–24, C61–65 and D7–9 repeatedly attribute these outputs to “the report’s chain.”

D9 then says the outcomes “fit the report’s mechanism only if uptake stayed well below its assumption.” That exceeds the terminology warranted by the calculation in three respects:

- it concerns partial recalculations;
- it concerns the paths tested, not every possible uptake path;
- compatibility is judged through projected \(k\) values at a designated error scale, not a comprehensive test of the mechanism.

The opening clause “Of the paths tested” does not adequately limit the general conclusion after “so.”

**C. “Uptake” moves among at least four measures.**  
The paper eventually recognises this at C87 and D15, but the abstract and introduction have already equated them.

The distinctions are material:

- report: entry-level service **plus discretionary selections**;
- CRTC: subscriptions to the entry-level service, with or without additions;
- MTM: self-reported starter-package adoption;
- Morrison: an estimate concerning “Canadians,” without a specified denominator.

The CRTC’s April release explicitly separates basic-package subscribers from those also taking individual channels or small packages. MTM’s 29% add-on figure is likewise distinct from its starter-package figure. These are not interchangeable observations of the model input. [CRTC release, local copy](/Users/brettreynolds/projects/LLM-CLI-projects/literature/crtc_2016-04-15_66000_basic_tv_package_release.md), [MTM release, local copy](/Users/brettreynolds/projects/LLM-CLI-projects/literature/mtm_2017-08-17_starter_tv_pick_and_pay_press_release.md).

Table A3’s row “CRTC count, 30 June 2016” then labels **four assumed annual shares**. Only the starting observation is counted.

**D. The cited-input band and the flat uptake scenarios sound like the same construction.**  
C57 says “That band assumes uptake between 10% and 35%.” Table A2 more precisely says it scales the original uptake-related components by \(10/15\) and \(35/15\).

That preserves the report’s ramp. It does not impose 10% or 35% in every year. Consequently, the band’s lower channel value, 0.75, differs from the flat 10% scenario’s 0.56. Both can be correct; the prose makes the difference look unexplained.

“Band implied by the forecasters’ inputs” also understates the author’s choices about scaling, closure components and projection.

**E. Compatibility language has an unstable object.**  
Sometimes an interval contains the original forecast’s \(k=1\); sometimes it overlaps a constructed band; sometimes it contains a recalculated scenario coefficient. These should be named separately.

Table A4 defines “consistent” as overlapping the band and “inconclusive” as containing zero and the band’s lower end. The second condition entails the first. The code gives “inconclusive” priority, but the caption does not state that rule.

C39 also says an outcome below the forecast path would be reported as “forecast exceeded.” The actual planned rule requires the **interval to lie above the band**. The distributor point estimate illustrates why these formulations are not equivalent.

**F. “Error” alternates between a realised discrepancy and a standard deviation.**  
C33 sets “the baseline’s error” equal to historical volatility. C41 and C78 say the Netflix comparison “puts the error at 1.3%.” These are scale calculations, not estimates of a realised Canadian baseline error.

Moreover, 1.3% is the Netflix-derived scale **before the historical-volatility floor**. The designated \(\sigma\) values are 2.2% and 1.9%. Figure 2’s “annual baseline error” similarly needs “standard deviation of annual changes in baseline error.”

The reused \(e_t\) at A24–28 and T111–121 is a separate, definite notation collision.

**G. “Loss” can imply a nominal decline where the intended claim is a baseline shortfall.**  
The abstract’s “channel losses that didn’t occur” is the clearest instance. Channel revenue did fall nominally; what did not appear was the projected baseline-relative shortfall at the designated comparison.

The distributor discussion at C65 is substantially better: it distinguishes nominal revenue decline, subscriber decline, per-subscriber revenue growth, and missing growth relative to the baseline. Preserve that vocabulary in the summaries.

**H. Sector labels and policy components need boundaries.**  
“Channels” is a readable shorthand, but the measured sector includes on-demand services. “Programming services” is broader still. C63’s “the report’s channels act on different factors” introduces an avoidable second meaning of “channels.”

Likewise, the hybrid streaming exemption order is different from the licensing exemption that makes some continuing television services disappear from individual-service lists. The repeated unqualified “exemption” vocabulary risks connecting two separate issues.

**I. Staffing terminology is qualified too late.**  
The direct/spin-off reconciliation is sound. The remaining problems are:

- I26 compares staff-count decline with an FTE shortfall before warning that these are unlike measures.
- “Pre-2015 trend” at I26 and C95 actually means a trend fitted over **2012–2015**, including 2015.
- C97 treats a change from an FTE-labelled series to a staff-count-labelled series as a demonstrated change of measure. The documentation shown establishes the label change and numerical discrepancy; the safest wording reports those directly.

**J. Chronology labels require precision, not a wholesale reclassification.**  
The paper responsibly identifies post hoc additions. Two details need repair:

- “Pre-stated for those sources” in Table A8 is weaker than pre-stated before any outcomes.
- The table stops before the survey-path additions, despite the prose referring readers there.

I checked the apparent 8% conflict: the plan at `66f9c25` already specifies 1–8%. Thus Figure 2’s description of that range as planned is supported. Table A8 should say the later work **extended the displayed sensitivity results to the already planned 8%**, rather than suggesting the range itself was newly chosen.

**3. Imported terms: fidelity to their sources**

| Source or term | Assessment |
|---|---|
| **Nordicity: BYOP** | The quotation is faithful, but the local shorthand is too broad. The report expands BYOP as **Build Your Own Package**, assumes entry-level service plus discretionary purchases, and specifies the annual subscriber shares in Table 18. Define that model input separately from basic-package adoption. |
| **CRTC/report: preponderance** | The underlying distinction is between Canadian services **offered** and services **received**. The report models the change using Canadian services’ share of wholesale fees among BYOP subscribers. The regulatory requirement and the report’s monetary proxy are different quantities. The draft’s component label is faithful but unexplained. |
| **Report: exemption order** | C59 correctly identifies the streaming mechanism. Use the source’s more specific “hybrid streaming exemption order” earlier. Separately identify exemption from individual television-service licensing in the closure analysis. |
| **Report: CPE** | The paper’s aggregate follows the report’s scope: programming services’ Canadian-programming spending **plus distributor contributions**. Table A1 is substantively aligned, but “programming expenditure” can sound like broadcaster spending alone. State the aggregate’s scope before the denominator argument. |
| **Report: ARPU** | Table A5 correctly retains the report’s Figure 19 series as a separate comparison. Expand **average revenue per subscriber** and distinguish it from the paper’s reconstructed revenue-per-subscriber quotient. Do not call either a package price. |
| **Report: direct/spin-off employment** | Faithful. The report defines direct employment within broadcasting and production, with spin-off employment elsewhere; its table notes include indirect and induced effects in spin-offs. “Direct result” in the testimony is correctly treated as causal attribution, not as a claim that all 15,130 FTEs were direct employment. |
| **CRTC: discretionary and on-demand services, BDUs, staff count** | The series mapping is present in methods/code and captions but not sufficiently visible at first use. “Staff count” should retain the source’s label; it should not silently become verified headcount. |
| **Kane: baseline; technical estimate/public forecasts** | I16 fairly describes Kane’s separate treatment of expert estimates and institutional forecasts, and his comparisons against different baseline periods. C31’s “much as Kane” needs qualification: varying uncertainty around one baseline is different from changing the baseline comparison period. |
| **Manski: point prediction, uncertainty, conditionality** | Faithful at I14 and D15. The draft does not need to import Manski’s whole taxonomy or call this “incredible certitude.” Its narrower claim about a missing numerical condition is appropriately limited. |
| **Harrington: quantity error** | I12 is faithful to the abstract. D9 is a reasonable analogy, but should say so: Harrington’s quantity errors concern achieved emission reductions and baseline/compliance assumptions, not television-package uptake. “If the 2016 count was the miss” also needs to identify the **uptake assumption**, rather than making the count sound erroneous. |
| **Gelman and Carlin: design analysis** | Appropriate as a broad description of calculations under hypothetical replications. The draft’s specific procedure is classification between two forecast worlds. D21’s “too little power” is looser: the reported 63% is classification accuracy, not a reported rejection probability for a specified hypothesis test. |
| **Gelman et al.: fake-data simulation; calibration** | “Fake-data simulation” is appropriate. The Netflix operation is an external choice of error scale, not simulation-based calibration or an empirical demonstration of probabilistic calibration. The paper does not explicitly claim otherwise, but the local definition should prevent that reading. |
| **Gelman and Stern; Gelman and Loken** | The uses at C76 are fair: verdict changes can reflect uncertainty changes without estimate changes, and reporting multiple defensible analyses addresses selective presentation. Neither citation makes the reported set exhaustive. The draft generally avoids that stronger claim. |

Sources checked include the relevant portions of [Nordicity and Miller](/Users/brettreynolds/projects/LLM-CLI-projects/literature/nordicity_miller_2015_canadian_television_2020.md), [CRTC 2015-96](/Users/brettreynolds/projects/LLM-CLI-projects/literature/crtc_2015-96_lets_talk_tv_world_of_choice.md), [Kane](/Users/brettreynolds/projects/LLM-CLI-projects/literature/kane_2026_after_sffa_predictions_ejw.md), [Manski](/Users/brettreynolds/projects/LLM-CLI-projects/literature/manski_2011_policy_analysis_incredible_certitude_pep10.md), [Harrington et al.’s available opening pages](/Users/brettreynolds/projects/LLM-CLI-projects/literature/harrington_morgenstern_nelson_1999_rff_dp9918_partial.md), [Gelman and Carlin](/Users/brettreynolds/projects/LLM-CLI-projects/literature/gelman2014types.md), and [Bayesian Workflow](/Users/brettreynolds/projects/LLM-CLI-projects/literature/gelman-etal-2020-bayesian-workflow.md).

**4. Proposed controlled vocabulary**

These definitions can be distributed across first uses; they need not become a glossary in the paper.

| Preferred term | First-use definition |
|---|---|
| **Report baseline** | The report’s forecast under its baseline regulatory assumptions, retaining technological and behavioural change but excluding the modelled LTTV changes. |
| **Report reform scenario / reform path** | The report’s assumptions with the modelled decisions implemented; a quantity’s resulting annual path is its reform path. For revenue, that path is \(B_t-I_t\). |
| **Forecast shortfall** | The amount by which the reform path falls below the report baseline; specify dollars \(I_t\) or logs \(\delta_t\). |
| **Observed log shortfall** | \(y_t=\log B_t-\log Y_t\), which is negative when observations exceed the report baseline. |
| **Nominal decline** | A decrease in observed current-dollar revenue between named years. |
| **Forecast scale \(k\); estimate \(\hat k\)** | \(k\) multiplies the report’s forecast log-shortfall path in the statistical model; \(\hat k\) is fitted from the observed series. |
| **Report mechanism** | The report’s proposed relationships connecting subscriber choices, revenue, programming expenditure and employment. “Chain” can be retired as its alternating technical label. |
| **Partial recalculation** | The paper’s rescaling of published uptake-related revenue components while holding the exemption-order and closure dollar components fixed. |
| **Recalculated scenario; scenario coefficient \(k^u\)** | A revenue path produced by that partial recalculation, and its projection onto the original forecast’s log-shortfall path. |
| **BYOP uptake** | The report’s share of distributor subscribers taking entry-level service with discretionary selections. |
| **Entry-level uptake** | The observed or reported share subscribing to the basic package, whether or not they buy additions. |
| **Assumed uptake path** | Annual BYOP shares supplied to a recalculation. Name the flat 1.6% path, flat 4% path, rising paths and illustrative survey path explicitly. |
| **Cited-input band** | The author’s range of projected \(k\) values constructed by scaling the report’s components using cited input estimates. It is a sensitivity band, not a probability interval. |
| **Baseline error \(e_t\); annual error scale \(\sigma\)** | The accumulated log error in the report baseline; \(\sigma\) is the standard deviation of its annual innovations. |
| **Calibration rule; designated error scale** | A rule for choosing \(\sigma\); the designated scale is the value selected by the pre-stated rule. |
| **Compatible / incompatible** | On this paper’s \(k\) comparison, a scenario coefficient is compatible when it lies inside the conditional 95% interval. State separately whether the interval overlaps the cited-input band. |
| **Pre-stated / post hoc** | Fixed before any outcome data were opened / chosen afterward. Add narrower timing qualifications where appropriate. |
| **Specialty and pay services** | The report’s sector, including pay-per-view and video-on-demand; mapped here to the CRTC discretionary-and-on-demand series with the stated exemption adjustment. |
| **Distributors** | Cable, satellite and Internet Protocol television providers—broadcasting distribution undertakings, or BDUs. |
| **Forecast employment shortfall / reported staffing** | Modelled employment below the report baseline, in FTEs / the CRTC staffing series under its published labels. |
| **Edition** | The data publication identified by its reference year, distinguished from publication date and the observation year within it. |

For financial flows, keep **retail revenue per subscriber**, **the report’s carriage fee**, and **observed affiliation payments per subscriber** distinct. They should not alternate as “price” or “fees” without specifying which is meant.

**5. Occurrence-level change list**

Grouped rows enumerate repeated occurrences. Quotations should remain verbatim; add explanations outside them. Changes to generated tables and figures belong in their generating scripts.

**Estimates, paths, bands and error language**

| Location | Existing wording or label | Proposed replacement |
|---|---|---|
| **I18; C35, opening definition** | “outcome measure … observed shortfall … as a multiple” | “For each revenue series, I estimate a scale \(k\) multiplying the report’s forecast log-shortfall path under a model of baseline error. Its fitted value is \(\hat k\).” Follow with the existing equation in C35. |
| **I18; C35** | “\(k=0\) is … no-reform path and \(k=1\) its forecast” | “\(k=0\) is the no-reform benchmark and \(k=1\) the report-impact benchmark, allowing baseline error in either case.” |
| **I22, observed result; I24, observed result** | \(k=0.12\); \(k=1.30\) | \(\hat k=0.12\); \(\hat k=1.30\). |
| **C35** | “specialty and pay revenue’s \(k\) is positive” | “the estimate \(\hat k\) for specialty and pay revenue is positive.” |
| **I22, two recalculated results; C57; C61** | \(k=\ldots\) for scenario outputs | \(k^u=\ldots\), with the scenario-coefficient definition supplied at first use. |
| **I24** | “distributors’ recalculated \(k\) … against the observed 1.30” | “distributors’ scenario coefficient \(k^u\) … against \(\hat k=1.30\).” |
| **T85; T103** | “Observed \(k\)” | “Estimated \(\hat k\).” |
| **T111** | “interval for \(k\), which is 0.12 … and 1.30” | “interval for \(k\); its estimate \(\hat k\) is 0.12 … and 1.30.” |
| **C10, after describing the two worlds** | No stable names for subsequent use | Add: “I call these the report baseline and the report reform scenario; each quantity has a path under each scenario.” |
| **M26; I22; I24; C46; C51; C61** | “forecast path,” referring specifically to the reform path | “report reform path,” shortened to “reform path” after definition. |
| **C55; C61** | Standard errors “from the forecast” | “from the report-impact benchmark, \(k=1\).” |
| **I24, interval clause; C76; D21, interval/coverage clauses** | Interval “includes the forecast”; distances or coverage of “the forecast” | “includes \(k=1\)”; “distance from \(k=1\)”; “covers \(k=1\),” as applicable. |
| **I24, faster-cord-cutting scenario; C63; C65, first two sentences; T149; T174** | “its scenario,” “the scenario,” “Report’s scenario,” meaning the original decisions scenario | “report reform scenario.” |
| **T22; T33** | “LTTV scenario 2020” | “report reform scenario, 2020.” |
| **T45** | “decisions-scenario level” | “reform-path level.” |
| **D21** | “technology-only baseline” | “report baseline.” |
| **C39, band definition** | “A band of \(k\) built from the estimates … counts as consistent with the forecast” | “I construct a cited-input band for \(k\) by scaling the report’s uptake-related components using the cited estimates and increasing closures in the upper case.” Retain the statement that the report did not publish the band. |
| **C55** | “band built from the report’s cited estimates” | “cited-input band.” |
| **C57, first sentence** | “That band assumes uptake between 10% and 35%.” | “The band scales the report’s uptake-related components by \(10/15\) and \(35/15\), preserving its uptake ramp; these are different paths from a constant 10% or 35% share.” |
| **C61; C72; C76; A18; F100** | “band … implied by/from the forecasters’ [cited] inputs” | “cited-input band constructed for this paper.” Later local mentions can use “cited-input band.” |
| **C31** | “treats the baseline’s error as unknown, puts a range on it” | “treats baseline error as unknown and varies the assumed annual error scale.” |
| **C31, Kane comparison** | “much as Kane … reports against more than one baseline” | “Kane varies the baseline comparison period; here I retain the report baseline and vary its assumed error scale.” |
| **C33** | “With the baseline’s error set at the volatility” | “With the annual error scale set to the historical volatility.” |
| **C37** | “The scale of that error” | “The standard deviation of annual changes in that error, \(\sigma\).” |
| **C41** | “by the pre-stated rule puts the error at 1.3% a year” | “gives a Netflix-derived annual error scale of 1.3%, before applying the historical-volatility floor.” |
| **C78, first sentence** | “puts the error at 1.3%” | “gives a Netflix-derived scale of 1.3%.” |
| **C78, subsequent 2016, pooled and growth calculations** | “miss gives”; “pooled estimate”; “puts the error at” | Identify each as a “Netflix-derived scale,” avoiding an implication that it estimates the realised Canadian baseline error. |
| **M26; I22; I24; C51; C55; C61; C72; T85** | “pre-stated error scale/calibration,” or “designated error scale” | Use “designated error scale”; define it once as “selected by the pre-stated calibration rule.” |
| **I22; C76** | “widest calibration” | “largest calibrated error scale.” This distinguishes 4.7% from the 8% sensitivity endpoint. |
| **C72; T111; F113** | “annual error,” including the Figure 2 axis | “annual error scale \(\sigma\)” in labels; define it in the caption as the standard deviation of annual baseline-error innovations. |
| **C76** | “assumed error grows”; “error reaches”; “assumed error crosses” | “assumed error scale increases/reaches/crosses.” |
| **A23** | “Calibrating the baseline’s error” | “Calibrating the annual error scale.” |
| **A24; A26; A28; T111; T121** | \(e_t\) for Netflix log observed/forecast | Use a distinct symbol, such as \(n_t\), throughout these expressions. Keep the formula and numerical signs unchanged. |
| **F115** | “\(k\) (0 = no-reform path, 1 = forecast)” | “\(k\) (0 = no-reform benchmark, 1 = report-impact benchmark).” |

**Mechanism, partial recalculation and compatibility**

| Location | Existing wording or label | Proposed replacement |
|---|---|---|
| **M26, exploratory conclusion** | “both series are compatible with the study’s chain, partially recalculated, only on low uptake paths such as…” | “At the designated error scales, only the tested path rising to 4% by 2019 gives partially recalculated scenarios compatible with both revenue estimates.” |
| **M26, following clause** | “at the survey’s level it projects channel losses that didn’t occur” | “Under the illustrative survey path, the projected channel shortfall is incompatible with the estimate at that scale.” |
| **I22** | “What it says about the report’s chain…”; “the chain gives” | “What the partial recalculation shows…”; “the partial recalculation gives.” |
| **I24, both occurrences** | “recalculated chain” | “partial recalculation.” |
| **I24, streaming sentence** | “what the chain misses” | “the shortfall left unexplained by the partial recalculation.” |
| **C57** | “Model-implied scenarios”; “Recalculating the report’s chain” | “Scenarios from partial recalculation”; “Partially recalculating the report’s published revenue components.” |
| **C61** | “the report’s chain gives” | “the partial recalculation gives.” |
| **C65, both occurrences** | “the report’s chain gives”; “lies beyond the chain” | “the partial recalculation gives”; “exceeds the shortfall in the partially recalculated scenario.” |
| **D7, mechanism sentence** | “the comparisons here can say only which uptake paths the outcomes are compatible with” | “the comparisons here assess the \(k\)-compatibility of partial recalculations under specified uptake paths.” |
| **D7, all three numerical references to the chain** | “recalculated chain”; “comes closer to the chain”; “what the chain projects” | “partially recalculated scenario”; “comes closer to the recalculated scenario”; “the partial recalculation projects.” |
| **D9, first sentence** | The sentence ending “only if uptake stayed well below its assumption” | “Among the paths tested, only a rise to about 4% by 2019 gives partial recalculations compatible with both estimates at the designated error scales.” |
| **D15** | “the recalculated chain gives a projected \(k\)” | “the partial recalculation gives a scenario coefficient \(k^u\).” |
| **A18** | “A model-implied scenario’s \(k\) … report’s chain recomputed” | “A recalculated scenario’s coefficient \(k^u\) … the partially recalculated revenue components.” |
| **T85; T91; T246** | “Model-implied scenarios”; “Model-implied \(k\)”; “Model-implied uptake scenarios” | “Scenarios from partial recalculation”; “Scenario coefficient \(k^u\)”; “Partial recalculations under assumed uptake paths.” |
| **T149; T174** | “report’s chain recalculated”; “Chain, per subscriber” | “partial recalculation”; “Recalculated per-subscriber shortfall.” |
| **C80; C82; T250** | Bare “model” in the residual check or offset analysis | “statistical baseline-error model,” then “error model.” |
| **C59; C97; D11** | Bare “model” referring to Nordicity’s economic relationships | “report’s model.” |
| **M26; I22; C55** | “inconsistent” | “incompatible,” with the object specified as \(k=1\) or the cited-input band. |
| **M26; C59; C61** | Statistical “consistent” | “compatible.” At C59, specify that the scenario coefficient lies inside the estimate’s interval. |
| **C39, final sentence** | “An outcome below the forecast path … forecast exceeded” | “If the interval lay wholly above the cited-input band, the planned label was ‘forecast exceeded’; an outcome below the reform path alone would not confirm or exceed the forecast under that rule.” |
| **T111, verdict definitions** | Overlapping definitions of consistent and inconclusive | Define in order: “inconclusive: interval includes zero and the band’s lower end; smaller: interval lies wholly below the band; compatible: interval overlaps the band but does not meet the inconclusive condition.” |
| **T133; T135; T136; T138; T139** | Distributor verdict “consistent” | “compatible.” |
| **I26; C12; C16** | Authorial “losses,” “lose … revenue,” “takes … out,” for modelled revenue effects | “forecast revenue shortfalls,” “revenue falls below the report baseline,” and “projects annual shortfalls … below the report baseline,” respectively. |

Retain ordinary “consistent with rounding” in Table A7. It is not a statistical verdict and causes no confusion.

**Uptake, sectors and imported labels**

| Location | Existing wording or label | Proposed replacement |
|---|---|---|
| **M26, uptake sentences** | One “uptake” apparently measured by all sources | “The study assumed 5% uptake of entry-level service with discretionary selections in 2016. The broader entry-level subscription measure was 1.6% in mid-2016; a 2017 survey put starter-package adoption near 10%.” Retain its status outside the source rule. |
| **I20, opening** | “The report’s main input was uptake.” | “The report’s main input was BYOP uptake: the share of distributor subscribers taking entry-level service with discretionary selections.” Expand BYOP here. |
| **I20, CRTC and MTM comparison** | “The CRTC counted 1.6%”; unqualified comparison with the report | “The CRTC’s entry-level subscriber count amounted to 1.6% of the 2016 subscriber total.” Add that both observed measures concern the basic package and do not establish the BYOP share. |
| **I22, first survey-path mention** | “an illustrative survey path, 10% from 2017” | “an illustrative survey path assuming 1.6% in 2016 and 10% in 2017–2019.” |
| **I24, rising path** | “the 4% Morrison cited” | “an assumed 4% of subscribers, using Morrison’s figure as an illustrative endpoint.” |
| **C24, outside the quotation** | “a much lower uptake figure than the report’s” | “a lower numerical estimate for entry-level adoption, although he did not specify the denominator or forecast horizon.” |
| **C57, second sentence** | Survey “put uptake near the low end” | “put starter-package adoption near 10%, without establishing the report’s BYOP measure.” |
| **C59** | “At counted uptake” | “With uptake assumed to remain at 1.6%.” |
| **C61** | “At the uptake the CRTC counted” | “With BYOP uptake assumed to remain at the CRTC’s 1.6% entry-level share.” |
| **C67; C82** | “counted-uptake comparison” | “flat-1.6% scenario comparison,” or, more naturally in prose, “comparison with uptake held at 1.6%.” |
| **C87, Oliver Wyman quotation** | Unexpanded BYOP/skinny-basic terminology | Keep the quotation; identify “skinny basic” as the entry-level package and BYOP as Build Your Own Package outside it. |
| **C87, 29% sentence** | Add-on result presented beside starter adoption without explicitly separating the measure | “Separately, 29% reported adding individual channels or bundles to their packages.” |
| **C87** | “10%, a floor” | “10%, a rounded-down representation of the release’s wording.” It is not a statistical lower bound on BYOP adoption. |
| **C87, final sentence; D23, first finding** | Unqualified comparison between “uptake” and the report assumption | Name “the mid-2016 entry-level subscription share” and “the report’s assumed 2016 BYOP share.” |
| **D7, first comparison** | “the CRTC’s count … the report’s 2016 assumption”; survey “put uptake near its figure” | Name the CRTC entry-level share, report BYOP assumption, and MTM starter-package share separately. |
| **T85; T91; T93** | “Uptake”; “Uptake path” | “Assumed BYOP share”; “Assumed uptake path.” |
| **T95** | “CRTC count, 30 June 2016” | “Held at the June 2016 entry-level share.” |
| **T96** | “Estimate Morrison cited (April 2016)” | “Held at 4%, treating Morrison’s figure as a subscriber share.” |
| **T97** | “Low end of cited range” | “Held at 10%, the low cited endpoint.” |
| **T99; T100** | Rising-path labels | “Linear rise from 1.6% to 4%”; “Linear rise from 1.6% to 10%.” |
| **T101** | “Survey path…” | “Illustrative survey path: 1.6%, then 10% from 2017.” Retain the outside-plan-source qualification. |
| **T176** | “Counted”; “Survey” | “Held at 1.6%”; “Survey path.” |
| **F72** | “Partial recalculation at counted uptake” | “Partial recalculation: uptake held at 1.6%.” |
| **I8** | “cable, satellite and IPTV distributors”; “a $25 entry-level package” | Expand Internet Protocol television and define BDUs here; change the package price to “at most $25 a month, excluding equipment.” |
| **C63, quoted BDUs** | “non-reporting BDUs” | Preserve the quotation; with the I8 definition, no further expansion is necessary. |
| **C63** | “the report’s channels act on different factors” | “the report’s model components act on different factors.” |
| **I22, first full outcome-series mention** | “Specialty and pay channels’ revenue” | “Specialty and pay services’ revenue,” followed by the mapping to CRTC discretionary and on-demand services. “Channel revenue” may then be explicitly designated as shorthand. |
| **C22, first authorial CPE definition; T6** | “Canadian programming expenditure” without aggregate scope | Define it as programming services’ spending plus the distributor contributions included in the report. |
| **T14–18; T28** | “Programming services” | Add “including conventional television” at its first table occurrence or in the caption. |
| **T45, first technical preponderance mention** | “preponderance components” | Define the component as the modelled effect of changing Canadian-service preponderance and access rules, represented through wholesale-fee shares. |
| **T55; T69** | “preponderance and access rules” | “changes to preponderance/access rules.” This makes the rows effects of changes, rather than the rules themselves. |
| **I22, first exemption-order mention** | “exemption-order … components” | “components for the hybrid streaming exemption order and service closures.” |
| **C93; D21** | Channels “left licensing for exemption”; “moves to exemption” | “continued operating under an exemption from individual licensing.” |
| **T149** | “Fig. 19’s ARPU” | “Figure 19’s average revenue per subscriber (ARPU).” |
| **I26; C89** | “The two fee measures differ by definition” | Name both: “the report’s Table 14 carriage-fee measure and observed affiliation payments divided by distributor subscribers.” |
| **C91** | “The aggregates don’t show why fees rose.” | “The aggregates don’t show why affiliation payments per subscriber rose.” |
| **T6, explanatory note** | Unexpanded scope-bearing abbreviations | Expand CMF, CBC/SRC, PPV and VOD in a table note: Canada Media Fund; Canadian Broadcasting Corporation/Société Radio-Canada; pay-per-view; video-on-demand. |

**Employment, editions and timing**

| Location | Existing wording or label | Proposed replacement |
|---|---|---|
| **I26** | “direct FTE loss” | “forecast shortfall in direct employment, measured in full-time equivalents (FTEs).” |
| **I26, comparison sentence** | Staff fell “by more than” the forecast FTE loss, without an immediate qualification | Add: “The reported staffing counts and modelled FTE shortfalls are different measures.” |
| **I26; C95** | “pre-2015 trend” | “2012–2015 trend.” |
| **I28, first spin-off use** | “spin-off employment in other sectors” | “spin-off employment—indirect and induced employment in other sectors.” |
| **C97** | “series changes from an FTE count to a staff count between editions” | “the earlier edition labels the series ‘Total Staff Count (FTE)’ and the later edition ‘Total Staff Count’; their overlapping 2016 values differ by 302.” |
| **D13** | “shed more staff than the forecast’s direct FTE loss” | “the reported staff-count decline was numerically larger than the forecast direct-employment shortfall in FTEs.” Retain the following unlike-measures qualification. |
| **T190; T201** | An undifferentiated “Distributors: staff” series | Label it “Distributors: reported staffing” and identify the FTE-labelled and staff-count-labelled segments in the caption. |
| **T200; T203** | “Report’s direct impact” | “Forecast direct-employment change (FTEs).” State that negative values are below-baseline changes. |
| **T211** | “FTE losses”; “Direct FTEs are jobs…” | “Forecast employment shortfalls, in FTEs”; “Direct employment is within the originating sector; spin-off employment comprises indirect and induced effects in other sectors.” |
| **C51, first edition reference** | “2016 edition … 2020 edition” | Add that these are the reference-year editions, published in 2017 and 2021. Subsequent “edition” uses can remain. |
| **C55; C59; C82** | “pre-stated reading/readings” | “reading/readings under the pre-stated rule.” |
| **D21** | “too little power for the planned test” | “too little ability to distinguish the two simulated worlds for the planned comparison.” |
| **D9, Harrington analogy** | “If the 2016 count was the miss, it’s the kind of quantity error…” | “If the uptake assumption was responsible for the discrepancy, that would be analogous to the quantity errors Harrington et al. identify in regulatory cost forecasts.” |
| **T242** | “pre-stated for those sources” | “after initial outcomes; before these sources.” |
| **T245** | “rule pre-stated, comparator post hoc” | “employment-comparison rule pre-stated; trend comparator post hoc.” |
| **T252** | “sensitivity range to 8%” | “displayed sensitivity results extended to the planned 8% endpoint.” |
| **Table A8, after its existing final row** | Survey additions absent | Add the survey-path rule at `026f602`—“post hoc; fixed before computing”—and its implementation/reporting at `ed8961d`, marked post hoc. |

The priority repairs are the definition of \(k\), the mechanism/recalculation distinction, the uptake measures, the band construction, and the two error conventions. Those affect how readers understand the substantive result; the remaining changes make those distinctions survive the summaries, figures and tables.
