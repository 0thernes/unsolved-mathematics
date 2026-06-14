---
title: "Meta-Analysis: The Riemann Hypothesis"
slug: riemann-hypothesis
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-calibrated survey of an open problem that correctly separates conditional from unconditional results and never overstates the frontier; references carry verification flags that require human source-checking."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Riemann Hypothesis

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Riemann Hypothesis (RH) asserts that every non-trivial zero of the Riemann zeta function $\zeta(s)$ has real part $\tfrac12$. Posed almost in passing in Riemann's 1859 memoir, it controls the error term in the distribution of primes and sits at the center of analytic number theory; it is a Clay Millennium Prize Problem and the eighth of Hilbert's 1900 list. This meta-analysis synthesizes the project dossier into a single assessment. We summarize the unconditional state of the art—infinitely many zeros on the line (Hardy), a positive proportion above 40% (Levinson, Conrey), zero-free regions, large-scale numerical verification past the $10^{13}$th zero, and the recent pinning of the de Bruijn–Newman constant to $\Lambda \in [0, 0.22]$—and contrast it with the vast body of consequences that follow *conditionally* on RH or GRH. We then examine the principal attack routes—critical-line proportions, the Hilbert–Pólya spectral program, function-field analogues, explicit-formula positivity criteria, and analytic/sieve methods—and name the structural barrier each one hits. The problem remains open; the assessment throughout is that the frontier is far from a proof and that a fundamentally new idea is likely required.

## 1. Statement and significance

In its standard form RH states that every non-trivial zero $\rho$ of $\zeta(s)$ satisfies $\Re(\rho) = \tfrac12$. The function $\zeta(s) = \prod_p (1-p^{-s})^{-1}$ for $\Re(s) > 1$ extends meromorphically to the plane with a single pole at $s = 1$ and obeys a functional equation symmetric about the critical line $\Re(s) = \tfrac12$; the trivial zeros lie at $-2, -4, \dots$, and all non-trivial zeros lie in the strip $0 < \Re(s) < 1$. Riemann's explicit formula expresses the prime-counting function $\pi(x)$ as a sum over these zeros, so their real parts directly govern the size of the prime-number error term.

The significance is twofold. First, RH is equivalent to a sharp battery of arithmetic statements: $\pi(x) = \operatorname{li}(x) + O(\sqrt{x}\log x)$ (von Koch, 1901); the Mertens-type bound $M(x) = \sum_{n\le x}\mu(n) = O(x^{1/2+\varepsilon})$; Robin's criterion $\sigma(n) < e^{\gamma} n\log\log n$ for $n>5040$; and positivity of the Li/Keiper coefficients. Second, the Generalized RH (GRH, for Dirichlet $L$-functions) and Grand RH (for automorphic $L$-functions) underwrite a large fraction of conditional number theory. The dossier ranks RH first in both centrality (100) and difficulty (99) among the problems surveyed.

## 2. State of the art

**Unconditional.** Hardy (1914) proved that infinitely many non-trivial zeros lie exactly on the critical line. Selberg (1942) established that a *positive proportion* do; Levinson (1974) pushed this past one third via the zeros of $\zeta'$, and Conrey (1989) past two fifths (40.7%), with later refinements (Bui–Conrey–Young, Pratt–Robles–Zaharescu) inching above 41% but never reaching 50%. On zero-free regions, $\zeta(1+it) \ne 0$ (the engine of the Prime Number Theorem, Hadamard and de la Vallée Poussin, 1896) and the Vinogradov–Korobov region $\sigma > 1 - c/((\log t)^{2/3}(\log\log t)^{1/3})$ are known; crucially, no region of the form $\sigma > 1-\delta$ for *fixed* $\delta > 0$ has been established—that gap is the heart of the difficulty. Zero-density estimates (Ingham, Huxley) bound how many zeros could lie off the line but do not eliminate them. Computation has verified more than $10^{13}$ low-lying zeros and individual zeros near the $10^{22}$nd, all on the line (Odlyzko; Gourdon–Demichel), with rigorous certified checks maintained by Platt, Trudgian and others. The de Bruijn–Newman constant is now pinned to $\Lambda \in [0, 0.22]$: Rodgers–Tao (2020) proved $\Lambda \ge 0$ (Newman's conjecture), and Polymath15 (2019) proved $\Lambda \le 0.22$. Since RH is equivalent to $\Lambda \le 0$, RH—if true—holds with no margin to spare, at the boundary $\Lambda = 0$.

**Conditional.** Assuming RH or GRH yields the sharp prime error term, strong bounds on $M(x)$, effective estimates across many $L$-function problems, deterministic primality and prime-gap results, and much of the quantitative theory of primes in arithmetic progressions. This dense web of consequences is strong circumstantial evidence and a powerful incentive, but it is not a proof.

## 3. Principal approaches and barriers

- **Critical-line proportions** (Hardy, Selberg, Levinson, Conrey). Mollified second- and fourth-moment methods raise the proportion of on-line zeros. **Barrier:** the method yields positive-proportion results with no known route to 100%; even a full-density result would not exclude finitely or sparsely many off-line zeros.
- **Hilbert–Pólya / spectral.** Realize the imaginary parts $\gamma$ of the zeros as eigenvalues of a self-adjoint operator $H$, forcing $\gamma \in \mathbb{R}$. Montgomery's pair-correlation conjecture (1973) and Dyson's GUE observation, confirmed computationally by Odlyzko, give striking support; Berry–Keating proposed $H \sim xp$; Connes (1999) recast RH as a trace-formula positivity. **Barrier:** no natural operator with provably the right spectrum and proven self-adjointness exists; Connes's positivity is itself unproven.
- **Function-field / arithmetic-geometry analogues.** The RH analogue is a *theorem* over finite fields: Weil (1948) for curves and abelian varieties, Deligne (1974) for the Weil conjectures in general, using $\ell$-adic cohomology and Frobenius. **Barrier:** the proofs rest on a variety over $\mathbb{F}_q$ with Frobenius and Poincaré duality, with no established counterpart for $\zeta$ over $\mathbb{Q}$; the "$\mathbb{F}_1$" program to supply it is speculative.
- **Explicit-formula / positivity criteria** (Weil, Li, Báez-Duarte / Nyman–Beurling). RH is equivalent to positivity of the Weil distribution, to $\lambda_n \ge 0$ for all $n$, or to a density statement in $L^2(0,1)$. **Barrier:** each equivalent is no easier to prove unconditionally; they reorganize the problem without cracking it.
- **Analytic / sieve and moment methods.** Zero-free regions, zero-density estimates, and CFKRS random-matrix moment predictions describe average behavior. **Barrier:** no zero-free *strip* of positive width is known; the **parity problem** of sieve theory blocks naive attacks, and exceptional/Siegel-zero phenomena cannot currently be ruled out by these means.

## 4. Critical assessment

What is solid is genuinely solid and should not be confused with progress toward a proof. The on-line proportion results, the zero-free regions, the GUE pair-correlation match, and the certified numerics are real theorems and real data; the de Bruijn–Newman result $\Lambda \ge 0$ is a clean, recent, peer-reviewed advance. The function-field analogues (Weil, Deligne) are full proofs of the *correct analogue in a different setting* and rightly show RH is not isolated. The dossier is careful—correctly—to label all of this as evidence and structure, not as movement past the central obstruction.

What is speculative is the leap from any of these to RH itself. Every route reformulates the hard core rather than removing it: positive proportion is not totality; an equivalent positivity criterion is not a proof of that positivity; a candidate Hamiltonian is not a self-adjoint operator with the right spectrum; the finite-field template lacks its arithmetic geometry over $\mathbb{Q}$. The frontier is, honestly, far from a proof. The single most telling fact is the absence of any fixed-width zero-free strip $\sigma > 1-\delta$—a target far weaker than RH that remains out of reach. The dossier's framing, that most experts regard RH as true but expect its resolution to require a fundamentally new idea, is a fair reading of the field rather than a hedge.

## 5. What a resolution would require / open directions

A proof must exclude *every* zero from the open strip $0 < \Re(s) < \tfrac12$ (equivalently $\tfrac12 < \Re(s) < 1$). The recognized routes each demand a missing ingredient: (i) a Hilbert–Pólya self-adjoint operator with spectrum equal to the zeros, with self-adjointness proved; (ii) the positivity in Weil's explicit formula or Connes's trace formula, established unconditionally; (iii) an arithmetic-geometry framework over $\mathbb{Q}$ (or $\mathbb{F}_1$) mirroring Deligne's finite-field proof, with a positive-definite cohomological pairing; or (iv) a genuinely new analytic input converting positive-proportion / zero-density control into the exclusion of all off-line zeros. Closing $\Lambda \le 0.22$ down to $\Lambda \le 0$ *is* RH, and the flow methods that gave the lower bound do not obviously supply the matching upper bound. The GUE correspondence is the most suggestive structural clue but is not itself a proof strategy.

## 6. Selected references

1. B. Riemann (1859), *Über die Anzahl der Primzahlen unter einer gegebenen Größe*. [high-confidence]
2. J. Hadamard (1896), *Sur la distribution des zéros de la fonction $\zeta(s)$ et ses conséquences arithmétiques*. [high-confidence]
3. C.-J. de la Vallée Poussin (1896), *Recherches analytiques sur la théorie des nombres premiers*. [high-confidence]
4. H. von Koch (1901), *Sur la distribution des nombres premiers*. [high-confidence]
5. G. H. Hardy (1914), *Sur les zéros de la fonction $\zeta(s)$ de Riemann*. [high-confidence]
6. C. L. Siegel (1932), *Über Riemanns Nachlaß zur analytischen Zahlentheorie*. [high-confidence]
7. A. Selberg (1942), *On the zeros of Riemann's zeta-function*. [high-confidence]
8. H. L. Montgomery (1973), *The pair correlation of zeros of the zeta function*. [high-confidence]
9. P. Deligne (1974), *La conjecture de Weil. I*. DOI: 10.1007/BF02684373. [high-confidence]
10. N. Levinson (1974), *More than one third of zeros of Riemann's zeta-function are on $\sigma=1/2$*. DOI: 10.1016/0001-8708(74)90039-8. [high-confidence]
11. A. M. Odlyzko (1987), *On the distribution of spacings between zeros of the zeta function*. DOI: 10.2307/2007890. [needs-verification]
12. J. B. Conrey (1989), *More than two fifths of the zeros of the Riemann zeta function are on the critical line*. DOI: 10.1515/crll.1989.399.1. [high-confidence]
13. A. Connes (1999), *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*. DOI: 10.1007/s000290050042. [needs-verification]
14. E. Bombieri (2000), *Problems of the Millennium: The Riemann Hypothesis* (official problem description). [high-confidence]
15. D. H. J. Polymath (2019), *Effective approximation of heat flow evolution of the Riemann $\xi$ function, and a new upper bound for the de Bruijn–Newman constant*. arXiv: 1904.12438. [needs-verification]
16. B. Rodgers, T. Tao (2020), *The De Bruijn–Newman constant is non-negative*. DOI: 10.1017/fmp.2020.6. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

This survey is, to my eye as a referee, unusually disciplined about the line between evidence and proof—the single most common failure mode in RH writing. It correctly states that positive-proportion results (Hardy, Selberg, Levinson at >1/3, Conrey at >40%) do not approach totality, that the equivalent positivity/density criteria (Weil, Li, Nyman–Beurling) merely relocate the difficulty, and that the function-field theorems of Weil and Deligne are proofs of an *analogue* lacking the arithmetic geometry needed over $\mathbb{Q}$. The de Bruijn–Newman framing—$\Lambda \in [0,0.22]$, RH equivalent to $\Lambda \le 0$, hence "barely true" if true—is accurate and well-deployed. The conditional/unconditional split in §2 is exactly the right organizing spine.

My concerns are three. First, the references carry explicit verification flags, and several of the most load-bearing recent items (Odlyzko 1987, Connes 1999, Polymath15 arXiv:1904.12438, Rodgers–Tao DOI 10.1017/fmp.2020.6) are marked **needs-verification**; the works are standard and real, but the exact DOI/arXiv strings must be checked against the publisher record before this is cited anywhere downstream. Second, a few quantitative claims lean on a single thread of the dossier and should be confirmed against primary literature rather than the survey's own summary—specifically the precise current best on-line proportion (the dossier says "above 41%," attributed to Bui–Conrey–Young and Pratt–Robles–Zaharescu) and the exact height/index of the largest individually verified zero (stated as "near the $10^{22}$nd"). Neither affects the conclusions, but both are the kind of figure that drifts.

Third and most important: a human reviewer should verify the §5 equivalences that the document treats as established—above all that RH is *equivalent* to $\Lambda \le 0$ and that Polymath15 / Rodgers–Tao bound $\Lambda$ as stated. If any of those is misstated, the "no margin to spare" narrative weakens. That is the one claim I would not pass to print without a source check.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; the citations, equivalences, and quantitative figures above should be checked against primary sources before the document is relied upon. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
