# Writing & LaTeX Style Guide

*A style guide for the Econophysics lecture notes, distilled from two reference texts:
David Tong's Cambridge lecture notes (e.g. "Classical Dynamics") and P. Perinotti's
"Dispense di Meccanica Statistica" (Pavia). Follow this guide for every chapter of the book.*

---

## 1. The golden rule: prose carries the document

The single most visible feature of professional lecture notes is that **the prose does the
work and the equations punctuate it** — not the other way around. A reader should be able
to read the document aloud, equations included, as a sequence of complete English sentences.

Concretely:

1. **Every displayed equation is part of a sentence.** It is introduced by a clause that
   ends naturally in the math, and it carries its own punctuation *inside* the display:
   a comma if the sentence continues, a period if it ends.

   ```latex
   Integrating both members, we finally obtain
   \[
   S_t = S_0\, e^{rt},
   \]
   which is the compound interest law in the continuum.
   ```

2. **Never leave an equation orphaned** between two unrelated paragraphs, and never use a
   colon mechanically before every display. Vary the connectives the way Tong and Perinotti
   do: *"we have", "which gives", "so that", "from which", "it follows that", "this yields",
   "Rearranging things,", "Taking the expectation of both sides,", "In formula:"*.

3. **Chains of algebra get narrated.** Between two consecutive displays there is always a
   short clause explaining what was done: *"while", "and therefore", "Substituting back,",
   "where, in the second equality, we used…"*. If a step needs no comment, merge it into an
   `align` environment rather than stacking separate displays.

## 2. The three-beat rhythm: motivate — derive — interpret

Each section, and each major result within a section, follows the same pattern found in
both reference texts:

- **Motivate.** Before any formalism, one or two sentences explaining *why* the object is
  being introduced or *what question* it answers. Rhetorical questions are effective when
  used sparingly (Tong: *"Of all these possible paths, only one is the true path taken by
  the system. The question is: which one?"*).

- **Derive.** The calculation itself, narrated step by step as prose (see §1). Assumptions
  are stated when they are used, not silently invoked.

- **Interpret.** After the boxed/final result, a paragraph in plain language about what the
  formula *says*. Tong after F = MR̈: *"This is an important formula. It tells us that the
  centre of mass of a system of particles acts just as if all the mass were concentrated
  there."* No key result should be left to speak for itself.

## 3. Lists are the exception, not the rule

Bullet points are for genuinely enumerable material: model hypotheses, classifications of
asset types, properties of a process. They are **not** for explanations, derivations, or
sequences of ideas — those are paragraphs.

When a list *is* appropriate:

- Each item is a complete sentence (or several), with a period.
- If items carry weight, introduce them (*"Some remarks on this important result:"*) and
  let each item be a small paragraph, as Tong does after the Euler–Lagrange equations.
- Prefer `enumerate` for hypotheses that will be referred to by number ("by hypothesis (iii)…").

A useful test: if the bullets read as a telegraphic outline (noun phrases, arrows, no
verbs), they are lecture-blackboard shorthand and must be rewritten as prose.

## 4. Signposting and structure

- **Chapter openers** (2–5 sentences): where we are coming from, what this chapter does,
  and where it leads. Both reference texts do this without exception.
- **Section transitions**: end a section by pointing at the next idea when natural
  (*"This observation opens the door to the model we develop next."*).
- **Cross-references**: refer backwards and forwards explicitly — *"as we saw in
  Section~\ref{...}"*, *"we will return to this point in Chapter~\ref{...}"*. This knits
  the book together.
- **Sections should not be too short.** A section of three lines is a paragraph of its
  parent section.

## 5. Mathematical typography

- `\[ ... \]` for unnumbered displays; `\begin{equation}` **only for equations that are
  referenced elsewhere** or are genuinely central results. (Tong numbers sparingly;
  unreferenced numbers are noise.) Never `$$ ... $$`.
- Multi-step manipulations: one `align` (or `align*`) with `&` on the relation sign, not a
  pile of separate displays.
- Punctuate display math (comma/period) as per §1. Use `\,` before differentials: `dx`,
  `\,dW_t`.
- Introduce every symbol at first use, in prose: *"where $\alpha$ is the speed of mean
  reversion"*. The reader should never meet an unexplained symbol.
- New terminology: `\emph{...}` at the point of definition, roman thereafter. Do not bold
  terms in running text; bold is reserved for structural headers.
- Important boxed results (`\boxed{...}`) at most once or twice per chapter — the truly
  famous equations (Black–Scholes PDE, Fokker–Planck). A box is a spotlight; too many and
  nothing is lit.
- Theorems and proofs: inline bold headers in Tong's fashion (*"\textbf{Theorem (…):} …
  \textbf{Proof:} … $\square$"*) or a `quote`-style statement, used sparingly and only for
  genuinely theorem-shaped results.

## 6. Voice and register

- **First person plural**, present tense: *"we now compute", "let us see why"*. The reader
  is a companion, not an audience.
- Confident, plain, and occasionally light. Tong permits himself personality (*"it doesn't
  matter if you throw a tennis ball or a very lively cat"*); one such touch per chapter is
  plenty. Never at the expense of precision.
- **Historical and real-world asides** ground the material (Tong: *"The concept of 'force'
  is very 17th century."*). In this book: dates of the founding papers, market crises,
  actual magnitudes (the size of global assets, real values of Pareto exponents).
- Short sentences for emphasis. Long sentences for flow. Alternate.
- Footnotes for tangents that would break the main line of argument: caveats, historical
  precision, pointers to literature. Tong uses them liberally; so should we.

## 7. Figures

- Every figure gets a `figure` environment with a `\caption` and, if referenced, a
  `\label`. Captions are one or two full sentences, informative in isolation.
- TikZ figures follow the geometry of the hand-drawn original but with clean proportions.
- Keep the `% TODO: INSERT COMPLEX IMAGE` convention for placeholders (see CLAUDE.md).

## 8. Source-code conventions (unchanged from CLAUDE.md)

- One sentence per source line (git-friendly diffs; PDF output unaffected).
- `% CLAUDE NOTE:` comments preserve the original notes wherever the compiled text
  corrects or expands them (unreviewed notes), or flag suspected errors that were
  transcribed verbatim (reviewed notes).
- Compile with `latexmk -pdf main.tex` after significant changes; zero undefined
  references is the bar.

## 9. Worked example of the transformation

**Before** (blackboard shorthand — what handwritten notes look like when transcribed
too literally):

```latex
\emph{Risk-free} means:
\begin{itemize}
    \item guaranteed return, zero credit risk
    \item abstraction: even ``too big to fail'' banks can default
    \item $r$ not constant $\to$ follows an SDE
\end{itemize}
```

**After** (lecture-notes prose):

```latex
The adjective \emph{risk-free} deserves a comment.
It means that the return is guaranteed: there is no credit risk whatsoever.
This is, of course, an abstraction.
Even banks considered ``too big to fail'' can default --- as the 2008 crisis made painfully clear --- and, more importantly, the rate $r$ is not truly constant in time: it fluctuates, and its future values are unknown.
A more honest description would promote $r$ itself to a stochastic process.
For the moment we set this complication aside and return to it in Chapter 6.
```

The content is identical; the difference is that the second version *reads*.

---

*Summary in one line: write so that a good student could learn the subject from the text
alone, without having attended the lecture — that is what Tong and Perinotti achieve.*
