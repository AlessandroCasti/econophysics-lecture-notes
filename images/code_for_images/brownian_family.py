"""Family of Brownian trajectories with Gaussian cross-sections (Chapter 2).

Reproduces the figure pasted in the handwritten notes (PDF 1, page 10, purple
annotation "gaussiane con maggiore varianza"): an ensemble of standard
Brownian paths, cut at two times t1 < t2; the cross-section profiles are
Gaussians whose variance grows linearly in time.
Output: images/brownian_family.pdf
"""
from pathlib import Path

import numpy as np

from _style import plt, FIGSIZE_WIDE, BLUE, RED

rng = np.random.default_rng(23)

T, N_STEPS, N_PATHS = 1.0, 800, 80
dt = T / N_STEPS
t = np.linspace(0.0, T, N_STEPS + 1)

dW = rng.standard_normal((N_PATHS, N_STEPS)) * np.sqrt(dt)
W = np.concatenate([np.zeros((N_PATHS, 1)), np.cumsum(dW, axis=1)], axis=1)

fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)
for i in range(N_PATHS):
    ax.plot(t, W[i], color=BLUE, alpha=0.18, lw=0.5)

# Gaussian cross-sections at two times: profiles drawn sideways, width ~ pdf.
y = np.linspace(-3.2, 3.2, 300)
for t_cut in (0.2, 0.8):
    pdf = np.exp(-y**2 / (2 * t_cut)) / np.sqrt(2 * np.pi * t_cut)
    ax.axvline(t_cut, color="indigo", lw=1.4)
    ax.plot(t_cut + 0.3 * pdf / pdf.max() * np.sqrt(t_cut), y,
            color=RED, lw=1.2)
    ax.text(t_cut, 3.35, rf"$t={t_cut}$", ha="center", fontsize=9,
            color="indigo")

ax.text(0.30, -3.15, r"$p(x,t)=\mathcal{N}(0,\,t)$: wider as $t$ grows",
        fontsize=9, color=RED)
ax.set_xlabel(r"$t$")
ax.set_ylabel(r"$x(t)$")
ax.set_xlim(0, 1.13)
ax.set_ylim(-3.6, 3.9)

out = Path(__file__).resolve().parent.parent / "brownian_family.pdf"
fig.savefig(out)
print(f"saved {out}")
