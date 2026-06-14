# Status & Frontier — Carmichael's Totient Conjecture

_Where the problem stands and what a resolution would require._

**Status: open.** The conjecture — that the totient multiplicity $A(n)=\#\varphi^{-1}(n)$ is never equal to $1$, i.e. no value of $\varphi$ is attained exactly once — has been **unresolved since 1907** and has neither a proof nor a counterexample. It is widely believed **true**.

## What is known (unconditional)

- **Enormous lower bound on any counterexample.** Successive computations have certified that the least counterexample, if it exists, exceeds roughly $10^{10^{10}}$ (Schlafly–Wagon 1994 to $\sim 10^{10^{7}}$; Ford 1998 and subsequent refinements beyond $10^{10^{10}}$). These rest on **Klee's (1947)** finite criterion for a minimal counterexample.
- **Strong structural constraints (Pomerance 1974).** A counterexample $m$ must satisfy $p^2 \mid m$ for every prime $p$ with $(p-1)\mid \varphi(m)$, forcing $m$ to be extraordinarily square-rich.
- **The companion problem is solved.** **Ford (1998)** proved Sierpiński's conjecture: every integer $k\geq 2$ is a multiplicity $A(n)$. Thus $k=1$ — the Carmichael case — is the **only** multiplicity whose realizability is undecided.
- **Distribution of totients is understood** (Ford): precise asymptotics for $V(x)=\#\{\varphi(m)\le x\}$ and for typical fiber sizes.

## What is known (conditional / heuristic)

- Heuristics strongly favor the conjecture: a sporadic value would have to evade essentially every sibling construction at once, an event of effectively zero probability under standard models of $\varphi$-fibers.
- Pomerance's constraint ties a counterexample to an implausible configuration of primes $p$ with $p-1$ smooth; making "implausible" into "impossible" would settle the question.

## What a full resolution requires

A proof must convert **average/structural control** of $\varphi$-fibers into a **uniform worst-case** statement excluding multiplicity $1$ for every $n$, however large. Concretely, it would need an analytic input showing the simultaneous prime conditions in Pomerance's theorem cannot all hold — a statement about the joint distribution of shifted primes that is currently beyond reach. A counterexample, conversely, would be a single explicitly square-structured integer larger than any tested bound; none is known, and the structural constraints make one seem unlikely.

## Plausible routes

1. **Shifted-prime analysis** — control of primes $p$ with $p-1$ supported on prescribed prime sets, extending Pomerance's program, is the most promising avenue.
2. **Sieve / large-deviation refinements** of Ford's totient machinery to reach the $k=1$ tail the current methods cannot.
3. **Continued computation** to raise the bound — useful as evidence and for ruling out small structured candidates, but not expected to prove the conjecture.

## Related problems

- [Lehmer's Totient Problem](../lehmer-totient-problem/) — whether $\varphi(n)\mid n-1$ forces $n$ prime; the other great open question about $\varphi$.
- [Odd Perfect Numbers](../odd-perfect-numbers/) — a kindred "structured-counterexample-or-none" multiplicative problem.
- [Goldbach's Conjecture](../goldbach-conjecture/) — additive prime structure, analytic-number-theory neighbor.
- [Twin Prime Conjecture](../twin-prime-conjecture/) — shifted-prime distribution, central to the most plausible route here.
- [Erdős–Straus Conjecture](../erdos-straus-conjecture/) — elementary-statement-hard-proof in the same tradition.
