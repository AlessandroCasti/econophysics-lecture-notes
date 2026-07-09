"""Shared matplotlib style for all book figures.

Import this module before plotting so every figure in the book shares the same
serif/mathtext look and sizing. Requires: matplotlib, numpy.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["STIXGeneral", "DejaVu Serif"],
    "mathtext.fontset": "stix",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 10,
    "legend.fontsize": 8.5,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "axes.linewidth": 0.8,
    "lines.linewidth": 1.2,
    "figure.dpi": 150,
    "savefig.bbox": "tight",
})

FIGSIZE_WIDE = (6.0, 3.2)
FIGSIZE_TALL = (6.0, 4.2)
BLUE = "#1f4e9c"
RED = "#b02020"
GRAY = "#888888"
