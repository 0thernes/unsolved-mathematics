# Attempts — Brocard's Problem

_Notable attempts, near-misses, retracted proofs._

Brocard's problem has the unusual profile of a famous open question with **no widely circulated false "proof"** and **no celebrated retraction** — its difficulty is recognized clearly enough that few have claimed to settle it, and the serious literature consists of partial results, generalizations, and computation rather than disputed announcements. The "near-misses" are therefore theorems that come tantalizingly close to the original case without covering it, plus computation that has steadily failed to find a fourth solution.

## Computational searches (the decisive negative evidence)

The most important body of work is computational. **Bruce C. Berndt and William F. Galway (2000)**, in *"On the Brocard–Ramanujan Diophantine equation $n!+1=m^2$"* (*The Ramanujan Journal*), searched all $n \le 10^9$ and found no solution beyond $n = 4, 5, 7$. This remains the canonical citation for the absence of further Brown numbers in a verified range. Subsequent searches — including work associated with **Daniel Gabric** and others, and various distributed computations — have extended the verified range well beyond $10^9$ (commonly quoted figures push $n$ into the $10^9$–$10^{12}$ region depending on the method and sieve), again with no new solution. These are not proofs of finiteness; they only certify that any fourth Brown number, if it exists, is enormous. The searches exploit congruence sieves: for a solution one needs $n!+1$ to be a quadratic residue modulo many primes simultaneously, which becomes increasingly improbable and is cheaply testable.

## Dąbrowski's near-miss (1996)

**Andrzej Dąbrowski's** theorem that $n! + A = m^2$ has only finitely many solutions for every fixed **non-square** $A$ is the closest structural result. It is a genuine theorem covering an infinite family of constants, yet it fails for $A = 1$ for a precise reason: when $A$ is a perfect square, $m^2 - A$ factors over $\mathbb{Z}$, and the growth/valuation contradiction Dąbrowski derives disappears. This is the canonical "so close" result — it brackets Brocard's problem on both sides without touching it.

## The abc-conditional resolution

Marius **Overholt** observed that a weak form of the **abc conjecture** implies Brocard's problem has only finitely many solutions (and the same for $n!+1 = m^k$ and $n!+A=m^2$). This is sometimes informally described as "the problem is solved modulo abc." It is a real and clean implication, but it is **conditional** on a conjecture that is itself unproven and at least as deep; it should not be read as a solution. (Note neutrally: Shinichi Mochizuki's claimed proof of abc via inter-universal Teichmüller theory, published in *PRIMS* in 2021, is **not accepted** by the broader mathematical community following the 2018 Scholze–Stix objection that a key inequality is unjustified; consequently the abc-conditional resolution of Brocard's problem cannot currently be promoted to unconditional.)

## Generalizations and variants

Several authors have attacked relatives in hopes of techniques transferring back:
- **$n! + 1 = m^k$** (perfect powers, not just squares): partial finiteness results exist, again often conditional or restricted.
- **Products of consecutive factorials equal to a factorial or a square**, and the **Erdős–Obláth** equation $n! + m! = k!$ and $n! \pm m! = \square$: these have been studied with elementary and computational methods, yielding finiteness in restricted regimes.
- **$x^2 - n! = A$ for fixed $A$**: the Dąbrowski framework applies for non-square $A$.

None of these transfers has cracked $A=1$.

## No accepted unconditional finiteness, no disputed claim of one

It bears emphasis for an honest reference: as of the present, there is **no accepted unconditional proof** that the number of Brown numbers is finite, and there is **no prominent claimed proof under dispute**. The problem's reputation as "easy to state, brutally hard to prove" rests on the absence of *any* purchase point for unconditional methods, not on a history of failed announcements. The live evidence is overwhelming numerically and persuasive heuristically, but the theorem itself is unproven.
