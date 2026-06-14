---
title: "Meta-Analysis: Furstenberg's ×2 ×3 Conjecture"
slug: furstenberg-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "An accurate, appropriately hedged survey of a genuinely open conjecture whose positive-entropy case is settled and whose zero-entropy core resists every known method; reference identifiers require primary-source checking."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Furstenberg's ×2 ×3 Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Furstenberg's ×2 ×3 conjecture asserts that the only non-atomic Borel probability measure on the circle $\mathbb{T} = \mathbb{R}/\mathbb{Z}$ that is simultaneously invariant and ergodic under $T_2 : x \mapsto 2x$ and $T_3 : x \mapsto 3x \pmod 1$ is Lebesgue measure. Posed by Harry Furstenberg in 1967 as the measure-theoretic sharpening of his proved topological rigidity theorem, it is the prototype of higher-rank measure rigidity: two multiplicatively independent expansions should be too constraining to admit exotic invariant measures. This meta-analysis surveys the state of the art. The decisive partial result is Rudolph's 1990 theorem — any joint-invariant ergodic measure with positive entropy under one map is Lebesgue — extended by Johnson (1992) and reproved by Host (1995). Every known technique succeeds under positive entropy and is silent at zero entropy, where a hypothetical counterexample must live. We assess the principal approaches (entropy/conditional measures, normal numbers, higher-rank homogeneous-dynamics transfer, Fourier and additive-combinatorial methods), the zero-entropy barrier they share, and what a resolution would require. The conjecture remains **open** (status `active-progress`); no counterexample is believed to exist.

## 1. Statement and significance

Let $\mu$ be a Borel probability measure on $\mathbb{T}$ invariant and ergodic under the joint action of the commuting endomorphisms $T_2$ and $T_3$. The conjecture states: if $\mu$ is non-atomic, then $\mu$ is Lebesgue measure. Equivalently, the only ergodic $\langle T_2, T_3\rangle$-invariant measures are Lebesgue and those supported on finite sets of rationals. The multiplicative independence of $2$ and $3$ — that $\log 3/\log 2 \notin \mathbb{Q}$, so the generated semigroup is non-lacunary — is essential; for $\times 2$ alone there is a rich zoo of invariant measures.

The problem matters far beyond its concrete statement. Furstenberg's 1967 observation that a *joint* action of two independent expansions is dramatically more rigid than any single map is the conceptual seed of higher-rank rigidity, a paradigm that animates Ratner's theorems, the Margulis program in homogeneous dynamics, and the Einsiedler–Katok–Lindenstrauss work on Littlewood's conjecture. The ×2 ×3 conjecture remains a benchmark — a "rigidity Everest" — against which measure-classification techniques are measured.

## 2. State of the art

**Topological rigidity (proved, Furstenberg 1967).** Every closed $\langle T_2, T_3\rangle$-invariant subset of $\mathbb{T}$ is finite or all of $\mathbb{T}$. This is the closed-set analogue and is settled; it is *not* the measure conjecture, and newcomers sometimes conflate the two.

**Positive-entropy rigidity (proved, conditional on entropy).** Rudolph (1990) proved that any joint-invariant ergodic $\mu$ with $h_\mu(T_2) > 0$ is Lebesgue. Johnson (1992) removed a coprimality restriction, extending to all multiplicatively independent $p, q \ge 2$; Host (1995) gave an independent proof via normal numbers. These reduce the entire conjecture to the zero-entropy case and are universally accepted.

**Cousin conjectures resolved (2019).** Furstenberg's intersection/slicing conjectures — Hausdorff-dimension statements about $\times 2$ versus $\times 3$ invariant sets — were proved independently by Shmerkin and by Wu. These are related but distinct; their resolution sharpened the toolkit without yielding the measure-rigidity conjecture.

The full conjecture is **unproven**. No non-atomic, non-Lebesgue, jointly invariant ergodic measure is known, and ruling out the zero-entropy regime resists every existing technique.

## 3. Principal approaches and barriers

A single dichotomy organizes all progress: every method succeeds at positive entropy and degenerates at zero entropy.

- **Rudolph's entropy / conditional-measure method.** Positive entropy forces the conditional measures of $\mu$ along the common refinement of the two digit partitions to spread out; multiplicative independence propagates the spreading under both maps until $\mu$ is Lebesgue. *Barrier:* the argument gives no information when $h_\mu(T_2) = 0$.
- **Host's normal-numbers / disjointness route.** Host reproved positive-entropy rigidity by showing $\mu$-typical base-$p$ digit sequences are strongly normal, via a martingale/conditional-expectation argument. *Barrier:* the normality input collapses at zero entropy.
- **Higher-rank homogeneous-dynamics transfer.** Reframe the commuting endomorphisms as a rank-$\ge 2$ abelian action and import conditional-measure machinery from diagonal flows (Margulis, Einsiedler, Katok, Lindenstrauss). *Barrier:* the homogeneous theorems require positive entropy/dimension along a direction, and the non-invertible endomorphism setting lacks the unipotent/Ratner structure that makes those arguments work.
- **Fourier-analytic and additive-combinatorial inputs.** Invariance relates $\hat\mu(k)$ and $\hat\mu(pk)$; multiplicative independence over-constrains the spectrum, and sum–product/decoupling estimates quantify expansion. *Barrier:* Fourier decay alone does not detect zero-entropy singular measures finely enough.

## 4. Critical assessment

The dossier's central claim — that the conjecture is open and reduces cleanly to the zero-entropy case — is well supported and matches the consensus understanding of the field. The Rudolph–Johnson–Host trio is the load-bearing established result, and the framing of zero entropy as the "true heart" is accurate rather than rhetorical: there is genuinely no known mechanism (entropy, recurrence, harmonic-analytic, or combinatorial) that constrains a deterministic, low-complexity measure invariant under two independent expansions.

Two points deserve emphasis. First, the absence of a counterexample is *evidence of difficulty, not of truth*: most experts believe no exotic measure exists, but belief is not proof, and the survey is careful to label this as consensus rather than fact. Second, the relationship to the 2019 intersection-conjecture resolutions (Shmerkin, Wu) is correctly described as cousin-not-parent — those are dimension statements, and the dossier does not overstate their implication for the measure problem. This restraint is the right call.

## 5. What a resolution would require / open directions

A complete proof must control zero-entropy, deterministic invariant measures — objects invisible to every entropy-based tool. The required statement is essentially structural: joint invariance under two multiplicatively independent expansions should itself be incompatible with low dynamical complexity unless the measure is Lebesgue or atomic. Plausible routes, none yet reaching the regime, include: (1) transferring the Einsiedler–Katok–Lindenstrauss conditional-measure machinery to the non-invertible endomorphism setting, the obstacle being the missing unipotent structure; (2) additive-combinatorial expansion (sum–product, decoupling) forcing entropy positive or the measure to Lebesgue; (3) extending the $L^q$-norm / CP-chain methods that resolved the intersection conjecture from dimension statements to full measure classification. Expert consensus holds that a genuinely new idea about zero-entropy systems is likely required.

## 6. Selected references

1. H. Furstenberg, *Disjointness in ergodic theory, minimal sets, and a problem in Diophantine approximation* (1967). [high-confidence]
2. H. Furstenberg, *Recurrence in Ergodic Theory and Combinatorial Number Theory* (1981). [high-confidence]
3. R. Lyons, *On measures simultaneously 2- and 3-invariant* (1988). [needs-verification]
4. D. J. Rudolph, *×2 and ×3 invariant measures and entropy*, Ergodic Theory and Dynamical Systems **10** (1990), 395–406. [high-confidence]
5. A. S. A. Johnson, *A note on the entropy of $p$- and $q$-invariant measures* (1992). [needs-verification]
6. B. Host, *Nombres normaux, entropie, translations* (1995). [needs-verification]
7. M. Einsiedler, K. Schmidt, *Rigidity of measurable structure for $\mathbb{Z}^d$-actions by automorphisms of a torus* (1998). [needs-verification]
8. A. Katok, R. Spatzier, *Invariant measures for higher-rank hyperbolic abelian actions* (2003). [needs-verification]
9. M. Einsiedler, A. Katok, E. Lindenstrauss, *Invariant measures and the set of exceptions to Littlewood's conjecture*, Annals (2006). [high-confidence]
10. E. Lindenstrauss, *Invariant measures and arithmetic quantum unique ergodicity* (2006). [high-confidence]
11. J. Bourgain, E. Lindenstrauss, P. Michel, A. Venkatesh, *Some effective results for $\times a\, \times b$* (2011). [needs-verification]
12. M. Einsiedler, T. Ward, *Ergodic theory: with a view towards number theory* (2012). [high-confidence]
13. M. Hochman, P. Shmerkin, *Self-similar measures and the Furstenberg dimension conjectures* (2015). [needs-verification]
14. P. Shmerkin, *On Furstenberg's intersection conjecture, self-similar measures, and the $L^q$ norms of convolutions* (2019), arXiv:1609.07802. [needs-verification]
15. M. Wu, *A proof of the Furstenberg intersection conjecture* (2019). [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is accurate, dense, and appropriately hedged. Its strongest feature is the correct identification and consistent application of the positive-entropy/zero-entropy dichotomy as the organizing principle of the whole field — this is faithful to how practitioners actually understand the problem, and the document never lets the proved Rudolph–Johnson–Host result blur into a claim about the full conjecture. The careful separation of Furstenberg's *topological* theorem (proved) from the *measure* conjecture (open), and of the 2019 intersection-conjecture resolutions (cousins) from the target problem, avoids the two most common ways such surveys overstate progress.

I flag three things for a human checker. (i) Every reference here inherits the dossier's verification flags, and several anchors I would otherwise treat as canonical — Lyons 1988, Johnson 1992, Host 1995 — are marked `needs-verification` for exact title, year, and venue; the arXiv identifier on Shmerkin 2019 (arXiv:1609.07802) and the Einsiedler–Katok–Lindenstrauss Annals citation must be confirmed against primary sources before any downstream use. Do not propagate these identifiers unchecked. (ii) The document leans on the dossier as a single upstream source; the entropy-proportionality remark ("$h_\mu(T_2) > 0$ equivalently $h_\mu(T_3) > 0$") and the precise statement of Johnson's generalization should be cross-checked against the original papers, as the relationship between the two entropies for joint-invariant ergodic measures is more subtle than a one-line parenthetical conveys. (iii) The single most important thing to verify is the headline reduction itself — that positive entropy under *one* map suffices to force Lebesgue, and hence that the conjecture is genuinely equivalent to excluding the zero-entropy case — by reading Rudolph (1990) directly; everything else in the survey rests on it.

Subject to those checks, nothing here overclaims, and the open status is stated honestly throughout.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending

_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This document is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; the in-house Claude review above is a structured self-critique, not an independent referee report, and the cited references carry verification flags requiring primary-source checking. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
