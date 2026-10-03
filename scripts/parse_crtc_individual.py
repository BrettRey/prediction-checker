#!/usr/bin/env python3
"""Parse per-service blocks from CRTC 'Individual Discretionary and On-Demand'
statistical and financial summaries (sheet 'Individuals').

Each block: a header row with 'Undertaking #', a row with the undertaking
number, service name, licensee, ultimate owner, type and publication year; a
year header row; then revenue and expense rows. Returns one record per service
with Total Revenue by year.
"""
import warnings
from pathlib import Path

import openpyxl

warnings.filterwarnings("ignore")


def _num(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    t = str(v).replace(",", "").strip()
    try:
        return float(t)
    except ValueError:
        return None


def parse(path):
    ws = openpyxl.load_workbook(path, read_only=True, data_only=True)["Individuals"]
    rows = [list(r) for r in ws.iter_rows(values_only=True)]
    out = []
    i = 0
    while i < len(rows):
        r = rows[i]
        if any(isinstance(c, str) and c.strip() == "Undertaking #" for c in r):
            hdr = {str(c).strip(): j for j, c in enumerate(r) if c is not None}
            d = rows[i + 1]
            get = lambda name: (str(d[hdr[name]]).strip() if name in hdr and hdr[name] < len(d) and d[hdr[name]] is not None else "")
            rec = dict(undertaking=get("Undertaking #"), service=get("Service Name"), licensee=get("Licensee"),
                       owner=get("Licensee Ultimate Owner"), type=get("Type"), revenue={})
            # find the year header row and the Total Revenue row within the block
            years = None
            j = i + 2
            while j < len(rows) and not any(isinstance(c, str) and c.strip() == "Undertaking #" for c in rows[j]):
                rr = rows[j]
                if years is None and any(str(c).strip().isdigit() and len(str(c).strip()) == 4 for c in rr if c is not None):
                    years = {k: int(str(c).strip()) for k, c in enumerate(rr)
                             if c is not None and str(c).strip().isdigit() and len(str(c).strip()) == 4}
                first = next((c for c in rr if c is not None), None)
                if years and isinstance(first, str) and first.strip() == "Total Revenue":
                    for k, yr in years.items():
                        v = _num(rr[k]) if k < len(rr) else None
                        if v is not None:
                            rec["revenue"][yr] = v
                j += 1
            out.append(rec)
            i = j
        else:
            i += 1
    return out


if __name__ == "__main__":
    import sys
    from collections import Counter
    recs = parse(Path(sys.argv[1]))
    print(len(recs), "services")
    print(Counter(r["type"] for r in recs).most_common())
    print(Counter(r["owner"] for r in recs).most_common(25))
