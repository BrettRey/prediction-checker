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
[post hoc, 2026-10-03] The plan's own rule, ownership by 2015 owner, is also
computed: the 19 specialty services Shaw Media held before the transfer to Corus
(CRTC ownership charts 32h and 32i, Internet Archive captures of 2016-03-31;
literature/crtc_ownership_chart32{h,i}_shaw_2016-03-31.md) are counted as VI,
and Corus's own services as independent.

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
# Shaw Media's specialty services before the transfer to Corus (completed 1 April 2016; CRTC 2016-110),
# by undertaking number in the 2016 vintage, with the service as named in the CRTC chart.
SHAW_MEDIA_2015 = {
    "305424997": ("Action", "32i"), "305424319": ("BBC Canada", "32i"), "535434906": ("BC News 1", "32h"),
    "305423907": ("Crime + Investigation", "32h"), "305426050": ("Deja View", "32h"), "535421151": ("DIY Network", "32i"),
    "305417299": ("DTOUR", "32h"), "305423329": ("Food Network Canada", "32i"), "305424020": ("fyi", "32i"),
    "205424055": ("H2", "32h"), "305417322": ("HGTV Canada", "32i"), "305417249": ("History Television", "32i"),
    "305425002": ("Lifetime", "32i"), "305426000": ("MovieTime", "32h"), "535434584": ("NatGeo Wild", "32i"),
    "305424294": ("National Geographic Channel", "32i"), "315413732": ("Showcase", "32i"), "315413724": ("Slice", "32i"),
    "105424006": ("The Independent Film Channel Canada", "32i"),
}

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

by_u = {r["undertaking"]: r for r in rows}
for u, (name, chart) in SHAW_MEDIA_2015.items():
    assert u in by_u and by_u[u]["owner_2016"] == CORUS, (u, name)
    first = name.split()[0].lower().strip("+")
    assert first[:4] in by_u[u]["service_2016"].lower().replace(".", "").replace("-", " "), (u, name, by_u[u]["service_2016"])
with open(DER / "closures_owner2015.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["undertaking", "service_2016", "owner_2016", "owner_2015", "crtc_chart_service", "crtc_chart"])
    for r in rows:
        sm = SHAW_MEDIA_2015.get(r["undertaking"])
        w.writerow([r["undertaking"], r["service_2016"], r["owner_2016"],
                    "Shaw Media Inc." if sm else r["owner_2016"], sm[0] if sm else "", sm[1] if sm else ""])

with open(DER / "closures_crosswalk.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)

summary = []
for corus_vi in (False, True, "plan_2015_owner"):
    groups = defaultdict(lambda: defaultdict(int))
    for r in rows:
        if corus_vi == "plan_2015_owner":
            vi = r["owner_2016"] in VI or r["undertaking"] in SHAW_MEDIA_2015
        else:
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
