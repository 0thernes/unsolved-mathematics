---
title: "Meta-Analysis: The Zariski Cancellation Problem"
slug: zariski-cancellation-problem
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-bounded survey of a problem resolved negatively in characteristic p and open in characteristic 0 for n>=3, whose references nonetheless carry verification flags and require primary-source checking."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Zariski Cancellation Problem

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Zariski Cancellation Problem (ZCP) asks whether an isomorphism $X \times \mathbb{A}^1_k \cong \mathbb{A}^{n+1}_k$ forces $X \cong \mathbb{A}^n_k$ — equivalently, whether $A^{[1]} \cong k^{[n+1]}$ forces $A \cong k^{[n]}$ for a finitely generated $k$-algebra $A$. Raised by Oscar Zariski around 1949 within his program to characterize affine space by intrinsic invariants, the problem is now sharply bifurcated. It holds for $n=1$ over any field (Abhyankar–Eakin–Heinzer) and for $n=2$ in characteristic zero (Fujita; Miyanishi–Sugie). The decisive modern development is negative: Neena Gupta (2014) proved that in characteristic $p>0$ cancellation *fails* for all $n \ge 3$, using Asanuma's deformation threefolds and a characteristic-$p$ Makar-Limanov-type invariant. The characteristic-zero case for $n \ge 3$ — above all the threefold question — remains genuinely open. This meta-analysis surveys the statement, the state of the art, the principal methods (affine-surface fibration theory, locally nilpotent derivations and the Makar-Limanov invariant, Asanuma deformations, and motivic/$\mathbb{A}^1$-homotopy characterizations), and the structural obstruction that keeps the characteristic-zero frontier closed. It asserts no new result.

## 1. Statement and significance

Write $\mathbb{A}^n_k$ for affine $n$-space over a field $k$, with coordinate ring $k[x_1,\dots,x_n]$. The ZCP asks: if $X \times \mathbb{A}^1_k \cong \mathbb{A}^{n+1}_k$, must $X \cong \mathbb{A}^n_k$? In ring-theoretic form: if $A$ is a finitely generated $k$-algebra with $A[t] \cong k[x_1,\dots,x_{n+1}]$, must $A \cong k[x_1,\dots,x_n]$? The name reflects the wish to "cancel" the common $\mathbb{A}^1$ factor.

The significance is its place in the program of *characterizing affine space among all varieties* by ring-theoretic or topological invariants rather than by an a priori coordinate choice. Cancellation, if universally true, would make $\mathbb{A}^n$ detectable purely from the abstract isomorphism type of any of its cylinders — a strong rigidity statement. The question is special precisely because the larger object is itself a polynomial ring: general algebra cancellation ($A[t]\cong B[t] \Rightarrow A\cong B$) already fails, by Hochster's 1972 counterexample built from a non-trivial vector bundle. ZCP thus isolates the rigidity of affine space, and sits in the same neighbourhood as the Jacobian conjecture, embedding and linearization questions, and the characterization of $\mathbb{A}^n$.

## 2. State of the art

The status is best summarized by a table over dimension and characteristic.

- **$n=1$, any field.** Cancellation holds (Abhyankar–Eakin–Heinzer, 1972): a curve $C$ with $C\times\mathbb{A}^1\cong\mathbb{A}^2$ is the line.
- **$n=2$, characteristic $0$.** Cancellation holds (Fujita 1979; Miyanishi–Sugie 1980): $X\times\mathbb{A}^1\cong\mathbb{A}^3 \Rightarrow X\cong\mathbb{A}^2$, via the structure theory of affine surfaces and $\mathbb{A}^1$-fibrations. The $n=2$ positive-characteristic case is also resolved positively.
- **$n\ge 3$, characteristic $p>0$: FALSE.** Neena Gupta (2014) constructed $A$ with $A^{[1]}\cong k^{[n+1]}$ but $A\not\cong k^{[n]}$ — the first counterexample in any setting. The dossier records the key paper as N. Gupta, *On the cancellation problem for the affine space $\mathbb{A}^3$ in characteristic $p$*, Inventiones Mathematicae (2014), with identifiers DOI `10.1007/s00222-013-0455-2` and arXiv:`1306.3043` given as best-known and flagged needs-verification.
- **$n\ge 3$, characteristic $0$: OPEN.** No accepted proof or counterexample. The flagship live case is the threefold: does $X\times\mathbb{A}^1\cong\mathbb{A}^4$ in characteristic $0$ force $X\cong\mathbb{A}^3$?

Gupta's work was recognized by the 2014 Ramanujan Prize; her resolution is broadly accepted, with no serious objection recorded in the dossier.

## 3. Principal approaches and barriers

**$\mathbb{A}^1$-fibrations and affine-surface theory.** In characteristic $0$, a smooth affine variety with enough $\mathbb{A}^1$-fibrations and the topology of affine space can be shown to *be* affine space. Miyanishi's structure theory of affine rational surfaces gives an essentially complete picture in dimension $2$. *Barrier:* the method leans on the fine classification of open surfaces (logarithmic Kodaira dimension, Mori theory of open surfaces) and on characteristic-zero phenomena; neither has a complete analogue in dimension $\ge 3$.

**Locally nilpotent derivations and the Makar-Limanov invariant.** An LND $D$ on $A$ is the infinitesimal generator of a $\mathbb{G}_a$-action, with $\ker D$ the invariants; $\mathrm{ML}(A) = \bigcap_D \ker D$, with $\mathrm{ML}(k^{[n]})=k$. Because $\mathrm{ML}$ behaves controllably under adding a variable, computing it on a candidate base can certify $X\not\cong\mathbb{A}^n$ even when $X\times\mathbb{A}^1\cong\mathbb{A}^{n+1}$. Makar-Limanov (1996) used this to prove the Russell cubic $\{x+x^2y+z^2+t^3=0\}$ is not $\mathbb{A}^3$. *Barrier:* in characteristic $0$, every known $X$ with $X\times\mathbb{A}^1\cong\mathbb{A}^4$ has so far had trivial ML invariant, so this exact tool has not yet produced a char-$0$ counterexample; the invariant is also hard to compute and is insensitive when two independent $\mathbb{G}_a$-actions exist.

**Asanuma deformations and the char-$p$ resolution.** Asanuma (1987) built characteristic-$p$ threefolds whose cylinders are polynomial rings but whose own structure is anomalous, exploiting Frobenius and inseparability. Gupta (2014) computed a characteristic-$p$ ML-type invariant on these to separate them from $\mathbb{A}^3$. *Barrier (for char 0):* the construction is intrinsically characteristic-$p$; the $p$-th-power maps and inseparable subextensions it depends on simply do not exist in characteristic zero, so the method gives no information about the open case.

**Homological/motivic characterizations.** Characterize $\mathbb{A}^n$ by contractibility, trivial Picard group, and cohomological vanishing; motivic and $\mathbb{A}^1$-homotopy methods (Dubouloz–Fasel and collaborators) probe $\mathbb{A}^1$-contractibility of Koras–Russell threefolds. *Barrier:* these conditions are necessary but provably not sufficient — the Russell cubic is contractible yet not $\mathbb{A}^3$ — so topology alone cannot decide cancellation.

## 4. Critical assessment

The dossier's central claims are internally consistent and align with the standard reading of the field: positive in low dimension, negative in characteristic $p$ for $n\ge 3$, open in characteristic $0$ for $n\ge 3$. The narrative correctly identifies the Makar-Limanov invariant as the load-bearing tool and correctly diagnoses why it does not yet close the char-$0$ case (triviality on all known cylinder bases). The framing of Gupta's result as a genuine theorem rather than a contested claim is appropriate and matches the recorded reception.

Two cautions. First, the most consequential factual assertions — Gupta's resolution and the exact attributions for the surface case — depend on bibliographic identifiers that the dossier itself flags as needs-verification (only Zariski's *Algebraic Surfaces*, Hochster's coefficient-ring paper, Miyanishi's *Open Algebraic Surfaces*, and Freudenburg's LND monograph are marked high-confidence). Second, dates and journal attributions in the timeline (e.g. Fujita 1979 vs. a 1976 grouping, the precise split of Miyanishi–Sugie papers) are reconstructed from standard citation practice and may differ in detail. None of this affects the qualitative state of the art, but it does bear on precise crediting.

## 5. What a resolution would require / open directions

A *positive* characteristic-zero resolution would require an invariant that is (a) preserved under adding a polynomial variable, (b) computable on candidate threefolds, and (c) able to distinguish any non-$\mathbb{A}^3$ base from $\mathbb{A}^3$. The ML invariant satisfies (a)–(b) but fails (c) on all known char-$0$ cylinder bases, so it cannot by itself close the problem. A *negative* resolution would require an explicit $X\not\cong\mathbb{A}^3$ with $X\times\mathbb{A}^1\cong\mathbb{A}^4$ in characteristic $0$ — obstructed by the fact that Gupta's counterexample engine is purely characteristic-$p$.

Plausible routes recorded in the dossier: (1) refined $\mathbb{G}_a$-action invariants beyond Makar-Limanov (Derksen invariant; controlled families of LNDs) tailored to char-$0$ threefolds; (2) $\mathbb{A}^1$-homotopy/motivic methods testing whether $\mathbb{A}^1$-contractibility plus extra structure forces $\mathbb{A}^3$; (3) new char-$0$ deformation families analogous to Asanuma's — none has yet materialized as a genuine cancellation failure.

## 6. Selected references

1. Oscar Zariski, *Algebraic Surfaces* (1935) — foundational. [high-confidence]
2. Melvin Hochster, *Nonuniqueness of coefficient rings in a polynomial ring* (1972) — foundational. [high-confidence]
3. S. S. Abhyankar, P. Eakin, W. Heinzer, *A note on the cancellation problem for polynomial rings* (1972) — foundational. [needs-verification]
4. M. Miyanishi, T. Sugie, *On affine-ruled rational surfaces* (1976) — breakthrough. [needs-verification]
5. Takao Fujita, *On Zariski's cancellation problem for affine surfaces* (1979) — breakthrough. [needs-verification]
6. M. Miyanishi, T. Sugie, *Affine surfaces containing cylinderlike open sets* (1980) — breakthrough. [needs-verification]
7. Teruo Asanuma, *Polynomial rings and the cancellation problem* (1987) — foundational. [needs-verification]
8. Leonid Makar-Limanov, work introducing the AK/ML invariant and the Russell cubic (1996) — breakthrough. [needs-verification]
9. S. Kaliman, L. Makar-Limanov, *On the hypersurface $x+x^2y+z^2+t^3=0$ ... not $\mathbb{C}^3$* (1997) — breakthrough. [needs-verification]
10. Masayoshi Miyanishi, *Open Algebraic Surfaces* (CRM Monograph, 1997) — survey. [high-confidence]
11. A. Crachiola, L. Makar-Limanov, *The Makar-Limanov invariant for locally nilpotent derivations* (2004) — modern. [needs-verification]
12. Gene Freudenburg, *Algebraic Theory of Locally Nilpotent Derivations* (2006) — survey. [high-confidence]
13. Neena Gupta, *On the cancellation problem for the affine space $\mathbb{A}^3$ in characteristic $p$*, Inventiones Math. (2014), DOI `10.1007/s00222-013-0455-2`, arXiv:`1306.3043` — breakthrough. [needs-verification]
14. Neena Gupta, *A survey on Zariski cancellation problem* (2015) — survey. [needs-verification]
15. A. Dubouloz, J. Fasel, *$\mathbb{A}^1$-contractibility of the Koras–Russell threefold* (2019) — modern. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

This is a careful and honestly bounded survey. Its principal strength is that it does not overclaim: it states plainly that ZCP is *resolved negatively* in characteristic $p$ for $n\ge 3$ (Gupta) and *open* in characteristic $0$ for $n\ge 3$, and it explains the structural reason the two cases diverge — the char-$p$ machinery rests on Frobenius and inseparability that have no char-$0$ analogue. The treatment of the Makar-Limanov invariant is the right organizing thread, and the Russell-cubic episode is correctly cast as a near-miss that produced the decisive tool rather than a counterexample.

Three cautions a human reviewer should weigh. (i) The references carry verification flags from the source dossier; only four items are marked high-confidence, and the rest — including the bibliographic identifiers for Gupta's resolution and for the surface-case papers — are flagged needs-verification and must be checked against MathSciNet/zbMATH and the actual journal record before this document is cited. (ii) The analysis relies heavily on a single dossier as its source; claims about reception ("no serious objection," the 2014 Ramanujan Prize) are plausible but single-sourced and should be independently confirmed. The timeline also embeds minor potential discrepancies (Fujita 1979 vs. a 1976 grouping; the precise Miyanishi–Sugie paper split) that affect crediting, not the state of the art.

The single most important thing to verify: that Gupta's 2014 Inventiones paper exists with the stated identifiers and proves cancellation *fails* for $\mathbb{A}^3$ in characteristic $p$ exactly as described — this is the load-bearing modern claim of the entire survey, and if its attribution or scope is off, Section 2 must be revised.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; the in-house Claude review above flags reference verification, single-source reliance, and the central Gupta attribution as the items most needing a human's source-checking. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
