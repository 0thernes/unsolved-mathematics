---
title: "Meta-Analysis: Sendov's Conjecture"
slug: sendov-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "An accurate, well-calibrated survey of a genuinely open problem whose unusual two-ended status (proved small and large, open in between) is correctly stated, but whose mid-table references need primary-source verification."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Sendov's Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Sendov's conjecture (1959) asserts that if every zero of a complex polynomial of degree $n \ge 2$ lies in the closed unit disk, then within distance $1$ of each zero lies a critical point — a zero of the derivative. It sharpens the classical Gauss–Lucas theorem from a global convex-hull containment to a local statement attached to each root, and the constant $1$ is sharp, witnessed by $p(z)=z^n-1$. This meta-analysis surveys the problem's history, the principal lines of attack, and the present frontier. The conjecture occupies an unusual position: it is verified rigorously for small degrees (roughly $n \le 8$) and, since Tao's 2020 theorem, proved for all sufficiently large $n$ — yet it remains open across a vast finite intermediate band of degrees. The decisive obstruction is twofold: the non-effectivity of the compactness argument that delivers the large-$n$ result, and the boundary-sharp regime, where the distinguished root approaches the unit circle and no error budget remains. I assess the credibility of the cited record, flag verification gaps in the dossier's bibliography, and identify what a complete resolution would demand.

## 1. Statement and significance

Let $p(z)=\prod_{k=1}^n (z-z_k)$ have all zeros in the closed unit disk, $|z_k|\le 1$. The conjecture states that for every root $z_j$,
$$\min_{w:\,p'(w)=0}\,|z_j-w|\le 1.$$
By scaling, this is equivalent to the assertion that if all roots lie in a disk of radius $r$, a critical point sits within distance $r$ of each root. The Gauss–Lucas theorem already confines all critical points to the convex hull of the roots; Sendov's conjecture is the strongest natural *local* refinement, demanding proximity to each individual root rather than mere global containment. Its significance is partly intrinsic — a clean, sharp extremal question in the geometry of polynomials — and partly as a testing ground for techniques relating root distributions to critical-point distributions, a theme connected to potential theory, random polynomials, and the logarithmic derivative $p'/p=\sum_k (z-z_k)^{-1}$.

## 2. State of the art

The problem's status is **active progress; open**, and its frontier is genuinely peculiar. At the small end, the degree-by-degree program — Rubinstein's $n=3$ (1968), and later work culminating in Brown–Xiang — established the conjecture rigorously up to roughly $n\le 8$. At the large end, **Terence Tao (2020)**, *"Sendov's conjecture for sufficiently high degree polynomials"* (arXiv:2012.04125), proved the conjecture for **all $n$ above some threshold $n_0$**, encoding the roots as a probability measure and analyzing the limiting equilibrium measure via compactness. Earlier, **Jérôme Dégot (2014)** had proved the large-degree case under the restriction that the distinguished root is bounded away from the unit circle, isolating the boundary as the hard regime. The combined effect is striking: the conjecture is known true at both ends of the degree spectrum, with only a finite — though astronomically large — intermediate band unproven. No complete proof exists, and the dossier correctly records that no claimed complete proof has survived expert scrutiny.

## 3. Principal approaches and barriers

**Direct estimation.** Fixing the distinguished root and bounding the nearest zero of $p'/p$ via variational/Lagrange-multiplier inequalities established the small degrees and identified $z^n-1$ as extremal. *Barrier:* the estimates degrade as $n$ grows; the configuration count explodes and the inequalities become too lossy for a uniform bound.

**Reduction to roots on the circle.** The hardest instances place the distinguished root, and the bulk of the others, on $|z|=1$. Sharp local statements were proved for this boundary case. *Barrier:* boundary sharpness leaves no slack to absorb errors — arguments valid in the interior collapse exactly where the conjecture is tightest.

**Asymptotic-in-degree (Dégot).** For a distinguished root with $|a|\le 1-\delta$, large $n$ forces a nearby critical point. *Barrier:* the threshold blows up as $|a|\to 1$, leaving the extremal boundary regime untouched.

**Potential theory (Tao).** The modern breakthrough: pass to a limiting measure $\mu$ and govern the zeros of $p'$ by the logarithmic potential / equilibrium properties of $\mu$. *Barrier:* the compactness step is non-effective in practice — a threshold $n_0$ exists but is not delivered at a usable scale, so it cannot be merged with the small-degree verifications.

There is no relativization- or natural-proofs-style formal barrier here; the obstructions are analytic (boundary sharpness and non-effectivity), which is the correct framing and one the dossier states carefully.

## 4. Critical assessment

The dossier is, to my reading, accurate and well-calibrated on the load-bearing facts. Three claims carry the weight: (i) the conjecture is verified for small degrees up to roughly $n\le 8$; (ii) Tao (2020) proved it for all sufficiently large $n$; (iii) the gap is a finite intermediate band created by non-effectivity. The first two are well documented and standard; the third is the correct synthesis and is what makes the problem's status genuinely unusual rather than merely "partially solved."

I would caution against two soft spots. First, the precise upper edge of rigorous small-degree verification ("$n\le 8$," with computer-assisted extensions "claimed somewhat higher") deserves a primary-source pin — the literature's exact verified ceiling has shifted over time and across rigor standards (interval-arithmetic vs. heuristic numerics), and the dossier itself hedges appropriately. Second, the precise content of Dégot's hypothesis (how $\delta$ enters and how the threshold depends on it) should be checked against the original rather than paraphrased. Neither caution undermines the survey's conclusions; both are about exactness of attribution, not direction.

## 5. What a resolution would require / open directions

A complete proof appears to need two complementary advances. **(1) An effective large-degree threshold:** convert Tao's existence-of-$n_0$ into an explicit, usable bound, ideally small enough to meet the verified small degrees. **(2) Closing the finite gap:** either push rigorous, certified verification up from $n\approx 8$ to meet a lowered threshold, or replace the compactness step with a quantitative argument valid for all $n$ — especially in the boundary-sharp regime. The most promising routes are effectivizing Tao's equilibrium-measure argument, sharpening quantitative potential theory to cover moderate $n$ directly, resolving the critical-points-near-the-circle case (work by Chalebgwa and collaborators), and extending certified degree-by-degree computation from below. Realistically, route (1) or (2) must render the gap finite-and-checkable before computation finishes it.

## 6. Selected references

1. W. K. Hayman, *Research Problems in Function Theory* (1967) — problem listing; conjecture attributed to Iliev. [high-confidence]
2. Z. Rubinstein, "On a problem of Ilieff" (case $n=3$), 1968. [high-confidence]
3. A. Meir, A. Sharma, "On Ilyeff's conjecture," 1969. [needs-verification]
4. D. Phelps, R. S. Rodriguez, "On a conjecture of Ilieff," 1969. [needs-verification]
5. A. W. Goodman, Q. I. Rahman, J. S. Ratti, "On the zeros of the derivative of a polynomial," 1969. [needs-verification]
6. A. Joyal, "On the zeros of the derivatives of a polynomial," 1972. [needs-verification]
7. J. E. Brown, "On the Ilieff–Sendov conjecture" (low-degree verification), 1991. [needs-verification]
8. Q. I. Rahman, G. Schmeisser, *Analytic Theory of Polynomials* (monograph), 1992/2002. [high-confidence]
9. J. Borcea, "Two results related to the Sendov conjecture," 1996. [needs-verification]
10. B. Bojanov, Q. I. Rahman, J. Szynal, "On the Sendov conjecture and related problems," 1999. [needs-verification]
11. J. Brown, G. Xiang, "Proof of the Sendov conjecture for polynomials of degree at most eight," 2002. [needs-verification]
12. J. Dégot, "Sendov conjecture for high-degree polynomials," 2014. [high-confidence]
13. T. Tao, "Sendov's conjecture for sufficiently high degree polynomials," 2020, arXiv:2012.04125. [high-confidence]
14. T. P. Chalebgwa (and/or collaborators), "On Sendov's conjecture about critical points near the unit circle," 2022. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

**Strengths.** This survey gets the architecture of the problem right, and that architecture is the whole point. The two-ended structure — proved for small $n$, proved for large $n$ by Tao, open in a finite band — is stated precisely and without hype, and the explanation for *why* the band persists (non-effectivity of compactness, plus boundary sharpness) is the correct and most illuminating framing. The anchor citations (Hayman 1967, Rubinstein, Rahman–Schmeisser's monograph, Dégot 2014, Tao's arXiv:2012.04125) are the right ones and are well-documented. The document is appropriately honest that no complete proof survives scrutiny.

**Concerns.** (i) A majority of the mid-table references carry `needs-verification` flags inherited from the dossier — exact titles, years, and venues for the 1969–2002 estimation literature (Meir–Sharma, Phelps–Rodriguez, Goodman–Rahman–Ratti, Bojanov–Rahman–Szynal, Brown, Brown–Xiang) were not confirmable from memory and must be checked against MathSciNet/zbMATH before any downstream citation; they should not be treated as settled. (ii) There is a mild single-source character to the "$n\le 8$" verified ceiling: it is repeated across the dossier but never pinned to a specific certified-numerics result, and the phrase "claimed somewhat higher" should not harden into fact. (iii) Tao's 2020 theorem is load-bearing and is treated as correct (it is widely so regarded), but a meta-analysis should not let a single paper's standing go unexamined — its precise statement and the *non-effective* nature of its threshold are exactly what the open gap hinges on, so any paraphrase of its hypotheses warrants a direct read.

**Most important thing to verify.** The single highest-value check is the **current rigorous lower edge of the open band** — i.e., the largest degree $n$ for which Sendov is *certifiably* proved (with what method and what rigor), confirmed against the primary computational papers. Everything in the "finite gap" narrative depends on where that edge actually sits today.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This document is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; the AI panel above is a structured first pass, not an endorsement. A human reviewer should source-check every `needs-verification` reference, confirm the current rigorous small-degree ceiling, and verify the exact statements of the Dégot (2014) and Tao (2020) theorems against their originals before this survey is relied upon. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
