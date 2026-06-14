---
title: "Meta-Analysis: The Erdős–Straus Conjecture"
slug: erdos-straus-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-structured survey of an open problem whose central claims track the established literature, but whose citation table mixes canonical references with several unverified or AI-suggested entries that require primary-source checking."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Erdős–Straus Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Erdős–Straus conjecture asserts that for every integer $n \ge 2$ the fraction $4/n$ can be written as a sum of three positive unit fractions, $4/n = 1/a + 1/b + 1/c$. Posed by Paul Erdős and Ernst G. Straus around 1948, it is a paradigm of an elementary statement that resists uniform proof. This meta-analysis surveys the structure of the problem and the four principal lines of attack: reduction to primes and residue classes (culminating in Mordell's modulo-$840$ classification of the hard cases), explicit parametric identities, analytic exceptional-set and representation-count methods (Vaughan; Elsholtz–Tao), and the geometry of the associated cubic surface. The recurring obstruction is that any finite list of parametric identities clears a prime only under a fixed quadratic-residue condition, and by quadratic reciprocity and Dirichlet's theorem the "bad" residues persist with positive density. The conjecture is verified computationally past $n \sim 10^{17}$ and believed true, but remains open for general $n$. We assess what a resolution would require and flag the source-verification limits of the underlying dossier.

## 1. Statement and significance

The conjecture states that for every integer $n \ge 2$ there exist positive integers $a, b, c$ with $4/n = 1/a + 1/b + 1/c$; the unit fractions need not be distinct. It belongs to the study of *Egyptian fractions*, a tradition reaching back to the Rhind Papyrus and formalized by Fibonacci's greedy algorithm, which guarantees that every rational in $(0,1)$ has *some* finite unit-fraction expansion. The Erdős–Straus question sharpens this to a specific, minimal demand: for the numerator $4$, do *three* terms always suffice? Its significance lies less in any application than in what it exposes — a clean instance of the general phenomenon that multiplicative structure (primes, quadratic residues) controls additive representations in ways we cannot yet master. It sits in a family of "elementary but unyielding" problems alongside the Goldbach conjecture and odd perfect numbers.

## 2. State of the art

The problem is **open** (dossier status: *active-progress*) and widely believed true. The unconditional knowledge base is well-developed. A solution for a divisor of $n$ scales to $n$, so the conjecture reduces to prime denominators. Mordell's textbook reduction (1967) shows $4/n$ is soluble for every $n$ outside six residue classes modulo $840 = 2^3 \cdot 3 \cdot 5 \cdot 7$, namely $n \equiv r^2 \pmod{840}$ for $r \in \{1, 11, 13, 17, 19, 23\}$ — equivalently the primes $p \equiv 1, 121, 169, 289, 361, 529 \pmod{840}$. Vaughan (1970) bounded the potential failure set by $E(N) \ll N \exp(-c(\log N)^{2/3})$, so counterexamples, if any, are exponentially rare. Elsholtz and Tao (2011, arXiv:1107.1010) gave the strongest structural result: sharp average and higher-moment bounds for the representation-count function $f(n)$, behavior on primes and progressions, and a link to point-counts on associated cubic congruences. Computation confirms the conjecture for all $n$ up to at least $\sim 10^{17}$, with the number of representations growing. There are no clean conditional theorems (e.g. "assuming GRH") that close the problem; the conditional flavor is heuristic.

## 3. Principal approaches and barriers

**Reduction to primes and residue classes.** Classifying $p$ modulo small moduli and exhibiting parametric solutions class by class recovers Mordell's six-class reduction. The method works when a small factor of $n$ can be forced into a denominator, collapsing the equation to a soluble quadratic-residue condition; for the six square classes no such forcing exists, and the method cannot, even in principle, reach them.

**Parametric and identity-based constructions.** One writes $a, b, c$ as polynomials in $n$ with free parameters (Rosati, Bernstein, Yamamoto, Hagedorn). Each identity covers $p$ only when a fixed quadratic-residue condition holds, and a finite union of such conditions provably cannot cover an entire arithmetic progression of primes — a genuine structural limitation, not a gap in ingenuity.

**Analytic and exceptional-set methods.** Sieves, character sums, and estimates for primes in progressions yield Vaughan's bound and the Elsholtz–Tao representation counts. These settle the *statistical* behavior but cannot exclude a single exceptional prime, and they degrade precisely on the sparse square classes. A parity-type limitation also blocks sieves from deciding whether a given progression always carries a solution.

**Geometry of the cubic surface.** Clearing denominators gives $4abc = n(ab + bc + ca)$, a cubic surface whose positive integral points encode solubility. This viewpoint explains *why* quadratic residues govern the problem, but the relevant surfaces are not of a type where the Hasse principle is provable or the Brauer–Manin obstruction is computable uniformly over a family of primes.

## 4. Critical assessment

The dossier's central narrative is coherent and matches the consensus picture: everything reduces to six square residue classes modulo $840$, and the controlling obstruction is that finite identity lists fail on a positive-density residual by quadratic reciprocity and Dirichlet. This is a substantive, correct framing of why the problem is hard — the barrier is structural, not merely unaddressed. The four-approach taxonomy is standard and the attribution of landmark results (Mordell, Vaughan, Elsholtz–Tao) is consistent with the well-established literature.

Two cautions temper this. First, several quantitative claims — the precise exponent $(\log N)^{2/3}$ in Vaughan's bound, the $N \log^3 N$ order in the Elsholtz–Tao average, and the exact verification ceiling ($\sim 10^{17}$) — are reported from the dossier and should be checked against primary sources before being relied upon; the dossier itself flags many citations as unverified. Second, the conjecture's truth is a *belief* supported by heuristics and computation, not a theorem, and the document is appropriately careful to say so. The verification ceiling in particular is cited variously as $10^{14}$ and $10^{17}$ across the dossier files, an internal inconsistency a reviewer should resolve.

## 5. What a resolution would require / open directions

A proof must handle the six square classes modulo $840$ *uniformly over all primes in them*, without depending on a fixed Legendre-symbol condition — since any finite identity list leaves a positive-density residual. Plausible routes: (i) constructions whose validity rests on a *varying* divisor of $p \pm (\text{small})$ rather than a fixed modulus, perhaps via descent or Brauer–Manin analysis of the cubic-surface family; (ii) strengthening Elsholtz–Tao lower bounds for $f(p)$ to a pointwise guarantee $f(p) \ge 1$ for all large $p$ in the hard classes, currently out of reach because analytic methods average; (iii) new character- or exponential-sum estimates forcing solubility pointwise. A disproof would need a specific prime $p$ for which $4abc = p(ab + bc + ca)$ has no positive integral solution — which computation and heuristics make appear very unlikely. No route is near completion.

## 6. Selected references

1. L. J. Mordell, *Diophantine Equations* (1967) — textbook source for the modulo-$840$ reduction. [high-confidence]
2. R. C. Vaughan, "On a problem of Erdős and Straus" (1970) — exceptional-set bound $E(N) \ll N\exp(-c(\log N)^{2/3})$. [high-confidence]
3. R. K. Guy, *Unsolved Problems in Number Theory* (1994), problem D11. [high-confidence]
4. C. Elsholtz and T. Tao, "Counting the number of solutions to the Erdős–Straus equation on unit fractions" (2011), arXiv:1107.1010. [high-confidence]
5. L. A. Rosati, "Su un problema di Erdős e Straus sull'equazione $4/n = 1/x+1/y+1/z$" (1956). [needs-verification]
6. H. Yamamoto, "On a conjecture of Erdős and Straus" (1964). [needs-verification]
7. R. Obláth, "Sopra l'equazione $4/n = 1/x+1/y+1/z$" (1954). [needs-verification]
8. A. Schinzel and W. Sierpiński, work on unit fractions $a/n$ (1962). [needs-verification]
9. W. Sierpiński, "On the equation $\sum 1/x_i = a/n$ in distinct integers" (1962). [needs-verification]
10. W. A. Webb, "Rationals not expressible as a sum of three unit fractions" (1974) — density results. [needs-verification]
11. P. Erdős and R. L. Graham, *Old and New Problems and Results in Combinatorial Number Theory* (1999). [needs-verification]
12. A. Swett, computational verification of the Erdős–Straus conjecture (web tables, c. 2002). [needs-verification]
13. C. Elsholtz, "Egyptian fractions" survey chapter (2012). [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is accurate where it matters most. The reduction to primes, Mordell's six square residue classes modulo $840$, and the quadratic-reciprocity obstruction to finite identity lists are presented correctly and form a genuine, defensible account of why the problem resists proof. The four-approach taxonomy and the role of Vaughan and of Elsholtz–Tao as the analytic and structural landmarks are faithful to the field. The document is also commendably honest about the gulf between "almost all $n$" and "all $n$," and never overstates computation as proof.

My reservations are about sourcing and precision. (i) The dossier explicitly flags most of its citations as *needs-verification* or *ai-suggested*; only the Mordell textbook, Vaughan's paper, Guy's D11, and the Elsholtz–Tao preprint (arXiv:1107.1010) are high-confidence. The early Italian, Polish, and Japanese congruence-class papers (Obláth, Rosati, Yamamoto, Schinzel–Sierpiński) almost certainly exist in substance, but their exact titles, years, and venues need primary-source confirmation before citation. (ii) There is single-source reliance on Elsholtz–Tao for the modern structural claims and on the dossier's own summaries for the analytic constants; the exponent $(\log N)^{2/3}$ and the $N\log^3 N$ average order should be checked against the original papers. (iii) The single most important thing a human reviewer should verify is the **computational verification ceiling**, which the dossier reports inconsistently as $\sim 10^{14}$ in one file and $\sim 10^{17}$ in others — a concrete, checkable discrepancy that should be reconciled against Swett's tables and any extended-range computations.

None of these undermine the survey's core, but they keep it short of publication-ready. The claims are believable and well-aligned with the literature; they are not yet independently sourced.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._
### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._
### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This assessment is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and its citations — several of which carry explicit verification flags — require checking against primary sources before any scholarly reliance. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
