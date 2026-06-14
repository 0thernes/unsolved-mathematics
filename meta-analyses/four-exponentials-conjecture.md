---
title: "Meta-Analysis: The Four Exponentials Conjecture"
slug: four-exponentials-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-calibrated survey of a genuinely open problem; the mathematics is sound and the honesty about partial results is exemplary, but the bibliography leans heavily on needs-verification citations that require primary-source confirmation."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Four Exponentials Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The four exponentials conjecture asserts that if $x_1, x_2$ are $\mathbb{Q}$-linearly independent complex numbers and $y_1, y_2$ are likewise $\mathbb{Q}$-linearly independent, then at least one of the four numbers $e^{x_i y_j}$ is transcendental. Equivalently, a $2\times 2$ matrix whose entries are logarithms of algebraic numbers, with linearly independent rows and columns, cannot exist — a rank-one collapse statement. Posed in its modern form by Serge Lang and, independently, K. Ramachandra in the 1960s (with roots in Schneider and Siegel), it remains open. Its proved sibling, the six exponentials theorem, differs only by adjoining a third value $y_3$; the gap between "six" and "four" measures exactly how far the auxiliary-function and interpolation-determinant methods fall short. Waldschmidt's five exponentials theorem is the closest unconditional approach, and Schanuel's conjecture implies the four exponentials conjecture outright. This meta-analysis surveys the statement, the state of the art, the principal analytic and structural approaches, and the sharp combinatorial barrier that localizes the missing idea. It makes no claim to resolve the problem.

## 1. Statement and significance

Let $x_1, x_2$ be complex numbers linearly independent over $\mathbb{Q}$, and likewise $y_1, y_2$. The conjecture states that at least one of
$$
e^{x_1 y_1},\quad e^{x_1 y_2},\quad e^{x_2 y_1},\quad e^{x_2 y_2}
$$
is transcendental. The matrix reformulation is the cleanest: if every entry of $\begin{pmatrix} x_1 y_1 & x_1 y_2 \\ x_2 y_1 & x_2 y_2 \end{pmatrix}$ is a logarithm of an algebraic number, then the rows (and columns) must be linearly dependent. Phrased contrapositively, a $2\times 2$ matrix of $\mathbb{Q}$-linearly-independent logarithms of algebraic numbers cannot have rank $1$.

The significance is structural rather than applied. The conjecture is the sharp, forced sharpening of a genuine theorem (six exponentials) and a recognized special case of Schanuel's conjecture, the master statement of the algebraic-independence hierarchy for the exponential function. Its difficulty rating in the dossier metadata (80) and low tractability (28) reflect a problem that is conceptually transparent yet has resisted all direct attack for over half a century.

## 2. State of the art

**Unconditional results.** The *six exponentials theorem* (Lang and Ramachandra, 1960s) is the proved sibling: for $\mathbb{Q}$-independent $x_1,x_2$ and $\mathbb{Q}$-independent $y_1,y_2,y_3$, at least one of the six $e^{x_i y_j}$ is transcendental. Waldschmidt's *five exponentials theorem* yields a four-exponentials-style conclusion at the cost of one auxiliary quantity and is the strongest unconditional approach, sharp for current methods. Damien Roy's *strong six exponentials theorem*, phrased via the rank of matrices of logarithms, anchors the "strong" hierarchy. Numerous special cases are settled where extra algebraic relations supply the missing interpolation data.

**Conditional results.** Both the four exponentials conjecture and its strengthening, the strong four exponentials conjecture, follow rigorously from **Schanuel's conjecture**. This conditional proof explains why specialists regard the statement as true, but is not an unconditional resolution — Schanuel's conjecture is dramatically harder and itself open.

## 3. Principal approaches and barriers

**Auxiliary functions (Schneider–Siegel).** One builds an auxiliary polynomial with algebraic coefficients (via Siegel's lemma) so that $F(z) = P(e^{x_1 z}, e^{x_2 z}, \dots)$ has many zeros, then derives a contradiction between an analytic upper bound and a Liouville-type arithmetic lower bound. The method succeeds at six because the third row $y_3$ supplies enough interpolation conditions; at four, the count falls short by a constant factor no parameter choice recovers.

**Interpolation determinants (Laurent).** Laurent reformulated the argument as bounding a determinant of derivatives of exponential monomials — above analytically (rows nearly dependent), below arithmetically (a nonzero algebraic number). This yields sharper constants and underlies modern six- and five-exponentials proofs, but the same rank deficiency makes the $2\times 2$ determinant too small to force a contradiction.

**Sharp variants.** Waldschmidt's economizing refinements deliver the five exponentials theorem; Roy's strong framework and related results push the analytic budget to its limit. Every such sharpening still requires the extra fifth quantity or an additional independence hypothesis.

**Structural reduction.** Schanuel's conjecture gives a complete conditional proof; Roy's matrices-of-logarithms program recasts the strong forms as a clean algebraic conjecture. Both clarify the target without breaking the analytic deadlock.

**Negative knowledge.** There is no counterexample — none is expected. The relevant negative result is a barrier: the auxiliary-function and interpolation-determinant methods, essentially optimal in their transcendence measures, provably cannot reach four in current form. Baker's theory of linear forms in logarithms is orthogonal — it proves nonvanishing, not the rank-collapse the conjecture needs.

## 4. Critical assessment

The dossier's central claim — that the obstruction is a sharp counting inequality between interpolation conditions and unknowns, satisfied at six, marginally at five, and violated at four — is the correct and widely held expert diagnosis, and the document states it with unusual precision. The honesty is a strength: it explicitly records that there is *no* community-accepted near-proof beyond the partial theorems, that the conjecture has not attracted dramatic false proofs (because the obstruction is well understood), and that any unconditional disproof would contradict Schanuel's conjecture.

Two cautions. First, attributions and dates compress a tangled history. The six exponentials theorem has genuinely multiple roots (Siegel, Schneider, Lang, Ramachandra), and the precise division of credit — including the antecedent attributed to unpublished Siegel work — should be stated as the dossier does: as a shared, somewhat folkloric lineage rather than a clean priority claim. Second, the "five clusters near four" framing is a useful heuristic but is a statement about method limits, not a theorem that four is unprovable; readers should not over-read the barrier as an impossibility result.

## 5. What a resolution would require / open directions

A proof must establish the rank-one collapse directly: rule out a $2\times 2$ matrix of $\mathbb{Q}$-linearly-independent logarithms of algebraic numbers of rank $1$. Concretely, the analytic upper bound on the interpolation determinant and the arithmetic lower bound must be made to cross with only four exponentials present — currently they cross only at five or six. Three plausible routes:

1. **A new zero estimate or extrapolation** sharp enough to operate in the $2\times 2$ regime — the most direct and least foreseeable path.
2. **A Roy-style structural reformulation** of the strong four exponentials conjecture into an algebraic statement about the $\mathbb{Q}$-vector space of logarithms of algebraic numbers, settleable by other means.
3. **Partial progress toward Schanuel's conjecture** in low transcendence degree, which would deliver the four exponentials conjecture as a corollary.

No credible timeline exists; the problem has been stable for decades and is treated as a deep, long-horizon target.

## 6. Selected references

1. Theodor Schneider, *Transzendenz von Potenzen mit algebraischem Exponenten* (Hilbert's 7th problem), 1934. [high-confidence]
2. A. O. Gelfond, *Sur le septième problème de Hilbert*, 1934. [high-confidence]
3. Theodor Schneider, *Einführung in die transzendenten Zahlen*, 1957. [high-confidence]
4. Serge Lang, *Introduction to Transcendental Numbers*, 1966. [high-confidence]
5. K. Ramachandra, *Contributions to the theory of transcendental numbers (I, II)*, 1968. [high-confidence]
6. Alan Baker, *Linear forms in the logarithms of algebraic numbers*, 1966. [high-confidence]
7. Alan Baker, *Transcendental Number Theory*, 1975. [high-confidence]
8. Michel Waldschmidt, *Transcendance et exponentielles en plusieurs variables*, 1981. [needs-verification]
9. Michel Waldschmidt, *Nombres transcendants et groupes algébriques*, 1985. [high-confidence]
10. Michel Laurent, *Sur la nature arithmétique des valeurs de fonctions (interpolation determinants)*, 1991. [needs-verification]
11. Michel Laurent, *Linear forms in two logarithms and interpolation determinants*, 1992. [needs-verification]
12. Damien Roy, *Matrices whose entries are logarithms of algebraic numbers (strong six exponentials)*, 1992. [needs-verification]
13. Michel Waldschmidt, *Diophantine Approximation on Linear Algebraic Groups*, 2000. [high-confidence]
14. Michel Waldschmidt, *Open Diophantine problems*, 2004, arXiv:math/0312440. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The mathematics in this survey is sound and faithfully reported. The matrix/rank-one reformulation is stated correctly, the six/five/four hierarchy is described accurately, and the identification of Schanuel's conjecture as the master statement implying the four exponentials conjecture is standard and right. The document's most valuable feature is its calibration: it consistently distinguishes proved theorems (six exponentials, five exponentials, strong six exponentials) from the open conjecture, and it resists the temptation to overstate any partial result as a near-resolution. The diagnosis of the barrier as a sharp counting inequality is the genuine expert consensus.

My principal reservation concerns the references. A majority of the research-article citations — Waldschmidt 1981, both Laurent entries, Roy 1992 — carry **needs-verification** flags in the source dossier, and the underlying papers.md openly notes that exact titles, journals, and years are reconstructed rather than confirmed. The *existence* of substantial work by these authors on these exact topics is not in doubt, but a human reviewer must check every flagged citation against MathSciNet or zbMATH before any of it is quoted authoritatively. I have deliberately excluded the dossier's ai-suggested rows (elliptic analogues, Hopf-algebra leads, a 2021 survey) from my reference list, since the dossier itself states these may not correspond to identifiable papers.

A second, milder concern is single-source framing: much of the modern synthesis traces through Waldschmidt, and the dossier acknowledges he is the field's principal expositor. That is accurate, but it means the "standard formulation" presented here is, to a degree, one school's formulation; a reviewer should confirm that the attributions to Lang versus Ramachandra, and the credit for the strong forms to Roy, are stated as the literature actually divides them.

The single most important thing a human reviewer should verify: that the five exponentials theorem and strong six exponentials theorem are cited to their correct primary publications with exact statements, since these are the load-bearing "near-miss" results on which the entire honest narrative depends. **Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; the AI panel above flags candidate issues but does not certify correctness, citation accuracy, or completeness. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
