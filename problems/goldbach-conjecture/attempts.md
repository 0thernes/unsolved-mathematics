# Attempts — Goldbach's Conjecture

_Notable attempts, near-misses, retracted proofs._

## Landmark partial results (genuine progress)

- **Brun's almost-prime theorem (1920).** Viggo Brun's new sieve produced the first finite bound: every large even number is a sum of two numbers each with at most 9 prime factors ("$9+9$"). A near-miss in spirit — the structure was right, the prime-factor counts too large — but it opened the entire sieve-theoretic line.
- **Schnirelmann (1930).** Showed every integer $>1$ is a sum of a bounded number of primes (originally a large constant, since reduced to $\le 6$ for evens by Ramaré, 1995). The first *unconditional* general additive-basis result.
- **Vinogradov (1937).** Every sufficiently large odd integer is a sum of three primes — the ternary problem solved for large $n$, unconditionally. The "sufficiently large" threshold was astronomically large (Borozdkin's explicit bound was around $e^{e^{16.038}}\approx 3^{3^{15}}$), leaving a vast unverifiable gap for decades.
- **Chen Jingrun (1966 announcement; 1973 full proof).** Every sufficiently large even integer is $p + P_2$. This "$1+2$" theorem is the strongest approximation to the binary conjecture and is regarded as one of the great sieve achievements; it sits exactly at the parity barrier.
- **Helfgott (2013).** Proved the **weak (ternary) Goldbach conjecture in full** for all odd $n>5$, closing Vinogradov's gap by driving down the threshold to about $10^{27}$ and verifying below it computationally with David Platt. The two-paper preprint (major and minor arcs) and accompanying book manuscript have been widely accepted by the community as a complete proof; as of this writing the unified monograph has been long in formal journal review, a status worth noting honestly, though the result is treated as established.

## Claimed proofs of the strong conjecture (disputed / unverified)

The binary conjecture's fame attracts frequent claimed proofs, none accepted:

- **Recurring arXiv/preprint claims.** Over the years numerous preprints have announced elementary or sieve-based proofs of binary Goldbach. The standard objection is uniform: any *elementary* sieve argument runs into **Selberg's parity problem**, which provably blocks distinguishing the "two primes" case from "two almost-primes" without auxiliary input. A claimed elementary proof that does not explicitly defeat parity is, on those grounds alone, presumed flawed by experts. Because none of these has survived peer scrutiny, this dossier names no specific individual claim as credible.
- **Probabilistic/heuristic "proofs."** Some attempts invoke the Cramér / Hardy–Littlewood probabilistic model of primes to argue Goldbach "must" hold. These establish that the conjecture is overwhelmingly *plausible* (the expected number of representations of $n$ grows like $\sim n/(\log n)^2$), but heuristics are not proofs — the model is not a theorem about the actual primes, and the objection is simply that no rigorous deduction has been supplied.

## Famous near-miss framing

The gap between what is proved and the conjecture is unusually narrow yet stubborn. Three facts illustrate it: (i) the conjecture holds for **almost all** even integers with a power-saving exceptional set (Montgomery–Vaughan); (ii) every large even number is $p+P_2$ (Chen); (iii) it is verified to $4\times10^{18}$. Each is "one step" from $p+p$, but each step is blocked by the same minor-arc / parity obstruction. The honest summary: the strong conjecture has resisted every method that resolved its weaker cousins.
