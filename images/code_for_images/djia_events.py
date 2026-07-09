"""Dow Jones Industrial Average with macro events annotated (Chapter 5).

Pedagogical figure after the course slides ("Mercati & Strumenti Finanziari"):
the DJIA time series with major exogenous events marked, framing the question
"is the dynamics of a financial asset Markovian?".

Data: FRED series DJIA (daily closes, ~10 years), downloaded from
https://fred.stlouisfed.org/graph/fredgraph.csv?id=DJIA
and stored in data/DJIA.csv. Output: images/djia_events.pdf
"""
import csv
from datetime import date
from pathlib import Path

from _style import plt, FIGSIZE_WIDE, BLUE

here = Path(__file__).resolve().parent
dates, closes = [], []
with open(here / "data" / "DJIA.csv") as f:
    for row in csv.DictReader(f):
        if row["DJIA"] in ("", "."):
            continue
        y, m, d = (int(s) for s in row["observation_date"].split("-"))
        dates.append(date(y, m, d))
        closes.append(float(row["DJIA"]))

fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)
ax.plot(dates, closes, color=BLUE, lw=0.7)
ax.set_xlabel("year")
ax.set_ylabel("DJIA (points)")

events = [
    (date(2018, 12, 24), 21792, "US--China trade\ndispute", date(2017, 9, 1), 15500),
    (date(2020, 3, 23), 18592, "COVID-19 becomes\na global pandemic", date(2019, 6, 1), 12800),
    (date(2022, 9, 30), 28726, "Fed starts a series\nof interest rate hikes", date(2021, 10, 1), 21000),
]
for xd, yv, label, tx, ty in events:
    ax.annotate(label, xy=(xd, yv), xytext=(tx, ty), fontsize=8,
                arrowprops=dict(arrowstyle="->", lw=0.7))
ax.set_ylim(10000, 48000)

out = here.parent / "djia_events.pdf"
fig.savefig(out)
print(f"saved {out}")
