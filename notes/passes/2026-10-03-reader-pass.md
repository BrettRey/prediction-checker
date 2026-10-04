# Reader pass, 2026-10-03
<!-- SUMMARY: in-order read of the built PDF (62c911f) by Claude Opus 5.5 plus an independent in-order read by Codex gpt-6-astra; main defect was machinery used before it was introduced; ~60 edits applied · status: applied · updated: 2026-10-03 -->

**Readers.** Primary: Claude Opus 5.5 read the built PDF (24 pp.) in order, pages 1–24, taking notes before fixing. Second: Codex gpt-6-astra (xhigh, read-only) read the PDF text in order independently (brief, manifest and verbatim report `REPORT-codex.md` in `notes/passes/reader-pass-2026-10-03/`). Mechanical pre-pass: `pointer_check.py` and `refcheck.py` on a flattened copy (5 and 37 flags; nearly all false positives; real ones: "Several calibrations", MTM and CMF unexpanded).

**Main finding (both readers).** The paper used its machinery before introducing it. The introduction's results paragraph used "the plan", "error scales", "uptake" and "the report's chain" before defining them; §3 used the band's "uptake-related components" and the 10%/35% estimates before the reader knew what either was, and never stated the verdict rules (they first appeared in table A4's caption); "preponderance" was never explained and the exemption order was glossed only at the end of §4.3, after figure 1, the recalculation and table 1 had used it; §4.3 cited four robustness checks (2017 and pooled calibrations, rescaled series, offset model) that the text introduces later or never.

## Applied

| Area | Defect | Fix |
|---|---|---|
| §1 para 3 | Terms before definitions; "compatible" undefined | Uptake defined first; error allowance described ("allowing for error in the report's own baseline at the scales the plan set"); the cited range (10% to 35%) named; post hoc recalculation result stated as "within their intervals" |
| §1 | IPTV unexpanded | Expanded |
| §2 | Four revenue components never introduced (both readers) | New paragraph: unbundling; preponderance received-to-offered with the end of access rules, modelled as Canadian channels' share of BYOP wholesale fees falling 86% to 50% (para. 212; new plan constants and macros); the exemption order for streaming services such as Crave TV and Shomi (para. xxiii); closures; which two scale with uptake and that the report values the other two partly from them (paras. 220, 234) |
| §2 | Pass-through base differed between §2 and §5.1 (Codex) | Both now: 86% of the lost retail revenue attributed to Canadian services, 75% of that part passed on (paras. 206–207) |
| §2 | Integrated companies, Category A/B, ACTRA unexplained | "Vertically integrated companies, which own both distributors and channels (Bell, Rogers and Shaw/Corus)" (n. 31); "Category A and B specialty channels"; ACTRA expanded |
| §2 | Source of the 10,060 unclear | "attributed to production and, within broadcasting, to specialty and pay services" |
| §3 | "annual error scale" used before σ | Glossed at first use |
| §3 | δ not identified as a log shortfall (Codex) | Defined in logs |
| §3 | k^u declared before recalculations exist | Moved to §4.3 |
| §3 | Proportional-impact assumption first disclosed in §6.1 (Codex) | Stated in §3 with the 87%/93% coverage under the dollar-impact simulation |
| §3 | Band projection implicit; 10% unattributed; ×2.5 unexplained; verdict rules only in table A4 (both) | Projection explained ("the estimate k̂ would take if revenue had followed that path exactly"); Corus's lower and Oliver Wyman's estimates named (para. 201); closures ×2.5 for Bell's and Oliver Wyman's higher closure estimates (para. 230); full ordered verdict rule in the text |
| §3/§4.1 | Splice check stranded at the end of the calibration paragraph | Moved to §4.1 |
| §3 | "That last clause" | "Allowing for a wrong baseline" |
| §4.1 | Opening didn't name the series; "incompatible ... at the report's assumed uptake" understated the result | Series and scale named; "at any uptake the report cited" |
| §4.2 | "its 15%" | "its 15% for 2018 onward" |
| §4.3 | "compatible" undefined; robustness checks premature (Codex); "don't fall to zero" answered an unposed question | Definition added; checks given with section references and a gloss for the rescaled series; the zero sentence reframed around uptake held at 1.6% |
| §4.4 | 67% and 68% adjacent, different questions (both) | Reordered into two paragraphs: split shares first, recalculation shares second, each named |
| §4.5 | Vague "Several calibrations"; Netflix sentence repeated §3 | "Every calibration other than the pre-stated one"; repetition cut |
| §4.6 | Double standardization; "first step"; "gap"; "absorbs both" | Each named |
| §5.1 | "differ by definition" never explained (Codex); wholesale code unmotivated | Both measures described (para. 180, Table 14; CRTC affiliation payments to Canadian affiliates over subscribers); wholesale code glossed from n. 80 and tied to the question it answers |
| §5.2 | Corus classification unexplained; CPE sentence thin | Report grouped Shaw and Corus (n. 31); CPE ranges given from macros |
| §5.3, §6 | "don't move together" blurs benchmarks (Codex) | Both now say staff (against trend) and revenue (against the report's baseline) point in opposite directions |
| §6 | "a fall against the baseline that didn't appear" contradicted §3's lost-ground point (Codex) | "far more lost ground against the baseline than appeared" |
| §6.1 | Testimony clause vague | Named, as in the introduction |
| Appendix | Tables A1–A8 lived in appendix B (both) | Renumbered B1–B8 (hyperlink anchors table.B1 etc.); a sentence maps tables to sections; δ^u named |
| Tables | CBC/SRC, CMF, PPV, VOD; units; ARPU; flat 10% vs band ramp; internal labels (lead case, splice rule, reading rule 6, multiverse, MTM, "That split"); exempt services | Note expanding acronyms; units restricted to dollar rows; ARPU dropped; caption distinguishes the flat path from the band; labels replaced with descriptions; "services exempt from individual licensing" |

## Not adopted or deferred

- Float placement (figure 1 before §4, table 1 and figure 2 mid-sentence): left to the EJW template, which re-typesets floats.
- Repeated labels that a survey or analysis is post hoc or outside the plan: kept; they are the labelling the project's rules require.
- Scope sentences (no causal estimate, no test of total employment): kept, one per place.
- "Starter", "skinny basic" and "entry-level": not harmonized further; the survey's own definition of "starter" isn't in the source.
- Table B6's "discretionary and on-demand services" against "specialty and pay": needs the CRTC's category definitions; deferred to source-reread.
- The five-findings inventory in §6.1: kept as a deliberate summary; its testimony clause made concrete.
- Table B1's unused component labels E, N1, N2: harmless, kept.

**Checks.** Rebuilt with nonstopmode, 25 pages, only the two pre-existing hairline overfulls; macro file changed only by the two new preponderance macros; check-style reports nothing new.
