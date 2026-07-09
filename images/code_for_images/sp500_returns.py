"""S&P 500 daily log-returns: volatility clustering and fat tails (Chapter 7).

Data: FRED series SP500 (daily closes, ~10 years), downloaded from
https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500
and stored in data/SP500.csv.

Outputs:
  images/sp500_logreturns.pdf  - time series of daily log-returns (clustering)
  images/sp500_ccdf.pdf        - log-log CCDF of |normalized returns| vs Gaussian,
                                 with the alpha ~ 3 (inverse cubic) guide line
  images/sp500_vs_gbm.pdf      - real S&P 500 path vs a GBM simulated with the
                                 same daily (mu, sigma) and same starting price
"""
import csv
from datetime import date
from math import erf
from pathlib import Path

import numpy as np

from _style import plt, FIGSIZE_WIDE, BLUE, RED, GRAY

here = Path(__file__).resolve().parent
dates, closes = [], []
with open(here / "data" / "SP500.csv") as f:
    for row in csv.DictReader(f):
        if row["SP500"] in ("", "."):
            continue
        y, m, d = (int(s) for s in row["observation_date"].split("-"))
        dates.append(date(y, m, d))
        closes.append(float(row["SP500"]))

closes = np.array(closes)
r = np.diff(np.log(closes))          # daily log-returns
z = (r - r.mean()) / r.std()         # normalized returns
tdates = np.array(dates[1:])

# --- Figure 1: the time series (volatility clustering) --------------------
fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)
ax.plot(tdates, r * 100, color=BLUE, lw=0.4)
ax.set_xlabel("year")
ax.set_ylabel("daily log-return (%)")
ax.annotate("Feb--Mar 2020", xy=(date(2020, 3, 16), -12.0),
            xytext=(date(2022, 6, 1), -9.5), fontsize=8.5,
            arrowprops=dict(arrowstyle="->", lw=0.7))
fig.savefig(here.parent / "sp500_logreturns.pdf")
print("saved sp500_logreturns.pdf")

# --- Figure 2: CCDF of |z| in log-log, vs Gaussian ------------------------
za = np.sort(np.abs(z))
ccdf = 1.0 - np.arange(1, len(za) + 1) / len(za)
mask = ccdf > 0

x = np.logspace(np.log10(0.1), np.log10(za.max()), 200)
gauss_ccdf = np.array([1.0 - erf(v / np.sqrt(2.0)) for v in x])  # P(|Z|>x)

fig, ax = plt.subplots(figsize=(4.6, 3.6))
ax.loglog(za[mask], ccdf[mask], ".", color=BLUE, ms=3,
          label="S&P 500 daily $|z|$")
ax.loglog(x, gauss_ccdf, color=GRAY, ls="--", lw=1.1, label="Gaussian")
xg = np.logspace(np.log10(2.5), np.log10(za.max()), 50)
ax.loglog(xg, 0.35 * xg**-3.0, color=RED, lw=1.1,
          label=r"$\propto |z|^{-3}$")
ax.set_xlabel(r"$|z|$ (normalized return)")
ax.set_ylabel(r"$P_>(|z|)$")
ax.set_xlim(0.1, za.max() * 1.5)
ax.set_ylim(1.0 / len(za) / 3, 1.2)
ax.legend(loc="lower left", frameon=False)
fig.savefig(here.parent / "sp500_ccdf.pdf")
print("saved sp500_ccdf.pdf")

# --- Figure 3: real S&P 500 vs GBM at the same (mu, sigma) -----------------
rng = np.random.default_rng(11)
m, s = r.mean(), r.std()                     # daily log-return moments
gbm = np.empty_like(closes)
gbm[0] = closes[0]
gbm[1:] = closes[0] * np.exp(np.cumsum(m + s * rng.standard_normal(len(r))))

fig, axes = plt.subplots(2, 1, figsize=(6.0, 4.4), sharex=True,
                         gridspec_kw={"hspace": 0.10})
axes[0].plot(np.array(dates), closes, color=BLUE, lw=0.7)
axes[0].text(0.02, 0.88, "real: S&P 500", transform=axes[0].transAxes, fontsize=9)
axes[1].plot(np.array(dates), gbm, color=RED, lw=0.7)
axes[1].text(0.02, 0.88, r"simulated: GBM, same $(\mu,\sigma)$",
             transform=axes[1].transAxes, fontsize=9)
for ax in axes:
    ax.set_ylabel(r"$S(t)$")
axes[1].set_xlabel("year")
fig.savefig(here.parent / "sp500_vs_gbm.pdf")
print("saved sp500_vs_gbm.pdf")
