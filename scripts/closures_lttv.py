#!/usr/bin/env python3
"""Case 2 closures check (definition fixed in notes/analysis-plan.md).

Denominator: Category A and B specialty services with 2015 revenue in the 2016
vintage of the CRTC individual-service summaries. A service is matched across
vintages by undertaking number. Status by 2019-2020 (2020 vintage):
  operating  - listed, revenue in 2019 or 2020
  closed     - listed, no revenue in 2019 and 2020
  absent     - not listed; closed OR became exempt (exempt services file
               returns but aren't published individually) [post hoc: reported
               as bounds because the source can't separate the two]
Ownership by owner field of the 2016 vintage: vertically integrated (VI) =
BCE, Rogers, Québecor (Les Placements Péladeau), Shaw; shown with and without
Corus, which by 2016 also held the former Shaw Media services.

Outputs: data/derived/closures_crosswalk.csv, data/derived/closures_summary.csv
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from parse_crtc_individual import parse  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "crtc"
DER = ROOT / "data" / "derived"
VI = {"BCE Inc.", "Rogers Communications Inc.", "Les Placements Péladeau inc.", "Shaw Communications Inc."}
CORUS = "Corus Entertainment Inc."

old = parse(RAW / "sfs2016_individual_discretionary.xlsx")
new = {r["undertaking"]: r for r in parse(RAW / "sfs2020_individual_discretionary.xlsx")}

rows = []
for r in old:
    cat = "A" if "category A service" in r["type"] and r["type"].startswith("Specialty") else \
          "B" if "category B service" in r["type"] and r["type"].startswith("Specialty") else None
    if cat is None or (r["revenue"].get(2015) or 0) <= 0:
        continue
    n = new.get(r["undertaking"])
    if n is None:
        status = "absent"
    elif (n["revenue"].get(2019) or 0) > 0 or (n["revenue"].get(2020) or 0) > 0:
        status = "operating"
    else:
        status = "closed"
    rows.append(dict(undertaking=r["undertaking"], service_2016=r["service"], owner_2016=r["owner"], category=cat,
                     revenue_2015=round(r["revenue"][2015]),
                     service_2020=n["service"] if n else "", owner_2020=n["owner"] if n else "",
                     revenue_2019=round(n["revenue"].get(2019, 0)) if n else "", revenue_2020=round(n["revenue"].get(2020, 0)) if n else "",
                     status=status))

with open(DER / "closures_crosswalk.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)

summary = []
for corus_vi in (False, True):
    groups = defaultdict(lambda: defaultdict(int))
    for r in rows:
        vi = r["owner_2016"] in VI or (corus_vi and r["owner_2016"] == CORUS)
        g = ("VI" if vi else "independent") + " A/B"
        groups[g][r["status"]] += 1
        groups[g]["n"] += 1
    for g, c in groups.items():
        lo = c["closed"] / c["n"]
        hi = (c["closed"] + c["absent"]) / c["n"]
        summary.append(dict(corus_counted_vi=corus_vi, group=g, n_2015=c["n"], operating=c["operating"],
                            closed=c["closed"], absent=c["absent"], share_closed_lower=round(lo, 3), share_closed_upper=round(hi, 3)))
with open(DER / "closures_summary.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(summary[0]))
    w.writeheader()
    w.writerows(summary)
for s in summary:
    print(s)
