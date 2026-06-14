---
title: "Meta-Analysis: Artin's Primitive Root Conjecture"
slug: artin-primitive-root-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful and well-proportioned survey of a conditionally-resolved problem whose GRH dependence is correctly identified as the crux, but whose mid-list citations carry verification flags requiring primary-source confirmation."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Artin's Primitive Root Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Artin's primitive root conjecture (1927) asserts that any integer $a$ that is neither $-1$ nor a perfect square is a primitive root modulo infinitely many primes, and more precisely that the primes for which this holds have a positive natural density equal to a rational correction factor $c_a$ times Artin's constant $A = \prod_q (1 - 1/(q(q-1))) \approx 0.3739558$. This meta-analysis surveys the problem's status, principal methods, and barriers. The conjecture is famously "morally solved": Hooley (1967) established the full quantitative statement assuming the Generalized Riemann Hypothesis (GRH) for the Dedekind zeta functions of the Kummer fields $\mathbb{Q}(\zeta_q, a^{1/q})$, and the function-field analogue is an unconditional theorem (Bilharz, completed via Weil's Riemann Hypothesis for curves). Unconditionally, Heath-Brown (1986) proved that at most two prime bases can be exceptions, yet for no single specified $a$ — not $2$, not $3$, not $10$ — is the conjecture known. The assessment concludes that the obstruction is squarely the absence of GRH-strength zero-free regions, and flags which cited references require primary-source verification before scholarly use.

## 1. Statement and significance

A primitive root modulo a prime $p$ is an integer $a$ generating the cyclic group $(\mathbb{Z}/p\mathbb{Z})^\times$. Fixing $a$ and varying $p$, Artin conjectured (to Hasse, 27 September 1927) that any $a \neq -1$ and non-square is a primitive root for infinitely many $p$, with density
$$
A(a) = c_a \prod_{q \text{ prime}} \left(1 - \frac{1}{q(q-1)}\right),
$$
where $c_a \in \mathbb{Q}$ (equal to $1$ generically) corrects for arithmetic entanglement. The heuristic — $a$ is a primitive root mod $p$ iff for every prime $q \mid p-1$ it is a non-$q$-th-power residue — translates a statement about prime densities into the splitting behaviour of $p$ in a tower of Kummer extensions, a quintessentially Artinian move contemporaneous with his reciprocity law. The problem is a touchstone for analytic number theory: it sits at the confluence of Chebotarev density, sieve theory, and the Riemann Hypothesis, and its many generalizations (number-field, matrix, and elliptic-curve analogues) drive an active, if small, research community.

## 2. State of the art

The problem's status is best described as **active progress, conditionally resolved**. The defining conditional theorem is Hooley's (1967): assuming GRH for all the fields $\mathbb{Q}(\zeta_q, a^{1/q})$, the count of primes $p \le x$ with $a$ a primitive root satisfies $N_a(x) \sim c_a A \cdot x/\log x$. This is universally accepted and is the benchmark; GRH is the entirety of what separates it from an unconditional theorem.

Unconditionally, the landmark is Heath-Brown (1986): Artin's qualitative conjecture fails for **at most two** prime values of $a$, so at least one of any three multiplicatively independent integers (e.g. $\{2,3,5\}$) is a primitive root infinitely often. Gupta–Murty (1984) earlier secured an infinite, density-zero set of bases. Goldfeld (1968) and Stephens (1969) proved the conjecture on average and for almost all $a$. The function-field analogue is fully proven (Bilharz 1937, made unconditional by Weil's 1948 proof of the Riemann Hypothesis for curves). The striking gap: despite all this, **no single named base** is known unconditionally to satisfy the conjecture.

## 3. Principal approaches and barriers

**Chebotarev / GRH (Hooley).** Inclusion–exclusion over squarefree $q$ writes $N_a(x) = \sum_q \mu(q)\, \pi_a(x,q)$, each term governed by the Chebotarev density theorem for $k_q = \mathbb{Q}(\zeta_q, a^{1/q})$. The barrier is the tail: summing over $q$ up to a usable range demands power-saving error uniform in $\deg k_q$, which only GRH-strength zero-free regions currently deliver.

**Sieve dichotomy (Gupta–Murty–Heath-Brown).** Restricting to finitely many $q$ and seeking a lower bound, combined with rank estimates and large-sieve/Brun–Titchmarsh inputs, yields the unconditional "at most two exceptions" theorem. Its limitation is structural: it is a non-effective dichotomy that cannot name a single base or remove the residual ambiguity.

**Entanglement framework (Lenstra–Stevenhagen–Moree).** A conceptual recasting of $c_a$ via the non-disjointness of the Kummer extensions yields uniform correction formulas for many variants, but reorganizes rather than removes the GRH dependence for individual densities.

**Averaging.** Goldfeld and Stephens average over $a$, smoothing away the dependence on individual zero-free regions — which is precisely why it succeeds and why it cannot resolve a named base.

## 4. Critical assessment

The dossier's central claim — that the conjecture is "morally solved," with GRH the sole missing ingredient — is well supported and is the mainstream view. The strongest evidence is the function-field case, where the analytic input (RH for curves) is a theorem and the conjecture follows; this is a genuine, load-bearing parallel, not rhetorical flourish. The two-sided structure of the field is also accurately rendered: a clean conditional theorem (Hooley) on one side, and an unconditional dichotomy (Heath-Brown) that conspicuously fails to name any base on the other.

Two points warrant care. First, the "density-zero set of size $\gg x/(\log x)^2$" attributed to Gupta–Murty should be checked against the original *Inventiones* paper, as the exact rate is easy to misquote. Second, the precise form of $c_a$ — a rational depending on the squarefree part of $a$ — is correct in spirit, but any reproduction of specific correction values (e.g. for $a = 2$, $a = 5$) should be cross-checked against Moree's 2012 survey rather than restated from memory. Neither point affects the qualitative picture.

## 5. What a resolution would require / open directions

Two plausible routes exist. **(1)** Prove sufficiently strong zero-free regions (or zero-density estimates) for the family $\zeta_{k_q}$, uniformly in $q$, to make Hooley's argument unconditional for a named base — essentially as hard as GRH for these fields. **(2)** Find a GRH-avoiding input controlling the large-$q$ tail $\sum_{q \text{ large}} \mu(q)\,\pi_a(x,q)$, perhaps via additive-combinatorial or large-sieve advances extending Gupta–Murty–Heath-Brown to a single specified $a$ and eliminating the two-exception ambiguity. No such input is presently on the horizon. The continuing payoff of route (2)-style work lies in the generalizations — number-field, matrix, and elliptic (Lang–Trotter-type) analogues — where partial unconditional results and exact constant computations remain achievable.

## 6. Selected references

1. C. F. Gauss (1801), *Disquisitiones Arithmeticae* — primitive roots; period of $1/p$. [high-confidence]
2. H. Bilharz (1937), *Primdivisoren mit vorgegebener Primitivwurzel* (function-field analogue, conditional on RH). [high-confidence]
3. D. H. Lehmer & E. Lehmer (1957), computations exposing the density discrepancy and forcing the correction factor. [needs-verification]
4. C. Hooley (1967), *On Artin's conjecture*, J. reine angew. Math. (Crelle) **225**. [high-confidence]
5. D. Goldfeld (1968), average / almost-all results for Artin's conjecture. [needs-verification]
6. P. J. Stephens (1969), an average result for Artin's conjecture. [needs-verification]
7. R. Gupta & M. R. Murty (1984), *A remark on Artin's conjecture*, Invent. Math. [high-confidence]
8. M. R. Murty (1985), *Primitive roots: a survey*. [needs-verification]
9. D. R. Heath-Brown (1986), *Artin's conjecture for primitive roots*, Quart. J. Math. (Oxford) **37**, DOI 10.1093/qmath/37.1.27. [needs-verification]
10. P. Stevenhagen & H. W. Lenstra (2005), *Chebotarev and his density theorem* (historical context). [needs-verification]
11. P. Moree (2012), *Artin's primitive root conjecture — a survey*, arXiv:1209.2376. [high-confidence]
12. A. Perucca et al. (2016), reductions of algebraic integers and entanglement of Kummer extensions. [ai-suggested]
13. P. Moree (2002), asymptotically exact heuristics for (near) primitive roots. [ai-suggested]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is faithful to the consensus and well-proportioned. Its principal strength is correctly locating the crux: the GRH dependence is not incidental but the whole obstruction, and the function-field analogue (where the corresponding RH is Weil's theorem) is deployed exactly as it should be — as concrete evidence that GRH is the right and sufficient hypothesis. The conditional/unconditional dichotomy — Hooley's clean theorem versus Heath-Brown's "at most two exceptions that cannot be named" — is rendered precisely, including the genuinely striking fact that no single specified base is settled.

I have three reservations a human reviewer should weigh. (i) The reference list carries explicit verification flags, and these are not cosmetic: rows for Goldfeld (1968), Stephens (1969), Murty's survey, the Lehmer computation, and the Stevenhagen–Lenstra and Perucca entries are flagged `needs-verification` or `ai-suggested`, meaning their exact titles, years, and venues are reconstructions that must be confirmed against MathSciNet/zbMATH before any scholarly citation. Even the Heath-Brown DOI is marked plausible-but-unconfirmed. (ii) There is a mild single-source risk: the modern structural narrative (entanglement, correction constants) leans heavily on the Moree/Lenstra–Stevenhagen circle, and the one fully solid modern citation is Moree's 2012 survey — a reader should not infer breadth of corroboration from what is effectively one authoritative survey plus its antecedents. (iii) No overstatement of *this* problem's status was found; the document consistently calls it open for every individual base.

The single most important thing a human reviewer should verify is the Heath-Brown (1986) result as stated — specifically that "at most two prime exceptions" is quoted with the correct quantifier and scope (prime bases, qualitative form) — since this is the load-bearing unconditional theorem and the most likely point of subtle misstatement. Secondarily, confirm the numerical value of Artin's constant and the Gupta–Murty density rate against primary sources.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This document is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; the claims, citations, and verification flags above should be checked against primary sources by a qualified human reviewer before scholarly use. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
