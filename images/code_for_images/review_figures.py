"""Deterministic review figures; cached FRED data only, no network."""
import csv
from datetime import date
from math import erfc, sqrt
from pathlib import Path
import numpy as np
from _style import plt, BLUE, RED, GRAY
here=Path(__file__).resolve().parent
# Actual Vasicek yield curve, annual units.
a,theta,sigma,r=.4,.04,.01,.01
def y(t):
 b=-np.expm1(-a*t)/a
 loga=(theta-sigma*sigma/(2*a*a))*(b-t)-sigma*sigma*b*b/(4*a)
 return 100*(r*b-loga)/t
x=np.linspace(.01,20,500)
fig,ax=plt.subplots(figsize=(5.2,3.1),layout='constrained')
ax.plot(x,y(x),'--',color=BLUE,label='Vasicek model')
t=np.array([.5,1,2,3,5,7,10,15,20])
ax.plot(t,y(t)+np.array([.06,-.04,.03,-.05,.06,-.03,.04,-.05,.03]),'o',ms=3,color=RED,label='synthetic points')
ax.set(xlabel='maturity (years)',ylabel='continuously compounded yield (%)')
ax.legend(frameon=False)
fig.savefig(here.parent/'vasicek_yield_review.pdf')
# Exact Gaussian survival, compared with Pareto survival on x>=1.
x=np.geomspace(1,8,300)
fig,ax=plt.subplots(figsize=(5,3),layout='constrained')
ax.loglog(x,.5*x**-1.7,color=BLUE,label=r'power-law tail, $\alpha=1.7$')
ax.loglog(x,[.5*erfc(v/sqrt(2)) for v in x],'--',color=RED,label='standard Gaussian upper tail')
ax.set(xlabel='x (logarithmic scale)',ylabel=r'$P(X>x)$ (logarithmic scale)',ylim=(1e-15,1))
ax.legend(frameon=False)
fig.savefig(here.parent/'tail_comparison_review.pdf')
# Intro panels with explicit provenance and reproducible W_0=0.
rng=np.random.default_rng(20260906);t=np.linspace(0,1,1001)
w=np.r_[0,np.cumsum(rng.normal(0,np.sqrt(.001),1000))]
fig,ax=plt.subplots(figsize=(3.3,2.05),layout='constrained')
ax.plot(t,w,color=BLUE,lw=.7);ax.set(xlabel='time',ylabel=r'$W(t)$')
fig.savefig(here.parent/'brownian_motion_1d.pdf')
dates=[];prices=[]
with (here/'data/SP500.csv').open() as inp:
 for row in csv.DictReader(inp):
  if row['SP500'] not in ('','.'):dates.append(date.fromisoformat(row['observation_date']));prices.append(float(row['SP500']))
fig,ax=plt.subplots(figsize=(3.3,2.05),layout='constrained')
ax.plot(dates,prices,color=BLUE,lw=.7);ax.set(xlabel='year',ylabel='S&P 500 (points)')
fig.savefig(here.parent/'spot_price_sp500.pdf')
print('Cached SP500 date range:', dates[0], dates[-1], '; observations:',len(prices))
print('Daily normalized log-return range:', (np.diff(np.log(prices))-np.diff(np.log(prices)).mean()).min()/np.diff(np.log(prices)).std(), (np.diff(np.log(prices))-np.diff(np.log(prices)).mean()).max()/np.diff(np.log(prices)).std())
