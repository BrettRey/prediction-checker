<!-- Saved verbatim by the parent session (Claude Opus 5.5) from codex-stdout.txt (gpt-6-astra, xhigh, read-only); see statistical-inference-audit-2026-10-03/MANIFEST.md. -->

**Model: GPT-6 (Codex).**

**1. Verdict**

**The arithmetic largely survives; the inference needs major revision.** The GLS calculations correctly account for the stipulated serial dependence. They produce valid conditional intervals **if** the Gaussian log-error model and its fixed error scale are correct. They do not establish 95% coverage for the actual procedure, which obtains its scale from extremely limited calibration data and assumes that those data describe Canadian television forecast errors. The design simulation also uses a materially different outcome model: applying the paper’s intervals to its simulated forecast-effect world gives approximately **87.1% coverage for channels and 92.7% for distributors**, despite nominal coverage of 95%.

The channel result can remain a qualified comparison with the published forecast paths. The distributors’ “2.1 standard errors” result cannot support the proposed inference about the source of their losses. The employment comparisons likewise cannot identify a failed causal mechanism. The descriptive observations, reconstructed scenarios, and documentary criticism of the testimony remain useful.

Everything below concerns commit `3046dc3`. No files were changed.

**2. Claim-by-claim audit**

Locations marked **T** refer to lines in the [rendered manuscript](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/notes/passes/statistical-inference-audit-2026-10-03/main.txt). Repeated occurrences of the same claim are grouped.

For the revenue calculations, the dependence unit is **one four-year revenue trajectory**, not four independent annual observations. “Conditional 95%” below means a marginal interval under the stipulated Gaussian random walk, treating its scale, forecast paths, and definitions as fixed. It does **not** mean that the calibration procedure has demonstrated 95% coverage.

**The 18 intervals and verdicts in Table A4**

Every interval and printed classification below reproduces. Each receives **valid with caveat** as a conditional calculation. Their interpretation as empirically calibrated 95% confidence intervals is unsupported.

| Location | Series; calibration | Reported interval | Quoted verdict | Audit |
|---|---|---:|---|---|
| T:720 | Channels; historical only | [−0.23, 0.46] | “smaller” | Valid with caveat |
| T:720 | Distributors; historical only | [0.49, 2.11] | “consistent” | Valid with caveat |
| T:721 | Channels; 2016 | [−0.57, 0.81] | “inconclusive” | Valid with caveat |
| T:721 | Distributors; 2016 | [−0.59, 3.20] | “inconclusive” | Valid with caveat |
| T:722 | Channels; 2017 | [−0.23, 0.46] | “smaller” | Valid with caveat |
| T:722 | Distributors; 2017 | [0.39, 2.22] | “consistent” | Valid with caveat |
| T:723; also T:83, 216–220 | Channels; **pre-stated 2018** | [−0.23, 0.46] | “smaller” | Valid with caveat |
| T:723; also T:91, 300–302 | Distributors; **pre-stated 2018** | [0.49, 2.11] | “consistent” | Valid with caveat |
| T:724 | Channels; pooled 2016–2018 | [−0.61, 0.85] | “inconclusive” | Valid with caveat |
| T:724 | Distributors; pooled 2016–2018 | [−0.70, 3.30] | “inconclusive” | Valid with caveat |
| T:725 | Channels; growth 2015–2016 | [−0.23, 0.46] | “smaller” | Valid with caveat |
| T:725 | Distributors; growth 2015–2016 | [0.49, 2.11] | “consistent” | Valid with caveat |
| T:726 | Channels; growth 2015–2017 | [−0.23, 0.46] | “smaller” | Valid with caveat |
| T:726 | Distributors; growth 2015–2017 | [0.49, 2.11] | “consistent” | Valid with caveat |
| T:727 | Channels; growth 2015–2018 | [−0.54, 0.78] | “inconclusive” | Valid with caveat |
| T:727 | Distributors; growth 2015–2018 | [−0.50, 3.11] | “inconclusive” | Valid with caveat |
| T:728 | Channels; growth pooled | [−0.51, 0.74] | “smaller” | Valid with caveat; borderline and changes with series version |
| T:728 | Distributors; growth pooled | [−0.41, 3.02] | “inconclusive” | Valid with caveat |

For all rows, use **“conditional 95% interval, holding the assumed annual error scale fixed.”** Replace the classifications with their operational meanings:

- “Smaller”: “At this assumed error scale, the interval lies below the projected cited-input band.”
- “Consistent”: “The interval includes the published forecast’s \(k=1\); this does not establish forecast accuracy.”
- “Inconclusive”: “The interval includes both zero and the lower endpoint of the projected band.”

An important distinction: **all nine channel intervals exclude \(k=1\)**, but three overlap the cited-input band. “Inconclusive” is therefore the paper’s particular band-based classification, not a statement that the published point forecast falls inside those intervals. At the pre-planned 8% scale, \(k=1\) does fall inside the channel interval.

**The 12 scenario comparisons in Table A3**

These use the same two conditional intervals, not 12 independently estimated intervals. All scenario calculations and inside/outside labels reproduce. The dependence unit remains the relevant four-year trajectory; the comparison level is the marginal conditional 95% interval.

| Location | Series; uptake scenario | Scenario \(k\) | Quoted label; distance in SEs | Audit and consequence |
|---|---|---:|---|---|
| T:286–287, 688 | Channels; flat counted uptake | 0.334643 | “inside”; 1.230 | **Valid with caveat:** the projected scenario is not excluded; the mechanism is not confirmed. |
| T:288, 689 | Channels; flat 4% | 0.396412 | “inside”; 1.580 | **Valid with caveat:** same qualification. |
| T:289, 690 | Channels; flat 10% | 0.559734 | “above”; 2.506 | **Valid with caveat:** exclusion depends on the fixed scale and chosen model. |
| T:691 | Channels; report’s ramp | 1.000000 | “above”; 5.001 | **Valid with caveat:** this repeats the published-forecast comparison. |
| T:290, 692 | Channels; rise to 4% | 0.432970 | “inside”; 1.788 | **Valid with caveat:** a hypothetical uptake path, not observed uptake. |
| T:290, 694 | Channels; rise to 10% | 0.687787 | “above”; 3.232 | **Valid with caveat:** conditional exclusion of this projection only. |
| T:302–304, 688 | Distributors; flat counted uptake | 0.434936 | “below”; 2.102 | **Valid with caveat** as arithmetic; **overstated** when used to infer the source of losses. |
| T:689 | Distributors; flat 4% | 0.481065 | “below”; 1.991 | **Valid with caveat:** exceptionally marginal; do not narrate as substantive rejection. |
| T:690 | Distributors; flat 10% | 0.598165 | “inside”; 1.707 | **Valid with caveat:** not excluded by this interval. |
| T:691 | Distributors; report’s ramp | 1.000000 | “inside”; 0.734 | **Valid with caveat:** repeats the published-forecast comparison. |
| T:692 | Distributors; rise to 4% | 0.519024 | “inside”; 1.899 | **Valid with caveat:** modest change in assumed uptake removes the exclusion. |
| T:694 | Distributors; rise to 10% | 0.731471 | “inside”; 1.384 | **Valid with caveat:** not excluded by this interval. |

Suggested caption: **“Exploratory comparisons of scenario projections with conditional intervals. Uptake after June 2016 is assumed. Inclusion does not validate the scenario’s full trajectory or mechanism.”**

**Other reported statistical and inferential claims**

| Location and quoted phrase | Dependence unit; level used | Verdict | Consequence and suggested wording |
|---|---|---|---|
| T:77–78, 186–191: “shortfall … as a multiple of its forecast impact”; “\(k=0\) is no effect” | Four-year trajectory; GLS coefficient | **Valid with caveat** | \(k\) is a coefficient on a **log-shortfall shape**, not a dollar-loss ratio or identified causal effect. Say “\(k=0\) corresponds to the report’s baseline path under the error model.” |
| T:193–197, 565–568: “95% interval”; “no degrees-of-freedom correction” | Four-year trajectory plus external/historical calibration; normal critical value | **Valid with caveat** conditionally; **overstated** as coverage of the actual procedure | State explicitly that neither calibration uncertainty nor uncertainty about transferring its scale to television revenues is included. |
| T:200–202, 569–571: inputs “define a band … consistent with their forecast” | Deterministic scenario paths; no probability level | **Valid with caveat** | This is a projected sensitivity band, not a confidence or predictive interval. Its uptake scaling preserves the report’s ramp; it is not flat 10–35% uptake each year. |
| T:17–19: “inconsistent with the forecast as made but consistent with … actual uptake” | Two trajectories; conditional intervals summarized without qualifications | **Overstated** | Replace with: “At the designated error scale, channel revenue rejects the published path but does not exclude an exploratory scenario holding uptake at its June 2016 level.” |
| T:216–217: “0.7 standard errors from no effect” | Channel trajectory; fixed-scale standardized distance | **Valid with caveat** | Correct distance, 0.666. Say “from the baseline-path value \(k=0\), using the conditional standard error.” This is not evidence of no policy effect. |
| T:217: “5.0 from the forecast” | Channel trajectory; same level | **Valid with caveat** | Correct, 5.001. It is not a calibrated five-sigma finding once scale/model uncertainty is admitted. |
| T:217–219: lower band endpoint “3.6 standard errors away” | Channel trajectory; same level | **Valid with caveat** | Correct, 3.585. Retain only with the fixed-scale qualification. |
| T:300: “3.2 standard errors from no effect” | Distributor trajectory; same level | **Valid with caveat** | Correct, 3.156. Evidence excluding zero does not survive the wider calibrations or an illustrative historical-scale uncertainty calculation. |
| T:300: “0.7 from the forecast” | Distributor trajectory; same level | **Valid with caveat** | Correct, 0.734. Small distance does not confirm the forecast. |
| T:92–95, 303–304, 404–405: “some … loss came from outside the model’s unbundling channel” | Distributor trajectory; post hoc scenario comparison | **Overstated** | The 2.102-SE discrepancy disappears under reported sensitivities and cannot allocate causes. Say: “The point estimate exceeds the flat-uptake scenario, but that discrepancy is sensitive to the error scale and treatment of level differences.” |
| T:182–184: channels “classified correctly … about 99%” | Independent simulated trajectories, serial dependence within each; no 5% test level | **Valid with caveat** | Reproduces as 98.78%, the smaller world-specific rate. Describe as classifier performance under the simulator, not power or interval coverage. |
| T:184: distributors “about 86%” | Same simulation unit | **Valid with caveat** | Reproduces as 86.12%; same qualification. |
| T:185: CPE “63% … set aside … as descriptive” | Same simulation unit | **Valid with caveat** | Reproduces as 63.00%. The pre-outcome decision is defensible; “low discrimination under this design” is more precise than “cannot test.” |
| T:576–579: \(y_t=\delta_t+e_t\) “up to a term of order” | Simulated trajectory; approximate model equivalence | **Overstated** | The expression is algebraically correct, but the approximation is inadequate for nominal coverage. State the different models and report the coverage discrepancy. |
| T:253–254, Figure 1: channels’ “95% range” | Individual year within a serial trajectory; marginal prediction range | **Valid with caveat** | Label “pointwise conditional 95% range.” It is not a simultaneous band for the trajectory. |
| T:253–254, Figure 1: distributors’ “95% range” | Same | **Valid with caveat** | Same correction. |
| T:280–284, Figure 2: channel interval “widens linearly” | Channel trajectory; intervals indexed by assumed scale | **Valid with caveat** | The linearity is exact for this covariance family. The figure does not propagate scale uncertainty. |
| T:280–284, Figure 2: distributor interval “widens linearly” | Distributor trajectory; same | **Valid with caveat** | Same qualification. |
| T:310–311: channel interval reaches band at “about 4.0%” | Channel trajectory; conditional 95% threshold | **Valid** as conditional arithmetic | Exact threshold is 4.04885% using the derived inputs. It is not an estimated upper bound on plausible error. |
| T:311–312: distributor interval includes zero at “about 3.0%” | Distributor trajectory; conditional 95% threshold | **Valid** as conditional arithmetic | Exact threshold is 3.04417%. Same qualification. |
| T:312: “No interval … excludes zero at any calibration” | Channel trajectory; nine correlated sensitivity calculations | **Valid with caveat** | Correct for the displayed calibrations. It neither establishes zero effect nor supplies nine independent pieces of evidence. |
| T:324–327: fitted residual changes “independent standard normal draws” | Four fitted residual changes; assumed \(N(0,1)\) reference | **Invalid** | Fitting \(k\) makes these residuals correlated and reduces their variances. Replace with the fitted-residual distribution or compare with simulations that refit \(k\). |
| T:327–329: residual pattern could be “a one-time gap” | One fitted trajectory; informal diagnostic | **Valid with caveat** | A possible description, not evidence selecting an offset model. With four points it cannot establish the covariance model. |
| T:337–339: channel offset estimate “0.20 (standard error 0.18)” | Four-year trajectory; post hoc two-parameter GLS | **Valid with caveat** | Reproduces. Its conditional interval is approximately [−0.156, 0.562]; scale and specification uncertainty remain omitted. |
| T:338–339: distributor offset estimate “1.23 (0.44)” | Same | **Valid with caveat** | Reproduces. Its conditional interval is approximately [0.368, 2.090]. |
| T:339: offset model leaves “both readings as they were” | Two trajectories; comparison across specifications | **Overstated** unless restricted to the original band verdicts | The original band verdicts persist. The counted-uptake exclusion for distributors does **not**. Say exactly which readings remain unchanged. |
| T:330–337: 2015 channel gap and standing distributor difference | Administrative series across editions; descriptive comparison | **Valid with caveat** | The comparisons reproduce. They support a level-comparability concern, not a diagnosis of every component of forecast error. |
| T:14–16, 79–82, 342–350, 396–398: “largest error”; “decisive”; uptake condition “didn’t hold” | Subscriber counts at two dates, annual forecast assumptions; no interval | **Overstated** | Mid-2016 uptake is below the report’s 2016 assumption. Later uptake is unknown, and “largest” is not established by a common error measure. Say “The available mid-2016 count was substantially below the assumed annual share.” |
| T:222, 286: scenarios show “how much … the failed input accounts for” | Reconstructed paths; deterministic sensitivity | **Overstated** | A scenario does not identify the actual contribution of an input error. Say “The scenarios show how the projected coefficient changes when uptake assumptions are changed.” |
| T:424–425: “channel losses of about 0.40 of the forecast” | Deterministic scenario projected onto the four-year shape | **Invalid** as a dollar-loss ratio | \(k=0.396\) is not that ratio. At flat 4% uptake, reconstructed 2019 channel losses are approximately **50.6%** of the original impact. Say “a projected coefficient \(k=0.40\).” |
| T:97–98, 356–361: payments per subscriber rose “10.5% … against 1.6%” | Two endpoints of aggregate payment/subscriber series; descriptive | **Valid with caveat** | Arithmetic reproduces. No sampling interval is necessary for the observed change; comparability of definitions remains necessary. |
| T:359: Canadian share “stayed near 87.8%” | Aggregate annual payment shares; descriptive | **Valid** | It is 87.82% in 2015 and 87.30% in 2019. “Near” is acceptable here as a descriptive approximation. |
| T:98, 362–364: “baseline fee path was too pessimistic” | Observed payment growth compared with an unobserved no-reform path; no interval | **Overstated** as attribution | Say “Observed aggregate payments per subscriber grew faster than the report’s baseline fee assumption.” This does not identify the true no-reform fee path. |
| T:448: aggregates show “pass-through didn’t appear” | Linked distributor/channel financial flows; no causal model or interval | **Overstated** | Aggregate increases can coexist with negative pass-through relative to a higher counterfactual. Say “The aggregates cannot identify the assumed pass-through rate.” |
| T:370–371: integrated closures “8%–11% … close” | Finite set of services; missing-status bounds, not confidence limits | **Valid with caveat** | Bounds reproduce; this is descriptive proximity, not validation of reform-induced closures. |
| T:372–373: independent closures “6%–33% … too wide to test” | Same | **Valid with caveat** | Correct: the bounds do not discriminate against 25%. |
| T:375–376: Corus-integrated bounds “6%–11%” | Same, alternative ownership coding | **Valid with caveat** | Correct descriptive bounds. |
| T:376: Corus-independent bounds “7%–44%” | Same | **Valid with caveat** | Correct; again inconclusive about the forecast. |
| T:376–377: CPE “stayed at or above the baseline” | Annual administrative aggregates; descriptive | **Valid** | Reproduces; no interval is required for the observed path comparison. |
| T:382–383: channel staff “1,282 below the trend” against 800 forecast FTEs | One serial staff series; extrapolated four-point trend, no interval | **Valid with caveat** descriptively | Numbers reproduce. State that the trend and staff counts do not supply the forecast’s employment counterfactual or units. |
| T:383–386: distributors “396 below … 1,834 above” trend; possible discontinuity | One serial staff series; same | **Valid with caveat** | Numbers reproduce. “Near trend” is not a demonstrated equivalence result; retain the actual deviations. The discontinuity is a hypothesis. |
| T:20–21, 99–101, 387–393: staffing “doesn’t track” the revenue chain | Two related revenue/staff trajectories; no inferential level | **Valid with caveat** only as descriptive juxtaposition | Prefer “Staff counts and revenue did not move together in the simple way illustrated by the model.” |
| T:414–418: employment fell “but not by the route the model describes” | Linked revenue/employment mechanisms; no identifying design | **Invalid** as causal inference | Remove. “These unlike measures do not permit a test of the predicted employment mechanism.” |
| T:407–413: 10,060 FTEs, “66%,” depend on channel revenue/spending | Accounting within the original model; no sampling level | **Valid** | This is a decomposition of the report’s forecast, not evidence that 66% of its job prediction has been falsified. |
| T:155–160, Table A1: stated 18% does not reproduce | Arithmetic identities; no dependence or sampling issue | **Valid** within the enumerated denominators | No interval is needed. Keep the bounded claim about the denominators actually reconstructed. |
| T:420–429: public argument “failed outright” | Documentary comparison; no statistical test | **Valid with caveat** | It can describe the testimony’s representation of the report. It must not imply that this study has tested and rejected the 2020 causal job-loss total. |

**3. Findings on checks 1–8**

**Check 1 — Dependence unit**

The code uses the appropriate covariance **for the random walk it stipulates**:

\[
\Sigma=\sigma^2 C,\qquad
C=
\begin{pmatrix}
2&2&2&2\\
2&3&3&3\\
2&3&4&4\\
2&3&4&5
\end{pmatrix}.
\]

Thus it does not make the basic mistake of treating four revenue observations as independent. See [GLS implementation](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/scripts/crtc_outcomes_lttv.py:111).

An equivalent analysis uses the initial two-year change divided by \(\sqrt2\), followed by three annual differences. This makes clear what is assumed: independent Gaussian innovations, constant innovation variance, no systematic drift in forecast error, and a fixed starting point.

A random walk is a defensible **sensitivity model** for accumulating forecast error. It is not established as the actual error process. A persistent level mismatch, deterministic forecast bias, correlated innovations, or a structural change can produce different uncertainty. The acknowledged 2014/2015 level differences directly challenge the zero-offset starting assumption.

Cross-series correlation is not needed for separate marginal GLS estimates. The manuscript does not report a formal pooled revenue test. It **would** be needed for an inferential contrast between sectors, a joint confidence claim, or a test that losses passed from distributors to channels. Payments and revenues share accounting flows and market shocks; they are not independent replications of a mechanism. In particular, rejection for one series and non-rejection for another does not itself establish a difference between their mechanisms.

**Check 2 — Four observations**

Four observations cannot usefully establish normality, innovation independence, constant variance, absence of drift, the starting-point assumption, or stability of the forecast-impact shape. The \(k\)-only fit leaves three residual dimensions; the offset fit leaves two.

The paper **does explicitly disclose** fixed calibration, the normal critical value, and absence of a degrees-of-freedom correction: T:193–197 and 565–568. This is a strength. With genuinely known covariance and the exact Gaussian model, a normal interval is valid even with four points. The problem is treating the estimated calibration as known, not a universal requirement to use \(t_3\) whenever \(n=4\).

The residual diagnostic contains a separate mathematical error. If \(T'T=C^{-1}\), \(x=T\delta\), and

\[
H=\frac{xx'}{x'x},
\]

then the fitted standardized residual changes satisfy

\[
z=T(y-\hat k\delta)/\sigma,\qquad
\operatorname{Cov}(z)=I-H.
\]

They are neither independent nor individually standard normal. For channels their variances are approximately

\[
(0.9234,\ 0.6331,\ 0.4812,\ 0.9623).
\]

This contradicts T:325 and [model-check script lines 5–8](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/scripts/model_check_lttv.py:5). Simulations used to assess that residual pattern must refit \(k\) on every simulated trajectory.

**Check 3 — Two-step uncertainty**

The primary intervals are actually determined by the **historical floors**, not the 2018 Netflix error:

- Channels: historical scale 2.21390%; Netflix scale 1.28681%.
- Distributors: historical scale 1.89080%; Netflix scale 1.28681%.

Those historical scales are sample standard deviations of **four annual growth changes**, with only three variance degrees of freedom. Moreover, historical revenue-growth variability is not itself a sample of errors in the report’s no-reform forecast. Netflix subscriber forecast errors are another different quantity. The paper offers a relevance argument for these calibrations, but no statistical model connecting their variances to the required revenue-error variances.

**The amount of uncertainty omitted cannot be uniquely estimated from these data.** Illustrative calculations show why it cannot be dismissed:

- If the four historical changes were independent normal draws with the required variance, their conventional 95% scale intervals would be approximately **1.25–8.25%** for channels and **1.07–7.05%** for distributors.
- If the single Netflix endpoint were genuinely one normal random-walk observation with the required variance, its scale interval would be approximately **0.57–41.06%**.
- The three-increment pooled Netflix calculation would give approximately **2.65–17.42%**.

These are illustrations under stronger assumptions, **not recommended replacement intervals**. They use the normal/chi-square relationship for variance estimation. [NIST’s standard-deviation confidence-limit formula](https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/sdconfli.htm)

Likewise, under an idealized independent historical variance estimate with three degrees of freedom, replacing 1.96 by \(t_{.975,3}=3.18245\) widens intervals by 62.4%:

| Series | Illustrative interval incorporating that variance-estimation uncertainty |
|---|---:|
| Channels | [−0.444, 0.679] |
| Distributors | [−0.011, 2.617] |

This is not the exact distribution of the paper’s maximum-of-calibrations rule. It demonstrates that fixing a noisy scale is consequential. Under this illustration, the distributor’s exclusion of zero disappears.

The nine calibrations and Figure 2 are useful sensitivity reporting. They are **not uncertainty propagation**: they provide no probability distribution, confidence set, or coverage guarantee for \(\sigma\), and cannot establish that plausible scales stop at 4.7%.

Chart-label rounding is a smaller issue for the principal calculations. But \(B\), \(I\), and the scenario band share reconstructed components, so their errors would be correlated if treated as uncertain. The cited-input band also lacks a probability interpretation. The paper should distinguish numerical rounding from uncertainty in the reconstruction, component-scaling assumptions, and unknown later uptake. Reproducing printed numbers does not settle these latter uncertainties.

**Check 4 — Simulation and classification**

I independently reproduced all **72 design-analysis rows**, using the stated seed and random-number consumption. All four reported classification rates in every row match at the CSV’s precision.

The classification rule is equivalent to choosing the forecast world when \(\hat k>0.5\). It is a legitimate decision rule. Reporting the smaller of its two world-specific success rates is a transparent conservative summary of classification performance. It is neither overall accuracy under a specified prevalence nor power at a 5% significance level. For example, the historical distributor calculation misclassifies about 11% of no-effect worlds as forecast-effect worlds.

The sign correction is harmless: a mean-zero Gaussian random walk has the same distribution after sign reversal.

**The additive-impact discrepancy is not harmless.** The estimation model implies

\[
Y_t=B_t\exp(-k\delta_t-e_t),
\]

and therefore, at \(k=1\),

\[
Y_t=(B_t-I_t)\exp(-e_t).
\]

The design simulator instead generates

\[
Y_t=B_t\exp(-e_t)-I_t.
\]

Writing \(r_t=I_t/B_t\), its log shortfall expands as

\[
y_t=\delta_t+\frac{e_t}{1-r_t}+O(e_t^2).
\]

The leading error is therefore multiplied by \(1/(1-r_t)\), which varies over time. For channels it reaches **1.271** in 2019. The induced error covariance is not the covariance used in the fit.

Applying the paper’s intervals to its own historical-scale forecast-effect simulations gives:

| Series | Nominal coverage | Actual simulated inclusion of \(k=1\) | Monte Carlo SE |
|---|---:|---:|---:|
| Channels | 95% | **87.085%** | about 0.24 percentage points |
| Distributors | 95% | **92.710%** | about 0.18 percentage points |

A first-order calculation independently gives approximately 86.8% and 92.5%, respectively. The corresponding standard errors are about **30.1% and 10.0% larger** than the fitted model’s standard errors.

These are checks of the paper’s interpretation of \(k=1\) as the published additive impact. They demonstrate the incompatibility between that simulator and the nominal interval claim. The paper must select and state a coherent model; fixing only the prose sign convention is insufficient.

There is no resampling analysis here. Bootstrapping the four annual observations independently would be inappropriate and would not solve the calibration problem.

**Check 5 — Multiplicity**

The actual analysis inventory is larger than “two series × nine calibrations × two versions”:

- Table A4 contains **18 displayed interval/verdict pairs**.
- The multiverse CSV contains **45**: three channel versions and two distributor versions, each at nine calibrations.
- The fixed-scale grid contains another **20 rows**, reusing the same trajectories.
- Table A3 contains **12 scenario comparisons**, including two repetitions of the published-forecast comparison.
- There are **two offset fits**, fitted-residual diagnostics, and multiple staffing, payment, uptake, and closure comparisons.
- The prose also compares estimates with zero, one, and band endpoints.

These are **not independent tests**, and mechanically applying a correction for every printed number would be wrong. In particular, one confidence interval can be compared with several fixed scalar reference values without treating each comparison as an independent experiment. Many calibration rows also give identical intervals.

The concern is the selection of a substantive story from these dependent comparisons. The post hoc distributor scenario exclusion is prominently interpreted while its disappearance under already reported alternatives is not given equal prominence. As a simple diagnostic, even a two-series Bonferroni critical value of 2.241 exceeds 2.102. This is not a proposed universal correction; it underscores how little margin that claim has.

The plan identifies channels as the primary model-level test and distributors as secondary ([analysis plan, lines 35–42](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/notes/analysis-plan.md:35)). The manuscript should retain that hierarchy and explicitly call the scenario/mechanism comparisons exploratory.

**Check 6 — Post-selection and chronology**

The chronology is mostly candid and corroborated by the commit order. Several distinctions need sharpening.

| Choice | Actual status and evidence | Consequence |
|---|---|---|
| Years, GLS coefficient, covariance, band rules, 2018 Netflix rule | Fixed before revenue outcomes; commit `66f9c25` | Legitimately pre-stated, but preregistration does not validate assumptions. |
| Exempt-services subtraction | Post hoc; `DECISIONS.md:100`, Table A7 | A reasonable attempt to address a discovered definition break. Alternate-series results should remain visible. It does not drive the main channel result. |
| Rescaling to the report’s 2014 level despite passing the splice rule | Post hoc; `DECISIONS.md:104` | Relevant sensitivity, particularly because it removes the distributor counted-uptake exclusion. Not individually identified in Table A7. |
| Other level calibrations and pooled calibration | Post hoc; `DECISIONS.md:114` | Properly shown as alternatives. They do not constitute replicated evidence. |
| Growth calibrations | Post hoc; `DECISIONS.md:118` | Properly disclosed, motivated by a discovered starting offset. |
| Flat uptake scenarios, corrected scaling, rising paths | Post hoc; `DECISIONS.md:152–160`, Table A7 | Disclosure is adequate in the body. “Actual uptake” in the abstract is not adequate because later uptake is assumed. |
| Payment observable and per-subscriber fee comparison | Post hoc; `DECISIONS.md:102,116,152` | Descriptive exploration; cannot identify a pass-through parameter. |
| Employment check | General rule pre-stated; `analysis-plan.md:42` | The **specific 2012–2015 straight-line comparator was not pre-stated**. Table A7’s “pre-stated rule” must not imply otherwise. |
| Offset model and residual check | Post hoc; `DECISIONS.md:172`, Table A7 | Properly identified; interpretation and residual reference distribution need correction. |
| Distances in SEs | Added after outcomes; `DECISIONS.md:174` | Mostly a re-expression of existing comparisons, not independently new tests. It does not rehabilitate the exploratory 2.1-SE claim. |
| Real changes | Post hoc descriptive; `DECISIONS.md:170` | No statistical-selection problem if retained as descriptive accounting. |

The pre-stated plan required sensitivity over **1–8% annual error**. The repository supplies selected grid values through 8%, but Figure 2 stops at 5% and Table A4 stops at the largest selected calibration, 4.7%. Restore the 8% extent or explain this reporting restriction. It matters because the channel interval then includes the published \(k=1\) forecast.

**Check 7 — Distances in standard errors**

“Standard errors” is the correct denominator **for a fixed scalar comparator**:

\[
z_u=\frac{\hat k-k_u}{\operatorname{SE}(\hat k)}.
\]

A scenario does not need its own sampling SE merely because it is compared with an estimate. Adding a second SE mechanically would be wrong.

The limitations are instead that the denominator is conditional, the scenario’s assumptions are uncertain, and \(k_u\) is only a projection of a potentially different-shaped trajectory.

For distributors at counted uptake:

- Main specification: **2.102 SEs**.
- With the 2017 calibration: **1.858 SEs**.
- With pooled calibration: **0.851 SEs**.
- With the reported 2014-rescaled series: **1.925 SEs**.
- With the offset model, projecting the scenario in that same model: approximately **1.83 SEs**.
- The scenario enters the main interval at \(\sigma=2.02809\%\), only about **7.3% above** the designated 1.89080% scale.

Thus the discrepancy does not survive straightforward reported sensitivities. Even a stable discrepancy would show a mismatch with the assumed scenario, not identify whether its cause was streaming, baseline bias, uptake after 2016, a misspecified component, or another mechanism.

The corresponding causal sentence should be removed, not defended by repeating “may.”

**Check 8 — Arithmetic**

The principal arithmetic is sound:

- All **45 multiverse intervals and verdicts** reproduce.
- All **20 fixed-grid estimates, bands, intervals, and verdicts** reproduce.
- All **12 scenario projections and interval classifications** reproduce.
- All **72 simulation rows** reproduce.
- Offset fits, employment summaries, fee growth, and closure bounds reproduce.

Small differences in the fifth decimal of \(k\) arise because the outcome CSV rounds revenues to $0.1 million while the main script initially uses workbook precision.

There are three minor reproducibility issues:

1. `crtc_lttv_cutoffs.csv` stores first-crossing grid values, **4.1% and 3.1%**, rather than exact cutoffs. The manuscript’s “about 4.0%” and “about 3.0%” are correct.
2. The offset script reads rounded \(\sigma\), producing slightly different SEs from a calculation using the full historical standard deviation. This does not change displayed conclusions.
3. `uptake_conditional_paths_lttv.csv` incorrectly labels the report-assumption uptake as **0.15 in 2016 and 2017**. Its impacts correctly retain the 5/10/15/15 ramp, and Table A3 prints the correct ramp. The error is in the CSV metadata, caused by [lines 261–272](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/scripts/crtc_outcomes_lttv.py:261).

**4. Recomputations**

These calculations were implemented independently from the derived inputs, rather than by running the outcome-writing scripts.

The inverse of the unit-scale covariance is

\[
C^{-1}=
\begin{pmatrix}
1.5&-1&0&0\\
-1&2&-1&0\\
0&-1&2&-1\\
0&0&-1&1
\end{pmatrix}.
\]

With \(D=\delta'C^{-1}\delta\),

\[
\hat k=\frac{\delta'C^{-1}y}{D},
\qquad
\operatorname{SE}(\hat k)=\frac{\sigma}{\sqrt D}.
\]

| Quantity | Channels | Distributors |
|---|---:|---:|
| Historical \(\sigma\) | 0.0221389705 | 0.0189080213 |
| \(\operatorname{SE}(\hat k)/\sigma\) | 7.96979184 | 21.83945622 |
| \(\hat k\), derived CSV precision | 0.11754366 | 1.30306784 |
| SE | 0.17644299 | 0.41294090 |
| Conditional 95% interval | [−0.22828459, 0.46337191] | [0.49370366, 2.11243201] |
| Projected cited-input band | [0.75000649, 2.5361585] | [0.79746962, 2.2353323] |
| Exact “inconclusive” scale cutoff | 4.04885% | 3.04417% |
| Interval at \(\sigma=8\%\) | [−1.13212, 1.36721] | [−2.12136, 4.72749] |
| 2014-rescaled \(\hat k\) | 0.12963468 | 1.23001060 |
| Rescaled conditional interval | [−0.21619357, 0.47546293] | [0.42064643, 2.03937477] |

Channels including exempt services give \(\hat k=0.12948924\), with interval [−0.21633901, 0.47531750].

The channel estimate being positive despite every observed channel revenue exceeding baseline is not an arithmetic error. Its GLS weights on the four log gaps are approximately

\[
(-3.268,\ -0.913,\ 4.194,\ 1.547).
\]

The estimate captures the changing gap’s alignment with the forecast shape. It should therefore not be described as a simple average or aggregate share of revenue lost.

The Netflix calculations, before CSV rounding, are:

| Calibration | Annual scale |
|---|---:|
| 2016 | 4.426895% |
| 2017 | 2.135597% |
| 2018 | 1.286807% |
| Pooled 2016–2018 | 4.672775% |
| Growth 2015–2016 | 1.537591% |
| Growth 2015–2017 | 0.724093% |
| Growth 2015–2018 | 4.212693% |
| Growth pooled | 4.011287% |

The analysis uses these rounded to four decimal places before applying the historical floor.

Offset fits, reproducing the script’s rounded scales:

| Quantity | Channels | Distributors |
|---|---:|---:|
| Offset \(\hat a\) | −0.05490759 | 0.01396742 |
| SE of offset | 0.03252542 | 0.02845545 |
| Offset-model \(\hat k\) | 0.20320916 | 1.22907204 |
| SE of \(k\) | 0.18329679 | 0.43943260 |
| Conditional interval for \(k\) | [−0.15605256, 0.56247087] | [0.36778414, 2.09035993] |

Historical-scale design-analysis shares:

| Quantity | Correct if no effect | Correct if forecast effect | Reported minimum |
|---|---:|---:|---:|
| Channels | 99.825% | 98.780% | 98.780% |
| Distributors | 88.945% | 86.120% | 86.120% |
| CPE | 63.595% | 63.000% | 63.000% |

Employment calculations, checked against workbook precision because the derived annual staff file rounds counts:

| Quantity | Channels | Distributors |
|---|---:|---:|
| Staff, 2015 | 5,898.78 | 27,243.67 |
| Staff, 2019 | 4,402.94 | 27,887.05 |
| Change | −1,495.84 | +643.38 |
| Fitted annual pre-period slope | −75.025 | −445.669 |
| 2018 deviation from extrapolated trend | −1,054.41 | −395.617 |
| 2019 deviation from extrapolated trend | −1,281.755 | +1,834.112 |
| Forecast 2019 direct FTE impact | −800 | −2,910 |

These are descriptive computations. They cannot establish that a trend deviation differs from the forecast impact without a defensible employment counterfactual and comparable units. Merely adding a regression interval to this four-point trend would not resolve those problems.

Payments to Canadian services rose from $3,014.1 million to $3,124.8 million, **3.6727%**. Dividing by the subscriber totals and 12 gives approximately **$22.3332 to $24.6766 per month**, an increase of **10.4929%**, compared with **1.5602%** for the report’s $20.51-to-$20.83 fee path. The input-check script itself acknowledges that the two levels differ by definition ([lines 138–141](/Users/brettreynolds/projects/LLM-CLI-projects/papers/development/prediction-checker/scripts/input_checks_lttv.py:138)); the manuscript should retain that qualification.

Closure bounds from counts are:

| Ownership classification | Integrated | Independent |
|---|---:|---:|
| Corus independent | 3/38 to 4/38 = **7.895–10.526%** | 8/127 to 42/127 = **6.299–33.071%** |
| Corus integrated | 5/80 to 9/80 = **6.250–11.250%** | 6/85 to 37/85 = **7.059–43.529%** |

The CPE arithmetic gives \(399/3155=12.6466\%\), \(399/3258=12.2468\%\), and approximately \(399/3286=12.1424\%\), supporting the manuscript’s rounded comparisons.

**5. What to add and what to cut**

Add:

- A direct statement that the intervals condition on fixed scales and **do not propagate calibration, cross-domain transfer, or model uncertainty**.
- A coherent choice between the additive-impact simulator and the multiplicative log-error estimation model, followed by coverage verification for the chosen interpretation.
- Correct fitted-residual diagnostics.
- The planned sensitivity display through 8%, with the rescaled-series and offset results relevant to the distributor scenario claim.
- A definition of \(k\) as a projected log-shortfall coefficient, including a brief explanation of why it can be positive when every observed channel level exceeds baseline.
- Explicit distinctions between a pre-stated employment-check rule and the later trend comparator, and between counted mid-2016 uptake and assumed subsequent uptake.
- “Pointwise” in Figure 1 and the fee-series definitional qualification in the main text.

Cut or downgrade:

- The claim that the 2.1-SE distributor discrepancy identifies losses outside the unbundling channel.
- “Channel employment fell … but not by the route the model describes.”
- “Actual uptake” when describing a four-year flat scenario.
- “Largest error” and “decisive” unless the scope is explicitly restricted to the observed mid-2016 comparison.
- The interpretation of \(k=0.40\) as 40% of dollar losses.
- Any implication that displaying nine calibrations supplies an unconditional 95% uncertainty statement.

The paper can support a careful **conditional forecast comparison and descriptive audit**. Its current stronger conclusions about the mechanisms responsible for revenue and employment outcomes do not survive.
