---
title: "Meta-Analysis: Vojta's Conjecture"
slug: vojta-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-structured survey of an open conjecture that correctly isolates the canonical-class obstruction, but it leans on paraphrased citations carrying verification flags that demand primary-source checking."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Vojta's Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Vojta's conjecture, formulated by Paul Vojta in his 1987 thesis and the Springer Lecture Notes *Diophantine Approximations and Value Distribution Theory*, is a single height inequality on smooth projective varieties that mirrors Nevanlinna's Second Main Theorem term-for-term. For a normal-crossings divisor $D$, canonical divisor $K_X$, ample $A$, and finite place set $S$, it predicts $m_S(P,D)+h_{K_X}(P)\le \varepsilon\,h_A(P)+O(1)$ off a proper Zariski-closed set. By varying the geometry it implies $abc$, Mordell/Faltings, Bombieri–Lang, Siegel, and a qualitative Subspace Theorem. This meta-analysis surveys the dossier's account of the problem's origin, the body of proved special cases (group-variety cases via Faltings; general-position divisors via the Subspace Theorem and the 2020 Ru–Vojta General Theorem), and the standing obstruction: controlling $h_{K_X}$ for a general-type variety with no boundary divisor and no group structure. The conjecture remains open in full; the adjacent Mochizuki $abc$ claim is recorded as disputed. We assess the dossier as accurate and appropriately cautious, and flag the citation-verification burden for human reviewers.

## 1. Statement and significance

Let $X$ be a smooth projective variety over a number field $k$, $D$ a normal-crossings divisor, $K_X$ the canonical divisor, $A$ an ample divisor, and $S$ a finite set of places. The conjecture asserts that for every $\varepsilon>0$ there is a proper Zariski-closed $Z\subsetneq X$ with
$$ m_S(P,D) + h_{K_X}(P) \le \varepsilon\, h_A(P) + O(1) $$
for all $P\in X(k)\setminus Z$, where $m_S$ is the arithmetic proximity (counting) function and $h$ denotes Weil heights. A sharper "arithmetic discriminant" form, $m_S(P,D)+h_{K_X}(P)\le (1+\varepsilon)\,d_k(P)+\varepsilon\,h_A(P)+O(1)$, handles algebraic points of bounded degree. The significance is structural: specializing $X$ and $D$ recovers the $abc$ conjecture, the Mordell conjecture, the Bombieri–Lang conjecture, Siegel's theorem, and Schmidt's Subspace Theorem. A single inequality thereby exposes much of Diophantine geometry as one phenomenon — the arithmetic of a variety governed by the positivity of its canonical class.

## 2. State of the art

**Status: open.** No general form is proved, and there is no claimed proof of the full statement. The unconditional record falls into two regimes. First, **group-variety cases**: Faltings' theorem (Mordell, 1983) and the Mordell–Lang "Big Theorem" (1991/1992) settle the finiteness content for subvarieties of abelian varieties; Vojta (1994, 1996) extended this to semiabelian varieties and integral points, the high-water mark of unconditional progress. Second, **general-position divisors**: via Schmidt's Subspace Theorem, the height inequality holds for divisors in general position on $\mathbb{P}^n$ and suitable varieties — Ru–Wong (1991), Evertse–Ferretti, Corvaja–Zannier, Levin, Autissier — unified by the **Ru–Vojta General Theorem (2020)** through a $\beta$/Seshadri positivity invariant. The function-field $abc$ analogue (Mason–Stothers) and many cases of the analytic Second Main Theorem (Yamanoi, McQuillan, Ru) hold but do not imply the arithmetic conjecture. Conditionally, the conjecture implies the full list of Section 1; conversely, unconditional uniform-bound results (Dimitrov–Gao–Habegger 2021, Kühne) realize some quantitative consequences for curves.

## 3. Principal approaches and barriers

The dossier identifies four lines. (i) The **Subspace Theorem method** builds auxiliary linear forms forcing approximating points into finite unions of proper subspaces; its barrier is intrinsic reliance on general position and silence on $h_{K_X}$ for general-type varieties — and its exceptional set is a union of linear subspaces, not the genuine Zariski-closed $Z$. (ii) The **Ru–Vojta $\beta$-constant synthesis** packages this into one General Theorem, but the $\beta$-condition still encodes a positivity hypothesis on $D$ that the canonical case lacks. (iii) The **Arakelov/arithmetic-geometry method** (Vojta 1991, Faltings, Bombieri) exploits the endomorphism and $[n]$-multiplication structure of abelian/semiabelian varieties and does not survive to arbitrary general-type varieties. (iv) **Nevanlinna-theoretic transfer** treats the analytic Second Main Theorem as a target, but there is no mechanism mapping an analytic SMT to its arithmetic mirror: the analytic side has the Ahlfors–Schwarz lemma, negative curvature, and integration over $\mathbb{C}$; the arithmetic side has no analogue. The common obstruction is the canonical term $h_{K_X}$ in the regime with no boundary divisor and no group structure.

## 4. Critical assessment

The dossier is internally consistent and, by the standards of an expository survey, accurate. It correctly distinguishes what is proved (special cases) from what is implied (the consequence list) and resists the temptation to read the analytic Second Main Theorem as evidence stronger than heuristic. Its central diagnosis — that the missing ingredient is an arithmetic positivity principle for $K_X$ without group structure or a large boundary — matches the consensus framing among practitioners and is stated without overreach.

Two cautions. First, the Mochizuki/IUT $abc$ episode is handled neutrally and correctly as disputed (Scholze–Stix's Corollary 3.12 objection versus Mochizuki's rebuttals), with the right logical conclusion drawn: since $abc$ is treated as open, no implication for Vojta's conjecture follows. This is the appropriate posture. Second, the dossier's confidence about precise attributions and the exact scope of each "best result" should be calibrated against the verification flags in the reference list, several of which are paraphrased titles. The mathematical claims are sound; the bibliographic precision is where risk concentrates.

## 5. What a resolution would require / open directions

A full proof must control $h_{K_X}$ for an arbitrary variety of general type with no boundary divisor and no group structure — the exact regime where every method fails — and must produce the genuine Zariski-closed exceptional $Z$ rather than a union of linear subspaces. Equivalently, it must supply an arithmetic surrogate for negative curvature and integration over $\mathbb{C}$. The dossier names three plausible routes: (1) weaken the Ru–Vojta $\beta$/general-position hypothesis toward the pure canonical case (the most active near-term line); (2) sharpen Vojta's arithmetic tautological inequality on the arithmetic discriminant to mirror McQuillan's surface result; (3) discover a genuinely new positivity principle for $K_X$ on integral points — widely regarded as a generational problem, consistent with the dossier's very low tractability rating.

## 6. Selected references

1. Rolf Nevanlinna (1925), *Zur Theorie der meromorphen Funktionen*. [high-confidence]
2. Klaus F. Roth (1955), *Rational approximations to algebraic numbers* (Mathematika). [high-confidence]
3. Wolfgang M. Schmidt (1972), *Norm form equations*. [high-confidence]
4. Charles F. Osgood (1980), *Concerning a certain Nevanlinna defect relation*. [needs-verification]
5. Gerd Faltings (1983), *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern* (Inventiones). [high-confidence]
6. Paul Vojta (1987), *Diophantine Approximations and Value Distribution Theory* (LNM 1239). [high-confidence]
7. Enrico Bombieri (1990), *The Mordell conjecture revisited*. [high-confidence]
8. Gerd Faltings (1991), *Diophantine approximation on abelian varieties*. [high-confidence]
9. Min Ru, Pit-Mann Wong (1991), *Integral points, divisors, and the second main theorem*. [needs-verification]
10. Gerd Faltings (1992), *The general case of S. Lang's conjecture*. [high-confidence]
11. Paul Vojta (1994), *Integral points on subvarieties of semiabelian varieties, I*. [needs-verification]
12. Paul Vojta (1996), *Integral points on subvarieties of semiabelian varieties, II*. [needs-verification]
13. Pietro Corvaja, Umberto Zannier (2002), *A subspace theorem approach to integral points on curves*. [needs-verification]
14. Marc Hindry, Joseph H. Silverman (2004), *Diophantine Geometry: An Introduction*. [high-confidence]
15. Enrico Bombieri, Walter Gubler (2006), *Heights in Diophantine Geometry*. [high-confidence]
16. Aaron Levin (2009), *Generalizations of Siegel's and Picard's theorems*. [needs-verification]
17. Min Ru, Paul Vojta (2020), *A birational Nevanlinna constant and its consequences* (Ru–Vojta General Theorem), DOI 10.1353/ajm.2020.0027. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey's strengths are real. It states the height inequality and its arithmetic-discriminant refinement correctly, it draws the proved/implied distinction cleanly, and it isolates the genuine obstruction — the canonical term $h_{K_X}$ outside the general-position and group-variety regimes — rather than gesturing vaguely at "depth." The treatment of the analytic mirror is appropriately deflationary: the dictionary is named a dictionary, not a theorem, and the absence of an arithmetic Ahlfors–Schwarz analogue is correctly flagged as the standing gap. The Mochizuki/IUT material is handled with exactly the neutrality the situation demands.

Three reservations a human reviewer should weigh. (i) The reference list carries explicit verification flags; the majority of the modern entries are marked needs-verification and several titles are, by the dossier's own admission, paraphrases rather than exact transcriptions. Roth 1955 (Mathematika), Faltings 1983 (Inventiones), and Bombieri–Gubler 2006 are safe; the Ru–Wong, Vojta semiabelian, Levin, and Ru–Vojta entries — including the single DOI — need confirmation against MathSciNet/zbMATH before citation. (ii) There is some single-source reliance in the framing: the claim that "no path is known that does not effectively prove $abc$" and the attribution of specific scope to each "best result" rest on the dossier's own synthesis and should be checked against a primary survey (e.g., Vojta's own ICM-era expositions or the Hindry–Silverman text). (iii) The most important single item to verify is the precise statement and hypotheses of the 2020 Ru–Vojta General Theorem and its DOI — this is the load-bearing modern result, and the meta-analysis's characterization of its reach (the $\beta$/Seshadri condition and what it does and does not cover) should be confirmed against the published *American Journal of Mathematics* paper.

I recommend acceptance once the bibliographic flags are resolved and the Ru–Vojta scope claim is source-checked; no mathematical claim here appears incorrect, but the citation precision is unverified.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending

_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

This AI review is not a substitute for human peer review. It is offered to assist academic verification per ../docs/review/ACADEMIC-REVIEW.md, and every cited reference should be checked against a primary source before reuse. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
