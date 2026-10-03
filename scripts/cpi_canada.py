#!/usr/bin/env python3
"""Annual consumer price index for Canada, all-items (2002=100), from
Statistics Canada table 18-10-0005-01, for stating nominal changes in real
terms. The report's paths are nominal, so k and every comparison with the
report's paths are unaffected by any deflator applied to both sides; the CPI
is used only for stand-alone changes in the outcomes.

Input:  data/raw/statcan/18100005-eng.zip (scripts/fetch_raw.sh)
Output: data/derived/cpi_canada_annual.csv
"""
import csv
import io
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "statcan" / "18100005-eng.zip"
OUT = ROOT / "data" / "derived" / "cpi_canada_annual.csv"
YEARS = range(2010, 2021)

with zipfile.ZipFile(RAW) as z:
    text = z.read("18100005.csv").decode("utf-8-sig")
cpi = {}
for r in csv.DictReader(io.StringIO(text)):
    if r["GEO"] == "Canada" and r["Products and product groups"] == "All-items" and r["UOM"] == "2002=100":
        cpi[int(r["REF_DATE"])] = float(r["VALUE"])
assert cpi[2002] == 100.0, cpi.get(2002)
with open(OUT, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["year", "cpi_all_items_2002_100", "source"])
    for y in YEARS:
        w.writerow([y, cpi[y], "Statistics Canada, table 18-10-0005-01 (vector v41693271)"])
print(f"wrote {OUT.relative_to(ROOT)}: " + ", ".join(f"{y} {cpi[y]}" for y in (2015, 2019)))
