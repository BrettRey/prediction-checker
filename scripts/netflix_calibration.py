#!/usr/bin/env python3
"""Technology-forecast calibration for case 2 (rule in notes/analysis-plan.md).

Compares the Nordicity report's forecast of US Netflix subscribers (Table 7,
from Trefis) with Netflix's reported US ("Domestic streaming") paid memberships
at year end, and computes sigma_tech = |log(observed 2018 / forecast 2018)| / sqrt(4).

Input: data/raw/netflix/form10k_q418.htm, Netflix Form 10-K for fiscal 2018,
  https://www.sec.gov/Archives/edgar/data/1065280/000106528019000043/form10k_q418.htm
  (retrieved 2026-10-03), Domestic Streaming Segment table, "Paid memberships at
  end of period" (thousands), columns 2018, 2017, 2016.
Output: data/derived/netflix_calibration.csv
"""
import csv
import math
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "raw" / "netflix" / "form10k_q418.htm"
FC = ROOT / "data" / "derived" / "nordicity_2015_us_ott_forecast.csv"
OUT = ROOT / "data" / "derived" / "netflix_calibration.csv"

text = subprocess.run(["pandoc", "-f", "html", "-t", "plain", "--wrap=none", str(SRC)],
                      check=True, capture_output=True, text=True).stdout
lines = text.splitlines()
start = next(i for i, l in enumerate(lines) if l.strip() == "Domestic Streaming Segment")
row = next(l for l in lines[start:start + 40] if "Paid memberships at end of period" in l)
vals = [int(v.replace(",", "")) for v in re.findall(r"\d{1,3}(?:,\d{3})+", row)]
assert len(vals) >= 3, row
observed = {2018: vals[0] / 1000, 2017: vals[1] / 1000, 2016: vals[2] / 1000}  # millions

forecast = {int(r["year"]): float(r["us_netflix_subscribers_m"]) for r in csv.DictReader(open(FC))}
sigma_tech = abs(math.log(observed[2018] / forecast[2018])) / math.sqrt(2018 - 2014)

with open(OUT, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["year", "forecast_us_netflix_m", "observed_us_paid_memberships_m", "log_ratio"])
    for y in (2016, 2017, 2018):
        w.writerow([y, forecast[y], round(observed[y], 3), round(math.log(observed[y] / forecast[y]), 4)])
    w.writerow(["sigma_tech", "", "", round(sigma_tech, 4)])
print("observed (M):", observed)
print("forecast (M):", {y: forecast[y] for y in (2016, 2017, 2018)})
print(f"sigma_tech = {sigma_tech:.4f}")
