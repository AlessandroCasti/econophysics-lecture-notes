"""Stylized facts of S&P 500 daily returns (Chapter 7).

Two pedagogical figures after the course slides ("Econophysics of the
Financial Market Dynamics"):

  images/sp500_hist.pdf - histogram of normalized daily log-returns against
                          the Gaussian with the same mean and variance
                          (sharp central body + fat tails);
  images/sp500_acf.pdf  - sample autocorrelation of the returns (vanishing
                          within a lag or two: efficient-market behaviour)
                          against the autocorrelation of |returns| (slow
                          power-law decay ~ tau^-0.3: volatility clustering).

Data: FRED series SP500 in data/SP500.csv (as for sp500_returns.py).
"""
import csv
from pathlib import Path

import numpy as np

from _style import plt, FIGSIZE_WIDE, BLUE, RED, GRAY

here = Path(__file__).resolve().parent
closes = []
with open(here / "data" / "SP500.csv") as f:
    for row in csv.DictReader(f):
        if row["SP500"] in ("", "."):
            continue
        closes.append(float(row["SP500"]))
closes = np.array(closes)
r = np.diff(np.log(closes))
z = (r - r.mean()) / r.std()

# --- Figure 1: histogram vs Gaussian ---------------------------------------
fig, ax = plt.subplots(figsize=(5.2, 3.4))
ax.hist(z, bins=120, density=True, color=BLUE, alpha=0.55, edgecolor="none",
        label="S&P 500 daily $z$")
x = np.linspace(-6, 6, 400)
ax.plot(x, np.exp(-x**2 / 2) / np.sqrt(2 * np.pi), color=RED, lw=1.2,
        label=r"$\mathcal{N}(0,1)$")
ax.set_xlim(-6, 6)
ax.set_xlabel(r"normalized daily log-return $z$")
ax.set_ylabel("probability density")
ax.legend(frameon=False)
fig.savefig(here.parent / "sp500_hist.pdf")
print("saved sp500_hist.pdf")

# --- Figure 2: ACF of returns vs |returns| ----------------------------------
def acf(x, max_lag):
    x = x - x.mean()
    c0 = np.dot(x, x) / len(x)
    return np.array([np.dot(x[:-k], x[k:]) / (len(x) * c0)
                     for k in range(1, max_lag + 1)])

max_lag = 250
lags = np.arange(1, max_lag + 1)
acf_r = acf(z, max_lag)
acf_abs = acf(np.abs(z), max_lag)
noise = 1.96 / np.sqrt(len(z))

fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)
ax.plot(lags, acf_r, ".", ms=3, color=GRAY, label=r"returns $z_t$")
ax.plot(lags, acf_abs, ".", ms=3, color=BLUE, label=r"absolute returns $|z_t|$")
ax.plot(lags, 0.32 * lags**-0.3, color=RED, lw=1.1,
        label=r"$\propto \tau^{-0.3}$")
ax.axhspan(-noise, noise, color=GRAY, alpha=0.18, lw=0)
ax.set_xscale("log")
ax.set_xlabel(r"time lag $\tau$ (days)")
ax.set_ylabel("autocorrelation")
ax.set_ylim(-0.1, 0.45)
ax.legend(frameon=False)
fig.savefig(here.parent / "sp500_acf.pdf")
print("saved sp500_acf.pdf")
