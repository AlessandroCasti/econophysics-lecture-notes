"""Two-regime income distribution: exponential bulk + Pareto tail (Chapter 8).

Schematic reproduction of the empirical shape reported by Yakovenko & Rosser,
Rev. Mod. Phys. 81, 1703 (2009) for US income data: about 97% of the
population follows an exponential (Boltzmann) law with temperature T_r, the
top ~3% a Pareto power law with exponent alpha ~ 1.7. The crossover is set at
r_* ~ 4 T_r. Sampled points are drawn from the composite model to mimic the
look of the empirical CCDF. Output: images/wealth_distribution.pdf
"""
from pathlib import Path

import numpy as np

from _style import plt, BLUE, RED, GRAY

rng = np.random.default_rng(3)

T_R = 40.0        # income "temperature" in k$ (Yakovenko: ~$40k)
ALPHA = 1.7       # Pareto exponent of the CDF tail
R_STAR = 4 * T_R  # bulk/tail crossover (tail mass exp(-4), about 1.83%)
F_TAIL = np.exp(-R_STAR / T_R)  # population fraction in the tail

N = 40_000
# Exact inverse survival sampling of the continuous composite CCDF.
u = rng.uniform(0, 1, N)
r = np.empty(N)
is_tail = u < F_TAIL
r[is_tail] = R_STAR * (F_TAIL / u[is_tail]) ** (1 / ALPHA)
r[~is_tail] = -T_R * np.log(u[~is_tail])
assert len(r) == N
rs = np.sort(r)
ccdf = 1.0 - np.arange(1, len(rs) + 1) / len(rs)
mask = ccdf > 0
# keep every 25th point in the bulk, every point in the (sparse) tail
n_tail_pts = int(len(rs) * F_TAIL * 1.5)
sub = np.concatenate([np.arange(0, len(rs) - n_tail_pts, 25),
                      np.arange(len(rs) - n_tail_pts, len(rs))])

fig, (axl, axr) = plt.subplots(1, 2, figsize=(6.4, 3.1), layout="constrained")

# Left panel: log-linear (exponential bulk is a straight line).
axl.semilogy(rs[sub], ccdf[sub], ".", color=BLUE, ms=3)
x = np.linspace(0, R_STAR * 1.6, 100)
axl.semilogy(x, np.exp(-x / T_R), color=RED, lw=1.1,
             label=rf"$e^{{-r/T_r}}$, $T_r={T_R:.0f}$ k\$")
axl.set_xlabel(r"income $r$ (k\$)")
axl.set_ylabel(r"$P_>(r)$")
axl.set_xlim(0, R_STAR * 1.6)
axl.set_ylim(1e-3, 1.2)
axl.legend(loc="upper right", frameon=False)
axl.set_title("log-linear: Boltzmann bulk", fontsize=9)

# Right panel: log-log (Pareto tail is a straight line).
axr.loglog(rs[sub][mask[sub]], ccdf[sub][mask[sub]], ".", color=BLUE, ms=3)
xt = np.logspace(np.log10(R_STAR), np.log10(rs.max()), 60)
axr.loglog(xt, F_TAIL * (xt / R_STAR) ** -ALPHA, color=RED, lw=1.1,
           label=rf"$r^{{-\alpha}}$, $\alpha={ALPHA}$")
axr.axvline(R_STAR, color=GRAY, ls=":", lw=0.9)
axr.text(R_STAR * 1.15, 0.4, r"$r_*$", fontsize=9)
axr.set_xlabel(r"income $r$ (k\$)")
axr.set_xlim(rs.min() + 1, rs.max() * 1.5)
axr.set_ylim(1.0 / len(rs) / 3, 1.2)
axr.legend(loc="lower left", frameon=False)
axr.set_title("log-log: Pareto tail", fontsize=9)

out = Path(__file__).resolve().parent.parent / "wealth_distribution.pdf"
fig.savefig(out)
print(f"saved {out}")
