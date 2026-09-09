# Econophysics Lecture Notes

Lecture notes for the Econophysics course at the University of Pavia. The material
covers Brownian motion, stochastic processes and calculus, derivative pricing,
interest-rate models, financial time series, stochastic volatility, and statistical
models of income and wealth distributions.

## Download

Clone the repository and enter its directory:

```sh
git clone https://github.com/AlessandroCasti/econophysics-lecture-notes.git
cd econophysics-lecture-notes
```

## Compile

From this folder, run:

```sh
./compile
```

This runs `latexmk` with XeLaTeX and Biber as often as necessary, produces
`econophysics-lecture-notes.pdf`, and removes its temporary build directory on
success or failure. The previous PDF is preserved if compilation fails; error
details are printed in the terminal. It requires a TeX installation (MacTeX on
macOS). Minion Pro is used when installed; otherwise the document automatically
falls back to the standard Latin Modern font. Every invocation is a fresh build.
