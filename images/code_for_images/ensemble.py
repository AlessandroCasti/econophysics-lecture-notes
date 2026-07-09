"""Realizations and ensemble of a stochastic process (Chapter 3).

Pedagogical figure after the course slides ("Processi Stocastici: definizioni
& classificazione"): several realizations x(t) of the same process, stacked to
suggest the ensemble (phase space); a vertical cut at time t0 across all
realizations defines the random variable X(t0).
Output: images/ensemble.pdf
"""
from pathlib import Path

import numpy as np

from _style import plt, BLUE, RED, GRAY

rng = np.random.default_rng(5)

T, N = 1.0, 600
t = np.linspace(0, T, N + 1)
n_paths = 5
offset = 2.6

fig, ax = plt.subplots(figsize=(6.0, 3.6))
for k in range(n_paths):
    dW = rng.standard_normal(N) * np.sqrt(T / N)
    x = np.concatenate([[0.0], np.cumsum(dW)])
    ax.plot(t, x + k * offset, color=BLUE, lw=0.8)
    ax.text(-0.02, k * offset, rf"$x^{{({k+1})}}(t)$", ha="right",
            va="center", fontsize=9)

t0 = 0.62
ax.axvline(t0, color=RED, lw=1.2)
ax.text(t0, n_paths * offset - 0.6, r"$X(t_0)$", color=RED, ha="center",
        fontsize=10)
ax.annotate("", xy=(1.0, -1.9), xytext=(0.0, -1.9),
            arrowprops=dict(arrowstyle="->", lw=0.8))
ax.text(0.5, -2.35, r"$t$", fontsize=10, ha="center")
ax.text(1.045, (n_paths - 1) * offset / 2, "ensemble\n(phase space)",
        fontsize=9, color=GRAY, va="center")

ax.set_xlim(-0.12, 1.25)
ax.set_ylim(-2.6, n_paths * offset)
ax.axis("off")

out = Path(__file__).resolve().parent.parent / "ensemble.pdf"
fig.savefig(out)
print(f"saved {out}")
