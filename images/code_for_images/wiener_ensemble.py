"""Monte Carlo ensemble of Wiener trajectories (Chapter 4, fig:wiener-sim).

Simulates N_PATHS standard Wiener processes via dW = eps*sqrt(dt), eps ~ N(0,1),
and shows the sqrt(t) fan-out together with the Gaussian histogram of the
endpoints. Output: images/wiener_ensemble.pdf
"""
from pathlib import Path

import numpy as np

from _style import plt, FIGSIZE_WIDE, BLUE, RED, GRAY

rng = np.random.default_rng(42)

T, N_STEPS, N_PATHS = 1.0, 1000, 300
dt = T / N_STEPS
t = np.linspace(0.0, T, N_STEPS + 1)

dW = rng.standard_normal((N_PATHS, N_STEPS)) * np.sqrt(dt)
W = np.concatenate([np.zeros((N_PATHS, 1)), np.cumsum(dW, axis=1)], axis=1)

fig, (ax, axh) = plt.subplots(
    1, 2, figsize=FIGSIZE_WIDE, sharey=True,
    gridspec_kw={"width_ratios": [3.2, 1.0], "wspace": 0.06},
)

for i in range(N_PATHS):
    ax.plot(t, W[i], color=BLUE, alpha=0.08, lw=0.5)
ax.plot(t, W[0], color=RED, lw=1.0, label="one realization")
for sign in (+1, -1):
    ax.plot(t, sign * np.sqrt(t), color="k", ls="--", lw=1.0)
ax.plot([], [], color="k", ls="--", lw=1.0, label=r"$\pm\sqrt{t}$")
ax.set_xlabel(r"$t$")
ax.set_ylabel(r"$W(t)$")
ax.set_xlim(0, T)
ax.legend(loc="upper left", frameon=False)

# Terminal histogram vs the exact N(0, T) density.
axh.hist(W[:, -1], bins=25, density=True, orientation="horizontal",
         color=BLUE, alpha=0.45, edgecolor="none")
x = np.linspace(-3.5, 3.5, 300)
axh.plot(np.exp(-x**2 / (2 * T)) / np.sqrt(2 * np.pi * T), x,
         color=RED, lw=1.2, label=r"$\mathcal{N}(0,T)$")
axh.set_xlabel(r"$P(W,T)$")
axh.legend(loc="upper right", frameon=False)
axh.tick_params(left=False)

out = Path(__file__).resolve().parent.parent / "wiener_ensemble.pdf"
fig.savefig(out)
print(f"saved {out}")
