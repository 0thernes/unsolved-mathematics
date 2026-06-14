---
title: "Meta-Analysis: Polignac's Conjecture"
slug: polignac-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-calibrated survey of the bounded-gaps program that correctly frames Polignac as open and names the parity and level-of-distribution barriers, but rests on several citations flagged needs-verification."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Polignac's Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Polignac's conjecture (1849) asserts that for every even integer $k$ there are infinitely many pairs of consecutive primes differing by exactly $k$; the case $k=2$ is the Twin Prime Conjecture. The conjecture remains open for every individual $k$, including $k=2$. Since 2013 a sequence of breakthroughs—Zhang's first unconditional bounded gap, the Maynard–Tao multidimensional sieve, and the Polymath8 optimizations—has established a genuine but qualitative weakening: at least one even $k \le 246$ occurs as a consecutive-prime gap infinitely often, though no specific value is identified. This meta-analysis synthesizes the dossier into a single survey, distinguishing unconditional from conditional results, naming the two structural barriers (Selberg's parity barrier and the limited level of distribution of primes in arithmetic progressions), and assessing how far the frontier really sits from a full resolution. The consensus it reflects is that Polignac is regarded as no easier than the twin prime conjecture and is expected to remain open, even as the bounded-gaps record is refined. All cited references retain their verification flags and require human source-checking.

## 1. Statement and significance

Polignac's conjecture states: for every even integer $k$, there exist infinitely many pairs of consecutive primes $(p_n, p_{n+1})$ with $p_{n+1} - p_n = k$. Taking $k=2$ recovers the Twin Prime Conjecture; $k=4$ yields infinitely many cousin primes, $k=6$ sexy primes, and so on. A companion form asks only for infinitely many prime pairs $p$, $p+k$ (permitting primes between them); the two coincide for the purpose of the conjecture and the literature treats them interchangeably. Alphonse de Polignac reached the conjecture empirically in 1849, tabulating gaps and observing that each even value recurred indefinitely. The significance is foundational: the conjecture organizes the modern theory of prime gaps, and the 2013–2014 breakthroughs are routinely described as proving "a weak form of Polignac." Its quantitative refinement is the Hardy–Littlewood $k$-tuple conjecture (1923), which predicts a precise asymptotic density and implies Polignac as a special case.

## 2. State of the art

The problem is **open with major partial progress**; no individual case is proved or disproved. The decisive unconditional results are about *bounded* gaps. Zhang (2013) proved $\liminf_n (p_{n+1}-p_n) < 7\times10^7$, the first unconditional statement that some even $k$ in an explicit range is a gap infinitely often. Maynard and, independently, Tao introduced a multidimensional sieve reaching $\le 600$ and proving the far stronger statement that for every $m$ there are infinitely many bounded-length intervals containing at least $m$ primes. Polymath8b drove the unconditional bound to **246**, the current record. Crucially, all of these are existential over a finite admissible set: they establish that *some* even $k \le 246$ recurs infinitely often without naming it, so they do not settle any single case of Polignac, $k=2$ included.

Other landmark unconditional results are Chen's theorem (1973)—infinitely many primes $p$ with $p+k$ prime or semiprime, for every fixed even $k$—and the GPY result (2005/2009) that $\liminf_n (p_{n+1}-p_n)/\log p_n = 0$. **Conditionally**, under the Elliott–Halberstam conjecture the Maynard–Tao method yields $\le 12$, and a generalized Elliott–Halberstam input gives $\le 6$. Even full Elliott–Halberstam does not reach $k=2$: a residual parity obstruction blocks the step from $\le 6$ to $2$.

## 3. Principal approaches and barriers

**Sieve theory and the parity barrier.** Brun's sieve (1915) and the Selberg sieve (1940s) deliver sharp *upper* bounds on prime-pair counts (and Brun's theorem that $\sum 1/p$ over twin primes converges) but cannot, alone, force *lower* bounds. This is **Selberg's parity barrier**: a pure sieve cannot separate integers with an even number of prime factors from those with an odd number. Every unconditional advance must inject non-sieve arithmetic—typically equidistribution of primes in arithmetic progressions—to break parity. **Chen's theorem** is the sharpest sieve-type result; its irreducible "semiprime alternative" is exactly the parity barrier made visible.

**Small-gaps / multidimensional sieve.** GPY weighted $k$-tuples and showed any level of distribution $\theta > 1/2$ would yield bounded gaps; the obstruction was concrete—nobody could pass $\theta = 1/2$ (Bombieri–Vinogradov). **Zhang** crossed it with a restricted equidistribution estimate to level $1/2 + 1/584$ over smooth moduli, using deep algebraic-geometry inputs (Weil/Deligne-type bounds). **Maynard–Tao** then decoupled the result from any distribution beyond Bombieri–Vinogradov via a fully multidimensional sieve. The persistent **level-of-distribution barrier** is that equidistribution tops out near $\theta = 1/2$, insufficient to isolate individual gaps.

**Hardy–Littlewood / circle-method heuristics.** The $k$-tuple conjecture predicts exact densities and would imply Polignac, but the circle method fails for binary additive problems (the minor arcs cannot be controlled)—a structural obstruction, not a technical one.

## 4. Critical assessment

What is solid is substantial and well-verified: the bounded-gaps theorems (Zhang; Maynard; Tao; Polymath8b) are published in top venues and were checked quickly by the community. The number 246 is genuine and unconditional. The dossier is appropriately careful that this is an *existential* result—it does not name any $k$—and the survey does not overstate it. The framing of the two barriers (parity and level of distribution) matches the standard understanding in analytic number theory.

What remains speculative is the route to any *individual* case. No mechanism is known to breach the parity barrier, and the equidistribution strength needed to pin down a specific gap exceeds even what the Riemann Hypothesis supplies. The honest assessment is that the frontier sits far from $k=2$: the gap between "$\le 6$ under generalized Elliott–Halberstam" and "$=2$" is not a matter of optimization but of a missing idea. The dossier's empirical caution is well taken—Polignac's own false companion claim (every odd number is $2^k+p$, refuted by 127, 149, 251) is a reminder that numerical pedigree guarantees nothing—and claimed elementary proofs continue to fail on the same parity-independence errors. One caveat for the reader: several quantitative specifics (e.g., Zhang's $1/584$ exponent, the exact Polymath8 chain) rest on sources flagged needs-verification and should be checked against primaries.

## 5. What a resolution would require / open directions

A full resolution demands, for *every* even $k$, infinitely many consecutive-prime gaps equal to $k$. Two distinct obstructions stand: (1) breaking the parity barrier to obtain a lower bound that distinguishes primes from semiprimes, for which no method exists; and (2) equidistribution of primes in progressions to a uniformity approaching $\theta \to 1$, beyond current reach. Realistic near-term progress is incremental: lowering 246 toward the conditional floor of 6, and proving stronger distribution estimates over restricted moduli in Zhang's style. Resolving even $k=2$ likely requires either a genuine parity breach or a Hardy–Littlewood-strength input; the $k$-tuple conjecture would imply Polignac outright but is itself far out of reach. Most experts expect the conjecture to remain open for the foreseeable future.

## 6. Selected references

- A. de Polignac (1849), *Recherches nouvelles sur les nombres premiers*, Comptes Rendus. [high-confidence]
- V. Brun (1919), *La série $\sum 1/p$ sur les nombres premiers jumeaux est convergente*. [needs-verification]
- G. H. Hardy & J. E. Littlewood (1923), *Some problems of 'Partitio Numerorum'; III*. [high-confidence]
- A. Selberg (1947), *On an elementary method in the theory of primes*. [needs-verification]
- E. Bombieri (1965), *On the large sieve*. [needs-verification]
- J. R. Chen (1973), *On the representation of a larger even integer as the sum of a prime and the product of at most two primes*. [high-confidence]
- H. Halberstam & H.-E. Richert (1974), *Sieve Methods* (monograph). [high-confidence]
- D. A. Goldston, J. Pintz & C. Y. Yıldırım (2009), *Primes in tuples I*, Ann. of Math., doi:10.4007/annals.2009.170.819. [high-confidence]
- Y. Zhang (2014), *Bounded gaps between primes*, Ann. of Math., doi:10.4007/annals.2014.179.3.7. [high-confidence]
- J. Maynard (2015), *Small gaps between primes*, Ann. of Math., doi:10.4007/annals.2015.181.1.7. [high-confidence]
- D. H. J. Polymath (2014), *Variants of the Selberg sieve, and bounded intervals containing many primes* (Polymath8b), arXiv:1407.4897. [needs-verification]
- K. Soundararajan (2015), *Bounded gaps between primes* (Bourbaki seminar, Astérisque). [ai-suggested]
- A. Granville (2016), *Primes in intervals of bounded length*, Bull. AMS, doi:10.1090/bull/1521. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

This survey is accurate where it matters most. It correctly states that Polignac is open for every individual $k$, frames the 2013–2014 work as a *qualitative* weakening rather than a resolution, and—critically—stresses that the bound 246 is existential over an admissible set and identifies no specific gap. The treatment of the two barriers (parity, level of distribution) is the right diagnostic, and the distinction between unconditional ($\le 246$) and conditional ($\le 12$ under Elliott–Halberstam, $\le 6$ generalized) results is handled with appropriate care, including the non-obvious point that even full Elliott–Halberstam does not reach $k=2$.

My principal concern is sourcing. A substantial fraction of the references carry needs-verification or ai-suggested flags, and some load-bearing quantitative claims depend on them: Zhang's level $1/2 + 1/584$, the Polymath8a $\to$ 4680 $\to$ Polymath8b $\to$ 246 chain, and the Maynard $\le 600$ figure should each be confirmed against the primary papers (Zhang 2014 Annals; Maynard 2015 Annals; the arXiv Polymath8 preprints) before publication. The survey occasionally leans on a single phrasing of these numbers; a human reviewer should verify the exponents and bounds independently rather than trusting the dossier's recollection.

A second, smaller flag: the survey presents the parity barrier as an absolute obstruction to any sieve lower bound. That is the standard view and I endorse it, but it is a heuristic-cum-theorem with technical content (Selberg's parity principle) that a careful referee should see stated precisely, lest it read as folklore. The single most important thing a human reviewer should verify is the unconditional bound itself and its existential character: that "$\liminf_n(p_{n+1}-p_n)\le 246$" is established and that it does *not* name any $k$—this is the one claim a casual reader is most likely to misread as settling the twin prime case.

No phrasing in the document claims a proof of Polignac, and the related proven results (Chen, Zhang, Maynard–Tao, GPY) are described as what they are. With the citation checks above, this is publishable as a survey.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; the citations in particular—several of which carry needs-verification or ai-suggested flags—require checking against primary sources before any scholarly reliance. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
