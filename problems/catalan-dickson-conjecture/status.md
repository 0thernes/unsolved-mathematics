# Status & Frontier — The Catalan–Dickson Conjecture (Aliquot Sequences)

_Where the problem stands and what a resolution would require._

**Status: open.** No aliquot sequence has been proved to diverge, and none of the small undetermined sequences has been proved to terminate or cycle. The Catalan–Dickson conjecture (every aliquot sequence is bounded) and the opposing Guy–Selfridge conjecture (a positive proportion diverge) are both unproved; expert opinion and computation favor Guy–Selfridge, but neither has a proof.

## What is known unconditionally

- **One-step dynamics are well understood.** Abundant numbers (with $s(n)>n$) have positive density $\approx 0.2476$; deficient numbers dominate but do not exclude growth. The average of $\log(s(n)/n)$ — the Bosma–Kane "aliquot constant" — is known, and over even $n$ the map tends to increase, lending rigorous plausibility to divergence.
- **Image and fibers of $s$ are controlled.** Untouchable numbers (not in the range of $s$) have positive lower density; the fibers $s^{-1}(m)$ obey sharp average bounds (Pomerance, Pollack, Kobayashi). Amicable pairs and sociable cycles have density-zero counting bounds.
- **Termination is decidable per sequence only when it happens.** Any individual sequence that terminates or cycles can be certified by extension; an unbounded one cannot be certified unbounded.
- **All starters below $1000$ are resolved except the Lehmer five** ($276, 552, 564, 660, 966$), which have been extended to thousands of terms and $200+$-digit values with no resolution.

## What is known conditionally

There is no clean conditional resolution (e.g., "Catalan–Dickson follows from hypothesis $X$"). The conditional landscape is heuristic: *if* the drivers/guides model with quasi-independence of successive terms is accurate, *then* sequences carrying persistent drivers diverge, contradicting Catalan–Dickson. This is a model, not a theorem, and it has no rigorous hypothesis from which the conclusion provably follows.

## What a full resolution requires

- **To prove Catalan–Dickson (boundedness):** one would need a *Lyapunov-type invariant* — a quantity provably non-increasing along every orbit, or an effective a priori bound on $\sup_k s^{(k)}(n)$ in terms of $n$. No candidate is known, and the positive average growth of $s$ on even numbers is evidence against any such bound existing universally.
- **To prove Guy–Selfridge (divergence):** one would need to certify that at least one explicit sequence (e.g. $276$) never descends below its current floor, or to show a positive-density family escapes to infinity — requiring rigorous control of an infinite, factorization-dependent orbit, far beyond present analytic technique.

## Plausible routes

1. **Rigorous probabilistic dynamics:** replace the quasi-independence assumption with a proven mixing/decorrelation statement for the iterated map — the most promising but most distant route.
2. **Driver-persistence theorems:** prove that certain drivers persist with controlled probability long enough to force growth, upgrading the heuristic toward a conditional divergence result.
3. **Extended structural theory of $s$:** push the Pomerance–Pollack program from one-step to multi-step statistics, controlling short orbit segments rigorously.
4. **Continued computation:** while it cannot resolve the conjecture, extending the Lehmer five and mapping open starters sharpens the empirical case and tests heuristics.

The realistic assessment is that the problem is genuinely hard and not close to resolution: there is no known mechanism to certify divergence and strong reason to doubt any universal bound forcing convergence.

## Related problems

- [Odd Perfect Numbers](../odd-perfect-numbers/README.md)
- [Infinitude of Mersenne Primes](../mersenne-primes-infinitude/README.md)
- [The Collatz Conjecture](../collatz-conjecture/README.md)
- [Erdős–Straus Conjecture](../erdos-straus-conjecture/README.md)
- [Lehmer's Totient Problem](../lehmer-totient-problem/README.md)
