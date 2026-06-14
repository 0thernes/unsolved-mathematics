---
title: "Meta-Analysis: Lehmer's Totient Problem"
slug: lehmer-totient-problem
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-framed survey of an open problem whose partial results are real but whose secondary citations carry verification flags and require primary-source checking."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Lehmer's Totient Problem

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Lehmer's totient problem (1932) asks whether any composite integer $n$ satisfies $\varphi(n) \mid n-1$, where $\varphi$ is Euler's totient. Every prime $p$ trivially satisfies $\varphi(p) = p-1 \mid p-1$; the open question is whether this divisibility characterizes the primes, i.e. whether no composite solution — a "Lehmer number" — exists. The expected answer is that none does, but this remains unproved after nearly a century. This meta-analysis surveys the state of the art: the structural constraints any solution must obey (odd, squarefree, $\omega(n) \ge 15$, $n > 10^{30}$, vastly larger if $3 \mid n$); the placement of Lehmer numbers inside the Carmichael hierarchy ($\text{primes} \subset \text{Lehmer} \subset \text{Carmichael}$); and the counting bound $L(x) \le x^{1/2}/(\log x)^{1/2+o(1)}$. It assesses the two principal attack lines — incremental lower bounds on $\omega(n)$ and sieve-theoretic density bounds — and the two barriers that block each from reaching a proof: the inability to reach $\omega(n) = \infty$ and the parity (square-root) barrier. It closes with what a resolution would require. No new mathematics is claimed.

## 1. Statement and significance

The problem asks: does there exist a composite $n$ with $\varphi(n) \mid n-1$? Equivalently, writing $k = (n-1)/\varphi(n)$, is there an integer $k \ge 2$ and a composite $n$ with $n - 1 = k\,\varphi(n)$? For primes $k = 1$ always works. A composite solution would be, in effect, a number "totient-indistinguishable" from a prime — a near-counterexample to the would-be primality criterion "$\varphi(n) = n-1 \iff n$ prime." The significance is twofold: the relation would furnish a primality characterization if no composite met it, and the problem sits at a confluence of multiplicative number theory, the theory of Carmichael numbers, and the limits of sieve methods, making it a recurring benchmark rather than an isolated curiosity.

## 2. State of the art

The status is **open**: no composite solution is known, and none has been proven impossible. The unconditional constraints on any solution $n$ are:

- $n$ is **odd** and **squarefree** (Lehmer, 1932);
- $\omega(n) \ge 15$ distinct prime factors, the floor having been raised from Lehmer's $7$ through Cohen–Hagis/Kishore's $14$;
- $n > 10^{30}$ in general, with far larger figures under side conditions — if $3 \mid n$ then $\omega(n) \ge 212$ and $n > 5.5 \times 10^{570}$ (Lieuwens, 1977);
- $n$ is a **Carmichael number**, since $\varphi(n) \mid n-1$ implies the weaker $\lambda(n) \mid n-1$ (Korselt's criterion), where $\lambda$ is the Carmichael function and $\lambda(n) \mid \varphi(n)$.

On the density side, the counting function $L(x) = \#\{n \le x : n \text{ composite},\ \varphi(n) \mid n-1\}$ satisfies $L(x) \le x^{1/2}/(\log x)^{1/2+o(1)}$ (Luca–Pomerance, 2011, sharpening Pomerance's earlier $x^{1/2+o(1)}$). No Carmichael number tabulated past $10^{18}$ satisfies the stronger totient condition.

## 3. Principal approaches and barriers

**Lower bounds on $\omega(n)$.** Expanding $n - 1 = k\prod(p_i - 1)$ against $n = \prod p_i$ forces each prime to be large and forces the product $\prod(1 - 1/p_i)$ to approximate $1/k$ tightly, driving $\omega(n)$ upward. *Barrier:* the constraints weaken only logarithmically in $k$; each increment of the floor demands a fresh large computation, and the method has no mechanism to reach $\omega(n) = \infty$, so it can never close the problem.

**Sieve / counting bounds.** Rather than rule out individual $n$, one bounds $L(x)$ using estimates for sparse integers with many prime factors. *Barrier:* the **parity (square-root) barrier** — sieves cannot distinguish an even from an odd number of prime factors and generically lose a factor of $\sqrt{x}$. A bound of order $x^{1/2}$ establishes extreme sparsity but is structurally incapable of reaching $L(x) = 0$.

**Restriction to structured families.** Within Fibonacci/Lucas sequences, repunits, and shifted primes, recurrence structure supplies congruences the general problem lacks; Banks, Luca and collaborators (2007–2008) proved non-existence or finiteness in several such sets. *Barrier:* these are measure-zero subsets with no route to the general $n$.

**Conditional / heuristic and computational lines.** Quasi-independence heuristics predict the expected count is zero; exhaustive search certifies non-existence in reachable ranges. *Barriers:* the heuristics rest on unproved hypotheses, and search can only ever clear a finite, astronomically small initial segment.

## 4. Critical assessment

The dossier's framing is sound and matches the consensus reflected in standard references (Guy, *Unsolved Problems in Number Theory*, problem B37; Sándor–Crstici, *Handbook of Number Theory*). The canonical core — Lehmer (1932); the lower-bound line of Lieuwens, Cohen–Hagis, and Kishore; the counting bounds of Pomerance and Luca–Pomerance; and the Carmichael context of Alford–Granville–Pomerance — is real and well-attested, and the two-barrier diagnosis (no path to $\omega(n) = \infty$; parity barrier on $L(x)$) is the honest, standard account of why the problem resists.

Two cautions. First, several numerical figures circulate with slightly different attributions across the secondary literature; the precise current floor (here stated as $\omega(n) \ge 15$, $n > 10^{30}$) and the exact form of the Luca–Pomerance exponent should be checked against the primary papers rather than against surveys. Second, the dossier's own papers table flags many entries as `needs-verification` or `ai-suggested` with identifiers withheld; this honest practice should be preserved, and no secondary citation should be promoted to a load-bearing claim without source-checking.

## 5. What a resolution would require / open directions

A proof of non-existence must rule out solutions for **all** $\omega(n)$ simultaneously — precisely what neither principal method can do. Two plausible routes: (i) a genuinely new algebraic obstruction that derives a contradiction from $\varphi(n) \mid n-1$ for squarefree $n$ with many prime factors, *independent of* $\omega(n)$; or (ii) advances in the distribution of primes in residue classes, stronger than currently available GRH-type inputs, that defeat the parity barrier for this specific multiplicative condition. A *counterexample*, conversely, would require exhibiting or proving the existence of an astronomically large squarefree product of $\ge 15$ primes meeting the divisibility — for which no construction and no existence heuristic is known. The sibling technology shared with odd perfect numbers ("$\omega(n)$ floor plus enormous size bound") suggests progress will remain incremental absent a structural breakthrough.

## 6. Selected references

1. D. H. Lehmer, *On Euler's totient function*, Bull. Amer. Math. Soc. 38 (1932). [high-confidence]
2. E. Lieuwens, *Do there exist composite numbers $m$ for which $\varphi(m) \mid m-1$?* (1977). [needs-verification]
3. C. Pomerance, *On composite $n$ for which $\varphi(n) \mid n-1$* (counting bound, 1977). [needs-verification]
4. G. L. Cohen and P. Hagis, *On the number of prime factors of $n$ if $\varphi(n) \mid n-1$* (1980). [needs-verification]
5. M. Kishore, *On the number of prime factors of $n$ for which $\varphi(n) \mid n-1$* (1980). [needs-verification]
6. C. Pomerance, *On composite $n$ for which $\varphi(n)$ divides $n-1$, II* (1988). [needs-verification]
7. W. R. Alford, A. Granville, C. Pomerance, *There are infinitely many Carmichael numbers*, Ann. of Math. (1994), 10.2307/2118576. [high-confidence]
8. R. K. Guy, *Unsolved Problems in Number Theory* (3rd ed.), problem B37 (2004). [high-confidence]
9. J. Sándor and B. Crstici, *Handbook of Number Theory I* (totient sections) (2004). [high-confidence]
10. F. Luca, *On the Lehmer problem restricted to Fibonacci and Lucas numbers* (2007). [needs-verification]
11. W. Banks and F. Luca, *Composite integers $n$ with $\varphi(n) \mid n-1$ in special sequences* (2007). [needs-verification]
12. W. Banks, A. Güloğlu, C. W. Nevans, *On numbers $n$ dividing the $n$th term of a linear recurrence and totient conditions* (2008). [needs-verification]
13. F. Luca and C. Pomerance, *On composite integers $n$ for which $\varphi(n) \mid n-1$* (2011). [needs-verification]
14. R. Pinch, *The Carmichael numbers up to $10^{18}$ and the Lehmer condition* (computational check) (2013). [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is faithful to its sources and avoids the failure mode such documents most invite: it never overstates the partial results into a near-proof. The Carmichael nesting is the right organizing idea, the two-barrier account (logarithmic weakening of the $\omega(n)$ floor; the parity barrier on $L(x)$) is the genuine mathematical reason the problem is hard, and the constraints quoted are consistent across the history, status, and attempts files. The prose correctly distinguishes what is unconditional from what is heuristic or family-restricted.

My principal reservation concerns citations. The dossier's own papers table flags a majority of entries as `needs-verification` or `ai-suggested` and deliberately withholds DOIs/arXiv ids rather than fabricate them — commendable, but it means almost none of the secondary references here is independently confirmed. A human reviewer should treat every reference except Lehmer (1932), Alford–Granville–Pomerance (1994, the one asserted DOI), Guy B37, and Sándor–Crstici as provisional until checked against the primary literature. I would also flag mild single-source reliance: the specific numbers $\omega(n) \ge 15$ and $n > 10^{30}$, and the exact exponent in the Luca–Pomerance bound, are quoted from the dossier without an external cross-check, and different surveys state slightly different floors.

The single most important thing a human reviewer should verify: that the **current unconditional lower bound on $\omega(n)$ and on $n$** stated here ($\ge 15$, $> 10^{30}$) matches the strongest published result, since this figure is the document's most concrete factual claim and is exactly the sort of number that drifts in secondary retellings. Subject to that check and the citation caveats, the document is an accurate, appropriately hedged survey.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This assessment is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and its citations — most of which carry `needs-verification` or `ai-suggested` flags — require checking against primary sources before any are relied upon. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
