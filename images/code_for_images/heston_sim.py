"""Monte Carlo simulation of the Heston model (Chapter 7).

Pedagogical figure after the course slides: sample paths of the asset price
and of its stochastic volatility in the Heston model, with negative
price-volatility correlation (leverage effect). Full truncation Euler scheme.
Output: images/heston_sim.pdf
"""
from pathlib import Path

import numpy as np

from _style import plt

rng = np.random.default_rng(14)

# Heston parameters (original-paper notation)
S0, v0 = 25.0, 0.0156          # v0 = (12.5% annual vol)^2
kappa, theta, sigma = 2.0, 0.02, 0.35
mu, rho = 0.05, -0.125
T, N, n_paths = 1.0, 2000, 6
dt = T / N
t = np.linspace(0, T, N + 1)

S = np.empty((n_paths, N + 1)); S[:, 0] = S0
v = np.empty((n_paths, N + 1)); v[:, 0] = v0
for n in range(N):
    z1 = rng.standard_normal(n_paths)
    z2 = rho * z1 + np.sqrt(1 - rho**2) * rng.standard_normal(n_paths)
    vp = np.maximum(v[:, n], 0.0)           # full truncation
    S[:, n + 1] = S[:, n] * np.exp((mu - 0.5 * vp) * dt
                                   + np.sqrt(vp * dt) * z1)
    v[:, n + 1] = v[:, n] + kappa * (theta - vp) * dt \
        + sigma * np.sqrt(vp * dt) * z2

fig, (axS, axv) = plt.subplots(1, 2, figsize=(6.4, 3.0))
for k in range(n_paths):
    axS.plot(t, S[k], lw=0.7)
    axv.plot(t, 100 * np.sqrt(np.maximum(v[k], 0)), lw=0.7)
axS.set_xlabel(r"$t$ (years)")
axS.set_ylabel(r"price $S(t)$")
axS.set_title("asset price", fontsize=9)
axv.set_xlabel(r"$t$ (years)")
axv.set_ylabel(r"volatility $\sqrt{v(t)}$ (%)")
axv.set_title("stochastic volatility", fontsize=9)

out = Path(__file__).resolve().parent.parent / "heston_sim.pdf"
fig.savefig(out)
print(f"saved {out}")
