---
title: "Meta-Analysis: Crouzeix's Conjecture"
slug: crouzeix-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful and well-calibrated survey of a genuinely open problem whose central claim — best general bound 1+sqrt2, conjectured optimum 2 — is sound, but whose reference list is largely unverified and must be source-checked before use."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Crouzeix's Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Crouzeix's conjecture (Michel Crouzeix, 2004) asserts that the numerical range $W(A)$ of any square matrix is a $2$-spectral set: for every polynomial $p$, $\|p(A)\| \le 2\max_{z\in W(A)}|p(z)|$, with the constant $2$ optimal. The conjecture refines von Neumann's inequality by replacing the unit disc with the convex field of values, and it underpins dimension-uniform functional-calculus bounds central to numerical linear algebra. This meta-analysis surveys the state of the art. The strongest unconditional result is the Crouzeix–Palencia bound $\|p(A)\|\le(1+\sqrt2)\|p\|_{W(A)}\approx 2.4142$ (2017), which superseded Crouzeix's 2007 constant of $11.08$. The sharp constant $2$ is proven in several special cases — all $2\times2$ matrices, matrices with disc-shaped numerical range, nilpotent Jordan blocks, and various structured families — and extensive computation has found no counterexample. The problem remains open in general; the obstruction is a quantitative gap in the interval $(2,\,1+\sqrt2]$ rather than a formal impossibility barrier. We assess the principal approaches, their structural floors, and what a full resolution would require.

## 1. Statement and significance

For $A\in\mathbb{C}^{n\times n}$, the numerical range $W(A)=\{\langle Ax,x\rangle:\|x\|=1\}$ is a compact convex subset of $\mathbb{C}$ (Toeplitz–Hausdorff, 1918–1919). Crouzeix's conjecture states that for every polynomial $p$,
$$\|p(A)\|\le 2\max_{z\in W(A)}|p(z)|,$$
in the operator norm, with $2$ optimal. Equivalently, $W(A)$ is a $K$-spectral set with absolute constant $K=2$, independent of $A$, the dimension $n$, and $\deg p$; by standard extension the bound carries to functions analytic on a neighborhood of $W(A)$ and to rationals with poles off $W(A)$.

The significance is twofold. Conceptually, the conjecture is the natural successor to von Neumann's 1951 spectral-set inequality, transplanting it from the disc (where the controlling quantity is $\|A\|$) to the field of values. Practically, the bound $\|f(A)\|\le C\|f\|_{W(A)}$ is exactly the kind of dimension-uniform estimate needed to analyze functions of non-normal matrices — resolvents, matrix exponentials, and rational approximants arising in stiff ODE solvers, exponential integrators, and Krylov/Faber methods — where the spectrum alone badly mispredicts $\|f(A)\|$.

## 2. State of the art

**Status: open, with active progress.** The general conjecture is unproven. The strongest unconditional theorem is the Crouzeix–Palencia bound (2017),
$$\|p(A)\|\le(1+\sqrt2)\,\|p\|_{W(A)}\approx 2.4142,$$
valid for all matrices, all dimensions, and all polynomials. This improved Crouzeix's own explicit 2007 constant of $11.08$ and reduced the gap to the conjectured value to roughly $21\%$.

The sharp constant $2$ is established unconditionally for: all $2\times2$ matrices (numerical range an ellipse; closed by an explicit conformal map and Blaschke-product computation); matrices whose numerical range is a disc (via the Okubo–Ando dilation); nilpotent Jordan blocks; and certain tridiagonal Toeplitz and other structured families. The $2\times2$ examples also certify that $2$ is optimal, approaching the ratio in the limit. Conditional bounds approaching $2$ exist under smoothness of $\partial W(A)$, normality/structural hypotheses, or within the completely-bounded framework. Large-scale extremal search (Greenbaum, Overton, Choi and collaborators) has found no counterexample; the observed supremum of $\|p(A)\|/\|p\|_{W(A)}$ sits at or just below $2$.

## 3. Principal approaches and barriers

**Cauchy-transform / boundary functional calculus (Crouzeix–Palencia).** Write $f(A)$ as a Cauchy integral over $\partial W(A)$ and exploit $\|(zI-A)^{-1}\|\le 1/\operatorname{dist}(z,W(A))$. The decisive device pairs $f$ with a conjugate companion so that $f+\overline{g}$ controls $f(A)$, yielding the $1+\sqrt2$ bound. *Barrier:* the symmetrization producing $1+\sqrt2$ is lossy; Ransford–Schwenninger showed the unmodified scheme is essentially tight near $2.4$ and cannot reach $2$ without new input.

**Spectral-set / dilation theory.** A $K$-spectral-set statement ties to a normal dilation on a larger space; constant $2$ in the complete sense would follow from a suitable normal dilation with spectrum on $\partial W(A)$. *Best:* exact constant $2$ for the disc (Okubo–Ando). *Barrier:* no known normal dilation achieves $2$ over a general convex domain, and the completely-bounded constant may exceed the scalar bound.

**Low-dimension / structured verification.** Settle the conjecture class by class. *Barrier:* the case analysis does not visibly converge — corners, flat boundary segments, and near-coalescing eigenvalues make each new dimension qualitatively harder; even fully general $3\times3$ has been stubborn.

**Potential theory / Faber operator.** Recast the bound as a sharp norm estimate for a Cauchy/Faber operator over $\partial W(A)$. *Barrier:* this operator norm is not known to be controlled by the figure yielding $2$ over all convex curves; curvature and corners degrade the estimates.

**Computation.** Treats the ratio as an optimization over matrices, polynomials, and boundary points. *Barrier:* corroborates but cannot prove a universal bound, and extremal configurations are nearly degenerate — exactly where analysis loses control.

Crucially, the dossier reports **no formal impossibility barrier** (no relativization-, natural-proofs-, or parity-type obstruction); the conjecture is widely believed true, and the obstruction is the quantitative gap $(2,\,1+\sqrt2]$.

## 4. Critical assessment

The dossier's central technical claims are mutually consistent and align with the well-established backbone of the field: Crouzeix (2004, 2007) $\to$ Crouzeix–Palencia (2017) $\to$ Ransford–Schwenninger (2017–2018) $\to$ Greenbaum–Overton computation. The framing of the difficulty is honest and unusually precise: this is a "last factor" problem, not a binary barrier, which plausibly explains the absence of a large corpus of publicized false proofs. The treatment correctly distinguishes proven special cases (sharp $2$) from the open general statement and refrains from over-claiming.

Two cautions. First, the constant $1+\sqrt2$ as the prevailing *general* record should be re-confirmed against the most recent literature, since incremental refinements and conditional sub-$2.41$ results are reported but described as not displacing $1+\sqrt2$ in full generality — a reader should verify no unconditional improvement has since been accepted. Second, the precise scope of "various $3\times3$ classes" and which structured families are settled are stated at a survey level; the exact frontier here is the kind of detail most likely to drift between sources.

## 5. What a resolution would require / open directions

A full proof must (i) hold for *arbitrary* convex $W(A)$, including corners and flat segments; (ii) be uniform in dimension and degree; and (iii) reach exactly $2$. The leading candidate routes are: (a) an *asymmetric* sharpening of the Crouzeix–Palencia pairing that avoids the lossy symmetrization; (b) a normal-dilation construction realizing constant $2$ on a general convex domain (yielding the stronger complete spectral-set statement); or (c) a potential-theoretic/Faber-operator bound controlling the relevant Cauchy operator over all convex curves. Most observers expect near-term progress on fully general $3\times3$ matrices and on mildly non-smooth numerical ranges, with a unified boundary or dilation argument as the eventual mechanism. Because no formal barrier is known, a single new idea bridging $(2,\,1+\sqrt2]$ could resolve it.

## 6. Selected references

1. O. Toeplitz, *Das algebraische Analogon zu einem Satze von Fejér* (1918) — convexity foundations of the numerical range. [high-confidence]
2. F. Hausdorff, *Der Wertvorrat einer Bilinearform* (1919) — completes the Toeplitz–Hausdorff theorem. [high-confidence]
3. J. von Neumann, *Eine Spektraltheorie für allgemeine Operatoren eines unitären Raumes* (1951) — the spectral-set inequality. [high-confidence]
4. K. Okubo, T. Ando, dilation results giving the sharp constant $2$ for the disc case (1971). [needs-verification]
5. M. Crouzeix, *Bounds for the numerical range and functional calculus* (2004) — origin of the conjecture. [high-confidence]
6. M. Crouzeix, *Numerical range and functional calculus in Hilbert space*, J. Funct. Anal. 244 (2007); DOI 10.1016/j.jfa.2006.04.005 — the constant $11.08$. [high-confidence]
7. C. Badea, B. Beckermann, M. Crouzeix, *The annulus as a $K$-spectral set* (2012). [needs-verification]
8. M. Crouzeix, C. Palencia, *Numerical range and functional calculus: the constant $1+\sqrt2$*, SIAM J. Matrix Anal. Appl. (2017); DOI 10.1137/17M1116672 — world-record general bound. [high-confidence]
9. T. Ransford, F. L. Schwenninger, *Some remarks on the Crouzeix–Palencia bound* (2017). [needs-verification]
10. A. Greenbaum, M. L. Overton, *Crouzeix's conjecture and related problems (numerical study)* (2017). [needs-verification]
11. D. Choi, *Crouzeix's conjecture for new classes of matrices* (2017). [needs-verification]
12. A. Greenbaum, M. Overton, T. Caldwell, *Variational and numerical investigation of Crouzeix's conjecture* (2018). [needs-verification]
13. T. Ransford, F. L. Schwenninger, *An improvement of a result of Crouzeix and Palencia* (2018). [needs-verification]
14. A. Greenbaum, K. Li, *A survey of the numerical range and Crouzeix's conjecture* (2020). [needs-verification]
15. *Recent progress on Crouzeix's conjecture for low-dimensional matrices* (2024) — representative frontier entry. [ai-suggested]

*Verification note carried from the dossier: rows for the founding papers (1–3), Crouzeix (2004, 2007), and Crouzeix–Palencia (2017) are canonical; the two DOIs are most-likely identifiers pending publisher confirmation. Entries flagged [needs-verification] and [ai-suggested] require MathSciNet/zbMATH source-checking for authorship, title, year, and identifier, and several may conflate distinct real publications.*

## AI Review Panel

### Claude (Anthropic) — in-house review

This is a careful, well-calibrated survey and I find no substantive error in its mathematical narrative. The spine — von Neumann's spectral-set inequality as ancestor, the descent of universal constants from $11.08$ (2007) to $1+\sqrt2$ (2017), the sharp-$2$ special cases, and the explicit absence of a formal barrier — is internally consistent and matches the structure one expects of this problem. The document's chief virtue is restraint: it cleanly separates proven facts (the $1+\sqrt2$ general bound; sharp $2$ for $2\times2$, disc, nilpotent, and structured cases) from the open general statement, and it correctly characterizes the difficulty as a quantitative gap in $(2,\,1+\sqrt2]$ rather than an impossibility obstruction.

My skepticism is concentrated on provenance, not substance. Per the dossier's own verification table, much of the reference list carries [needs-verification] or [ai-suggested] flags; only the founding papers, Crouzeix (2004, 2007), and Crouzeix–Palencia (2017) are canonical, and even the two DOIs are "most-likely" identifiers. A human must source-check every flagged row against MathSciNet/zbMATH before any of these citations is relied upon — several ai-suggested entries may not correspond to single real papers. I also flag possible single-source reliance: the precise claim that the *unmodified* Crouzeix–Palencia mechanism cannot beat $\approx 2.4$ rests on the Ransford–Schwenninger analyses, and the survey should not let that harden into folklore without confirming the original statements and their exact hypotheses.

If I had to name the single most important thing for a human reviewer to verify, it is the current-record claim: that $1+\sqrt2$ remains the best *unconditional, fully general* constant as of the latest literature, with no accepted improvement strictly below it. That is the one fact whose obsolescence would most change the document, and it is precisely the kind of fast-moving frontier detail an offline survey can get wrong. Subject to that check and the citation cleanup, the document is sound and publishable as a survey.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and its mathematical claims and especially its citations require checking against primary sources before scholarly use. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
