"""Constants fixed in notes/analysis-plan.md or quoted from the Nordicity/Miller
report, shared by every script so the analysis and the manuscript can't drift.
"""
# Report's own assumptions (Nordicity and Miller 2015)
REPORT_UPTAKE_2018 = 0.15        # BYOP share of subscribers from 2018 (Table 18, p. 76)
REPORT_PASS_THROUGH = 0.75       # share of BDU retail loss passed to Canadian services (para. 207, p. 77)
REPORT_CANADIAN_SHARE = 0.86     # Canadian services' share of BDU retail loss (para. 206, p. 77)
REPORT_CLOSURES_VI = 0.10        # vertically integrated A/B services shut by 2020 (para. 232, p. 85)
REPORT_CLOSURES_INDEP = 0.25     # independent A/B services shut by 2020 (para. 233, p. 85)
# Ranges the report cites from others (paras. 201, 230)
CITED_UPTAKE_LOW = 0.10          # Corus, low end
CITED_UPTAKE_HIGH = 0.35         # Oliver Wyman, "as many as"
CITED_CLOSURES_HIGH_MULT = 2.5   # Bell ~25%, Oliver Wyman 26%, against the report's 10%
# Plan rules (notes/analysis-plan.md)
SPLICE_TOLERANCE = 0.02          # CRTC series used as published if within 2% of the report, 2012-2014
