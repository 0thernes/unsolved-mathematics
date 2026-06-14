---
title: "Meta-Analysis: Sarnak's Möbius Disjointness Conjecture"
slug: sarnak-mobius-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "An accurate, well-scoped survey of a genuinely open problem; the science is sound but several cited identifiers carry needs-verification flags and must be source-checked before publication."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Sarnak's Möbius Disjointness Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Sarnak's Möbius disjointness conjecture (2010) asserts that the Möbius function $\mu(n)$ is asymptotically orthogonal to every observable $f(T^n x)$ arising from a topological dynamical system $(X,T)$ of zero topological entropy: $\frac1N\sum_{n\le N}\mu(n)f(T^nx)\to 0$ for all $f\in C(X)$ and all $x\in X$. It formalizes the heuristic that $\mu$ does not correlate with any "low-complexity" deterministic sequence, with zero entropy as the precise meaning of low complexity. This meta-analysis surveys the problem's origin, its tight coupling to Chowla's 1965 correlation conjecture, and the state of the art. Substantial classes are settled unconditionally — Kronecker, nilsystems, horocycle flows, automatic sequences — and Tao's entropy-decrement method established the logarithmically-averaged two-point Chowla and the equivalence log-Sarnak $\iff$ log-Chowla. Frantzikinakis–Host (2018) proved log-Sarnak for systems with countably many ergodic measures. The universal Cesàro-average statement remains open; the log-to-ordinary-average gap and "wild" zero-entropy systems are the principal barriers. The status is **active-progress**.

## 1. Statement and significance

Let $(X,T)$ be a compact metric space with a homeomorphism $T$. A sequence $\xi(n)=f(T^n x)$ with $f\in C(X)$ is an *observable* of the system. Sarnak's conjecture states that if $h_{\mathrm{top}}(T)=0$, then $\frac1N\sum_{n\le N}\mu(n)f(T^n x)\to 0$ as $N\to\infty$, uniformly in the sense of holding for every $f$ and every $x$. Equivalently, $\mu$ is disjoint, in Furstenberg's joinings sense, from every zero-entropy system.

The conjecture is significant as a unifying organizing principle. The Prime Number Theorem is exactly disjointness from the trivial one-point system; Davenport's 1937 bound on $\sum\mu(n)e(n\alpha)$ is disjointness from circle rotations. It packages dozens of disparate cancellation results under one statement and makes transparent the link to the **Chowla conjecture** (1965), which is the disjointness instance for the shift acting on $\mu$'s own correlation sequence. Chowla implies Sarnak; the converse fails in general, though Tao (2017) proved the two are equivalent in logarithmic average. The zero-entropy hypothesis is essential and non-removable: positive-entropy systems support observables that correlate with $\mu$.

## 2. State of the art

The problem is **open** with active progress. Unconditionally settled classes include: circle rotations and Kronecker systems (Davenport); all nilsystems and nilsequences (Green–Tao with the Bourgain–Sarnak–Ziegler criterion); horocycle flows (BSZ, 2013); the Thue–Morse and Rudin–Shapiro sequences (Mauduit–Rivat) and, more generally, all automatic sequences (Müllner, 2017); discrete- and quasi-discrete-spectrum systems; many rank-one and interval-exchange systems; and certain analytic skew products and smooth time-changes.

The strongest general theorem is Frantzikinakis–Host (2018): the conjecture holds, in **logarithmic average**, for every system with countably many ergodic invariant measures. On the Chowla side, Tao (2016) proved the logarithmically-averaged two-point Chowla conjecture via an entropy-decrement argument, and Tao (2017) proved log-Sarnak $\iff$ log-Chowla, so logarithmic progress transfers freely between them. Tao–Teräväinen extended the log-Chowla picture to odd orders. The analytic engine underlying most recent advances is the Matomäki–Radziwiłł theorem (2016) on multiplicative functions in short intervals.

## 3. Principal approaches and barriers

**Bourgain–Sarnak–Ziegler orthogonality criterion.** A bilinear/type-II decorrelation of dilated shifts $\xi(pn),\xi(qn)$ over primes yields orthogonality to $\mu$. This is the standard engine for concrete sequences (nilsystems, horocycle flows) but requires uniform decorrelation over many primes that fails or is unknown for general low-complexity systems.

**Ergodic structure theory.** Decompose a zero-entropy system into tractable factors (discrete spectrum, nilfactors, isometric extensions) and prove disjointness factor by factor. This reaches the Frantzikinakis–Host class but breaks down for systems with uncountably many ergodic measures and genuinely wild zero-entropy behavior.

**The Chowla route via entropy decrement.** Proving (a form of) Chowla implies Sarnak. Tao's entropy-decrement argument controls correlations by exploiting multiplicativity across scales, but loses a logarithm — yielding only logarithmic averages, not the ordinary Cesàro mean.

**Exponential-sum / type-I–type-II methods.** Vaughan/Heath-Brown identities treat orbit sums as arithmetic exponential sums; decisive for algebraic sequences but inaccessible for systems without arithmetic structure.

**Sieve / averaged approaches.** Disjointness on average or for almost every parameter, weaker than the every-$x$, every-$f$ demand.

The dominant barrier is the **log-to-Cesàro gap**: several results are known only logarithmically, and no general device converts them. Even ordinary two-point Chowla is unproven.

## 4. Critical assessment

The dossier's framing is, on the mathematics, careful and consistent with the consensus view of the field. Three points deserve emphasis. First, the field's defining honesty is that it does *not* overclaim: there is no claimed full proof, no disputed announcement to adjudicate, and the partial results are correctly stated as partial. This is a healthy literature. Second, the central conceptual gap — logarithmic versus ordinary Cesàro averaging — is genuine and load-bearing; the dossier rightly flags conflation of the two as the most common error in informal attempts. Third, the conjecture's reduction structure (Chowla $\Rightarrow$ Sarnak; log-equivalence) is accurately rendered, including the important caveat that Sarnak does not imply Chowla at the Cesàro level.

A reader should treat the precise attributions and dates as approximate pending source-checking. The dossier itself flags that several arXiv identifiers are reconstructed from memory. The split of the Tao–Teräväinen work into one or two papers, and the exact year tags on Mauduit–Rivat and BSZ, are the kind of detail that surveys frequently get slightly wrong.

## 5. What a resolution would require / open directions

A full proof would need to (i) close the log-to-Cesàro gap — equivalently, prove ordinary two-point Chowla, which no current method achieves; (ii) handle wild zero-entropy systems beyond the countably-many-ergodic-measure class, where structure theory is unavailable; and (iii) supply a universal mechanism linking multiplicativity of $\mu$ to zero entropy, rather than the present case-by-case verifications. The most-cited plausible routes are strengthening Matomäki–Radziwiłł short-interval technology to break the logarithmic barrier, extending the Frantzikinakis–Host joinings method past its countability hypothesis, and pushing higher-order Fourier analysis to even orders and ordinary averaging. The community broadly regards ordinary-average Chowla as the crux.

## 6. Selected references

1. H. Davenport (1937), *On some infinite series involving arithmetical functions (II)*. [high-confidence]
2. S. Chowla (1965), *The Riemann Hypothesis and Hilbert's Tenth Problem*. [high-confidence]
3. H. Furstenberg (1968), *Disjointness in ergodic theory, minimal sets, and a problem in Diophantine approximation*. [high-confidence]
4. P. Sarnak (2010), *Three lectures on the Möbius function, randomness and dynamics*. [high-confidence]
5. J. Bourgain, P. Sarnak, T. Ziegler (2010), *Möbius and nilsequences*. [needs-verification]
6. B. Green, T. Tao (2012), *The Möbius function is strongly orthogonal to nilsequences*. [high-confidence]
7. J. Bourgain, P. Sarnak, T. Ziegler (2013), *Disjointness of Möbius from horocycle flows*. [high-confidence]
8. C. Mauduit, J. Rivat (2010), *Sur un problème de Gelfond: la somme des chiffres des nombres premiers*. [high-confidence]
9. K. Matomäki, M. Radziwiłł (2016), *Multiplicative functions in short intervals*, arXiv:1501.04585. [high-confidence]
10. K. Matomäki, M. Radziwiłł, T. Tao (2015), *An averaged form of Chowla's conjecture*, arXiv:1503.05121. [needs-verification]
11. T. Tao (2016), *The logarithmically averaged Chowla and Elliott conjectures for two-point correlations*, arXiv:1509.05422. [high-confidence]
12. T. Tao (2017), *Equivalence of the logarithmically averaged Chowla and Sarnak conjectures*, arXiv:1605.06602. [needs-verification]
13. T. Tao, J. Teräväinen (2018), *The structure of logarithmically averaged correlations of multiplicative functions...*, arXiv:1708.02610. [needs-verification]
14. N. Frantzikinakis, B. Host (2018), *The logarithmic Sarnak conjecture for ergodic weights*, arXiv:1708.00677. [needs-verification]
15. C. Müllner (2017), *Automatic sequences fulfill the Sarnak conjecture*, arXiv:1602.03042. [needs-verification]
16. N. Frantzikinakis (2017), *Sarnak's conjecture: what's new (survey)*, arXiv:1704.09314. [needs-verification]
17. E. H. El Abdalaoui, J. Kułaga-Przymus, M. Lemańczyk, T. de la Rue (2014), *The Chowla and the Sarnak conjectures from ergodic theory point of view*, arXiv:1410.1673. [needs-verification]
18. A. Kanigowski, M. Lemańczyk, M. Radziwiłł (2021), *Disjointness of Möbius from analytic skew products / smooth time-changes*. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is accurate and appropriately scoped. Its strengths are real: it correctly identifies the open status, draws the Chowla–Sarnak relationship with the right directionality (Chowla $\Rightarrow$ Sarnak, log-equivalence, no Cesàro converse), and centers the log-to-ordinary-average gap as the genuine obstruction rather than a technicality. The taxonomy of approaches (BSZ, ergodic structure theory, entropy decrement, exponential sums, sieve/averaged) matches how practitioners in this field actually carve up the territory, and the negative results — entropy being essential, averaged statements being strictly weaker than the every-$x$ demand — are stated with the right force.

That said, a referee must register caveats. (i) Every citation here carries a verification flag, and the dossier explicitly admits that several arXiv identifiers and at least one author/year attribution are reconstructed from memory; these require primary-source checking against MathSciNet/zbMATH before any reuse — in particular entries 5, 10, 12–18, and the one-versus-two-paper split of the Tao–Teräväinen work (both arXiv:1708.02610 in the dossier, which is likely an error). (ii) Some claims rest effectively on a single source thread — for example the precise statement of the Frantzikinakis–Host result as "countably many ergodic measures" in *logarithmic* average should be confirmed verbatim, as the strength of the hypothesis is doing real work and is easy to overstate. (iii) The single most important thing a human reviewer should verify is the exact averaging mode attached to each headline result (Cesàro vs logarithmic), since the entire honest framing of "what is open" hinges on not silently upgrading a logarithmic result to an ordinary one.

None of these caveats touch the central mathematical content, which is sound and makes no claim of a new result. They are matters of citation hygiene and precision of statement, appropriate to a survey rather than indicative of a flaw.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This assessment is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; an accredited human reviewer should confirm the mathematical statements, the averaging modes of each cited result, and the bibliographic details flagged above before the document is relied upon. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
