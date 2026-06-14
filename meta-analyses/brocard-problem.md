---
title: "Meta-Analysis: Brocard's Problem"
slug: brocard-problem
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-calibrated survey of a genuinely open Diophantine problem whose only honesty risk is the thin, partly unverified citation base it must lean on."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Brocard's Problem

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Brocard's problem asks whether the Diophantine equation $n! + 1 = m^2$ has only finitely many solutions in positive integers $n$. The integers $n$ for which a solution exists are the **Brown numbers**; only three are known, $n \in \{4, 5, 7\}$, giving $25 = 5^2$, $121 = 11^2$, and $5041 = 71^2$. Posed by Henri Brocard in 1876 and independently by Ramanujan in 1913 (Question 469), the equation is conjectured to have no further solutions, but neither finiteness nor the exact list is proved unconditionally. This meta-analysis surveys the four principal lines of attack — elementary/congruence methods, the abc-conditional finiteness argument, the Dąbrowski generalization program, and large-scale computation — and assesses the structural obstruction common to all: a factorial carries vast, fully controlled small-prime factorization but no exploitable algebraic structure as a function of $n$. The single strongest conditional result, that a weak form of the abc conjecture forces finiteness, cannot be promoted to a theorem because abc itself is open. We catalog what a genuine resolution would require, flag the thinness and partial unverifiability of the primary literature, and conclude that the problem is hard rather than merely unattacked.

## 1. Statement and significance

The problem is to determine all positive integers $n$ with $n! + 1 = m^2$ for some integer $m$ — equivalently, to decide whether the solution set is finite. The known solutions $n = 4, 5, 7$ have been the complete list for nearly 150 years. Its significance is twofold. First, it is a canonical "easy to state, brutally hard to prove" benchmark in Diophantine analysis: the statement requires no machinery, yet resists every unconditional method. Second, it sits at the intersection of two themes that almost never interact controllably — the multiplicative irregularity of $n!$ and the additive rigidity of perfect squares. A density heuristic models $n! + 1$ as a random integer near $m^2$, giving a square-probability of order $(n!)^{-1/2}$; the sum over $n$ converges with extreme speed, so the *expected* number of solutions beyond a small bound is essentially zero. This explains the universal belief that $\{4,5,7\}$ is complete, while underscoring that the belief rests on heuristics, not proof.

## 2. State of the art

**Unconditional.** The three solutions are verified complete to very large bounds: Berndt and Galway (2000) found no solution for $n \le 10^9$, and later sieve-based searches push the verified range into the $10^9$–$10^{12}$ region with no new Brown number. The strongest structural theorem is Dąbrowski (1996): for every fixed **non-square** integer $A$, the equation $n! + A = m^2$ has only finitely many solutions. This brackets Brocard's problem on all sides except the one case that matters — $A = 1$ — because when $A$ is a perfect square the factorization $m^2 - A = (m-\sqrt A)(m+\sqrt A)$ over $\mathbb{Z}$ removes the growth/valuation obstruction the proof exploits.

**Conditional.** Overholt observed that a weak form of the abc conjecture implies Brocard finiteness. Applied to $1 + n! = m^2$, abc bounds $m^2$ via the radical $\mathrm{rad}(n! \cdot m)$; since $\mathrm{rad}(n!) = \prod_{p \le n} p = e^{(1+o(1))n}$ is exponentially smaller than $n! = e^{(1+o(1))n\log n}$, abc forces $n$ bounded. The same argument covers $n!+1=m^k$ and $n!+A=m^2$. This cannot become unconditional: abc is open, and Mochizuki's claimed proof (PRIMS, 2021) is not accepted by the broader community following the Scholze–Stix (2018) objection.

## 3. Principal approaches and barriers

**Elementary / congruence.** Writing $n! = (m-1)(m+1)$ with $\gcd(m-1, m+1) \in \{1,2\}$ and using Legendre's formula for $v_p(n!)$ yields necessary conditions and powers the computational sieves, but cannot bound $n$. Barrier: $n!$ is "too smooth" — every small prime appears to high power, so square/congruence obstructions are automatically satisfiable and none forces $n!+1$ off the squares for large $n$.

**abc / Diophantine transfer.** The most successful conditional route, as above. Barrier: abc is unproved and at least as deep; the implication is ineffective absent an explicit abc constant.

**Generalization (Dąbrowski).** Solves all non-square $A$; the method dies exactly at $A = 1$. Barrier: the square case loses the factorization obstruction.

**Effective transcendence.** One hopes to import Baker's linear-forms-in-logarithms bounds, which solve fixed-base equations like Pillai's $a^x - b^y = c$. Barrier: $n!$ is neither a fixed exponential $a^n$ nor a value of a fixed polynomial/binary form — its "base" changes with $n$ — so Baker's machinery does not engage and no effective bound on Brown numbers exists.

The recurring wall is identical across approaches: a factorial supplies a huge, totally controlled set of small prime factors and no usable structure as a function of $n$.

## 4. Critical assessment

The dossier's framing is accurate and admirably disciplined: it states clearly that no unconditional finiteness proof exists, that the abc route is conditional on an open (and presently unaccepted-as-proved) conjecture, and that computation certifies only the absence of *small* further solutions. The asymmetry at the heart of the problem — Dąbrowski settling every non-square $A$ while $A=1$ remains untouched — is correctly identified as the precise technical reason the original case survives. The probabilistic heuristic is appropriately labeled inadmissible as evidence of finiteness.

Two cautions temper the survey. First, the heuristic argument is so persuasive that it risks being mistaken for near-proof; it is not, and cannot distinguish "finitely many" from "no more than three." Second, the load on the abc conjecture is heavy: the single clean finiteness implication routes entirely through a result the community does not currently hold. An honest reading is that Brocard's problem is, today, no closer to unconditional resolution than it was when Dąbrowski's theorem appeared in 1996.

## 5. What a resolution would require / open directions

A complete answer must either (1) prove abc — or just the weak quantitative form sufficient here — yielding finiteness immediately but ineffectively; or (2) supply a genuinely new effective handle on $n!$, some descent or reduction to an object with fixed algebraic structure on which Baker-type bounds bite, to bound $n$ directly. Proving the stronger claim that $\{4,5,7\}$ is the *exact* solution set additionally demands an explicit, computable bound on $n$ small enough to be closed by the existing verified search range. Plausible incremental directions: extending Dąbrowski-type theorems toward the square-$A$ boundary; sharper effective methods for factorial-shaped equations; and continued computation, which keeps the conjecture empirically airtight without proving it. No credible near-term route to an unconditional proof is on the horizon.

## 6. Selected references

1. Henri Brocard, *Question (sur $n!+1=\square$)*, Nouvelle correspondance mathématique 2 (1876). [high-confidence]
2. Henri Brocard, restatement of the factorial-square question, Mathesis 5 (1885). [high-confidence]
3. Srinivasa Ramanujan, Question 469, Journal of the Indian Mathematical Society (1913). [high-confidence]
4. G. H. Hardy, P. V. Seshu Aiyar, B. M. Wilson (eds.), *Collected Papers of Srinivasa Ramanujan* (1927). [high-confidence]
5. Richard Obláth, *Über die Diophantische Gleichung $n!+1=m^k$ und Verwandtes* (1935). [needs-verification]
6. Daniel Shanks, *Solved and Unsolved Problems in Number Theory* (1976). [high-confidence]
7. L. E. Dickson, *History of the Theory of Numbers, Vol. II* (reprint, Diophantine analysis) (1981). [high-confidence]
8. Richard K. Guy, *Unsolved Problems in Number Theory*, 2nd ed., entry on $n!+1=\square$ (1993). [high-confidence]
9. Andrzej Dąbrowski, *On the Diophantine equation $x! + A = y^2$* (1996). [high-confidence]
10. Bruce C. Berndt, William F. Galway, *On the Brocard–Ramanujan Diophantine equation $n!+1=m^2$*, The Ramanujan Journal (2000). [high-confidence]
11. Marius Overholt (attrib.), notes on abc and its Diophantine consequences, Brocard among them (2002). [needs-verification]
12. Richard K. Guy, *Unsolved Problems in Number Theory*, 3rd ed. (2004). [high-confidence]
13. D. Gabric (attrib.) and others, computational extension of the search for Brown numbers (2014). [needs-verification]
14. Shinichi Mochizuki, *Inter-universal Teichmüller theory IV* (claimed abc proof; disputed), PRIMS, DOI 10.4171/PRIMS/57-1-1 (2021). [needs-verification]
15. Peter Scholze, Jakob Stix, *Why abc is still a conjecture* (Scholze–Stix objection) (2018). [high-confidence]

## AI Review Panel

### Claude (Anthropic) — in-house review

This is a careful and honest survey. Its principal strength is calibration: it never confuses the abc-conditional finiteness result with a theorem, it correctly isolates the $A=1$ square case as the technical reason Dąbrowski's result stops short, and it resists the temptation to let the (genuinely overwhelming) heuristic and computational evidence masquerade as proof. The taxonomy of approaches and the single shared obstruction — a factorial's controlled smoothness coupled with its lack of structure as a function of $n$ — is the right organizing idea and is presented without overstatement.

Three things a human reviewer must check before relying on this document. (i) The citation base is thin and partly unverified. Several references — notably the Obláth 1935 title and year, the Overholt attribution and the form of his statement, and the Gabric-attributed computational extension — carry needs-verification flags in the source dossier; the Overholt result in particular should be traced to a primary source rather than to survey hearsay, since it is load-bearing for the entire "conditional resolution" narrative. (ii) There is real single-source reliance: the unconditional empirical backbone rests almost entirely on Berndt–Galway (2000), and quoted extensions of the search range into the $10^9$–$10^{12}$ region are stated loosely ("commonly quoted figures") and should be pinned to specific, citable computations or presented as approximate. (iii) The one precise claim most worth independent verification is Dąbrowski's theorem and its exact hypothesis — that finiteness holds for every fixed non-square $A$ — together with the precise reason squareness of $A$ breaks the argument; this is the structural keystone of the whole assessment and should be confirmed against the 1996 paper itself.

No overclaiming was detected: the document makes no assertion that Brocard's problem is resolved, and its conditional statements are properly hedged. The needed revisions are citation-level, not substantive.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This assessment is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and every non-high-confidence citation, numerical search bound, and attributed result above requires checking against primary sources before being relied upon. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
