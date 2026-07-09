"""Monte Carlo ensemble of Ornstein-Uhlenbeck trajectories (Chapter 4).

Simulates the OU process dx = -kappa*x*dt + sqrt(D)*dW from a common initial
condition x0, showing the noisy relaxation to the stationary band, together
with the analytic mean x0*exp(-kappa t) and the +-1 s.d. envelope
sqrt(D/(2 kappa) * (1 - exp(-2 kappa t))). Output: images/ou_ensemble.pdf
"""
from pathlib import Path

import numpy as np

from _style import plt, FIGSIZE_WIDE, BLUE, RED, GRAY

rng = np.random.default_rng(7)

KAPPA, D, X0 = 2.0, 1.0, 3.0
T, N_STEPS, N_PATHS = 4.0, 2000, 200
dt = T / N_STEPS
t = np.linspace(0.0, T, N_STEPS + 1)

x = np.empty((N_PATHS, N_STEPS + 1))
x[:, 0] = X0
noise = rng.standard_normal((N_PATHS, N_STEPS)) * np.sqrt(D * dt)
for n in range(N_STEPS):
    x[:, n + 1] = x[:, n] - KAPPA * x[:, n] * dt + noise[:, n]

mean = X0 * np.exp(-KAPPA * t)
sd = np.sqrt(D / (2 * KAPPA) * (1.0 - np.exp(-2 * KAPPA * t)))

fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)
for i in range(N_PATHS):
    ax.plot(t, x[i], color=BLUE, alpha=0.06, lw=0.5)
ax.plot(t, x[0], color=GRAY, lw=0.8)
ax.plot(t, mean, color=RED, lw=1.4, label=r"$\langle x(t)\rangle = x_0 e^{-\kappa t}$")
ax.plot(t, mean + sd, color="k", ls="--", lw=1.0,
        label=r"$\langle x\rangle \pm \mathrm{s.d.}[x(t)]$")
ax.plot(t, mean - sd, color="k", ls="--", lw=1.0)
ax.axhline(np.sqrt(D / (2 * KAPPA)), color=GRAY, ls=":", lw=0.9)
ax.axhline(-np.sqrt(D / (2 * KAPPA)), color=GRAY, ls=":", lw=0.9)
ax.text(T * 0.99, np.sqrt(D / (2 * KAPPA)) + 0.12,
        r"$\pm\sqrt{D/2\kappa}$", ha="right", fontsize=9, color="k")
ax.set_xlabel(r"$t$")
ax.set_ylabel(r"$x(t)$")
ax.set_xlim(0, T)
ax.legend(loc="upper right", frameon=False)

out = Path(__file__).resolve().parent.parent / "ou_ensemble.pdf"
fig.savefig(out)
print(f"saved {out}")
