---
title: "Meta-Analysis: The Hadamard Matrix Conjecture"
slug: hadamard-matrix-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-sourced survey of an open constructive problem; the core claims are sound, but several citations carry verification flags and the asymptotic-bound statements need primary-source checking."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Hadamard Matrix Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Hadamard matrix conjecture asserts that an $n \times n$ matrix with entries in $\{+1,-1\}$ and pairwise-orthogonal rows — equivalently $HH^{\top} = nI_n$ — exists for every order $n = 4k$. Divisibility by $4$ (for $n > 2$) is the only known necessary condition, proven by Hadamard in 1893 as the equality case of his determinant bound; the conjecture is that it is also sufficient. This meta-analysis surveys the constructive landscape: Sylvester/Kronecker doubling, the finite-field Paley families, Williamson's circulant array method and its plug-in generalizations, cocyclic and difference-set machinery, asymptotic-existence theorems (Turyn, Seberry/Wallis, Craigen, de Launey–Gordon), and SAT/algebraic search. The problem is unusual: it is attacked almost entirely by construction, progress is bookkept as a shrinking list of open orders, and there are no impossibility results beyond $4 \mid n$. The smallest undecided order is $668 = 4 \cdot 167$. We assess why every known framework covers only a structured, incomplete set of orders, what a universal resolution would require, and which claims in the dossier most need primary-source verification. The community regards the conjecture as "morally true" but genuinely hard; expected progress is incremental rather than a single decisive theorem.

## 1. Statement and significance

A **Hadamard matrix** of order $n$ is a $\{\pm1\}$ matrix $H$ with $HH^{\top} = nI_n$. Such matrices attain Hadamard's determinant bound $|\det| \le n^{n/2}$ for matrices with entries of modulus at most $1$, with equality forcing $\pm1$ entries and orthogonal rows, hence $n \in \{1, 2\} \cup 4\mathbb{Z}_{>0}$. The conjecture is the converse: a Hadamard matrix exists for **every** order $4k$.

The significance is broad because the object is multiply reformulable. Existence at order $4k$ is equivalent to a symmetric $2$-$(4k-1, 2k-1, k-1)$ Hadamard design, to certain regular two-graphs and conference structures, and (via codeword substitution) to binary codes meeting the Plotkin bound. These dictionaries route the problem through design theory, finite geometry, group theory (difference sets, group-developed and cocyclic matrices), and algebraic number theory, and Hadamard matrices recur in coding, signal processing (pulse compression, surface-wave encodings), and statistical design. The problem is thus a load-bearing node in combinatorics rather than an isolated curiosity.

## 2. State of the art

The conjecture is **open (active progress)**. Known unconditional results combine several infinite families: Sylvester doubling settles all $2^m$; the Paley constructions settle orders $q+1$ ($q \equiv 3 \bmod 4$) and $2(q+1)$ ($q \equiv 1 \bmod 4$) for prime powers $q$; Williamson, Goethals–Seidel, and base-sequence methods supply most sporadic orders; cocyclic constructions unify and extend these. Together these settle a set of orders of positive density and every multiple of $4$ below the current frontier.

The **smallest open order is $668 = 4 \cdot 167$**. The previous frontier, order $428$, was resolved by Kharaghani and Tayfeh-Rezaie (announced 2004, published 2005). Order $668$ lies outside direct Paley reach and has resisted Williamson search, base-sequence methods, and SAT/algebraic search.

The strongest **general** theorem is asymptotic: for every odd $m$, a Hadamard matrix of order $2^t m$ exists for all $t \ge 2\log_2(m-3)$ (attributed in the dossier to Seberry/Wallis, 1985), with the exponent later lowered by Craigen and by de Launey–Gordon. Under number-theoretic hypotheses on primes in short intervals, the exponent improves further. The conjectural target is $t = 2$ for all $m$; closing the gap between "for large $t$" and "$t = 2$" is the unsolved core.

## 3. Principal approaches and barriers

- **Sylvester/Kronecker doubling.** $H_a \otimes H_b$ is Hadamard of order $ab$. *Barrier:* multiplicativity only propagates known orders by powers of $2$; it never produces a *first* construction at a new odd multiple.
- **Paley (finite-field/quadratic-residue).** Builds matrices near prime powers via the Jacobsthal/Legendre construction. *Barrier:* reachable orders cluster around prime powers; infinitely many $4k$ (e.g. $668$) lie outside Paley-plus-doubling reach.
- **Williamson and plug-in arrays.** Reduces order $4n$ to four symmetric circulants with $A^2+B^2+C^2+D^2 = 4nI$; Baumert–Hall and Goethals–Seidel arrays generalize to base sequences. *Barrier:* Williamson-type solutions provably fail at some orders (exhaustive search ruled them out at order $140 = 4\cdot35$), so the method is not universal.
- **Difference sets, group development, cocyclic matrices.** The cocyclic Hadamard conjecture (de Launey–Horadam) posits a cocyclic Hadamard matrix at every $4k$, unifying Sylvester, Paley, and Williamson via group cohomology. *Barrier:* it is at least as hard, and the cohomological search space grows rapidly with $k$.
- **Asymptotic existence.** The strongest general theorems (Turyn; Seberry/Wallis; Craigen; de Launey–Gordon). *Barrier:* none reaches the $t = 2$ frontier required for *all* $m$.
- **Computational/SAT/algebraic search.** Settles individual orders (cleared $428$). *Barrier:* exponential search space; no general theorem.

The unifying obstruction is not an impossibility result. There are **no known obstructions beyond $4 \mid n$**; counting heuristics suggest the number of inequivalent matrices of order $4k$ grows super-exponentially, so non-existence at any large order is intuitively implausible. The genuine barrier is constructive — each framework covers a structured but incomplete residue pattern, and no single framework is known to cover all residue classes simultaneously, an analogue of the "parity barrier" in sieve theory.

## 4. Critical assessment

The dossier's central factual claims are consistent with the mainstream picture and internally coherent: the $4 \mid n$ necessity, the dual Hadamard/Paley origin, the construction taxonomy, and the $428 \to 668$ frontier shift. The framing of the problem as constructive rather than obstruction-bound is correct and is the most important conceptual point: this is why no counterexample is expected and why "morally true" is the community's honest stance.

Three points warrant caution. First, the asymptotic exponent is stated as $t \ge 2\log_2(m-3)$ attributed to Seberry/Wallis 1985; the exact form of the bound, its attribution, and the precise improvements credited to Craigen and de Launey–Gordon should be checked against primary sources, since asymptotic-existence statements in this literature vary in their constants and hypotheses across papers. Second, the claim that order $668$ "lies outside Paley reach" is correct as stated but rests on the specific arithmetic of $167$ and $168$; a human reviewer should confirm the precise reason rather than the heuristic given. Third, the super-exponential growth heuristic for the count of inequivalent matrices is widely repeated but is a heuristic, not a theorem, and should be presented as such.

## 5. What a resolution would require / open directions

A proof must produce, or prove existence of, a $\{\pm1\}$ orthogonal-row matrix at **every** order $4k$ — including the infinitely many $k$ where $4k$ is far from any prime power and doubling cannot help. Three plausible routes:

1. **A universal construction** covering all residue classes, plausibly via cocyclic/relative-difference-set machinery subsuming Paley and Williamson simultaneously.
2. **Lowering the asymptotic exponent to $t = 2$** outright, converting Seberry-type theorems into "for all $m$" via sharper number theory (primes in short intervals) plus combinatorial amplification.
3. **A probabilistic/entropy-counting existence proof** establishing non-emptiness without explicit construction — no such method is currently known to handle orthogonality constraints this rigid.

The realistic community expectation is incremental: clearing $668$ and successive open orders, and shrinking the asymptotic exponent, rather than one decisive theorem.

## 6. Selected references

1. J. J. Sylvester (1867), *Thoughts on inverse orthogonal matrices… tessellated pavements in two or more colours*. Foundational. [high-confidence]
2. J. Hadamard (1893), *Résolution d'une question relative aux déterminants*. Foundational. [high-confidence]
3. R. E. A. C. Paley (1933), *On orthogonal matrices*, DOI 10.1002/sapm193312311. Foundational. [high-confidence]
4. J. Williamson (1944), *Hadamard's determinant theorem and the sum of four squares*, DOI 10.1215/S0012-7094-44-01108-7. Breakthrough. [high-confidence]
5. L. D. Baumert, S. W. Golomb, M. Hall Jr. (1962), *Discovery of an Hadamard matrix of order 92*, DOI 10.1090/S0002-9904-1962-10761-7. Breakthrough. [high-confidence]
6. R. J. Turyn (1972/74), *Hadamard matrices, Baumert–Hall units, four-symbol sequences, pulse compression, and surface wave encodings*, DOI 10.1016/0097-3165(74)90079-8. Breakthrough. [needs-verification]
7. W. D. Wallis, A. P. Street, J. S. Wallis (1972), *Combinatorics: Room Squares, Sum-Free Sets, Hadamard Matrices* (LNM 292), DOI 10.1007/BFb0069907. Foundational. [needs-verification]
8. J. Seberry (Wallis) (1985), *On the asymptotic existence of Hadamard matrices*. Breakthrough. [needs-verification]
9. W. de Launey, K. J. Horadam (1995), *Cocyclic Hadamard matrices and Hadamard groups are equivalent*. Breakthrough. [needs-verification]
10. R. Craigen (2001), *A note on the existence of Hadamard matrices (asymptotic improvements)*. Modern. [needs-verification]
11. H. Kharaghani, B. Tayfeh-Rezaie (2005), *A Hadamard matrix of order 428*, DOI 10.1002/jcd.20043. Breakthrough. [high-confidence]
12. K. J. Horadam (2006), *Hadamard Matrices and Their Applications*, DOI 10.1515/9781400842902. Survey/monograph. [needs-verification]
13. W. de Launey, D. M. Gordon (2009), *On the asymptotic existence of cocyclic Hadamard matrices / partial difference families*. Modern. [needs-verification]
14. R. Craigen, H. Kharaghani (2011), *Hadamard matrices: a survey of the existence question and constructions*. Survey. [needs-verification]
15. (Horadam school, 2013), *A survey of cocyclic Hadamard matrices and the cocyclic conjecture*. Survey. [ai-suggested]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is accurate where it matters most and admirably honest about the problem's true character: this is a constructive existence question with no impossibility results beyond $4 \mid n$, attacked by accumulating constructions rather than by grand proofs. The taxonomy of methods, the explanation of why each falls short (multiplicativity only propagates upward, Paley clusters near prime powers, Williamson provably fails at order $140$), and the identification of the asymptotic exponent gap as the unsolved core are all sound and well-motivated. The "parity-barrier" analogy is apt and not overstated.

My principal reservations concern sourcing. The reference list carries explicit verification flags, and several load-bearing items — Seberry's 1985 asymptotic theorem, de Launey–Horadam's cocyclic equivalence, the Craigen and de Launey–Gordon improvements, the Wallis–Street–Wallis LNM 292, and Horadam's monograph — are marked **needs-verification** for exact title, year, journal, or identifier. These should be confirmed against a registry before formal citation. Only the Sylvester, Hadamard, Paley, Williamson, Baumert–Golomb–Hall, and Kharaghani–Tayfeh-Rezaie entries are flagged high-confidence.

Two substantive cautions: (i) the asymptotic bound $t \ge 2\log_2(m-3)$ and its attribution rest on a single line in the dossier and on a literature where constants and hypotheses vary between papers — this is the most important thing a human reviewer should verify, since it anchors the "state of the art" section; (ii) the super-exponential growth count and the "$668$ is outside Paley reach" claim are correct as heuristics but should not be presented with more certainty than their underlying arguments support. There is no single-source overstatement that rises to a factual error, but the document leans on community survey tables (Seberry; Craigen–Kharaghani) whose specific claims I could not independently confirm here.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This assessment is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and its citations — especially those flagged needs-verification or ai-suggested — require primary-source checking before any formal use. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
