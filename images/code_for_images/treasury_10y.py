"""US 10-Year Treasury constant-maturity rate (Chapter 6).

Data: FRED series GS10 (monthly averages), downloaded from
https://fred.stlouisfed.org/graph/fredgraph.csv?id=GS10
and stored in data/GS10.csv. Output: images/treasury_10y.pdf
"""
import csv
from datetime import date
from pathlib import Path

import numpy as np

from _style import plt, FIGSIZE_WIDE, BLUE, GRAY

here = Path(__file__).resolve().parent
dates, rates = [], []
with open(here / "data" / "GS10.csv") as f:
    for row in csv.DictReader(f):
        if row["GS10"] in ("", "."):
            continue
        y, m, d = (int(s) for s in row["observation_date"].split("-"))
        dates.append(date(y, m, d))
        rates.append(float(row["GS10"]))

dates = np.array(dates)
rates = np.array(rates)

fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)
ax.plot(dates, rates, color=BLUE, lw=0.9)
ax.axhline(0.0, color=GRAY, lw=0.6)
ax.set_xlabel("year")
ax.set_ylabel(r"$R(t,T)$ (%), $T = 10$ y")
ax.set_ylim(bottom=0)
ax.annotate("Volcker peak\n(Sep 1981, 15.3%)",
            xy=(date(1981, 9, 1), 15.3), xytext=(date(1990, 1, 1), 13.5),
            fontsize=8.5, arrowprops=dict(arrowstyle="->", lw=0.7))
ax.annotate("post-2008 / QE era",
            xy=(date(2016, 7, 1), 1.5), xytext=(date(1995, 1, 1), 8.0),
            fontsize=8.5, arrowprops=dict(arrowstyle="->", lw=0.7))

out = here.parent / "treasury_10y.pdf"
fig.savefig(out)
print(f"saved {out}")
