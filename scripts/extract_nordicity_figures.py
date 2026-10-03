#!/usr/bin/env python3
"""Extract bar-chart values from the Nordicity/Miller (2015) report.

Reads the data labels printed on the report's stacked bar charts, using word
coordinates from poppler's `pdftotext -bbox`. Each label is assigned to the
year column whose x-axis tick it sits above, and to a series by its height in
the stack (lowest label = lowest segment), following the legend order given
below. Nothing is read off by eye.

Outputs
  data/derived/nordicity_2015_figure_labels.csv   every label, with position
  data/derived/nordicity_2015_scenarios.csv       per quantity and year: LTTV
                                                  level, impacts, baseline level
and prints consistency checks against totals stated in the report's text.

Source PDF: literature/nordicity_miller_2015_canadian_television_2020.pdf
(sha256 recorded in its .md companion). Printed page = PDF page - 4.
"""
import csv
import html as htmllib
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT.parents[2] / "literature" / "nordicity_miller_2015_canadian_television_2020.pdf"
OUT = ROOT / "data" / "derived"

YEARS = list(range(2010, 2021))

# figure number -> (PDF page, series from the bottom of each stack upwards)
FIGURES = {
    8: (28, ["cmf", "independent_funds", "community_channels", "stack_total"]),
    9: (28, ["specialty", "cbc_src_conventional", "private_conventional", "pay_ppv_vod", "stack_total"]),
    34: (81, ["lttv_level", "unbundling"]),
    35: (82, ["lttv_level", "unbundling"]),
    36: (84, ["lttv_level", "unbundling", "preponderance_access"]),
    39: (87, ["lttv_level", "unbundling", "preponderance_access", "exemption_order"]),
    40: (88, ["lttv_level", "unbundling", "exemption_order"]),
    41: (90, ["lttv_level", "unbundling", "preponderance_access", "exemption_order", "closures"]),
    42: (91, ["lttv_level", "unbundling", "exemption_order", "closures"]),
    43: (92, ["lttv_level", "programming_services_cpe", "bdu_contributions"]),
    20: (62, ["baseline_level"]),
}
FIGURE_YEARS = {20: list(range(2007, 2021))}

# Labels the chart nudged sideways off their own bar, found by listing every label
# more than half a column from the nearest tick. Keyed by (figure, value, rounded x).
# Each is confirmed by the cross-figure identities checked in main(): the same
# component carries the same value in every figure that shows it.
OVERRIDES = {
    (39, 53, 379): 2016,   # exemption order 2016; sits in the 2016 stack above 138 and 9
    (39, 102, 411): 2017,  # exemption order 2017; Fig. 41 shows 102 in the 2017 column
}

WORD = re.compile(
    r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>'
)
NUM = re.compile(r"^\d{1,3}(,\d{3})*$")
TICK = re.compile(r"^'(\d\d)F?$")


def words_on(page):
    html = subprocess.run(
        ["pdftotext", "-bbox", "-f", str(page), "-l", str(page), str(PDF), "-"],
        check=True, capture_output=True, text=True,
    ).stdout
    return [
        ((float(a) + float(c)) / 2, float(b), htmllib.unescape(w))
        for a, b, c, d, w in WORD.findall(html)
    ]


def figure_band(words, fig):
    """y-range from the figure's caption to the next 'Source:' line."""
    cap = None
    for i, (x, y, w) in enumerate(words):
        if w == "Figure" and i + 1 < len(words) and words[i + 1][2] == str(fig):
            cap = y
            break
    if cap is None:
        sys.exit(f"Figure {fig}: caption not found")
    src = min(y for x, y, w in words if w == "Source:" and y > cap)
    return cap, src


def extract(fig, page, series):
    years = FIGURE_YEARS.get(fig, YEARS)
    words = words_on(page)
    top, bottom = figure_band(words, fig)
    ticks = [(x, 2000 + int(TICK.match(w).group(1)))
             for x, y, w in words if top < y < bottom + 40 and TICK.match(w)]
    ticks = sorted(set(ticks))
    if [yr for _, yr in ticks] != years:
        sys.exit(f"Figure {fig}: expected ticks {years[0]}-{years[-1]}, got {[yr for _, yr in ticks]}")
    xs = [x for x, _ in ticks]
    half = (xs[1] - xs[0]) / 2
    cols = defaultdict(list)
    for x, y, w in words:
        if not (top < y < bottom) or not NUM.match(w):
            continue
        if x < xs[0] - half:  # y-axis tick labels
            continue
        val = int(w.replace(",", ""))
        forced = OVERRIDES.get((fig, val, round(x)))
        if forced is not None:
            cols[forced].append((y, val, x))
            continue
        j = min(range(len(xs)), key=lambda k: abs(xs[k] - x))
        if abs(xs[j] - x) <= half:
            cols[years[j]].append((y, val, x))
    rows = []
    for yr in years:
        stack = sorted(cols[yr], key=lambda t: -t[0])  # lowest on page first
        if len(stack) > len(series):
            sys.exit(f"Figure {fig}, {yr}: {len(stack)} labels for {len(series)} series")
        for name, (y, v, x) in zip(series, stack):
            rows.append(dict(figure=fig, pdf_page=page, printed_page=page - 4,
                             year=yr, series=name, value=v, x=round(x, 1), y=round(y, 1)))
    return rows


def table7():
    """Report's US forecasts (Table 7, PDF p. 55): Netflix subscribers (Trefis),
    composite OTT subscribers, households, penetration. Policy-independent."""
    txt = subprocess.run(["pdftotext", "-layout", "-f", "55", "-l", "55", str(PDF), "-"],
                         check=True, capture_output=True, text=True).stdout
    def nums(label_regex, pct=False):
        line = next(l for l in txt.splitlines() if re.search(label_regex, l))
        vals = re.findall(r"(\d+(?:\.\d+)?)%" if pct else r"(?<![\d.])(\d+\.\d)(?![\d%])", line)
        return [float(v) for v in vals]
    out = {
        "us_netflix_subscribers_m": nums(r"^\s*\(M\)\s+45\.5"),
        "us_ott_subscribers_composite_m": nums(r"subscribers \(M\)†"),
        "us_households_m": nums(r"US households"),
        "us_ott_penetration": [v / 100 for v in nums(r"Penetration rate", pct=True)],
    }
    for k, v in out.items():
        if len(v) != 6:
            sys.exit(f"Table 7 {k}: expected 6 values for 2015-2020, got {v}")
    return out


def text_facts():
    """Forecast facts printed as text or tables: Table 1 (PDF p. 16), Table 18
    (PDF p. 80) and the stated CPE share (para. 239, PDF p. 91)."""
    def page(n):
        return subprocess.run(["pdftotext", "-layout", "-f", str(n), "-l", str(n), str(PDF), "-"],
                              check=True, capture_output=True, text=True).stdout
    p16, p80, p91 = page(16), page(80), page(91)
    def row(txt, label):
        line = next(l for l in txt.splitlines() if re.match(r"\s*" + label, l))
        return [float(v.replace(",", "")) for v in re.findall(r"\(?([\d,]+(?:\.\d)?)\)?", line.split(label, 1)[1])]
    # Table 1 rows appear in order Direct, Spin-off, Total for FTEs, then for GDP.
    lines16 = p16.splitlines()
    i_emp = next(i for i, l in enumerate(lines16) if "Employment (FTEs)" in l)
    i_gdp = next(i for i, l in enumerate(lines16) if "GDP ($M)" in l)
    def block(i0):
        vals = {}
        for l in lines16[i0 + 1:i0 + 4]:
            key = l.split()[0].rstrip("*").lower()
            vals[key] = [float(v.replace(",", "")) for v in re.findall(r"\(?([\d,]+(?:\.\d)?)\)?", l[l.index(l.split()[0]) + len(l.split()[0]):])]
        return vals
    emp, gdp = block(i_emp), block(i_gdp)
    nxt = p80.splitlines()
    k = next(i for i, l in enumerate(nxt) if "BYOP subscribers as a share" in l)
    byop = [float(v) for v in re.findall(r"(\d+)%", " ".join(nxt[k:k + 2]))]
    # Tables 22-23 (PDF pp. 95-96): 2020 employment totals by sector.
    p95, p96 = page(95), page(96)
    sectors = {}
    current = None
    for l in p95.splitlines():
        t = l.strip()
        for name in ("BDUs", "Specialty and pay TV services", "Private conventional TV", "Total broadcasting sector"):
            if t == name:
                current, in_emp = name, False
        if t.startswith("Employment (FTEs)"):
            in_emp = True
        elif t.startswith("GDP ($M)"):
            in_emp = False
        if current and in_emp and t.startswith("Total") and current not in sectors:
            sectors[current] = [float(v.replace(",", "")) for v in re.findall(r"\(?([\d,]+)\)?", t[len("Total"):])]
    l23 = next(l for l in p96.splitlines() if l.strip().startswith("Total") and "(" in l and "Employment" not in l
               and p96.splitlines().index(l) > next(i for i, x in enumerate(p96.splitlines()) if "Employment (FTEs)" in x))
    sectors["Independent production"] = [float(v.replace(",", "")) for v in re.findall(r"\(?([\d,]+)\)?", l23.strip()[len("Total"):])]
    stated = re.search(r"\$399 million reduction in CPE by 2020, or (\d+)% of baseline CPE", " ".join(p91.split()))
    return dict(table1_employment=emp, table1_gdp=gdp, table18_byop_share=byop, sector_employment=sectors,
                cpe_share_stated=float(stated.group(1)) if stated else None)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    labels = []
    for fig, (page, series) in FIGURES.items():
        labels += extract(fig, page, series)
    with open(OUT / "nordicity_2015_figure_labels.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(labels[0]))
        w.writeheader()
        w.writerows(labels)

    v = {(r["figure"], r["year"], r["series"]): r["value"] for r in labels}

    def get(fig, yr, s, default=None):
        return v.get((fig, yr, s), default)

    # Specialty and pay revenue (Fig. 41); 2016 impacts are unlabelled there, so
    # take each component from the figure that introduces it (35, 36, 39).
    # Closures carry no 2016 label in Fig. 41; recorded as missing, not zero.
    scen = []
    for yr in YEARS:
        comp = {}
        for s, alt in [("unbundling", 35), ("preponderance_access", 36),
                       ("exemption_order", 39), ("closures", None)]:
            val = get(41, yr, s)
            src = "41"
            if val is None and alt is not None:
                val, src = get(alt, yr, s), str(alt)
            comp[s] = (val, src)
        level = get(41, yr, "lttv_level")
        known = [c for c, _ in comp.values() if c is not None]
        scen.append(dict(quantity="specialty_pay_revenue", year=yr, lttv_level=level,
                         **{k: c for k, (c, _) in comp.items()},
                         impact_total=sum(known) if known else 0,
                         components_missing=";".join(k for k, (c, _) in comp.items()
                                                     if c is None and yr >= 2016),
                         component_sources=";".join(f"{k}:{s}" for k, (c, s) in comp.items()
                                                    if c is not None)))
    # BDU revenue (Fig. 42), 2016 from Figs. 34 and 40.
    for yr in YEARS:
        comp = {}
        for s, alt in [("unbundling", 34), ("exemption_order", 40), ("closures", None)]:
            val, src = get(42, yr, s), "42"
            if val is None and alt is not None:
                val, src = get(alt, yr, s), str(alt)
            comp[s] = (val, src)
        known = [c for c, _ in comp.values() if c is not None]
        scen.append(dict(quantity="bdu_revenue", year=yr, lttv_level=get(42, yr, "lttv_level"),
                         **{k: c for k, (c, _) in comp.items()},
                         impact_total=sum(known) if known else 0,
                         components_missing=";".join(k for k, (c, _) in comp.items()
                                                     if c is None and yr >= 2016),
                         component_sources=";".join(f"{k}:{s}" for k, (c, s) in comp.items()
                                                    if c is not None)))
    # CPE (Fig. 43).
    for yr in YEARS:
        a = get(43, yr, "programming_services_cpe")
        b = get(43, yr, "bdu_contributions")
        known = [c for c in (a, b) if c is not None]
        scen.append(dict(quantity="cpe", year=yr, lttv_level=get(43, yr, "lttv_level"),
                         programming_services_cpe=a, bdu_contributions=b,
                         impact_total=sum(known) if known else 0,
                         components_missing="", component_sources="43"))
    # Closures carry no 2016 label. Where the figure without closures (39, 40)
    # shows the same level as the full figure (41, 42), closures that year are zero.
    for r in scen:
        if r["year"] == 2016 and "closures" in r["components_missing"]:
            partial = 39 if r["quantity"] == "specialty_pay_revenue" else 40
            full = 41 if r["quantity"] == "specialty_pay_revenue" else 42
            if abs(get(partial, 2016, "lttv_level") - get(full, 2016, "lttv_level")) <= 1:
                r["closures"] = 0
                r["components_missing"] = ""
                r["component_sources"] += f";closures:0 from fig {partial} level = fig {full} level"
    for r in scen:
        r["baseline_level"] = (r["lttv_level"] + r["impact_total"]) if r["lttv_level"] is not None else None
        r["impact_share_of_baseline"] = (round(r["impact_total"] / r["baseline_level"], 4)
                                         if r["baseline_level"] else None)
    fields = ["quantity", "year", "lttv_level", "baseline_level", "impact_total",
              "impact_share_of_baseline", "unbundling", "preponderance_access",
              "exemption_order", "closures", "programming_services_cpe",
              "bdu_contributions", "components_missing", "component_sources"]
    with open(OUT / "nordicity_2015_scenarios.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(scen)

    # Checks against totals stated in the report's text.
    def row(q, yr):
        return next(r for r in scen if r["quantity"] == q and r["year"] == yr)
    checks = [
        ("specialty/pay impact 2020 = $970M (¶235)", row("specialty_pay_revenue", 2020)["impact_total"], 970),
        ("BDU retail impact 2020 = $858M (¶237)", row("bdu_revenue", 2020)["impact_total"], 858),
        ("CPE impact 2020 = $399M (¶239)", row("cpe", 2020)["impact_total"], 399),
        ("CPE programming services 2020 = $352M (¶239)", row("cpe", 2020)["programming_services_cpe"], 352),
        ("unbundling on specialty/pay 2020 = $466M (¶209)", row("specialty_pay_revenue", 2020)["unbundling"], 466),
        ("preponderance 2020 = $173M (¶214)", row("specialty_pay_revenue", 2020)["preponderance_access"], 173),
        ("exemption order on specialty/pay 2020 = $229M (¶226)", row("specialty_pay_revenue", 2020)["exemption_order"], 229),
        ("closures on specialty/pay 2020 = $102M (¶235)", row("specialty_pay_revenue", 2020)["closures"], 102),
        ("unbundling on BDU 2020 = $488M (¶205)", row("bdu_revenue", 2020)["unbundling"], 488),
        ("exemption order on BDU 2020 = $234M (¶228)", row("bdu_revenue", 2020)["exemption_order"], 234),
        ("closures on BDU 2020 = $136M (¶237)", row("bdu_revenue", 2020)["closures"], 136),
    ]
    # Cross-figure identities: a component has one value wherever it appears, and
    # the level in a figure showing fewer components exceeds the full figure's
    # level by the omitted components (allowing 1 for rounding).
    def same(series, figs):
        for yr in range(2016, 2021):
            vals = {f: get(f, yr, series) for f in figs if get(f, yr, series) is not None}
            if len(set(vals.values())) > 1:
                checks.append((f"{series} {yr} equal across figs {sorted(vals)}", vals, "equal"))
            elif vals:
                checks.append((f"{series} {yr} equal across figs {sorted(vals)}", "equal", "equal"))
    same("unbundling", [35, 36, 39, 41])
    same("preponderance_access", [36, 39, 41])
    same("exemption_order", [39, 41])
    same("unbundling", [34, 40, 42])
    same("exemption_order", [40, 42])
    for yr in range(2016, 2021):
        for partial, full, omitted in [(39, 41, ["closures"]), (40, 42, ["closures"]),
                                       (36, 39, ["exemption_order"]), (35, 36, ["preponderance_access"])]:
            lp, lf = get(partial, yr, "lttv_level"), get(full, yr, "lttv_level")
            om = sum(get(full, yr, s, 0) or 0 for s in omitted)
            good = lp is not None and lf is not None and abs(lp - lf - om) <= 1
            checks.append((f"level fig {partial} - fig {full} = {'+'.join(omitted)} ({yr})",
                           "ok" if good else (lp, lf, om), "ok"))

    # Fig. 20 is the baseline BDU revenue figure; it should match level + impacts.
    for yr in range(2016, 2021):
        f20 = get(20, yr, "baseline_level")
        derived = row("bdu_revenue", yr)["baseline_level"]
        checks.append((f"Fig. 20 baseline BDU revenue {yr} = Fig. 42 level + impacts",
                       "ok" if f20 is not None and abs(f20 - derived) <= 1 else (f20, derived), "ok"))

    t7 = table7()
    with open(OUT / "nordicity_2015_us_ott_forecast.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["year"] + list(t7))
        for i, yr in enumerate(range(2015, 2021)):
            w.writerow([yr] + [t7[k][i] for k in t7])
    t7_notes = []
    for i, yr in enumerate(range(2015, 2021)):
        pen = t7["us_ott_subscribers_composite_m"][i] / t7["us_households_m"][i]
        if abs(pen - t7["us_ott_penetration"][i]) > 0.005 + 1e-9:
            t7_notes.append(f"Table 7 {yr}: printed penetration {t7['us_ott_penetration'][i]:.2f}, "
                            f"composite / households = {pen:.3f}")

    tf = text_facts()
    with open(OUT / "nordicity_2015_text_facts.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["fact", "year", "value", "source"])
        for key, src in (("table1_employment", "Table 1, p. 12"), ("table1_gdp", "Table 1, p. 12")):
            for kind, vals in tf[key].items():
                for yr, val in zip(range(2015, 2021), vals):
                    w.writerow([f"{key}_{kind}", yr, val, src])
        for yr, val in zip(range(2015, 2021), tf["table18_byop_share"]):
            w.writerow(["table18_byop_share_pct", yr, val, "Table 18, p. 76"])
        w.writerow(["cpe_share_stated_pct", 2020, tf["cpe_share_stated"], "para. 239, p. 87"])
        for name, vals in tf["sector_employment"].items():
            key = "sector_fte_" + re.sub(r"[^a-z]+", "_", name.lower()).strip("_")
            for yr, val in zip(range(2015, 2021), vals):
                w.writerow([key, yr, val, "Tables 22-23, pp. 91-92"])
    checks.append(("Table 1 total FTE 2020 = 15,130 (para. 250)", tf["table1_employment"]["total"][-1], 15130))
    checks.append(("Table 1 direct FTE 2020 = 6,830", tf["table1_employment"]["direct"][-1], 6830))
    checks.append(("Table 1 total GDP 2020 = 1,411.1", tf["table1_gdp"]["total"][-1], 1411.1))
    checks.append(("Table 18 BYOP 2018 = 15%", tf["table18_byop_share"][3] if len(tf["table18_byop_share"]) > 3 else None, 15))
    checks.append(("stated CPE share = 18% (para. 239)", tf["cpe_share_stated"], 18))
    se = tf["sector_employment"]
    checks.append(("Table 22 BDU FTE 2020 = 5,010", se.get("BDUs", [None])[-1], 5010))
    checks.append(("Table 22 specialty/pay FTE 2020 = 2,880", se.get("Specialty and pay TV services", [None])[-1], 2880))
    checks.append(("Table 22 broadcasting total FTE 2020 = 7,950 (para. 246)", se.get("Total broadcasting sector", [None])[-1], 7950))
    checks.append(("Table 23 production FTE 2020 = 7,180 (para. 248)", se.get("Independent production", [None])[-1], 7180))
    checks.append(("broadcasting + production = Table 1 total",
                   se["Total broadcasting sector"][-1] + se["Independent production"][-1], tf["table1_employment"]["total"][-1]))

    ok = True
    for name, got, want in checks:
        flag = "ok" if got == want else "MISMATCH"
        ok &= got == want
        print(f"{flag:8} {name}: extracted {got}")
    for yr in (2018, 2020):
        f8, f9 = get(8, yr, "stack_total"), get(9, yr, "stack_total")
        if f8 is not None and f9 is not None:
            print(f"{'note':8} baseline CPE {yr} from Figs. 8+9 (baseline scenario): {f8} + {f9} = {f8 + f9}; "
                  f"Fig. 43 baseline {row('cpe', yr)['baseline_level']}")
    for n in t7_notes:
        print(f"{'note':8} {n}")
    yr = 2020
    f9 = {k: get(9, yr, k) for k in ("specialty", "cbc_src_conventional", "private_conventional", "pay_ppv_vod", "stack_total")}
    f8 = get(8, yr, "stack_total")
    imp, ps_imp = row("cpe", yr)["impact_total"], row("cpe", yr)["programming_services_cpe"]
    cands = {
        "all CPE (Figs. 8+9)": (imp, f9["stack_total"] + f8),
        "programming services only": (imp, f9["stack_total"]),
        "programming services excl. CBC/SRC": (imp, f9["stack_total"] - f9["cbc_src_conventional"]),
        "excl. CBC/SRC, with BDU contributions": (imp, f9["stack_total"] - f9["cbc_src_conventional"] + f8),
        "private (specialty+private conv.+pay) + BDU": (imp, f9["specialty"] + f9["private_conventional"] + f9["pay_ppv_vod"] + f8),
        "specialty + pay": (imp, f9["specialty"] + f9["pay_ppv_vod"]),
        "specialty only": (imp, f9["specialty"]),
        "$352M programming-services impact / programming services": (ps_imp, f9["stack_total"]),
        "$352M / programming services excl. CBC/SRC": (ps_imp, f9["stack_total"] - f9["cbc_src_conventional"]),
        "$352M / specialty + pay": (ps_imp, f9["specialty"] + f9["pay_ppv_vod"]),
        "$399M / 2020 LTTV-scenario CPE (Fig. 43 level)": (imp, row("cpe", yr)["lttv_level"]),
    }
    print(f"{'note':8} Fig. 9 2020 components: {f9}; Fig. 8 2020 total: {f8}")
    for name, (num, den) in cands.items():
        print(f"{'cpe18':8} {name}: {num}/{den} = {num / den:.3f}")
    for q, stated, para in [("specialty_pay_revenue", 0.23, "¶235"), ("bdu_revenue", 0.09, "¶237"),
                            ("cpe", 0.18, "¶239")]:
        r = row(q, 2020)
        print(f"{'note':8} {q} 2020: impact {r['impact_total']} / baseline {r['baseline_level']} "
              f"= {r['impact_share_of_baseline']:.3f} (text {para} says {stated:.2f})")
    for r in scen:
        if r["components_missing"]:
            print(f"{'gap':8} {r['quantity']} {r['year']}: no label for {r['components_missing']}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
