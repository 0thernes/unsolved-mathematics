---
title: "Meta-Analysis: The Elliott–Halberstam Conjecture"
slug: elliott-halberstam-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "An accurate, well-scoped survey of a genuinely open problem; conclusions are sound but the citation table leans on several needs-verification entries that require primary-source checking."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Elliott–Halberstam Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Elliott–Halberstam conjecture (EH), stated by Peter D. T. A. Elliott and Heini Halberstam in 1968, asserts that the primes are equidistributed in arithmetic progressions, averaged over the modulus, up to level of distribution $\theta < 1$ — that is, for moduli as large as $x^{1-\varepsilon}$. It is the natural maximal strengthening of the Bombieri–Vinogradov theorem (1965), which secures $\theta = 1/2$ unconditionally and is often described as "GRH on average." This meta-analysis surveys EH's statement, its role as the linchpin of the bounded-gaps-between-primes program, and the state of the art. EH remains open for every $\theta > 1/2$ in the uniform (maximum-over-residue-class) sense. The deepest unconditional evidence is the Bombieri–Friedländer–Iwaniec result reaching $\theta = 4/7$ for a *fixed* residue class; Zhang's 2013 restricted estimate for smooth moduli at $\theta = 1/2 + 1/584$ sufficed, via Goldston–Pintz–Yıldırım, for the first finite prime gap. The central obstructions — the sharpness of the large sieve at $x^{1/2}$ and Selberg's parity problem — are well understood and constrain what any proof could yield. The document makes no claim of resolution.

## 1. Statement and significance

For $(a,q)=1$ write the error in the prime-counting function as $\Delta(x;q,a) = \pi(x;q,a) - \pi(x)/\varphi(q)$. The **level of distribution** $\theta$ is the supremum of exponents for which, for every $A > 0$,
$$\sum_{q \le x^{\theta}} \max_{(a,q)=1} \left| \psi(x;q,a) - \frac{x}{\varphi(q)} \right| \ll_A \frac{x}{(\log x)^A}.$$
The Bombieri–Vinogradov theorem gives $\theta = 1/2$. EH conjectures that the same average bound holds for every $\theta < 1$. The exclusion of $\theta = 1$ is deliberate: at level $1$ the modulus is comparable to $x$, a single progression contains $O(1)$ primes, and the asymptotic main term ceases to dominate — the boundary where the parity obstruction bites.

EH's modern significance is almost entirely instrumental. Goldston, Pintz, and Yıldırım (2005) showed that *any* $\theta > 1/2$ forces bounded gaps between primes, and that full EH yields $\liminf_n (p_{n+1}-p_n) \le 16$. EH is thus the cleanest single hypothesis governing how small prime gaps can provably be.

## 2. State of the art

**Unconditional.** Level $\theta = 1/2$ uniform in $a$ (Bombieri–Vinogradov, 1965) is the benchmark; subsequent refinements (Gallagher, Vaughan, Motohashi) sharpen constants but do not break $1/2$. For a **fixed** residue class, Bombieri, Friedländer, and Iwaniec (1986–89) reached $\theta = 4/7 \approx 0.571$ using Linnik's dispersion method and Deshouillers–Iwaniec bounds for averaged Kloosterman sums. For **smooth/well-factorable** moduli, Zhang (2013) obtained $\theta = 1/2 + 1/584$, optimized by Polymath8a toward $\theta = 1/2 + 7/300 \approx 0.523$.

**Conditional.** Under full EH the GPY sieve gives $\liminf(p_{n+1}-p_n) \le 16$; under the generalized conjecture GEH the Maynard–Tao multidimensional sieve (Polymath8b, 2014) gives $\le 12$, with bounds on $p_{n+2}-p_n$. Unconditionally, using only $\theta = 1/2$, Maynard (2013) and Tao reached $\le 246$.

## 3. Principal approaches and barriers

**Large sieve / Bombieri–Vinogradov.** Bounds the average error via the large sieve inequality, reducing to mean values of $L$-functions and bilinear (Vaughan/Heath-Brown) decompositions of $\Lambda$. Barrier: the large sieve is *sharp* at modulus $x^{1/2}$; the relevant bilinear ranges multiply to roughly $x$, and breaking $1/2$ by this route alone is provably impossible without new exponential-sum cancellation.

**Dispersion method and Kloosterman bounds (BFI).** Fixing $a$ and injecting cancellation from averaged Kloosterman sums (via Kuznetsov's trace formula / spectral theory of automorphic forms) supplies arithmetic input the large sieve cannot. Barrier: the method intrinsically fixes the residue class, so it does not yield the uniform max-over-$a$ statement; spectral bounds also cap the attainable $\theta$ well below $1$.

**Restricted EH for smooth moduli (Zhang; Polymath8).** Restricting to $y$-smooth, well-factorable moduli exposes extra bilinear structure, combined with Weil/Deligne bounds for algebraic exponential sums. Barrier: the statements are restricted to special moduli and the gains are tiny.

**The parity problem.** Selberg's parity obstruction shows pure sieve methods cannot distinguish numbers with an even versus odd number of prime factors; consequently EH/GEH alone cannot reach the twin-prime bound $\le 2$ — the best the framework reaches is $\le 6$ for certain configurations.

## 4. Critical assessment

The dossier's central claims are, on internal grounds, accurate and conservatively stated. The key load-bearing facts — Bombieri–Vinogradov gives $\theta = 1/2$; BFI reach $4/7$ for fixed classes but not uniformly; Zhang's restricted estimate is at $1/2 + 1/584$; GPY converts $\theta > 1/2$ into bounded gaps; the parity problem caps what EH can deliver — are standard, mutually consistent, and correctly attributed. The framing of the $1/2$ barrier as an artifact of method rather than a feature of the primes is the orthodox heuristic and is properly flagged as heuristic rather than proof.

Two points warrant care. First, the precise numerical exponents (the Polymath8a value $7/300$; the GPY conditional bound of $16$; the GEH bound of $12$) are quoted from secondary characterizations and should be checked against the published optimizations, since several competing exponents circulate in the literature for closely related estimates. Second, the relationship between EH, GEH, and the various *restricted* forms ($\mathrm{MPZ}[\varpi,\delta]$, well-factorable EH) is subtle; the document handles it correctly but a reader should not conflate Zhang's restricted smooth-modulus result with progress toward *uniform* EH, which it explicitly is not.

## 5. What a resolution would require / open directions

A proof of uniform EH for any $\theta > 1/2$ would require a source of cancellation in the governing bilinear/exponential sums that goes genuinely beyond the large sieve, which is provably sharp at $x^{1/2}$. The fixed-class BFI gains suggest the truth lies near $\theta = 1$, but no method has converted those gains into a uniform (max-over-$a$) statement — the dispersion method structurally fixes the class. Plausible routes: (1) extend BFI uniformly by removing the fixed-class restriction (most studied, most obstructed); (2) sharpen algebraic exponential-sum bounds to enlarge the smooth-moduli range (Zhang–Polymath line, gains tiny); (3) discover new large-sieve-type inequalities capturing arithmetic structure the classical one misses. Any uniform improvement past $1/2$ would be a landmark; the parity obstruction frames precisely what such an improvement could and could not deliver downstream in the prime-gaps program.

## 6. Selected references

1. E. Bombieri, *On the large sieve* (1965). [high-confidence]
2. A. I. Vinogradov, *The density of zeros of Dirichlet L-series and the distribution of primes in arithmetic progressions* (1965). [high-confidence]
3. H. Halberstam & K. F. Roth, *Sequences*, Vol. I (1966). [high-confidence]
4. P. D. T. A. Elliott & H. Halberstam, statement of the conjecture, in *Sequences* (1968). [needs-verification]
5. Y. Motohashi, *An induction principle for the generalization of Bombieri's prime number theorem* (1976). [needs-verification]
6. H. Halberstam & H.-E. Richert, *Sieve Methods* (1974). [high-confidence]
7. J.-M. Deshouillers & H. Iwaniec, *Kloosterman sums and Fourier coefficients of cusp forms* (1980). [needs-verification]
8. E. Bombieri, J. Friedlander & H. Iwaniec, *Primes in arithmetic progressions to large moduli* (1986). [high-confidence]
9. E. Bombieri, J. Friedlander & H. Iwaniec, *Primes in arithmetic progressions to large moduli. II* (1987). [needs-verification]
10. E. Bombieri, J. Friedlander & H. Iwaniec, *Primes in arithmetic progressions to large moduli. III* (1989). [needs-verification]
11. D. Goldston, J. Pintz & C. Yıldırım, *Small gaps between primes exist* (2005), arXiv:math/0505300. [needs-verification]
12. D. A. Goldston, J. Pintz & C. Y. Yıldırım, *Primes in tuples I* (2009), arXiv:math/0508185. [high-confidence]
13. J. Friedlander & H. Iwaniec, *Opera de Cribro* (2010). [high-confidence]
14. Yitang Zhang, *Bounded gaps between primes* (2014). [high-confidence]
15. D.H.J. Polymath, *New equidistribution estimates of Zhang type, and bounded gaps between primes* (Polymath8a, 2014), arXiv:1402.0811. [high-confidence]
16. James Maynard, *Small gaps between primes* (2015), arXiv:1311.4600. [high-confidence]
17. D.H.J. Polymath, *Variants of the Selberg sieve, and bounded intervals containing many primes* (Polymath8b, 2014), arXiv:1407.4897. [high-confidence]
18. A. Granville, *Primes in intervals of bounded length* (survey, 2016). [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is well-calibrated to what is actually known. Its principal strength is honesty about scope: it never confuses the *restricted* smooth-modulus results (Zhang, Polymath8a) or the *fixed-class* dispersion results (BFI) with progress toward the *uniform* conjecture, a distinction amateurs and even some expository accounts blur. The barrier analysis — large-sieve sharpness at $x^{1/2}$ and Selberg's parity obstruction — is correctly identified as the dual structural reason EH is both hard to prove and limited in what it could deliver. The conditional-consequence chain (GPY, Maynard–Tao, Polymath8b) is reported with appropriate hedging.

Three caveats a referee should weigh. (i) The citation table is honest about its own uncertainty: rows 4, 5, 7, 9, 10, 11, and 18 carry a needs-verification flag, and the original 1968 *Sequences* statement, Motohashi's induction principle, and the Granville survey title/year in particular must be checked against primary sources before any downstream citation. The high-confidence canonical works (Bombieri, BFI I, GPY *Primes in Tuples*, Zhang, Maynard, the two Polymath8 papers, *Opera de Cribro*) are reliable, but even their arXiv identifiers should be confirmed against published versions. (ii) The document relies substantially on a single coherent narrative thread (the bounded-gaps program as told through Tao's Polymath organization); this is the correct frame, but it means alternative formulations of EH and the GEH/restricted-EH hierarchy are compressed, and a reader could overstate how close the smooth-modulus gains bring us to uniform EH — they do not.

(iii) The single most important thing a human reviewer should verify is the precise numerical exponents and conditional bounds: the Polymath8a level ($1/2 + 7/300$), the GPY-under-EH gap bound ($16$), and the GEH gap bound ($12$). Multiple nearby values appear across the literature for closely related estimates, and these numbers are the document's most falsifiable specific claims. None of this undermines the central, correct conclusion that EH is open for every $\theta > 1/2$ in the uniform sense.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending

_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This assessment is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; the in-house panel above flags points requiring primary-source confirmation but does not substitute for an expert referee. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
