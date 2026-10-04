<!-- Saved verbatim by the parent session from codex-stdout.txt (Codex gpt-6-astra, xhigh, read-only), 2026-10-03. -->

**Model: GPT-6 (Codex).** I read the supplied PDF text once, in order, through Table A8, then checked paragraph boundaries and targeted references in the LaTeX. No files were changed.

The paper’s argument is recoverable, and the distinction between checking a conditional forecast and estimating a policy’s causal effect is clear. The greatest reading costs arise in the recalculations: readers encounter unexplained policy components, an incompletely explained projection, and sensitivity checks that haven’t yet been introduced. Some concluding language also obscures distinctions established earlier.

My section-by-section notes follow. Proposed fixes appear in the consolidated list afterward.

| Section | Reader’s knowledge, new material, promises, and shape |
|---|---|
| **Title and abstract** | The title identifies the case and assessed years. The abstract establishes the limited target, but “error scale,” the baseline, and the uptake-derived comparison arrive together before their relationship is understandable. It reads as a compressed results inventory. Its substantive promises are subsequently addressed. |
| **1 Introduction** | The policy, testimony, report, and intended comparison become clear. IPTV and “specialty and pay services” assume broadcasting knowledge. The results paragraph introduces partial recalculations before their motivation and refers to “the report’s share” of programming expenditure before introducing the disputed percentage. The later introduction of \(k\) is clear and useful. The section has a recognizable progression from case to precedent to method, although the results paragraph is overloaded. The section roadmap is fulfilled. |
| **2 The forecast and its presentation to Parliament** | Readers arrive knowing the headline and broad comparison. Baseline, reform scenario, reform path, BYOP, CPE, and the employment decomposition are introduced and reused. **BYOP and CPE are expanded at their first uses.** Category A/B channels and integrated companies remain unexplained. The causal chain gives this section a shape, but it doesn’t introduce all four policy components subsequently manipulated. Table A7 eventually makes the employment cross-classification easy to reconstruct. |
| **2.1 What the committee heard** | The distinction between the report and testimony is clear. The arithmetic and uptake discussion follow intelligibly from the quoted testimony. Table A1 delivers the promised denominator comparisons. “Two of these phrases” requires a small backward search. The later conclusion’s “three identifiable respects” isn’t a numerical contradiction: it adds the omitted connection to the uptake assumption. |
| **3 Comparing outcomes with the report’s reform paths** | The baseline problem motivates the method well. Readers learn the simulation, error model, interval, cited-input band, and calibration. However, \(\delta_t\) isn’t explicitly identified as a **log** shortfall; the band’s projection is left implicit; and the complete verdict rules arrive only in Table A4. \(k^u\) is introduced ahead of its practical purpose, but **is reused**, so it isn’t dead notation. The promised calibration and uncertainty illustration are delivered, although Figure 1 interrupts the calibration’s introduction. |
| **4 Revenue outcomes and their sensitivity to baseline error** | The sequence—outcomes, uptake, recalculations, decomposition, sensitivity, diagnostics—has a shape. Its main problem is that §4.3 borrows material from later subsections before introducing it. |
| **4.1 Against the report’s paths** | The two revenue comparisons are presented in a sensible parallel order. “At the designated error scale” starts a paragraph without naming which revenue series its estimate concerns. The distinction between revenue remaining above baseline and losing ground against it is intelligible because §3 has explained it. |
| **4.2 Uptake: the report’s assumption and the evidence** | The differences among the forecast’s BYOP measure, the CRTC count, and the survey are explained fairly. The survey path is introduced here and delivered in §4.3; it isn’t an orphaned reference. “The report took its 15%” requires remembering that 15% applies from 2018. “Skinny-basic,” “starter,” and “entry-level” add naming friction. The section moves from evidence to a possible explanation and then a limitation. |
| **4.3 Partial recalculations under assumed uptake paths** | This is the hardest section. Readers understand why uptake matters, but not the “preponderance” component or the exemption order when the recalculation first uses them. “Projected in the same way as the band” assumes an explanation that §3 didn’t provide. The 2017 calibration, pooled calibration, rescaled series, and offset model arrive prematurely. Table 1 and Table A3 deliver the four/seven paths. The final explanation of why recalculations don’t reach zero comes after the calculations and answers a question the text hasn’t posed. |
| **4.4 Distributors’ revenue by subscribers and revenue per subscriber** | The decomposition has a clear purpose and a sensible order: construction, comparability, findings, limitations. Its paragraph openings repeatedly require recovering the comparison or baseline. Cord shaving is finally glossed near the end, after earlier uses. Table A5 delivers the decomposition. The two percentages, 67% unexplained by one recalculation and 68% attributable to missing per-subscriber growth, need more separation because they answer different questions. |
| **4.5 Sensitivity to the error scale** | Readers now receive the explanation needed earlier in §4.3. The distinction between an unchanged estimate and widening intervals is clear. “Both intervals” requires recovering the two revenue estimates after the decomposition. The alternative calibrations are delivered in Appendix A and Table A4. The complete meaning of “inconclusive” still awaits that table. |
| **4.6 Checking the error model** | The diagnostic has a useful progression from residual pattern to possible level differences to an offset model. “First step,” two forms of standardization, and “absorbs both” create avoidable interpretive work. This section delivers the offset model promised implicitly in §4.3, but not the rescaled-series explanation. |
| **5 Payments, closures and staff counts** | The subsections follow the report’s chain and fulfill the introduction’s roadmap. No separate introductory paragraph is necessary. |
| **5.1 Payments to Canadian channels** | The payment comparison is motivated. Its central qualification—carriage fees and affiliation payments “differ by definition”—never tells readers what the difference is. The wording of the 75% assumption differs from §2. The wholesale-code sentence introduces a new regulatory object at the end without explaining the objection it addresses. |
| **5.2 Closures and programming expenditure** | The closure bounds and classification sensitivity are understandable in outline, but the reader still lacks definitions of the channel categories and ownership groups. The reason for treating Corus under both classifications isn’t explained. Programming expenditure receives one concluding sentence, making the subsection feel like a closure result with another finding attached. |
| **5.3 Staff counts** | The alternative benchmark and measurement limitations are stated. Table A6 delivers the annual series. “For two sectors” unnecessarily withholds their names. The claim that staff and revenue “don’t move together” mixes changes over time with positions relative to different benchmarks; the following qualifications don’t entirely repair that wording. |
| **6 What the revenue evidence establishes and what the testimony omitted** | The section has a discernible progression from findings through testimony to a practical lesson. It nevertheless repeats much of §4.3’s detailed results. “A fall against the baseline that didn’t appear” blurs the earlier distinction between losing ground and falling below baseline. The report’s transparency and acknowledged uncertainty receive fair treatment. |
| **6.1 Limits of the check** | Most limitations are familiar, but the proportional-impact assumption and its difference from the design simulation arrive here for the first time. That is consequential information to defer until the limitations. The section consists of two long inventories: limitations and findings said not to depend on the error model. The second largely repeats previous summaries. |
| **Data and code** | The availability and provenance statement is clear. Its promises concern the repository, which this reader pass didn’t audit. The AI statement repeats the front-matter disclosure but serves a recognizable documentation purpose. |
| **References** | No reader-facing break in the citation chain stood out. The list resolves the named sources; it doesn’t supply the missing explanation of the low uptake estimate or closure multiplier. This was a reading pass, not citation verification. |
| **Appendix A: The outcome measure** | The formal model finally supplies the precise log-shortfall definition and projection formula. The promised illustration of uncertainty in \(\sigma\) is delivered. The notation is generally economical and reused. \(\delta^u\) should be explicitly named as the recalculated log-shortfall vector before its formula. |
| **Appendix A: Design analysis** | The simulation and meaning of “classified correctly” are explained. The difference between applying the impact in dollars and proportionally is made explicit, with its coverage consequences. This fulfills the appendix reference, but confirms that an important qualification was delayed. |
| **Appendix A: Calibrating the annual error scale** | The Netflix comparison, endpoint alternatives, pooling, and growth calculations are explained. \(n_t\) and \(h\) are introduced and used. This subsection has a clear procedural shape. |
| **Appendix B: Tables** | The opening sentence explains computational checking rather than helping readers navigate the tables. The tables themselves fulfill most earlier promises. Calling them A1–A8 within Appendix B is mildly disorienting. |
| **Table A1** | Delivers the percentage comparisons. CBC/SRC, CMF, PPV, and VOD are unexplained. Component labels E, N1, and N2 aren’t subsequently used as labels. |
| **Table A2** | Delivers the revenue inputs and defines historical volatility precisely. “Preponderance and access rules” remains unexplained. The caption’s blanket “in $ millions” doesn’t cover the log quantities and coefficients. |
| **Table A3** | Delivers all seven paths. The distinction between a constant 10% path here and the ramp-preserving low-input band is recoverable, but unnecessarily easy to miss. |
| **Table A4** | Delivers all calibrations and, for the first time, the complete ordered verdict rule. That rule belongs earlier because it governs the paper’s headline labels. |
| **Table A5** | Delivers the decomposition and its comparison paths. ARPU is expanded but then unused; the column is labelled “Fig. 19.” |
| **Table A6** | Delivers the staff counts, trend, and forecast changes. The change from “specialty and pay” to “discretionary and on-demand” needs a scope explanation. IPTV remains unexpanded. |
| **Table A7** | Clearly explains the two cross-classifications of the employment total. This is useful delivery of §2’s promise. |
| **Table A8** | Delivers the chronology. It also introduces internal terminology—“lead case,” “splice rule,” “reading rule 6,” “multiverse,” and MTM—and supplies the first explanation of the previously mentioned rescaling. “That split” is another avoidable pointer. |

The following defects are ranked by their cost to a first-time reader.

1. **The recalculation depends on policy components the paper hasn’t explained.**

   **Locations:** Figure 1, “the exemption-order and closure dollar components”; §4.3, “unbundling and preponderance components”; Table 1; Table A2’s caption and both “changes to preponderance and access rules” rows; Table A3’s caption.

   Section 2 explains package choice, pass-through, and closures. It doesn’t equip a nonspecialist to understand the four-part revenue decomposition later being manipulated. “Preponderance” never receives a substantive explanation. The exemption order gets a limited explanation only at the end of §4.3, after Figure 1, the calculation, and Table 1 have used it.

   **Fix:** Introduce the four components together in §2, with one plain-language clause explaining each. Explain why uptake rescales two components while two dollar components remain fixed. Distinguish the streaming exemption order from the individual-licensing exemptions discussed under closures.

2. **The band, scenario coefficients, and verdicts aren’t fully explained before they govern the results.**

   **Locations:** §3, “each cited estimate (10% and 35%)” and “multiplying closures by 2.5”; §4.3, “projected in the same way as the band”; Table A4, “Verdicts are the plan’s pre-stated labels, applied in this order.”

   Three gaps accumulate. The 10% estimate isn’t attributed; the closure multiplier isn’t explained; and §3 hasn’t actually described projecting an alternative path onto the forecast path. The complete verdict rule appears on page 21. Consequently, a reader can reasonably wonder why an interval that overlaps the band is sometimes called “consistent” and sometimes “inconclusive.”

   **Fix:** In §3, identify the two uptake estimates and the closure assumption, explain the projection in one sentence, and give the complete ordered decision rule. The distinction between an uncertainty interval and a nonprobabilistic input band is already stated well and should remain.

   Also distinguish the band’s **scaled uptake ramp** from Table A3’s **constant 10% uptake path** at the latter’s first use. Their different coefficients aren’t a contradiction, but readers shouldn’t have to reconstruct why.

3. **A consequential assumption about the intervals appears only in the limitations.**

   **Locations:** §6.1, “they assume the forecast impact applies proportionally to the drifted baseline”; Appendix A, “The estimation model is the proportional one.”

   Readers have already absorbed the design-analysis success rates and multiple 95% intervals before learning that the design simulation applies the impact differently from the estimation model. The appendix reports 87% and 93% coverage under the dollar-impact simulation. This is a qualification of how the earlier interval language should be understood, not merely additional technical detail.

   **Fix:** State the proportional-impact assumption when introducing the model in §3. Briefly flag the simulation’s different construction there, with the coverage details left in Appendix A.

4. **Several statements blur level, change, and benchmark-relative comparisons.**

   **All affected sites:**
   
   - §6: “the recalculation projects a fall against the baseline that didn’t appear.”
   - §5.3: “Staff counts and revenue don’t move together as the report’s chain implies.”
   - §6: “Staff counts and revenue didn’t move together as the report’s chain implies.”

   The first risks contradicting §3’s explicit explanation that specialty/pay revenue **did lose ground against the baseline**, producing positive \(\hat k\), while remaining above it. What didn’t appear was the recalculated magnitude.

   The staff wording also suggests an absence of ordinary co-movement, although §4.1 reports declining specialty/pay revenue and §5.3 reports declining staff. The intended contrast concerns different positions relative to different benchmarks.

   **Fix:** For the survey path, say that revenue lost **less ground than the recalculation implies**. For staff, name the revenue baseline and staff-trend benchmark and describe the contrasting comparisons directly. Avoid using “don’t move together” as their summary.

5. **The pass-through rate appears to change denominator.**

   **Locations:** §2, “75% of their retail revenue loss,” followed by the 86% attribution; §5.1, “75% of the retail loss attributed to Canadian services.”

   As written, §2 sounds like 75% of total retail loss, whereas §5.1 sounds like 75% of the Canadian-attributed portion. A reader cannot tell whether the assumption changed or the wording compressed a two-stage calculation.

   **Fix:** State the calculation’s base explicitly and identically in both places. This is an internal wording conflict; I haven’t adjudicated the underlying report’s intended calculation.

6. **§4.3 cites robustness results before introducing the checks.**

   **Location:** “the 2017 or pooled calibration, the rescaled series or the offset model (1.9, 0.9, 1.9 and 1.8).”

   Every member of that list is premature:

   | Reference in §4.3 | Where its explanation arrives |
   |---|---|
   | “2017 … calibration” | Appendix A and Table A4 |
   | “pooled calibration” | §4.5, then Appendix A |
   | “rescaled series” | Only briefly in Table A8: rescaled to the report’s 2014 |
   | “offset model” | §4.6 |

   The same paragraph uses “the largest calibrated error scale” before identifying the relevant calibration.

   **Fix:** Keep the designated-scale comparison in §4.3. Move the robustness enumeration to the relevant sensitivity discussion, or supply short identifying descriptions and explicit forward references. The rescaled series needs an actual explanation, not just a chronology entry.

7. **The payment comparison invokes a definitional difference without explaining it.**

   **Location:** §5.1, “differ by definition, so their growth is compared, not their levels.”

   That tells readers how the comparison was handled, but not what makes the measures different or why growth is sufficiently comparable. The same unexplained distinction returns in §6 as “a growth comparison of two measures that differ by definition.”

   **Fix:** State what the report’s carriage-fee measure includes and what the CRTC affiliation-payment measure includes, identifying the relevant difference in scope or denominator. One sentence or a short footnote should suffice.

8. **The residual diagnostic requires readers to reconstruct two standardizations.**

   **Location:** §4.6, “the standardized changes … are correlated and have variances below one,” followed by “Divided by their standard deviations under the fit.”

   “Standardized” initially invites the expectation of unit variance. The next sentence then standardizes again. Readers must distinguish properties induced by fitting from the observed diagnostic pattern without being told that distinction directly.

   **Fix:** Name each denominator and separate the consequences of fitting \(k\) from the empirical finding about the 2014–2016 residual. Replace “which absorbs both” later in the subsection with the two differences the offset absorbs.

9. **Float placement creates three interruptions, one of them substantively premature.**

   - **Figure 1, page 6:** interrupts “Tre- / fis” in §3’s calibration explanation and introduces the partial recalculation before §4.3.
   - **Table 1, page 8:** interrupts “Among / the paths tested” in §4.3.
   - **Figure 2, page 9:** interrupts §4.4’s sentence about subscribers falling, before §4.5 introduces the sensitivity discussion.

   **Fix:** Keep Figure 1 after the completed calibration explanation and its first callout. Prefer paragraph-boundary placements for Table 1 and Figure 2. Figure 1’s premature content costs more than the other two ordinary float interruptions.

10. **Two passages answer questions the current exposition hasn’t posed.**

   **Locations:** §4.3, “The recalculations don’t fall to zero”; §5.1, “The CRTC’s wholesale code … is in both of the report’s scenarios.”

   No zero-uptake scenario has been presented, and “recalculations” doesn’t specify whether zero refers to revenue, a shortfall, or \(k^u\). The wholesale code arrives without a gloss or an explanation of why readers should consider it.

   **Fix:** Introduce the first as an explanation of the remaining forecast shortfall when uptake is low. For the second, state the specific alternative explanation being addressed and what the code concerns, or move the detail to a note. Both currently resemble replies to earlier editorial questions whose motivating sentences are absent.

11. **The programming-expenditure heading promises more than its treatment delivers.**

   **Location:** §5.2, “CPE, read only descriptively, stayed at or above the baseline path through 2019.”

   That single sentence is the whole outcome treatment under “Closures and programming expenditure.” No magnitude or direct path reference accompanies it; the appendix tables don’t supply a CPE outcome path.

   **Fix:** Add one concrete comparison and a precise source or replication pointer, or reduce the heading’s promise and present this explicitly as a brief descriptive observation.

12. **Paragraph openings repeatedly substitute pointers for the subject.**

   The inventory below includes locally recoverable references as well as costly ones. The locally clear cases are minor; they aren’t evidence that ordinary anaphora is inherently defective. Quoted excerpts identify the opening sentence.

   | Location and quoted opening | What it should name |
   |---|---|
   | §1: “The number came from an economic-impact study …” | The **15,130-job estimate**. Locally clear. |
   | §1: “That work concerns mainly regulators’ estimates of compliance costs and benefits.” | The **retrospective regulatory-cost literature** just discussed. Locally clear. |
   | §1: “A close precedent is Kane (2026) …” | A precedent for **checking technical forecasts separately from their public presentation**. The paragraph eventually explains this. |
   | §2: “Those figures sit at the end of a chain.” | The **employment and GDP estimates**. |
   | §2.1: “Two of these phrases depart from the report.” | **“Media jobs” and “what now exists.”** |
   | §3: “That last clause is the hard part.” | **Allowing for error in the report’s baseline.** |
   | §3: “The 95% interval for \(k\) comes from generalized least squares under that model …” | The **random-walk model of baseline error**. This reference is immediate and low-cost. |
   | §4.1: “At the designated error scale \(\hat k=0.12\), with a standard error of 0.18.” | **Specialty and pay revenue**, and preferably its 2.2% error scale. |
   | §4.2: “The report took its 15% from outside estimates …” | The **BYOP share assumed from 2018 onward**. |
   | §4.3: “To ask what the report’s chain implies at other uptake levels …” | The **revenue components being recalculated**; see defect 1. |
   | §4.3: “With uptake held at the CRTC’s June 2016 share …” | The opening starts clearly, but its continuation requires the four unnamed checks listed in defect 6. |
   | §4.3: “The recalculations don’t fall to zero …” | The **scenario coefficient or forecast shortfall**, whichever is intended. |
   | §4.4: “Splitting distributors’ revenue into subscribers and revenue per subscriber locates their shortfall.” | Their **shortfall relative to the report’s baseline**, rather than relative to its reform path. |
   | §4.4: “The comparison is of changes from 2014 …” | The **observed and forecast subscriber/per-subscriber revenue paths**. |
   | §4.4: “By 2019, measured this way, subscribers had fallen a further 3.9% below the report’s baseline path, against 1.5% in its reform scenario.” | **The change in the subscriber gap since 2014**. “Further” adds another unnecessary reference to resolve. |
   | §4.4: “The split was added after the outcome data was opened …” | The **subscriber/per-subscriber revenue decomposition**. |
   | §4.5: “Both intervals depend on the error scale (figure 2).” | The **two revenue-series intervals for \(k\)**. |
   | §4.6: “A check of the statistical error model … finds the specialty and pay residual concentrated in its first step.” | The **2014–2016 step**, rather than making readers infer which observation interval is first. |
   | §4.6: “Part of the specialty and pay gap is already visible in 2015 …” | The **gap between observed revenue and the report’s baseline forecast**. |
   | §5.3: “For two sectors, the CRTC’s staff counts allow a descriptive comparison with the last link, from revenue to jobs …” | **Specialty/pay services and distributors**. |
   | §6: “Three other links can be read without assuming later uptake.” | **Payments, closures, and staff counts**. |
   | §6: “Judged against the report rather than against outcomes, Morrison’s summary to the committee departed from the report in three identifiable respects.” | The **employment label, expenditure denominator, and connection to the uptake condition**. The next sentence supplies them, so the cost is small. |
   | §6: “The report deserves credit for what made this check possible.” | Its **published assumptions and annual scenario paths**. |
   | Table A8: “That split; corrected residual check; coverage check …” | The **subscriber/per-subscriber revenue decomposition**. |

   Appendix A’s “With \(\Sigma\) that covariance matrix” is an immediate reference to the displayed covariance formula and presents no comparable reading problem.

13. **Repeated summaries crowd out the progression of the argument.**

   These are the recurring points made more than twice. Repetition in an abstract, introduction, and conclusion is often justified; the extra repetition within the body or successive concluding paragraphs creates the avoidable cost.

   | Repeated point | All substantive locations | Proposed treatment |
   |---|---|---|
   | Specialty/pay revenue is the main employment-related test and gives the smaller verdict | Abstract; §1 results paragraph; §2’s employment-share rationale; §4.1; §6 opening | Keep the rationale in §2 and evidence in §4.1; shorten the surrounding previews. |
   | Distributors’ revenue is consistent with the forecast | Abstract; §1; §4.1; §6 opening | Normal summary repetition; no additional restatement is needed. |
   | Mid-2016 uptake was far below the report’s assumption | Abstract; §1; §4.2’s evidence and closing comparison; §6 uptake paragraph; §6.1’s final inventory | Remove the second concluding restatement in §6.1. |
   | Only one tested low/rising uptake path accommodates both series at the designated scales | §1; §4.3; §6 uptake paragraph; displayed again in Tables 1 and A3 | Retain the table detail; avoid repeating the standard-error inventory in §6. |
   | The survey is outside the plan’s accepted sources | Abstract; §1; §4.2; §4.3; Table 1; §6; Table A3; Table A5; Table A8 | Explain fully in §4.2. Retain necessary table notes, but shorten repeated prose qualifications. |
   | The analysis doesn’t estimate the policy’s causal effect or test total employment | Abstract; §1; §3’s causal qualification; §5.3’s employment qualification; §6 opening and staff summary | Preserve the initial scope statement and the locally necessary methodological qualifications. Compress the conclusion. |
   | Testimony mislabels employment, changes the expenditure denominator, and fails to connect uptake to the headline | Abstract, partially; §1; §2.1; §6 testimony paragraph; §6.1 final clause; expenditure point also in Table A1 | Let §2.1 establish the differences and §6 interpret them. Delete the further inventory in §6.1. |
   | Intervals condition on a known error scale | §3; Figure 2 caption; §6.1; Appendix A; Table A4 | Mostly justified repetition because displays must stand alone; shorten rather than remove indiscriminately. |
   | Prediction/design choices preceded outcome inspection | Abstract; §1; §3; Appendix A’s design analysis; Data and code; Table A8 | Keep the chronology in Table A8 and the operative methodological statement in §3; compress other repetitions. |

   The abstract and introduction also carry too many of these qualifications before readers understand the comparison. A brief gloss of “error scale” as the **assumed size of baseline-forecast error** would help more than another result detail.

14. **Several specialist terms, acronyms, and labels remain unexplained or unused.**

   The remaining inventory is:

   | Item and locations | Defect and proposed fix |
   |---|---|
   | **“Specialty and pay services”**: first in §1; **“discretionary and on-demand services”** in Table A6 | Define the relevant service grouping and explain whether the later label denotes the same scope. |
   | **“Category A and B”**: §§2, 5.2 | Give a short explanation of these regulatory categories and their role in the closure denominator. |
   | **“Integrated,” “independents”**: §2; §§5.1–5.2; §6 closure summary | State the ownership criterion. Explain why Corus is shown under both classifications. |
   | **“Exempt services”**: Figure 1; Table A2; Table A6; Table A8 | Identify the licensing exemption and distinguish it from the streaming exemption order. |
   | **“Cord cutting” / “cord shaving”**: §4.3; §4.4; Table A5 | Gloss at first substantive use. “Cord shaving to smaller packages” arrives only at the end of §4.4. |
   | **“Skinny-basic,” “starter,” “entry-level”**: §4.2, with starter-package language already in §1 | Establish the naming relationship while retaining the important difference between package adoption and BYOP uptake. |
   | **IPTV**: §1 and Table A6 | Expand at first use. |
   | **ACTRA**: §2 and References | Expand or give a short identifying description. |
   | **CBC/SRC, CMF, PPV, VOD**: Table A1 | Supply a table note expanding them. CBC/SRC occurs in the denominator rows and component C; the others occur in components A and F. |
   | **MTM**: Table A8 | Use “Media Technology Monitor,” already introduced in §4.2, or explicitly connect the acronym to it. |
   | **“Lead case,” “splice rule,” “reading rule 6,” “multiverse”**: Table A8 | Replace internal project labels with descriptions that identify the choice being recorded, or provide an exact plan reference. |
   | **\(\delta_t\)**: §3 | Define it explicitly as \(\log B_t-\log(B_t-I_t)\), not just “forecast shortfall.” |
   | **\(\delta^u\)**: Appendix A and Table A3 | Explicitly identify the recalculated log-shortfall vector before using it in the projection. |
   | **ARPU**: Table A5 | Expanded but never reused. Remove the acronym or use it as the relevant column label. |
   | **E, N1, N2**: Table A1 | The quantities are useful; these symbolic labels aren’t subsequently used. Remove the unused labels unless they serve a stated cross-reference. |
   | **“Inputs to \(k\), in $ millions”**: Table A2 | Restrict the units statement to monetary rows; the log quantities and coefficients are dimensionless. |
   | **Appendix B containing Tables A1–A8** | Align appendix/table numbering or explain the convention. |

Beyond these, I found no abandoned central symbol, missing numbered section, or wholly unfulfilled principal table reference. The repair is primarily to introduce the existing machinery in the order readers need it, then make the summaries preserve the distinctions the method already establishes.
