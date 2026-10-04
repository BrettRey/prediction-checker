# Coherence and cohesion pass, 2026-10-03
<!-- SUMMARY: spine map plus 14 proposed flow edits for Brett's approval (CriticMarkup, Roughdraft); text at commit bafa1ec · status: awaiting review · updated: 2026-10-03 -->

Run by Claude Opus 5.5 on the main text (sections 1–6) at commit bafa1ec, following `passes/registry/coherence-cohesion.yaml`: spine map first, then a sliding three-paragraph window. Edits are proposed, not applied. Accept or reject each one; I'll apply the accepted ones to the LaTeX. Excerpts show rendered numbers, not macros.

## 1. Spine

| Section | Question it answers | What it establishes |
|---|---|---|
| 1 Introduction | What forecast went to Parliament, and what can be checked? | The case, the gap (no published comparison found), scope (intermediate predictions; no causal or total-jobs test), main findings, two objects of assessment (after Kane), method preview |
| 2 The forecast and its presentation | What did the report forecast, through which chain and assumptions? | Baseline, reform scenario and reform path; jobs accounting; BYOP uptake, pass-through, closures; four revenue components; 2020 magnitudes |
| 2.1 What the committee heard | How did the testimony differ from the report? | Two departures, the faithful elements, the 18% arithmetic, the 4% remark |
| 3 Comparing outcomes | How can outcomes be compared with paths whose baseline may be wrong? | Prediction record and design analysis; k and its interval; cited-input band; verdict rule; designated error scale |
| 4 Revenue outcomes | What did revenue do against the paths, and how does that depend on uptake and baseline error? | Verdicts (smaller, consistent); the uptake evidence; recalculations; distributors' split; sensitivity; model check |
| 5 Payments, closures, staff | What did the other links do? | Payments per subscriber outgrew the baseline fee; integrated closures below the report on the plan's rule, around it on the report's grouping; staff and revenue pointed opposite ways |
| 6 Discussion | What does the evidence establish, and what did the testimony omit? | Bounded conclusion; the uptake dependence; three departures; credit; the monitoring lesson; limits; five model-free findings |

Every section's line can be written, so there's no structural finding. The defects are at the joins.

## 2. Proposed edits

**E1** (§1, para 2). The Miller sentence qualifies the novelty claim, but the link is unmarked.

> My recorded searches of scholarly databases and the web found no published comparison of the forecast's numerical paths with outcomes (the queries are in the replication files). {~~Miller's later work~>Miller's own later work~~}{#s1} for the CRTC discusses what the decisions led to, and acknowledges an error in a separate prediction of station closures.

**E2** (§1, para 3, 195 words). Split: the first two sentences say what the paper does; the rest give the findings.

> ... It tests neither the total employment forecast nor the decisions' causal effect. {==The report's main input is uptake==}{>>Start a new paragraph here.<<}{#c1}, the share of subscribers taking an entry-level package with chosen channels. ...

**E3** (§1, method paragraph). After the paragraph on the two objects of assessment, the method paragraph applies to the technical claim only; the reader isn't told.

> {~~I fixed the forecast record~>For the technical claim, I fixed the forecast record~~}{#s2} before downloading any CRTC outcome file, and ran a simulation ...

**E4** (§2). "The revenue shortfall" is named before its size is given: the magnitudes paragraph comes after the components.

> {==By 2020 the reform path runs $970 million (23%) a year below the baseline for the revenue of specialty and pay services ... runs $399 million below.==}{>>Move this paragraph up, directly after the chain paragraph ("The job and GDP figures sit at the end of a chain ..."), so it precedes "The report divides the revenue shortfall into four components". No wording change.<<}{#c2}

**E5** (§2.1). Two sentences re-say one point, with "own" three times.

> {~~The 18% itself is the report's, and its own figures don't reproduce it. The report's own baseline figures put 2020 CPE at $3,155 million~>The 18% itself is the report's, though its figures don't reproduce it: its baseline puts 2020 CPE at $3,155 million~~}{#s3}, so its $399 million reduction is 12.6% of baseline, not the 18% its text states.

**E6** (§3, para 3). After the paragraph on the counterfactual, this paragraph returns to the design analysis without saying so.

> {~~With the annual error scale (the standard deviation of the yearly change in the baseline's error) set to the historical volatility of the report's own 2010–2014 data, the design analysis classified~>In the design analysis, with the annual error scale (the standard deviation of the yearly change in the baseline's error) set to the historical volatility of the report's own 2010–2014 data, the simulation classified~~}{#s4} specialty and pay revenue correctly in about 99% of simulated worlds ...

**E7** (§3, last paragraph). The calibration paragraph delivers the "described below" promise about σ, three paragraphs later; naming σ links them.

> The outcome series alone can't identify how wrong the baseline was, so the plan fixed an external check{++ on the error scale σ++}{#s5}: the forecast of US Netflix subscribers ...

**E8** (§4.1, first sentence). Two unrelated clauses joined by a semicolon; the data check belongs before the figure.

> {~~Figure 1 shows each revenue series against the report's two paths; the CRTC series reproduce the report's 2012–2014 values within 2% (CRTC 2017, 2021).~>The CRTC series reproduce the report's 2012–2014 values within 2% (CRTC 2017, 2021), and figure 1 shows each against the report's two paths.~~}{#s6}

**E9** (§4.2, para 1, about 180 words). Split: CRTC counts, then the survey.

> ... I found no later CRTC count. {==A survey by the Media Technology Monitor==}{>>Start a new paragraph here.<<}{#c3}, released in August 2017, ...

**E10** (§4.3, para 1). "Those two ... the first two" makes the reader count back.

> {~~Since the report values those two partly from the first two~>Since the report values the exemption-order and closure components partly from the other two~~}{#s7}, the recalculation is partial.

**E11** (§4.4, para 2). "The comparison" is a pointer; the paragraph is about how the split is measured.

> {~~The comparison is of changes from 2014, since~>The split is measured as changes from 2014, since~~}{#s8} in the report's actual years the CRTC's subscriber counts sit 1.7% to 2.1% below the report's ...

**E12** (§5.1, para 2, about 210 words). Split: the definitions and the two uptake readings, then what the aggregates can't show.

> ... and observed payments instead grew faster than it. {==The aggregates can't say==}{>>Start a new paragraph here.<<}{#c4} what fees would have been without the decisions ...

**E13** (§5.2, about 230 words). Split into integrated companies, independents, and CPE.

> ... gives 6% to 11%, around the report's figure. {==For the independents the bounds==}{>>Start a new paragraph here.<<}{#c5}, 7% to 39% on the plan's classification ... {==CPE, read only descriptively==}{>>And here.<<}{#c6}, ran between $3,204 million and $3,427 million a year ...

**E14** (§6, para 2, about 230 words). The paragraph moves from what the evidence can say to the post hoc recalculations without marking the change in status; split there and mark it.

> ... put starter-package adoption near the report's figure for 2017. {>>Start a new paragraph here.<<}{#c7}{~~The partial recalculations can say only~>The partial recalculations, added after the outcome data was opened, can say only~~}{#s9} which assumed uptake paths the outcomes are compatible with.

## 3. Noted, no edit proposed

- **Duplicated verdict, §6 para 2 and §4.3.** The standard-error sentence ("the distributors' estimate lies 2.1 standard errors above ... 3.7 standard errors above the estimate") repeats §4.3. I'd keep it: it's the only place the discussion states the two readings concretely. Cut it if you prefer a shorter discussion.
- **§4.2 opening.** The move from the revenue verdicts to the uptake evidence is carried by the heading alone. I think that's enough.
- **No announcing openers** ("In this section I ...") found. The introduction's roadmap is a roadmap, not an announcement.

---
comments:
  c1:
    by: Claude Opus 5.5
    at: "2026-10-03T22:00:00-04:00"
  c2:
    by: Claude Opus 5.5
    at: "2026-10-03T22:00:00-04:00"
  c3:
    by: Claude Opus 5.5
    at: "2026-10-03T22:00:00-04:00"
  c4:
    by: Claude Opus 5.5
    at: "2026-10-03T22:00:00-04:00"
  c5:
    by: Claude Opus 5.5
    at: "2026-10-03T22:00:00-04:00"
  c6:
    by: Claude Opus 5.5
    at: "2026-10-03T22:00:00-04:00"
  c7:
    by: Claude Opus 5.5
    at: "2026-10-03T22:00:00-04:00"
suggestions:
  s1:
    by: Claude Opus 5.5
    at: "2026-10-03T22:00:00-04:00"
  s2:
    by: Claude Opus 5.5
    at: "2026-10-03T22:00:00-04:00"
  s3:
    by: Claude Opus 5.5
    at: "2026-10-03T22:00:00-04:00"
  s4:
    by: Claude Opus 5.5
    at: "2026-10-03T22:00:00-04:00"
  s5:
    by: Claude Opus 5.5
    at: "2026-10-03T22:00:00-04:00"
  s6:
    by: Claude Opus 5.5
    at: "2026-10-03T22:00:00-04:00"
  s7:
    by: Claude Opus 5.5
    at: "2026-10-03T22:00:00-04:00"
  s8:
    by: Claude Opus 5.5
    at: "2026-10-03T22:00:00-04:00"
  s9:
    by: Claude Opus 5.5
    at: "2026-10-03T22:00:00-04:00"
