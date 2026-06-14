---
title: "Meta-Analysis: Lehmer's Mahler Measure Conjecture"
slug: lehmer-mahler-measure-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-scoped survey of an open Diophantine problem that correctly separates proven partial results from the still-open conjecture, but leans on a citation table with several unverified identifiers."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Lehmer's Mahler Measure Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Lehmer's conjecture, posed in 1933 as a by-product of a search for large primes, asks whether there is an absolute constant $c>1$ such that the Mahler measure $M(\alpha)$ of every non-cyclotomic algebraic integer satisfies $M(\alpha)\ge c$. The conjectural extremal value is Lehmer's number $\lambda_0=1.17628081\ldots$, the largest root of a degree-$10$ Salem polynomial. Equivalently, the conjecture demands a degree-independent lower bound on the logarithmic Weil height, $h(\alpha)\ge c'/\deg(\alpha)$. This meta-analysis surveys the problem's origin, its equivalent formulations, and the principal lines of attack: the auxiliary-polynomial (Dobrowolski) method, which yields only a bound tending to $1$; restriction to special polynomial families (Smyth's non-reciprocal theorem); degree-independent bounds in structured fields (Amoroso–Dvornicich's abelian case); and dynamical/equidistribution and computational approaches. We emphasize the sharp separation between genuinely proven partial and sibling results — including Dimitrov's 2019 resolution of the related Schinzel–Zassenhaus conjecture — and the central conjecture, which remains open. The assessment flags the structural barrier (degree-sensitivity of every known method) and identifies what a resolution would require.

## 1. Statement and significance

For a monic integer polynomial $P$ with roots $\alpha_i$, the **Mahler measure** is $M(P)=\prod_i\max(1,|\alpha_i|)$ (with leading coefficient $|a_d|$ as a prefactor in the non-monic case). By **Kronecker's theorem (1857)**, $M(P)=1$ if and only if $P$ is, up to a power of $x$, a product of cyclotomic polynomials — i.e. all roots are roots of unity. Lehmer asked whether non-cyclotomic polynomials can have measure arbitrarily close to $1$. The modern **conjecture** asserts they cannot: $\inf\{M(\alpha):M(\alpha)>1\}\ge c>1$, with $\lambda_0=1.17628\ldots$ the conjectured minimum.

The significance is structural. Via $h(\alpha)=\log M(\alpha)/\deg(\alpha)$, the conjecture is a uniform height lower bound — the toral ($\mathbb{G}_m$) case of a family of Lehmer-type problems spanning abelian varieties (the elliptic Lehmer problem) and arithmetic dynamics, where $\log M$ is the canonical height of a toral endomorphism. The smallest measures arise from **Salem numbers**, tying the problem to Pisot theory and to questions about the distribution of conjugates. It is worth stressing, as the dossier does, that Lehmer himself posed an open question and did not conjecture that $\lambda_0$ is optimal; the strong form is later folklore, well-tested but never asserted by Lehmer.

## 2. State of the art

The conjecture is **open** (mid-2026). The best general unconditional result remains **Dobrowolski's (1979)** inequality, in Voutier's explicit form
$$M(\alpha)\ge 1+\tfrac14\left(\frac{\log\log d}{\log d}\right)^3$$
for non-cyclotomic $\alpha$ of degree $d\ge2$. Crucially this tends to $1$ as $d\to\infty$, so it does not supply the degree-independent constant the conjecture demands. Complete unconditional resolution exists only for restricted classes: **Smyth (1971)** for non-reciprocal polynomials ($M\ge\theta_0=1.32472\ldots$, the smallest Pisot number); **Borwein–Dobrowolski–Mossinghoff (1999)** for odd-coefficient polynomials; and various bounded-height or few-term families. The general problem reduces to **reciprocal** polynomials, where Salem numbers — and the hard cases — concentrate.

Under Galois constraints the full uniform bound is known: **Amoroso–Dvornicich (2000)** proved $h(\alpha)\ge(\log 5)/12$ for any non-torsion $\alpha$ in an abelian extension of $\mathbb{Q}$, with extensions by Amoroso–Zannier (controlled local degrees) and Amoroso–David (the higher-dimensional $\mathbb{G}_m^n$ analogue). Exhaustive searches past degree $40$ (Boyd, Mossinghoff, Rhin, Flammang, Wu) have not displaced $\lambda_0$ as the smallest known measure exceeding $1$.

## 3. Principal approaches and barriers

**Auxiliary polynomials (Dobrowolski method).** One builds an auxiliary polynomial vanishing to high order at the conjugates and their $p$-power images, exploiting the congruence $\alpha_i^p\equiv\alpha_i\pmod p$ (a Frobenius/Fermat phenomenon), then derives a contradiction if $M(\alpha)$ is too small. Four decades of refinement (Cantor–Straus 1981, Louboutin 1983, Voutier 1996) improved constants but never the asymptotic shape: the bound still decays to $1$. The barrier is intrinsic degree-sensitivity.

**Restricting the polynomial class.** Smyth's non-reciprocal theorem is the cleanest near-miss, halving the problem but powerless on reciprocal polynomials where $\lambda_0$ lives. Odd-coefficient and few-term results share the same limitation.

**Heights in structured fields.** Abelian and bounded-local-degree results exploit special ramification/congruence control unavailable for a generic Galois group (e.g. $S_d$).

**Salem numbers, dynamics, equidistribution.** Bilu equidistribution gives a soft reason small-measure conjugates cluster on the unit circle, consistent with but not forcing a quantitative gap. The barrier: equidistribution is asymptotic and does not by itself produce a uniform constant.

**Computation.** Exhaustive search disciplines the strong form but cannot, in principle, close an infinite family.

## 4. Critical assessment

The dossier's central virtue is honesty about scope. It repeatedly and correctly distinguishes proven results from the open conjecture, and it handles the most seductive confusion — the **Schinzel–Zassenhaus conjecture**, resolved by **Dimitrov in 2019** — with precision: bounding the *house* (largest conjugate modulus) is strictly weaker than bounding the *measure*, and Dimitrov's metric/Pólya-type method has not transferred to Lehmer. Equally, it flags that abelian-case results are sometimes misreported in popular accounts as "solving Lehmer," which they do not.

The recurring theme — that every known method is degree-sensitive and that crossing from "$1+o(1)$" to "$\ge c>1$" needs a genuinely new idea — is the correct diagnosis and is well-supported by the persistent failure to improve Dobrowolski's asymptotic shape. The treatment of computation as "disciplining but not proving" is appropriately modest.

Two cautions. First, the strong form (that $\lambda_0$ is the exact minimum) is folklore; the document is careful to attribute restraint to Lehmer, and this care should be preserved in any downstream summary. Second, the empirical claim "searches past degree $40$" and the constants quoted (e.g. Voutier's $\tfrac14$) are stated cleanly but rest on a citation table several of whose identifiers are unverified (see §6).

## 5. What a resolution would require / open directions

A resolution must exhibit a constant $c>1$ with $M(\alpha)\ge c$ for *every* non-cyclotomic algebraic integer, uniformly in degree — equivalently $h(\alpha)\ge c'/\deg(\alpha)$. The central obstruction is the degree-sensitivity of the auxiliary-polynomial machinery. Plausible routes flagged in the dossier: (i) extending Dimitrov-type metric/equidistribution inequalities from the house to the full measure; (ii) pushing height bounds from abelian/structured fields to arbitrary Galois groups; (iii) a dynamical or arithmetic-equidistribution argument forcing a quantitative gap from the clustering of conjugates; (iv) new transcendence-theoretic auxiliary constructions. A negative resolution — a family of non-cyclotomic measures tending to $1$ — would require a construction that has eluded all exhaustive searches and seems, empirically, very unlikely.

## 6. Selected references

1. D. H. Lehmer, *Factorization of certain cyclotomic functions*, Ann. of Math. (1933). DOI 10.2307/1968172. [high-confidence]
2. C. J. Smyth, *On the product of the conjugates outside the unit circle of an algebraic integer*, Bull. LMS (1971). DOI 10.1112/blms/3.2.169. [high-confidence]
3. P. E. Blanksby, H. L. Montgomery, *Algebraic integers whose conjugates lie near the unit circle*, Acta Arith. (1971). DOI 10.4064/aa-18-1-355-369. [high-confidence]
4. E. Dobrowolski, *On a question of Lehmer and the number of irreducible factors of a polynomial*, Acta Arith. (1979). DOI 10.4064/aa-34-4-391-401. [high-confidence]
5. D. W. Boyd, *Reciprocal polynomials having small measure*, Math. Comp. (1980). DOI 10.2307/2006401. [high-confidence]
6. R. Salem, *Algebraic numbers and Fourier analysis* (1962). [high-confidence]
7. P. Voutier, *An effective lower bound for the height of algebraic numbers*, Acta Arith. (1996). DOI 10.4064/aa-74-1-81-95. [needs-verification]
8. F. Amoroso, S. David, *Le problème de Lehmer en dimension supérieure*, J. reine angew. Math. (1999). DOI 10.1515/crll.1999.058. [needs-verification]
9. P. Borwein, E. Dobrowolski, M. J. Mossinghoff, *Lehmer's problem for polynomials with odd coefficients* (1999). [needs-verification]
10. F. Amoroso, R. Dvornicich, *A lower bound for the height in abelian extensions*, J. Number Theory (2000). DOI 10.1006/jnth.2000.2514. [high-confidence]
11. C. J. Smyth, *The Mahler measure of algebraic numbers: a survey* (2008). [high-confidence]
12. V. Dimitrov, *A proof of the Schinzel–Zassenhaus conjecture on polynomials* (2019; arXiv:1912.12545, Acta Math.). [high-confidence]
13. V. Dimitrov, P. Habegger, *Galois orbits and equidistribution: towards the Schinzel–Zassenhaus conjecture* (2020). [needs-verification]
14. V. Flammang, *Salem numbers of small trace and totally positive algebraic integers* (2016). [ai-suggested]
15. M. J. Mossinghoff et al., *The smallest Mahler measures (updated computational tables)* (2021). [ai-suggested]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is technically sound and unusually disciplined for a problem that attracts overreach. Its principal strength is the clean taxonomy: it correctly identifies that the conjecture reduces to reciprocal polynomials after Smyth, that Dobrowolski's bound is the best *general* result but is degree-decaying, and that the abelian and higher-dimensional theorems are genuine but conditional on Galois structure. The handling of the Schinzel–Zassenhaus / Lehmer distinction is exactly right and is the single most important thing a reader could get wrong; the document states plainly that Dimitrov resolved the *sibling* problem and that Lehmer's measure conjecture remains open. The equivalences (Mahler measure ↔ Weil height ↔ canonical height of a toral map) are stated accurately.

My referee concerns are three. (i) The reference apparatus is only partly verified: several DOIs are flagged "needs-verification," and items 14–15 are "ai-suggested," meaning the exact title/year may be approximate — these must be checked against MathSciNet/zbMATH primary records before any citation is relied upon. (ii) There is mild single-source reliance on the dossier's own framing for a few quantitative claims (the explicit $\tfrac14$ constant in Voutier's form; "searches past degree $40$"); both are plausible and consistent with the literature but should be confirmed against the primary papers rather than the survey. (iii) The attribution of Smyth's bound and the smallest-Pisot identification $\theta_0=1.32472\ldots$ (the plastic number) is standard and correct, but a reviewer should confirm the precise statement scope (algebraic *integers* vs. algebraic *numbers*) as worded.

The single most important thing a human reviewer should verify: that no claimed transfer of Dimitrov's method to the full measure exists in the post-2020 literature — i.e. that the "still open" status is current as of review, since this is the one place where a recent result could silently change the verdict.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This assessment is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and all flagged citations require primary-source checking against MathSciNet, zbMATH, or the publishers of record. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
