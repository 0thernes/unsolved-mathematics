---
title: "Meta-Analysis: Giuga's Conjecture"
slug: giuga-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-structured survey of an open primality conjecture whose claims about bounds and equivalences are sound but whose reference apparatus carries multiple unverified flags requiring primary-source checking."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Giuga's Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Giuga's conjecture (1950) asserts that an integer $n>1$ is prime if and only if the power sum $S_n=\sum_{k=1}^{n-1}k^{\,n-1}$ satisfies $S_n\equiv -1\pmod n$. The forward implication is an immediate corollary of Fermat's little theorem; the open content is the converse, namely that no composite $n$ satisfies the congruence. Giuga reduced any composite counterexample to a transparent multiplicative form: such $n$ must be squarefree with $p\mid(n/p-1)$ for every prime $p\mid n$, equivalently a **Giuga number** ($\sum_{p\mid n}1/p-\prod_{p\mid n}1/p\in\mathbb Z$) that is simultaneously a **Carmichael number**. This double constraint explains both why no small counterexample exists and why the problem resists proof. This meta-analysis surveys the principal lines of attack — elementary factor-counting, Carmichael structure theory, the equivalent Bernoulli-number (Agoh–Giuga) formulation, the relaxed Giuga-number problem, and computational verification — and assesses what a genuine resolution would require. The consensus that emerges is that all existing techniques raise a lower bound without supplying a finiteness mechanism. The conjecture remains open. This document is a survey and makes no claim of a new result.

## 1. Statement and significance

Let $S_n=\sum_{k=1}^{n-1}k^{\,n-1}$. Giuga conjectured that $n>1$ is prime $\iff S_n\equiv-1\pmod n$. The "$\Rightarrow$" direction is elementary: for prime $p$, Fermat's little theorem gives $k^{p-1}\equiv1\pmod p$ for each $1\le k\le p-1$, so $S_p\equiv p-1\equiv-1\pmod p$. The conjecture's substance is the converse — that the congruence is a *characterization* of primality with no composite exceptions, in contrast to the many one-directional primality tests that admit pseudoprimes.

The significance lies in Giuga's reduction. A composite counterexample must be squarefree and satisfy $p\mid(n/p-1)$, i.e. $p^2\mid(n-p)$, for each prime factor $p$. This converts an analytic-looking congruence into a multiplicative divisibility condition and exposes the problem's two-sided nature: a counterexample must behave like a Carmichael number (Fermat congruences for all bases) *and* satisfy the rarer Giuga relation. The conjecture is a canonical "hard elementary" problem — trivial in one direction, computationally unfalsified to astronomical scale, yet apparently beyond current technique.

## 2. State of the art

The problem is **open**. The strongest unconditional results are structural and quantitative bounds on hypothetical counterexamples. Borwein–Borwein–Borwein–Girgensohn (1996) proved any counterexample has at least **13 distinct prime factors** and exceeds $10^{1700}$; subsequent computation reportedly raised the floor to roughly $10^{13{,}800}$, requiring thousands of distinct primes. The same 1996 work established the **equivalence** of Giuga's congruence with Agoh's Bernoulli criterion $nB_{n-1}\equiv-1\pmod n$, unifying two literatures into the **Agoh–Giuga conjecture**.

On the relaxed side, genuine **Giuga numbers** are known — the smallest is $30=2\cdot3\cdot5$, followed by $858,1722,66198,\dots$ — but none is a counterexample, because each fails the Carmichael condition. Whether infinitely many Giuga numbers exist is itself open. Contextually, Alford–Granville–Pomerance (1994) showed there are infinitely many Carmichael numbers, so the ambient class of a hypothetical counterexample is infinite while the Giuga sub-condition prunes it drastically.

## 3. Principal approaches and barriers

**Elementary factor-counting.** Summing the conditions $p_i\mid\prod_{j\ne i}p_j-1$ yields $\sum_i 1/p_i-1/n\in\mathbb Z$, forcing $\sum_i 1/p_i>1$ and hence lower bounds on the number of prime factors and on $n$. *Barrier:* this produces ever-larger lower bounds but no finiteness — nothing forbids an enormous $n$ with sufficiently many factors.

**Carmichael structure.** Every counterexample is a Carmichael number, and the Giuga condition $p\mid(n/p-1)$ is strictly stronger than Korselt's $p-1\mid n-1$, so counterexamples are far rarer than Carmichael numbers. *Barrier:* the ambient class is infinite (Alford–Granville–Pomerance), and the Giuga sub-condition is not known to be satisfiable or unsatisfiable infinitely often.

**Bernoulli / Agoh formulation.** Via Faulhaber's formula the congruence is equivalent to $nB_{n-1}\equiv-1\pmod n$, inviting von Staudt–Clausen and Kummer-type $p$-adic tools. *Barrier:* the equivalence is a translation, not a resolution; the Bernoulli form inherits the same difficulty.

**Relaxed Giuga-number problem.** Studying objects satisfying only the multiplicative relation isolates a tractable combinatorial problem (Giuga sequences, infinite families). *Barrier:* these are not counterexamples, and progress on them does not bear on the primality converse.

**Computational verification.** Structural constraints make exhaustive-in-structure search feasible far beyond naive ranges. *Barrier:* unbounded above; it only raises the floor.

## 4. Critical assessment

The dossier is internally consistent and the mathematics it reports is sound where it is canonical. Three load-bearing facts are genuinely established and well-attested: the Fermat-based forward direction; Giuga's reduction to the squarefree divisibility condition; and the Agoh–Giuga equivalence together with the 13-factor / $10^{1700}$ bound from Borwein et al. (1996). These can be stated with confidence.

Two claims warrant more caution. First, the often-quoted floor of "$\sim 10^{13{,}800}$" is a computational result whose precise provenance and exact value are not pinned down in the source material — the underlying papers (papers.md rows 18–19) are flagged *ai-suggested*, and this number should be treated as indicative rather than exact. Second, the unifying narrative that "a counterexample must be a Carmichael number *and* a Giuga number" is correct as stated, but readers should note the subtlety that the Giuga divisibility condition $p\mid(n/p-1)$ is what is reduced to; its identification with the rational relation $\sum 1/p-\prod 1/p\in\mathbb Z$ holds for the relevant squarefree objects and is worth verifying carefully rather than taking on faith.

The most important structural honesty in the dossier is its repeated insistence that no approach supplies a *finiteness mechanism*. This is the correct framing and the analysis does not overstate any route's prospects.

## 5. What a resolution would require / open directions

A proof must establish the converse **unconditionally**: no composite $n$, however large or however many prime factors, satisfies the congruence. Because the counting and size arguments yield only lower bounds, a resolution needs a new idea converting the simultaneous Carmichael + Giuga conditions into an outright contradiction. Three plausible but undeveloped routes: (1) a Bernoulli/$p$-adic obstruction forcing the Agoh form to fail for composites via von Staudt–Clausen and Kummer congruences; (2) a structural impossibility proof for the intersection Carmichael $\cap$ Giuga, using the constraint $\sum 1/p_i\approx$ integer alongside Korselt's criterion; (3) density/sieve methods showing the count of candidate counterexamples below $x$ is $o(1)$ unconditionally. None is close to completion; near-term progress is most likely in raising the verification floor and in partial results on generalized Giuga numbers.

## 6. Selected references

1. G. Giuga (1950), *Su una presunta proprietà caratteristica dei numeri primi* — the founding paper; states the conjecture, proves the prime direction, gives the reduction. [high-confidence]
2. D. Borwein, J. M. Borwein, P. B. Borwein, R. Girgensohn (1996), *Giuga's Conjecture on Primality*, Amer. Math. Monthly 103 — equivalence and the 13-factor / $10^{1700}$ bound. [high-confidence]
3. W. R. Alford, A. Granville, C. Pomerance (1994), *There are infinitely many Carmichael numbers*, Annals of Mathematics. [high-confidence]
4. P. Ribenboim (1997), *The New Book of Prime Number Records* — Giuga/Carmichael context. [high-confidence]
5. R. K. Guy (2004), *Unsolved Problems in Number Theory* — Giuga's conjecture entry. [high-confidence]
6. E. Bedocchi (1985), *Nota ad una congettura sui numeri primi* — sharpened structural and size constraints. [needs-verification]
7. (Agoh / related, 1996), *On a conjecture of Agoh concerning Bernoulli numbers and primality* — the Bernoulli criterion. [needs-verification]
8. K. G. C. von Staudt (1845), denominators of Bernoulli numbers (von Staudt–Clausen). [needs-verification]
9. A. Korselt (1899), criterion for Carmichael numbers. [needs-verification]
10. R. D. Carmichael (1910), pseudoprime numbers / number-theoretic function. [needs-verification]
11. J. M. Grau, A. M. Oller-Marcén (2009), *On the generalization of Giuga numbers*. [needs-verification]
12. J. M. Grau, A. M. Oller-Marcén (2012), *About the congruence $\sum k^{n-1}\equiv-1\pmod n$*. [needs-verification]
13. J. M. Grau, A. M. Oller-Marcén (2012), *Giuga numbers and the arithmetic of $\sum 1/p-\prod 1/p$*. [needs-verification]
14. (Borwein-school follow-up, 2005), *Giuga numbers and Giuga sequences: structure and examples*. [needs-verification]
15. (various, 2013), *Computational bounds on counterexamples to Giuga's conjecture*. [ai-suggested]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is accurate where it counts and admirably honest about the gap between bounding a counterexample and excluding one. The reduction, the Fermat forward direction, and the Agoh–Giuga equivalence are correctly presented, and the central thesis — that every known method raises a floor without supplying a finiteness mechanism — is the right diagnosis and is not oversold. The separation of the tractable relaxed (Giuga-number) problem from the intractable primality converse is handled cleanly and is the most valuable conceptual contribution here.

My principal reservation is the reference apparatus. Of the fifteen selected references only five carry a [high-confidence] flag; the remainder are [needs-verification] or [ai-suggested], and several titles/years (notably Bedocchi 1985, the Agoh paper, and the Grau–Oller-Marcén entries) are reconstructed. These must be checked against primary sources before any citation is relied upon. The Bedocchi and Grau–Oller-Marcén research lines are real, but exact bibliographic details are not confirmed here.

Two further points. (i) Single-source reliance: the entire modern quantitative backbone — both the 13-factor / $10^{1700}$ bound and the equivalence — rests on the single 1996 Borwein–Borwein–Borwein–Girgensohn paper; this is legitimately canonical, but a reviewer should confirm the paper says exactly what is attributed to it. (ii) Possible overstatement: the "$\sim 10^{13{,}800}$" verification floor is stated more precisely than its [ai-suggested] provenance warrants and should be softened or sourced. The single most important thing a human reviewer should verify is the exact statement and venue of Borwein et al. (1996) — Amer. Math. Monthly 103 — since nearly every quantitative claim in this document traces back to it.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and its claims, bounds, and especially its references require checking against primary sources by a qualified human reviewer before being relied upon. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
