---
title: "Meta-Analysis: Bunyakovsky's Conjecture"
slug: bunyakovsky-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-structured survey of an open problem that correctly centers the parity barrier and one-dimensionality, but leans on several verification-flagged references that require source-checking."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Bunyakovsky's Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Bunyakovsky's conjecture (1857) asserts that an irreducible integer polynomial of degree at least two, with positive leading coefficient and no fixed prime divisor, takes prime values infinitely often. It is the single-polynomial ($k=1$) seed of the modern web of prime-distribution conjectures — Schinzel's Hypothesis H, Hardy–Littlewood Conjecture F, and Bateman–Horn — and its flagship instance, $x^2+1$ (Landau's fourth problem), remains unresolved. This meta-analysis synthesizes the problem's history, the state of the art, and the principal lines of attack. The conjecture is completely open for every degree $\ge 2$: the strongest unconditional result is Iwaniec's 1978 theorem that admissible quadratics represent a $P_2$ (product of at most two primes) infinitely often. Two structural barriers — Selberg's parity problem and the one-dimensionality of single-variable sequences — explain why genuine primes have been reached only for thin *multivariate* families ($a^2+b^4$, $a^3+2b^3$) and for function-field analogues, but never for a one-variable polynomial of degree $\ge 2$. We assess what is solid, what is conditional, and what a resolution would require.

## 1. Statement and significance

Let $f(x)\in\mathbb{Z}[x]$ have degree $d\ge 1$ and positive leading coefficient. Bunyakovsky conjectured that $f(n)$ is prime for infinitely many positive integers $n$ provided that (1) $f$ is irreducible over $\mathbb{Q}$; (2) the leading coefficient is positive; and (3) there is no fixed prime divisor, i.e. $\gcd\{f(n):n\in\mathbb{Z}\}=1$. Condition (3) is indispensable: $x^2+x+2$ is irreducible yet always even. It is finitely checkable, since any prime dividing all values satisfies $p\le d$.

The conjecture's significance is structural. The degree-one case is Dirichlet's 1837 theorem; condition (3) is the exact local-to-global obstruction that, once removed, *should* leave no barrier to prime values. Bunyakovsky's framing — only visible congruence obstructions matter — propagates directly into Hypothesis H (1958), Hardy–Littlewood F (1923), and the quantitative Bateman–Horn law (1962). Resolving even one degree-$\ge 2$ case would be the first crack in a fifty-year edifice that is conjecturally complete but unconditionally untouched.

## 2. State of the art

**Unconditional results.** The conjecture is open for *every* polynomial of degree $\ge 2$; there is no single such polynomial proven to be prime-rich. What sieve theory delivers is almost-primes and sharp upper bounds:

- *Almost-primes.* Iwaniec (1978): every admissible irreducible quadratic represents a $P_2$ infinitely often; for $x^2+1$ this is the closest unconditional approach to Landau's problem. Halberstam–Richert weighted sieves give $P_r$ results for higher degree, with $r$ growing in $d$.
- *Upper bounds.* Sieves yield $\#\{n\le N: f(n)\text{ prime}\}\ll N/\log N$ with the conjecturally correct order; only the matching lower bound is missing.
- *Multivariate primes (not single-variable).* Friedlander–Iwaniec (1998) proved infinitely many primes of the form $a^2+b^4$ (density $\sim N^{3/4}$); Heath-Brown (2001) did so for $a^3+2b^3$ (density $\sim N^{2/3}$). These genuinely break parity, but for *two-variable* thin sequences; they cover no one-variable degree-$\ge 2$ polynomial.

**Conditional results.** The Bateman–Horn conjecture predicts the exact density of prime values and is numerically confirmed to high precision; it implies Bunyakovsky but is itself unproven. Sufficiently strong, uniform forms of the prime $k$-tuple / Elliott–Halberstam hypotheses also imply Bunyakovsky-type conclusions, but those hypotheses are open, and ordinary GRH is not known to suffice. Over function fields $\mathbb{F}_q[t]$, Hypothesis-H/Bunyakovsky statements are *theorems* — Sawin–Shusterman for large $q$, with antecedents in Pollack — proved unconditionally via geometric inputs (the Riemann hypothesis for curves, monodromy) that have no integer counterpart.

## 3. Principal approaches and barriers

**Sieve methods.** The dominant attack (Brun, Selberg, Rosser–Iwaniec sieves) on $\{f(n)\}_{n\le N}$ produces almost-primes and correct upper bounds but cannot certify primality. The decisive obstruction is the **parity problem** (Selberg): classical sieves cannot distinguish integers with an even number of prime factors from those with an odd number, so they cannot push $P_2$ down to $P_1$.

**Bilinear / Type-II forms.** Breaking parity requires injecting bilinear (Type-II) arithmetic information — the "asymptotic sieve for primes" of Bombieri and Friedlander–Iwaniec. This succeeded for the two-variable sequences $a^2+b^4$ and $a^3+2b^3$ precisely because a second free variable supplies the bilinear structure. The **one-dimensionality** of $f(n)$ is the barrier: a single-variable polynomial offers no room for the bilinear decomposition.

**Circle method.** Effective only for forms in *many* variables; a single one-variable polynomial gives too few major-arc contributions and uncontrollable minor arcs. Its lasting role is heuristic — the singular series $\mathfrak{S}(f)$ that defines the conjectural density.

**$k$-tuple / GPY–Maynard machinery.** Bunyakovsky is the $k=1$ case of Hypothesis H. Goldston–Pintz–Yıldırım and Maynard–Tao proved bounded gaps and "one of $k$ admissible *linear* shifts is prime infinitely often," but their weights act on linear forms and produce no prime values of a nonlinear $f$; they sharpen, rather than resolve, the difficulty.

The named barriers: **parity** (blocks pure sieves from $P_1$), **one-dimensionality** (denies the parity-breaking bilinear structure), and the **absence of an unconditional RH-strength input** over $\mathbb{Z}$ (the function-field successes lean on RH for curves; even GRH is not known to suffice).

## 4. Critical assessment

What is solid is genuinely solid. Iwaniec's $P_2$ theorem, the Friedlander–Iwaniec and Heath-Brown prime theorems for thin multivariate forms, the sharp sieve upper bounds, and the function-field theorems are all fully accepted, frequently cited, and methodologically central. The dossier's diagnosis — that the gap between these results and Bunyakovsky is *structural*, not merely technical — is, in my assessment, the correct reading of the field and is stated without overreach.

What is speculative is correctly labeled as such. The conjecture's "truth" rests on heuristic (Bateman–Horn) and analogy (function-field) evidence, not on any unconditional integer theorem. The dossier is appropriately firm that no claimed elementary proof — not even of $x^2+1$ — is accepted, and that the standard, decisive objection is always the parity problem: a density lower bound from a classical sieve certifies $P_2$-ness, not primality.

How far is the frontier? Honestly, very far. The realistic frontier sits at *two-variable* thin sequences and at function fields; the one-variable degree-$\ge 2$ case is untouched. The community consensus, faithfully reported here, is that even $x^2+1$ is expected to remain open for the foreseeable future. I would caution that the survey's three "plausible routes" are better read as a map of where a breakthrough would have to come from than as live programs — each currently lacks its essential ingredient (a single-variable bilinear input; an integer transfer of RH-for-curves; a proven fragment of $k$-tuple strong enough to yield $k=1$).

## 5. What a resolution would require / open directions

A proof for a single-variable degree-$\ge 2$ polynomial must overcome both structural barriers simultaneously:

1. **Defeat the parity problem.** Supply a genuinely new arithmetic input — a usable Type-II/bilinear estimate or an asymptotic-sieve-for-primes error term — for the one-dimensional sequence $\{f(n)\}$.
2. **Provide RH-strength equidistribution without a second variable.** Match, over $\mathbb{Z}$, the control that the function-field proofs obtain from RH for curves and monodromy — with no extra variable to manufacture bilinear structure.

Plausible directions, all currently out of reach: (a) extending Friedlander–Iwaniec asymptotic-sieve technology to a single variable; (b) transferring the function-field successes to $\mathbb{Z}$ via a major new equidistribution theorem; (c) deducing the $k=1$ case from a proven fragment of the prime $k$-tuple conjecture. Continued numerical and statistical testing of Bateman–Horn (e.g. prime-bias studies) refines confidence in the prediction without advancing a proof.

## 6. Selected references

1. P. G. L. Dirichlet (1837), *Beweis des Satzes, dass jede unbegrenzte arithmetische Progression… unendlich viele Primzahlen enthält* — degree-one case. [high-confidence]
2. V. Bunyakovsky (1857), memoir stating the conjecture, Imperial St. Petersburg Academy. [high-confidence]
3. L. E. Dickson (1904), *A new extension of Dirichlet's theorem on prime numbers* — precursor to Hypothesis H. [high-confidence]
4. E. Landau (1912), ICM address listing the four problems, including $n^2+1$. [high-confidence]
5. G. H. Hardy and J. E. Littlewood (1923), *Some problems of 'Partitio Numerorum' III* (Conjecture F). [high-confidence]
6. A. Schinzel and W. Sierpiński (1958), *Sur certaines hypothèses concernant les nombres premiers* (Hypothesis H). [high-confidence]
7. P. T. Bateman and R. A. Horn (1962), *A heuristic asymptotic formula…*, doi:10.1090/S0025-5718-1962-0148632-7. [high-confidence]
8. A. Selberg (1947 / 1965), the Selberg sieve and the parity discussion. [needs-verification]
9. H. Halberstam and H.-E. Richert (1974), *Sieve Methods* (monograph). [high-confidence]
10. H. Iwaniec (1978), *Almost-primes represented by quadratic polynomials*, doi:10.1007/BF01403066. [high-confidence]
11. J. Friedlander and H. Iwaniec (1998), *The polynomial $X^2+Y^4$ captures its primes*, doi:10.2307/120972. [high-confidence]
12. J. Friedlander and H. Iwaniec (1998), *Asymptotic sieve for primes*, doi:10.2307/120971. [high-confidence]
13. D. R. Heath-Brown (2001), *Primes represented by $x^3+2y^3$*. [high-confidence]
14. J. Friedlander and H. Iwaniec (2006), *Opera de Cribro* (sieve treatise). [high-confidence]
15. P. Pollack (2008), Hypothesis H in $\mathbb{F}_q[t]$. [needs-verification]
16. J. Maynard (2014), *Small gaps between primes*, doi:10.4007/annals.2015.181.1.7. [high-confidence]
17. W. Sawin and M. Shusterman (2018+), Bateman–Horn/Hypothesis-H over function fields for large $q$. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

This is a careful and well-organized survey. Its central virtue is that it identifies the *right* obstruction structure: the parity problem and one-dimensionality are correctly named as the reasons single-variable degree-$\ge 2$ cases remain untouched while two-variable thin sequences and function-field analogues have yielded genuine primes. The separation of unconditional from conditional results is clean, and the document is commendably explicit that no claimed elementary proof of $x^2+1$ is accepted, naming the parity problem as the standard refutation. I see no place where progress is overstated; if anything the tone is appropriately pessimistic about the near term.

That said, several load-bearing claims rest on references that carry verification flags and must be checked against primary sources. Specifically: the Selberg parity citations (#8 here; entries #6 and #9 in the dossier's paper list) have uncertain titles/dates; the Pollack and Sawin–Shusterman function-field entries are flagged needs-verification, yet the "true in spirit" narrative leans heavily on them. The exact statement, the range of $q$, and the degree restrictions in the Sawin–Shusterman result should be confirmed before the survey's strong "Bunyakovsky is a theorem over $\mathbb{F}_q[t]$" framing is relied upon. The dossier's own paper note already flags entry #13 as ai-suggested and #19/#22/#24 as uncertain — those should not be cited without confirmation.

The survey occasionally leans on a single methodological lineage (the Friedlander–Iwaniec school) as the de facto frontier; this is defensible and standard, but a human reviewer should confirm that no more recent (2018–2026) partial result narrows the gap further, since the dossier's timeline effectively stops around 2018. The single most important thing to verify: that the function-field results are stated with their precise hypotheses, because they carry the bulk of the "the integer statement is true" argument and are exactly the entries flagged as needing verification.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md; the citations, their verification flags, and especially the function-field and parity-problem references require checking against primary sources before any reliance. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
