---
title: "Meta-Analysis: Schinzel's Hypothesis H"
slug: schinzel-hypothesis-h
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-calibrated survey of Hypothesis H that correctly centers the one-variable parity barrier, but leans on references whose identifiers are self-flagged as reconstructed and needs primary-source verification."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Schinzel's Hypothesis H

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Schinzel's Hypothesis H (Schinzel and Sierpiński, 1958) asserts a clean local-to-global principle: a finite system of irreducible integer polynomials with positive leading coefficients whose product has no fixed prime divisor takes simultaneous prime values infinitely often. It unifies Bunyakovsky's single-polynomial conjecture and Dickson's linear conjecture, and thereby implies the twin-prime conjecture, the infinitude of primes $n^2+1$, and the Sophie Germain conjecture. The Bateman–Horn conjecture (1962) supplies the matching asymptotic density. The hypothesis is **open** in every nonlinear instance and in every prescribed twin-type instance; not a single concrete case is proved. This meta-analysis surveys the partial results that ring the problem — sieve upper bounds of the correct order, Chen's $P_2$ theorem, the Friedlander–Iwaniec and Heath-Brown thin two-variable cases, Green–Tao–Ziegler's finite-complexity linear systems, the Zhang–Maynard bounded-gaps revolution, and the Sawin–Shusterman function-field analogues. It identifies the parity problem in the one-variable setting as the structural obstruction that all current methods share, and assesses what a genuine resolution would demand.

## 1. Statement and significance

Let $f_1,\dots,f_k \in \mathbb{Z}[x]$ be irreducible with positive leading coefficients, and set $F = f_1\cdots f_k$. Hypothesis H states that if $F$ has **no fixed prime divisor** — for every prime $p$ there exists $n$ with $p \nmid F(n)$ — then there are infinitely many $n$ for which $f_1(n),\dots,f_k(n)$ are all prime. The "no fixed divisor" condition is exactly the obvious local obstruction; the hypothesis is the assertion that no obstruction beyond the local one exists.

Its significance is its scope. The case $k=1$, $\deg f \ge 2$ is Bunyakovsky's conjecture; the case of several linear $f_i$ is Dickson's; $\{x, x+2\}$ is twin primes; $f(x)=x^2+1$ is the oldest unsolved instance. Because so many landmark conjectures are special cases, Hypothesis H functions throughout analytic number theory as a benchmark "if-then" hypothesis. Its quantitative companion, Bateman–Horn, predicts the count up to $x$ as $\frac{1}{D}\,\mathfrak{S}\int_2^x \frac{dt}{(\log t)^k}$ with singular series $\mathfrak{S}=\prod_p (1-\omega(p)/p)(1-1/p)^{-k}$, specializing to the Hardy–Littlewood constants.

## 2. State of the art

The status is unambiguous: **open, with no proved instance**. The known unconditional results approach from several directions without touching any concrete case.

- **Right-order upper bounds.** Brun's and Selberg's sieves bound the count by $O(\mathfrak{S}\,x/(\log x)^k)$, matching Bateman–Horn up to a constant; the conjecture cannot fail by overcounting.
- **Almost-primes.** Chen's theorem (1973) yields infinitely many $p$ with $p+2$ prime or $P_2$ — one prime factor short of twin primes, by the parity barrier.
- **Thin two-variable sequences.** Friedlander–Iwaniec ($a^2+b^4$, 1998) and Heath-Brown ($a^3+2b^3$, 2001) prove primality for sparse polynomial sequences, breaking parity via bilinear structure — but these are two-variable, not instances of Hypothesis H.
- **Finite-complexity linear systems.** Green–Tao (2008) and Green–Tao–Ziegler (2010–2012) establish the Hardy–Littlewood asymptotic for any linear system of finite complexity — a large unconditional fragment of Dickson, excluding the infinite-complexity twin pattern.
- **Bounded gaps.** Zhang (2014), Maynard (2015), and Polymath8 give infinitely many bounded prime $m$-tuples for every $m$ (gaps $\le 246$): *some* admissible tuple recurs, but no prescribed one.
- **Function fields.** Sawin–Shusterman established Hypothesis H, twin-prime, and Bateman–Horn analogues over $\mathbb{F}_q[t]$ for suitable $q$, with power-saving errors — the only setting where a full analogue is a theorem.

Conditionally, Maynard's sieve gives gaps $\le 12$ under Elliott–Halberstam and $\le 6$ under its generalized form. No known conjecture of comparable plausibility is known to imply Hypothesis H.

## 3. Principal approaches and barriers

**Sieve methods.** Treating $F(n)$ as integers to be sifted produces correct-order upper bounds and almost-primes. The decisive obstacle is Selberg's **parity problem**: sieves cannot distinguish integers with an even versus odd number of prime factors, so they cannot force the factor count down to exactly one. Chen's $P_2$ sits precisely at this edge.

**Bilinear forms / dispersion.** Injecting Type I/II equidistribution (Bombieri–Vinogradov; the Friedlander–Iwaniec dispersion method) breaks parity for *two-variable* sequences. The single-variable values of Hypothesis H offer no factorization of the variable and hence no analogous bilinear input — the one-variable case is untouched.

**Circle method / higher-order Fourier analysis.** Hardy–Littlewood gives the expected main term, but minor arcs are uncontrollable with too few variables. Green–Tao–Ziegler's higher-order Fourier analysis resolves finite-complexity linear systems; the twin configuration $\{n,n+2\}$ has **infinite complexity**, where the controlling norms degenerate.

**Bounded-gaps sieves.** GPY/Maynard–Tao detect primes *somewhere* in an admissible tuple but cannot pin them to prescribed coordinates — parity reasserts itself.

**Function-field transfer.** The Sawin–Shusterman proofs rely on Weil's RH and monodromy, with no integer counterpart; the transfer to $\mathbb{Z}$ is heuristic only.

## 4. Critical assessment

The dossier's central claim — that a single structural obstruction, the **one-variable parity problem**, blocks every current route — is, in this reviewer's reading, accurate and well supported by the cited landmarks. The framing is honest in an important respect: it does not present the proximity of partial results (Chen's $P_2$, gaps $\le 246$, the function-field theorem) as near-resolution, but correctly notes that each stops at a structural wall rather than a removable gap. The distinction between two-variable breakthroughs ($a^2+b^4$) and the genuinely one-variable Hypothesis H is drawn carefully and is the crux of why the problem remains hard.

Two points warrant tightening. First, the survey occasionally compresses dates and attributions (e.g., Green–Tao "2008" versus the 2010 *Annals* version of "Linear equations in primes," and the 2004 arXiv versus 2008 publication of the arithmetic-progressions theorem); these are bibliographic, not mathematical, but a human editor should reconcile them. Second, the assertion that "no known conjecture of comparable plausibility implies Hypothesis H" is plausible and standard but is the kind of negative claim that merits an explicit source rather than community lore.

## 5. What a resolution would require / open directions

A proof must defeat the parity problem in the **one-variable** regime — the hardest known obstacle in the area. Concretely, this seems to require a genuinely new arithmetic input: an equidistribution statement for $\mu$ or $\Lambda$ against one-variable polynomial values strong enough to break parity, with no candidate presently known; or a rigorous function-field-to-integer transfer, which would appear to demand an unconditional substitute for RH over $\mathbb{Z}$. Three routes are live: (i) extending higher-order Fourier analysis past finite complexity, the direct attack on the twin heart; (ii) a one-variable analogue of the Friedlander–Iwaniec bilinear breakthrough; (iii) making the Sawin–Shusterman geometry rigorous over $\mathbb{Z}$. The community consensus, faithfully reported in the dossier, is that the problem is far from resolution.

## 6. Selected references

1. A. Schinzel & W. Sierpiński (1958), *Sur certaines hypothèses concernant les nombres premiers*, Acta Arithmetica 4. [high-confidence]
2. L. E. Dickson (1904), *A new extension of Dirichlet's theorem on prime numbers*. [high-confidence]
3. V. Bunyakovsky (1857), note on prime values of polynomials. [needs-verification]
4. G. H. Hardy & J. E. Littlewood (1923), *Partitio Numerorum III*, DOI 10.1007/BF02403921. [needs-verification]
5. P. T. Bateman & R. A. Horn (1962), *A heuristic asymptotic formula concerning the distribution of prime numbers*, DOI 10.1090/S0025-5718-1962-0148632-7. [needs-verification]
6. E. Bombieri (1965), *On the large sieve*. [high-confidence]
7. Chen Jingrun (1973), on a prime plus a product of at most two primes. [high-confidence]
8. H. Halberstam & H.-E. Richert (1974), *Sieve Methods*. [high-confidence]
9. J. Friedlander & H. Iwaniec (1998), *The polynomial $X^2+Y^4$ captures its primes*, DOI 10.2307/120966. [needs-verification]
10. D. R. Heath-Brown (2001), *Primes represented by $x^3+2y^3$*. [needs-verification]
11. B. Green & T. Tao (2008), *The primes contain arbitrarily long arithmetic progressions*, DOI 10.4007/annals.2008.167.481. [needs-verification]
12. D. Goldston, J. Pintz & C. Yıldırım (2009), *Primes in tuples I*, DOI 10.4007/annals.2009.170.819. [needs-verification]
13. B. Green & T. Tao (2010), *Linear equations in primes*, DOI 10.4007/annals.2010.171.1753. [needs-verification]
14. B. Green & T. Tao (2012), *The Möbius function is strongly orthogonal to nilsequences*, DOI 10.4007/annals.2012.175.2.3. [needs-verification]
15. Y. Zhang (2014), *Bounded gaps between primes*, DOI 10.4007/annals.2014.179.3.7. [high-confidence]
16. J. Maynard (2015), *Small gaps between primes*, DOI 10.4007/annals.2015.181.1.7. [high-confidence]
17. D. H. J. Polymath (2014), *Variants of the Selberg sieve...* (Polymath8b), arXiv:1407.4897. [needs-verification]
18. W. Sawin & M. Shusterman (2022), *On the Chowla and twin primes conjectures over $\mathbb{F}_q[t]$*, arXiv:1804.09140. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The dossier is a strong, honest survey. Its principal strength is conceptual discipline: it consistently distinguishes the *appearance* of progress from progress on the actual target, never letting Chen's $P_2$, the $\le 246$ gap, or the function-field theorem be mistaken for an instance of the integer Hypothesis H. The parity problem is correctly identified as a theorem about method classes rather than a patchable gap, which is the single most important thing a non-specialist reader could misunderstand. The treatment of why $a^2+b^4$ does not transfer to $n^2+1$ — the absence of a one-variable bilinear factorization — is the right diagnosis and is stated precisely.

Three cautions. (i) **Reference reliability.** The papers file self-discloses that several DOIs and arXiv identifiers (notably entries #3, #5, #13 in that file, and the *Annals* DOIs) are reconstructed from memory and carry `needs-verification` flags; I have preserved those flags above, but a human must check every identifier against the publisher before any of this is cited authoritatively. The arXiv number 1407.4897 for Polymath8b and 1804.09140 for Sawin–Shusterman are exactly the kind of recollection that is plausibly correct yet must not be trusted unverified. (ii) **Single-source / lore reliance.** The negative claim that no comparably plausible conjecture implies Hypothesis H, and the precise complexity-theoretic statement that the twin pattern has "infinite complexity," are stated as community consensus without a pinpoint citation; both are believable and standard but should be sourced. (iii) **Bibliographic drift.** Green–Tao dates (2004/2008 arXiv vs. *Annals*; 2008 vs. 2010 for "Linear equations in primes") are compressed and should be reconciled.

The single most important thing a human reviewer should verify: that the identifiers in the references — particularly the two arXiv IDs and the Bateman–Horn and Hardy–Littlewood DOIs — resolve to the works as described, since these are self-flagged as reconstructed.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This document is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and its mathematical claims, attributions, and especially its citation identifiers require checking against primary sources by a qualified human reader. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
