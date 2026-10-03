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

# [post hoc] 2015 from the 10-K for fiscal 2017 (same table, columns 2017, 2016, 2015),
#   https://www.sec.gov/Archives/edgar/data/1065280/000106528018000069/q4nflx201710k.htm
SRC17 = ROOT / "data" / "raw" / "netflix" / "q4nflx201710k.htm"
t17 = subprocess.run(["pandoc", "-f", "html", "-t", "plain", "--wrap=none", str(SRC17)],
                     check=True, capture_output=True, text=True).stdout.splitlines()
s17 = next(i for i, l in enumerate(t17) if l.strip() == "Domestic Streaming Segment")
row17 = next(l for l in t17[s17:s17 + 40] if "Paid memberships at end of period" in l)
v17 = [int(v.replace(",", "")) for v in re.findall(r"\d{1,3}(?:,\d{3})+", row17)]
assert v17[0] / 1000 == observed[2017] and v17[1] / 1000 == observed[2016], (v17, observed)
observed[2015] = v17[2] / 1000

forecast = {int(r["year"]): float(r["us_netflix_subscribers_m"]) for r in csv.DictReader(open(FC))}
sigma_tech = abs(math.log(observed[2018] / forecast[2018])) / math.sqrt(2018 - 2014)
# [post hoc, multiverse] the same formula for each year, and a pooled estimate:
# the maximum-likelihood SD of a random walk from 2014 observed at h = 2, 3, 4
# (increments e2 ~ N(0, 2 s^2), e3 - e2 and e4 - e3 ~ N(0, s^2)).
per_year = {y: abs(math.log(observed[y] / forecast[y])) / math.sqrt(y - 2014) for y in (2016, 2017, 2018)}
e = {y: math.log(observed[y] / forecast[y]) for y in (2016, 2017, 2018)}
pooled = math.sqrt((e[2016] ** 2 / 2 + (e[2017] - e[2016]) ** 2 + (e[2018] - e[2017]) ** 2) / 3)
# [post hoc] Growth-based: Table 7's 2015 base already differs from the actual
# 2015 count, so measure forecast error in growth from 2015 (h = year - 2015).
e15 = math.log(observed[2015] / forecast[2015])
g = {y: e[y] - e15 for y in (2016, 2017, 2018)}
growth = {y: abs(g[y]) / math.sqrt(y - 2015) for y in (2016, 2017, 2018)}
pooled15 = math.sqrt((g[2016] ** 2 + (g[2017] - g[2016]) ** 2 + (g[2018] - g[2017]) ** 2) / 3)

with open(OUT, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["year", "forecast_us_netflix_m", "observed_us_paid_memberships_m", "log_ratio"])
    for y in (2015, 2016, 2017, 2018):
        w.writerow([y, forecast[y], round(observed[y], 3), round(math.log(observed[y] / forecast[y]), 4)])
    w.writerow(["sigma_tech", "", "", round(sigma_tech, 4)])
    for y, v in per_year.items():
        w.writerow([f"sigma_tech_{y}", "", "", round(v, 4)])
    w.writerow(["sigma_tech_pooled_2016_2018", "", "", round(pooled, 4)])
    for y, v in growth.items():
        w.writerow([f"sigma_growth_2015_{y}", "", "", round(v, 4)])
    w.writerow(["sigma_growth_pooled_2015_2018", "", "", round(pooled15, 4)])
print("observed (M):", observed)
print("forecast (M):", {y: forecast[y] for y in (2016, 2017, 2018)})
print(f"sigma_tech = {sigma_tech:.4f}; per year {per_year}; pooled {pooled:.4f}; 2015 offset {e15:+.4f}; growth {growth}; pooled from 2015 {pooled15:.4f}")
