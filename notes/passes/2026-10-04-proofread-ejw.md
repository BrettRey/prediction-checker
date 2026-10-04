# Proofread of the EJW-class build, 2026-10-04
<!-- SUMMARY: read-only proofread (Claude, /proofread skill) of tv-unbundling-forecast-check.tex after the EJW conversion; no critical or major issues; nine minor findings, six proposed for fixing · status: items 1–7 applied (Brett), 8–9 left · updated: 2026-10-04 -->

Linter (`check-style.py`) and terminology check (`check-terms.py --follow-inputs`) run; their hits are mostly known false positives (maths subscripts, "pointwise", ranges with real endpoints). No doubled-name citations, no unsourced claims, no em dashes, no unresolved references (build log clean).

| # | Location | Category | Severity | Current | Suggested fix |
|---|---|---|---|---|---|
| 1 | intro.tex:19 | latex/style | minor | "(pp.~319--321)" after Simpson | "(319--321)": the EJW class prints locators without "p." ("Simpson (2014, 322)") |
| 2 | case-lttv.tex:91 | grammar/clarity | minor | "the CRTC's cover broadcast years ending 31 August" (reads as "CRTC's cover") | "the CRTC's series cover broadcast years ending 31 August" |
| 3 | intro.tex:16; case-lttv.tex:28 (×2); discussion.tex:17, 33 | numbers | minor | literal "18\%", "\$399 million" | use \lttvCPEShareStated and \lttvCPEImpactTwenty (numbers-from-files rule); Morrison's "\$400" stays as quoted |
| 4 | case-lttv.tex:83, 95, 97 | numbers | minor | literal "1.6\%" (and "10\%" for the survey path) | \lttvUptakeJuneShare for 1.6%; the survey path's 10% is the reading of "just over 1 in 10", keep |
| 5 | appendix.tex:39 | terminology | minor | "RSS" never expanded | "(the residual sum of squares)" at first use |
| 6 | appendix.tex:33 | style (EJW abbreviations) | minor | "s.d." | "standard deviation" |
| 7 | discussion.tex:42 | grammar | minor | "It supplied leads and reported forecast figures, every one of which was checked ..., and none of the calculations reported here." | "...checked against primary sources before use; it supplied none of the calculations reported here." |
| 8 | throughout | quality | minor | paragraphs over 100 words (intro bullet 1; §2 chain paragraph; §2.1 18% paragraph; §4.3, §4.5, §5.1 long paragraphs; discussion paragraphs 1–4; appendix estimator and design paragraphs) | optional `density-leavening` pass; not a submission blocker |
| 9 | figure 1 caption; text | style (EJW/Chicago) | minor | British spellings (modelled, labelled, licence, enrolment, behaviour in a quotation) and "in per cent of the baseline" | leave for EJW copyediting, or switch to American spelling and "percent" now (Brett) |

Also noted, no change proposed: case-lttv.tex:133's "[p.~72, n.~80; p.~73, n.~82]" mixes page and note locators, which the class prints as typed; "package uptake" in the abstract is unglossed but explained by the abstract's next sentence; GDP unexpanded (free for EJW readers).

Outcome (Brett: "apply the figures and proofread fixes"): items 1–7 applied; 8 (paragraph length) and 9 (spelling, "per cent") left for an optional pass and copyediting. The figures pass's one finding (figure 1's 50% band in a hard-coded grey) fixed by deriving the shade from the palette (light blended with dark at 0.13), same appearance.
