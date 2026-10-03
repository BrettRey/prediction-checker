# Literature search, 2026-10-03
<!-- SUMMARY: Inward then outward search for the EJW paper (Let's Talk TV case); six strands; core positioning literature is ex ante vs ex post accuracy of regulatory and industry estimates; nothing found evaluating the Nordicity forecast or LTTV outcomes · status: first pass done · updated: 2026-10-03 -->

Purpose: position the *Econ Journal Watch* paper and back its novelty claim with a stated search. Every work below is marked READ (text opened, passage located) or IDENTIFIED (metadata only; not to be cited for content until read).

## Inward (Brett's corpus)

- `lit resolve` for: tetlock, manski, "incredible certitude", crompton, "economic impact", "regulatory cost", "expert political judgment", "forecast accuracy", superforecasting, "impact assessment", cost-benefit. Only hit: `canadaAIA2026` (an algorithmic impact assessment tool; irrelevant).
- Central bibliography grep for authors Tetlock, Manski, Crompton, Morgenstern, Harrington (Winston), Hahn (Robert), Sunstein, Mellers: one hit, Manski 2003 *Partial Identification of Probability Distributions* (not the policy-certitude work).
- qmd query over `literature/` (BM25 `"ex post" "ex ante" regulatory cost estimates accuracy`; vector "comparing ex ante regulatory impact estimates with ex post outcomes retrospective review accuracy"; BM25 `"economic impact" forecast evaluation policy testimony accuracy`): no relevant hits.
- Conclusion: none of the strands below is in the portfolio. This is new ground for Brett.

## Outward: method

OpenAlex API, 2026-10-03. A first run of full-text searches sorted by citations was too noisy to use (output in the session scratchpad). The productive run used title-restricted filters (`title.search:`), listed per strand below. Web searches for the case-specific novelty question are logged in `novelty-search.md`.

## Strands

### A. Ex ante versus ex post accuracy of regulatory estimates (core positioning)

Queries: `title.search:accuracy regulatory cost estimates` (5 hits); `title.search:ex ante ex post regulation` (47, almost all on liability versus regulation, off-topic); `title.search:retrospective regulatory analysis` (46, mostly drug regulation, off-topic); `title.search:regulators overestimate costs` (1).

- **READ** Harrington, Morgenstern and Nelson, *On the Accuracy of Regulatory Cost Estimates*, RFF Discussion Paper 99-18 (January 1999); published *JPAM* 19(2): 297–322 (2000). Partial copy only (first six pages: abstract, contents, start of introduction). Abstract: ex ante estimates of total direct costs exceeded actuals for 12 of 25 rules and fell short for 6; "The quantity errors are driven by both baseline and compliance issues"; and "discovering how and when to adjust ex ante estimates provides the strongest possible justification for more credible ex post studies". `literature/harrington_morgenstern_nelson_1999_rff_dp9918_partial`.
- **READ** Simpson, "Do regulators overestimate the costs of regulation?", *J. Benefit-Cost Analysis* 5(2): 315–332 (2014). Abstract: the frequency of overestimates and an average ex ante/ex post ratio above one don't by themselves show bias (skewed cost distributions; Jensen's inequality); a regression test can't reject unbiasedness; argues for "more and better information". Pp. 319–320 review earlier studies, including industry rather than regulator estimates (below). `literature/simpson_2014_jbca_regulators_overestimate_costs`.
- IDENTIFIED: MacLeod, Moran and Harrington 2001 ("Improving the Accuracy of UK Regulatory Cost Estimates", AgEcon, OA); Sherrington and Moran 2007 ("The accuracy of regulatory cost estimates: a study of the London congestion charging scheme", *European Environment*); *JBCA* 2023 "Ex Ante Costs Versus Ex Post Costs of the Large Municipal Waste Combustor Rule"; *JBCA* 2017 "Retrospective Analysis of U.S. Federal Environmental Regulation" and "Retrospective Analyses Are Hard: A Cautionary Tale from EPA's Air Toxics Regulations"; Hammitt 2000 ("Are the Costs of Proposed Environmental Regulations Overestimated? Evidence from the CFC Phaseout", *Environmental and Resource Economics*).

### B. Stakeholder and industry claims about costs

Queries: `title.search:overestimating costs environmental regulation` (1: Hammitt 2000); `title.search:industry claims cost regulation` (1, off-topic).

- Known only through Simpson (2014, 319–320), so cite as "reviewed in Simpson 2014" until read: Putnam, Hayes and Bartlett (1980) for EPA, where "In four of five cases industry overestimated capital costs"; Hodges (1997), 12 regulations, ex ante estimates above realized costs in each and "more than double costs realized ex post" in 11 of 12, a study that "focuses on industry's rather than regulators' estimates"; Bailey, Haq and Goudson (2002, Stockholm Environment Institute), industry estimates in regulatory negotiations "consistently higher than ex post realizations of actual costs".

### C. Critiques of economic impact studies and multipliers

Queries: `title.search:economic impact studies` (8,165; unusable); `title.search:economic impact analysis multiplier` (23); `title.search:political shenanigans` (3); `title.search:economics of sports facilities and their communities` (1).

- IDENTIFIED: Crompton 2006, "Economic Impact Studies: Instruments for Political Shenanigans?", *Journal of Travel Research* (no open copy); Siegfried and Zimbalist 2000, "The Economics of Sports Facilities and Their Communities", *JEP* 14(3), DOI 10.1257/jep.14.3.95 (download refused twice); Hughes 2003, "Policy Uses of Economic Multiplier and Impact Analysis" (AgEcon, open; not yet fetched).

### D. Policy forecasting and certitude

Queries: `title.search:incredible certitude` (10); `title.search:expert political judgment` (22); `title.search:policy forecasts accuracy` (34, mostly central-bank forecasting).

- **READ** Manski, *Policy Analysis with Incredible Certitude*, LSE STICERD Public Economics Programme Discussion Paper 10 (2011); published *Economic Journal* 121(554): F261–F289. P. 4: "Point predictions are common and expressions of uncertainty are rare. Yet policy predictions often are fragile." §5, "Conflating Science and Advocacy" (p. 23), on reversing the direction of inference from assumptions to conclusions. `literature/manski_2011_policy_analysis_incredible_certitude_pep10`.
- IDENTIFIED: Manski 2012 (*Public Policy in an Uncertain World*); Manski 2019 ("The lure of incredible certitude", *Economics and Philosophy*); Tetlock 2005 (*Expert Political Judgment*).

### E. Canadian television unbundling and *Let's Talk TV*

Queries: full-text `pick-and-pay television unbundling Canada`, `Let's Talk TV CRTC`, `a la carte cable television unbundling welfare`; `title.search:pick-and-pay` (75, none on television), `title.search:skinny basic` (2, off-topic), `title.search:unbundling television` (0), `title.search:canadian broadcasting regulation` (35).

- IDENTIFIED: Crawford and Yurukoglu 2012, "The Welfare Effects of Bundling in Multichannel Television Markets", *AER* 102(2), DOI 10.1257/aer.102.2.643 (open copies didn't download: the AEA link returned HTML, the Zurich repository page showed no PDF); Davis and Zboralska 2017, "Transnational over-the-top media distribution as a business and policy disruptor: The case of Netflix in Canada", *Journal of Media Innovations* (open; not read); Salter and Odartey-Wellington 2008, *The CRTC and Broadcasting Regulation in Canada*.
- **No study found that evaluates *Let's Talk TV* outcomes or the Nordicity/Miller forecast** in these databases (queries above and in `novelty-search.md`). The forecaster's own later CRTC work doesn't revisit it (T14, T15).

### F. Forecasts made in testimony or litigation

Queries: `title.search:predictions that didn't come true` (2, off-topic); `title.search:testimony forecast` (2, off-topic); EJW source `title.search:forecast` (2).

- **READ** Kane 2026 (*EJW* 23(2): 485–508), the exemplar.
- IDENTIFIED (EJW's own forecast checks): "Mankiw vs. DeLong and Krugman on the CEA's Real GDP Forecasts in Early 2009: ..." (2012; full title not yet seen); "Paul Krugman Denies Having Concurred With an Administration Forecast: A Note" (2013).

## What this means for the paper

1. **Contribution, in the venue's terms.** The ex ante/ex post literature mostly compares regulators' compliance-cost estimates with outcomes, with a smaller strand on industry cost claims (Simpson 2014, 319–320). This paper asks the same question of a stakeholder's *economic-impact* forecast (revenue, programming spending, jobs, GDP) placed before Parliament, and checks it link by link along its causal chain, which a total-cost comparison can't do. Harrington et al. trace misses to baseline and quantity errors; the baseline problem is the centre of this case too.
2. **One case, no bias claim.** Simpson's argument that over-estimate counts don't show bias is a reason to frame the paper as a check of one forecast, with uncertainty, not as evidence that stakeholder forecasts are biased.
3. **Certitude.** The report disclaims probabilities (¶111) and calls its scenarios "conceivable and plausible" (¶109); the testimony gave single numbers as things that "will be lost". Manski's point about point predictions fits; his science/advocacy distinction should be used with care and charity (Rapoport's rules), since the paper can show the testimony's overstatement without imputing motive to the forecasters.
4. **EJW precedent.** EJW has checked policy forecasts before (2012, 2013) and Kane (2026) checked forecasts placed before a court. Read the 2012 piece before citing it.

## To read before drafting the introduction

Open copies: Hughes 2003; Davis and Zboralska 2017; MacLeod, Moran and Harrington 2001; the two 2017 *JBCA* retrospectives and the 2023 *JBCA* comparison if open; the EJW 2012 forecast piece. Need library access (Brett): Crawford and Yurukoglu 2012; Crompton 2006; Siegfried and Zimbalist 2000; Hodges 1997; Hammitt 2000; the full Harrington et al. paper.
