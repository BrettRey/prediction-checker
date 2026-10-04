#!/usr/bin/env python3
"""[post hoc] k with the baseline's annual error scale sigma integrated out
(case 2), added after the outcome data was opened. Specification fixed in
DECISIONS.md (2026-10-04) before this was run. Nothing here replaces the
pre-stated reading, which conditions on a calibrated sigma.

Model as in section 3: y = k delta + e, with e a random walk from 2014
(covariance sigma^2 * min(h, h')), a flat prior on k, the as-published
series, 2016-2019. Given sigma, k is normal with mean k-hat (which doesn't
depend on sigma) and variance sigma^2 / delta' Omega^-1 delta. Integrating k
out leaves a likelihood for sigma from the outcome residuals,
sigma^-(n-1) exp(-RSS / 2 sigma^2), with 3 degrees of freedom.

Priors on sigma:
  primary    uniform on 1% to 8% a year (the plan's sensitivity range);
  secondary  the report's 2010-2014 volatility treated as data:
             sigma^2 ~ scaled-inverse-chi^2(3, s_hist^2).

Two versions of each (DECISIONS.md, 2026-10-04): the specified one, in which
the outcome residuals also inform sigma, and a prior-only one, computed after
the specified one had been seen, in which the prior alone sets sigma (closer
to section 3, where sigma is calibrated, not estimated from the outcomes).

The posterior for k is a normal scale mixture, computed on a grid over sigma
and checked by Monte Carlo. Output: data/derived/sigma_integrated_lttv.csv.
"""

import csv
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crtc_outcomes_lttv import HIGH, LOW, YEARS, forecast, observed, scen_impact, verdict  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DER = ROOT / "data" / "derived"
GRID = np.arange(0.001, 0.2, 0.0001)        # sigma, a year
GRID_WIDE = np.arange(0.001, 1.0, 0.0001)   # check: how far the 95% ends move if the grid runs to 100%
PRIOR_RANGE = (0.01, 0.08)                  # the plan's sensitivity range
NU_HIST = 3                                 # four annual changes, 2010-2014
SEED = 20261004
SERIES = ("specialty_pay_revenue", "bdu_revenue")


def norm_cdf(x):
    return 0.5 * (1 + np.vectorize(math.erf)(x / math.sqrt(2)))


def mixture_quantile(p, khat, scales, w):
    lo, hi = khat - 50 * scales.max(), khat + 50 * scales.max()
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if np.sum(w * norm_cdf((mid - khat) / scales)) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def weighted_quantile(x, w, p):
    c = np.cumsum(w) / np.sum(w)
    return float(x[np.searchsorted(c, p)])


def main():
    obs, fc = observed(), forecast()
    h = np.array([t - 2014 for t in YEARS], dtype=float)
    Oinv = np.linalg.inv(np.minimum.outer(h, h))  # sigma = 1
    n = len(YEARS)
    rng = np.random.default_rng(SEED)
    out = []
    for q in SERIES:
        B = np.array([fc[(q, t)]["B"] for t in YEARS])
        I = np.array([fc[(q, t)]["I"] for t in YEARS])
        delta = np.log(B) - np.log(B - I)
        y = np.log(B) - np.log(np.array([obs[q][t] for t in YEARS]))
        d_lo = np.log(B) - np.log(B - np.array([scen_impact(fc, q, t, LOW) for t in YEARS]))
        d_hi = np.log(B) - np.log(B - np.array([scen_impact(fc, q, t, HIGH) for t in YEARS]))
        info1 = delta @ Oinv @ delta
        khat = (delta @ Oinv @ y) / info1
        band_lo, band_hi = (delta @ Oinv @ d_lo) / info1, (delta @ Oinv @ d_hi) / info1
        rss = y @ Oinv @ y - (delta @ Oinv @ y) ** 2 / info1
        loglik = -(n - 1) * np.log(GRID) - rss / (2 * GRID ** 2)
        loglik_w = -(n - 1) * np.log(GRID_WIDE) - rss / (2 * GRID_WIDE ** 2)

        hist = np.diff(np.log([fc[(q, t)]["B"] for t in range(2010, 2015)]))
        s_hist = float(np.std(hist, ddof=1))
        def prior_fns(g):
            return {
                "uniform 1-8% (plan's sensitivity range)":
                    np.where((g >= PRIOR_RANGE[0]) & (g <= PRIOR_RANGE[1]), 0.0, -np.inf),
                "historical volatility as data (scaled-inv-chi2, 3 df)":
                    -(NU_HIST + 1) * np.log(g) - NU_HIST * s_hist ** 2 / (2 * g ** 2),
            }
        priors, priors_w = prior_fns(GRID), prior_fns(GRID_WIDE)
        for (pname, logprior), (sigma_from, use_lik) in ((pp, v) for pp in priors.items()
                                                          for v in (("prior and outcomes", True), ("prior only", False))):
            lp = logprior + (loglik if use_lik else 0.0)
            w = np.exp(lp - lp[np.isfinite(lp)].max())
            w[~np.isfinite(lp)] = 0.0
            w /= w.sum()
            scales = GRID / math.sqrt(info1)
            keep = w > 1e-14
            qs = {p: mixture_quantile(p, khat, scales[keep], w[keep]) for p in (0.025, 0.25, 0.5, 0.75, 0.975)}
            lpw = priors_w[pname] + (loglik_w if use_lik else 0.0)
            ww = np.exp(lpw - lpw[np.isfinite(lpw)].max())
            ww[~np.isfinite(lpw)] = 0.0
            ww /= ww.sum()
            kw = ww > 1e-14
            wide = [mixture_quantile(p, khat, GRID_WIDE[kw] / math.sqrt(info1), ww[kw]) for p in (0.025, 0.975)]
            # Monte Carlo check of the 95% interval.
            sig = rng.choice(GRID, size=400_000, p=w)
            draws = khat + rng.standard_normal(sig.size) * sig / math.sqrt(info1)
            mc_lo, mc_hi = np.quantile(draws, [0.025, 0.975])
            assert abs(mc_lo - qs[0.025]) < 0.03 and abs(mc_hi - qs[0.975]) < 0.03, (q, pname, sigma_from, mc_lo, mc_hi, qs)
            out.append(dict(
                quantity=q, prior=pname, sigma_from=sigma_from, s_hist=round(s_hist, 4),
                k_hat=round(khat, 4), k_median=round(qs[0.5], 4),
                lo95=round(qs[0.025], 4), hi95=round(qs[0.975], 4),
                lo50=round(qs[0.25], 4), hi50=round(qs[0.75], 4),
                sigma_median=round(weighted_quantile(GRID, w, 0.5), 4),
                sigma_lo95=round(weighted_quantile(GRID, w, 0.025), 4),
                sigma_hi95=round(weighted_quantile(GRID, w, 0.975), 4),
                band_lo=round(band_lo, 4), band_hi=round(band_hi, 4),
                p_below_band=round(float(np.mean(draws < band_lo)), 4),
                verdict95=verdict(qs[0.025], qs[0.975], band_lo, band_hi),
                mc_lo95=round(float(mc_lo), 4), mc_hi95=round(float(mc_hi), 4),
                lo95_grid100=round(wide[0], 4), hi95_grid100=round(wide[1], 4),
            ))
    with open(DER / "sigma_integrated_lttv.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    for r in out:
        print(r)


if __name__ == "__main__":
    main()
