---
title: "Meta-Analysis: The 1/3–2/3 Conjecture"
slug: one-third-two-thirds-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful and well-calibrated survey of a genuinely open conjecture whose chief weakness is a reference list largely flagged needs-verification and reliant on a small canon."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The 1/3–2/3 Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The 1/3–2/3 Conjecture asserts that every finite partially ordered set that is not a chain contains an incomparable pair $(x,y)$ whose betweenness probability $\Pr[x\prec y]$, taken over the uniform distribution on linear extensions, lies in $[\tfrac13,\tfrac23]$. Equivalently, the worst-case "balance parameter" of any non-chain poset is at least $1/3$. The constant is best possible, achieved on the three-element V-poset. Raised independently by Kislitsyn (1968), Fredman (1976), and crystallized by Linial (1984), the conjecture connects order theory, convex geometry, entropy, and the complexity of sorting under partial information. This meta-analysis surveys the state of the art: the unconditional universal balance constant $\tfrac12-\tfrac{\sqrt5}{10}\approx0.2764$ (Kahn–Saks 1991; Brightwell–Felsner–Trotter 1995), the resolution of the algorithmic consequence (Kahn–Kim 1994 and successors), and the class-by-class verifications (width 2, height 2, semiorders, $N$-free, series–parallel). It assesses why the two analytic engines plateau below $1/3$, characterizes the remaining gap, and identifies what a resolution would require. The conjecture remains open with no counterexample; the document advances no new result.

## 1. Statement and significance

Let $P=(X,\prec)$ be a finite poset that is not a total order. A *linear extension* is a total order refining $\prec$; write $e(P)$ for their number. For incomparable $x,y$, set $\Pr[x\prec y]$ equal to the fraction of linear extensions in which $x$ precedes $y$. The conjecture states that some incomparable pair satisfies $\Pr[x\prec y]\in[\tfrac13,\tfrac23]$. The bound is tight: in the poset with a single relation $a\prec b$ and $c$ incomparable to both, every incomparable pair realizes exactly $1/3$ or $2/3$, and disjoint unions of such V/Λ gadgets form the recurring extremal family.

The significance is twofold. Order-theoretically, it is a clean unavoidability statement: a poset far from total must hide a comparison whose outcome is genuinely uncertain. Algorithmically, a balanced pair lets a comparison-based procedure query $x{:}y$ and reduce the number of consistent extensions by a constant factor regardless of the answer, so the conjecture would say that sorting under partial information needs close to the information-theoretic minimum $\lceil\log_2 e(P)\rceil$ of comparisons in the worst case.

## 2. State of the art

The conjecture is **open** (status: active-progress) with no known counterexample, standing since its 1968 root and 1984 modern formulation. The principal unconditional facts:

- **Universal balance constant.** Every non-chain poset has a pair with $\Pr[x\prec y]\in[\tfrac12-\tfrac{\sqrt5}{10},\,\tfrac12+\tfrac{\sqrt5}{10}]$, i.e. balance $\ge\approx0.2764$. Kahn–Saks (1991) first proved $[\tfrac{3}{11},\tfrac{8}{11}]$; Brightwell–Felsner–Trotter (1995) refined it to the golden-ratio value, which remains the best general bound three decades later and sits below the target $1/3\approx0.333$.
- **Sharp results on classes.** The full conjecture holds for width-2 posets (Linial 1984, with the sharp constant), height-2 posets, semiorders, $N$-free and series–parallel posets, and all small posets by exhaustive computation.
- **Algorithmic consequence settled.** Kahn–Kim (1994) give a polynomial-time comparison achieving a constant-factor reduction in extensions; the sorting-under-partial-information line (Cardinal–Fiorini–Joret–Jungers–Munro) makes this fully algorithmic. The information-theoretic payoff is therefore essentially established even though the exact $1/3$ is open.

Notably, the universal record $\approx0.276$ exactly equals the width-2 extremal constant — a suggestive coincidence that has not been converted into a proof.

## 3. Principal approaches and barriers

**Convex geometry / Brunn–Minkowski (Kahn–Saks).** Encoding linear extensions via the order/chain polytope, the count of extensions placing a fixed element in position $i$ is log-concave, a consequence of Brunn–Minkowski applied to convex slices. This forces a pair bounded away from $0$ and $1$. *Barrier:* the method controls a single element's position distribution, not the worst *pair*; it does not see the V-poset extremizer tightly, and there is no known route past $\approx0.276$ to $1/3$.

**Entropy and the comparability graph (Kahn–Kim).** A balanced comparison corresponds to a constant-factor entropy drop, computable in polynomial time. *Barrier:* entropy is an averaged quantity controlling totals, not the worst incomparable pair; the constant it yields is again below $1/3$.

**Structural / class-by-class verification.** Induct on a chain decomposition, a forbidden subposet, or a recursive build; reduce to lattice-path counting (as in the Fibonacci/golden-ratio width-2 computation). *Barrier:* each class leans on structure absent in general; deleting or contracting an element can change all betweenness probabilities unpredictably, so class results do not compose. Forests and trees are a stubborn, partly open sub-front.

**Correlation inequalities (XYZ / FKG).** Shepp's XYZ inequality and FKG-type results give qualitative monotonicity used as lemmas. *Barrier:* they deliver monotonicity, not the quantitative two-sided $[\tfrac13,\tfrac23]$ window.

## 4. Critical assessment

The evidence for truth is strong and consistent: two powerful analytic methods deliver a universal constant, every structural class examined confirms the conjecture, and exhaustive computation has never produced a counterexample. The pattern is characteristic of a "true but resistant" conjecture rather than one in doubt.

The crux is that the constant $1/3$ is *best possible*, tight on the smallest non-trivial poset. This makes the problem qualitatively harder than producing *some* universal constant (which Kahn–Saks settled): any successful method must be exact at the extremizer, not merely constant-yielding. The two analytic engines are believed structurally incapable of exactness because they aggregate over a single position distribution or an averaged entropy, while the extremal configuration is a pairwise phenomenon. The dossier's framing here is careful and, in my assessment, correct: the $0.276\to1/3$ gap is the whole problem, and it has resisted every technique tried since 1991.

One caveat about confidence levels: the claim that the analytic methods are "structurally incapable" of reaching $1/3$ is a community belief and heuristic, not a theorem. The dossier states this appropriately ("believed," "appears intrinsic") and does not overclaim an impossibility result, which is the honest posture.

## 5. What a resolution would require / open directions

A full proof must close the gap from $\approx0.2764$ to $1/3$ for arbitrary finite non-chain posets, with a method exact at the V/Λ extremizer. Plausible routes, in rough order of how the field weighs them:

1. **A pair-sensitive convexity/correlation inequality** sharpening the Brunn–Minkowski step so that its extremizer is exactly the conjectured tight family.
2. **Resolving forests/trees** (Zaguia et al.) as a stepping stone, then attacking general posets by decomposition.
3. **A tailored entropy** with the correct extremal poset, refining Kahn–Kim.
4. **Computer-assisted extremal analysis** to surface a new tight family revealing the right invariant — none beyond the V/Λ gadgets has appeared.

A negative resolution (a counterexample) would require a poset, necessarily not in any verified class, whose every incomparable pair is unbalanced beyond $[\tfrac13,\tfrac23]$; nothing in the computational record suggests one exists.

## 6. Selected references

1. M. L. Fredman, *How good is the information theory bound in sorting?* (1976) — [high-confidence]
2. L. A. Shepp, *The XYZ conjecture and the FKG inequality* (1980) — [high-confidence]
3. N. Linial, *The information-theoretic bound is good for merging*, SIAM J. Comput. (1984), DOI 10.1137/0213049 — [high-confidence]
4. W. T. Trotter, *Combinatorics and Partially Ordered Sets: Dimension Theory* (1984) — [high-confidence]
5. J. Kahn and M. Saks, *Balancing poset extensions*, Order (1991) — [high-confidence]
6. G. R. Brightwell, *Semiorders and the 1/3–2/3 conjecture* (1992) — [needs-verification]
7. J. Kahn and J. H. Kim, *Entropy and sorting* (1994) — [high-confidence]
8. G. Brightwell, S. Felsner, W. T. Trotter, *Balanced pairs in partially ordered sets* (1995) — [high-confidence]
9. G. R. Brightwell, *Balanced pairs in partial orders* (survey), Discrete Math. (1999) — [high-confidence]
10. J. Cardinal, S. Fiorini, G. Joret, R. Jungers, J. I. Munro, *Sorting under partial information* (2010) — [needs-verification]
11. S. Felsner and collaborators, *The conjecture for N-free and series–parallel posets* (2008) — [needs-verification]
12. N. Zaguia and collaborators, *The 1/3–2/3 conjecture for forests / trees* (2016) — [needs-verification]
13. S. S. Kislitsyn, *Finite partially ordered sets and probability distributions on them* (orig. Russian, 1968) — [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

This survey is faithful to its sources and, more importantly, well-calibrated about uncertainty. Its strengths: it states the conjecture and its tight constant precisely; it correctly identifies the central fact that the universal record ($\approx0.2764$) coincides with the width-2 extremal constant and sits below $1/3$; and it draws the right distinction between the *algorithmic* consequence (essentially settled) and the *exact* combinatorial constant (open). It does not at any point suggest the problem is solved, and it correctly attributes the breakthrough constant to Kahn–Saks (1991) refined by Brightwell–Felsner–Trotter (1995).

Three cautions for a human checker. (i) The reference list is the weak point: only a minority of entries are flagged high-confidence, and the dossier's own papers note that the honest count of certainly-real canonical works is roughly six to eight, with many rows marked needs-verification or ai-suggested. Every citation here — venues, years, and especially the single DOI (10.1137/0213049 for Linial)— must be checked against MathSciNet/zbMATH before reuse; I have not independently verified that DOI. (ii) There is a degree of single-source reliance: the narrative leans heavily on Brightwell's survey and the Kahn–Saks/BFT line, which is appropriate given the field's small canon but means the historiography (notably the Kislitsyn 1968 attribution and the exact golden-ratio constant) rests on few independent confirmations. (iii) The most important single thing to verify is the numerical claim that the best general lower bound is exactly $\tfrac12-\tfrac{\sqrt5}{10}$ from Brightwell–Felsner–Trotter (1995) and that no peer-reviewed work has surpassed it for general posets — the entire "state of the art" hinges on this constant being current.

The document is honest, appropriately hedged, and free of overstatement; its deficiencies are bibliographic rather than mathematical, and are correctable by source-checking. **Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; the citations and their verification flags in particular require human source-checking against primary literature. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
