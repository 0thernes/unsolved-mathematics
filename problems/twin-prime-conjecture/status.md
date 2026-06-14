# Status & Frontier — The Twin Prime Conjecture

_Where the problem stands and what a resolution would require._

## Current status: open, with major partial progress

The twin prime conjecture — infinitely many primes $p$ with $p+2$ prime — remains **unproved**. Status: *active progress*. The last decade transformed the landscape, but the specific gap of $2$ is still beyond reach. What follows separates what is rigorously known from what is conjectural.

## Strongest unconditional results

- **Bounded gaps (gap $\le 246$).** There exists an even $h \le 246$ such that $p_{n+1}-p_n = h$ for infinitely many $n$ — equivalently, infinitely many prime pairs differ by at most $246$. This follows from Zhang (2013), Maynard, and Tao, optimized by Polymath8b (2014). It is a uniform case of Polignac's conjecture, though it does **not** identify which gap recurs.
- **Chen's theorem (1973).** Infinitely many primes $p$ have $p+2$ equal to a prime or a product of two primes ($P_2$). This is the strongest "almost-twin" statement: replace "prime" by "$\le 2$ prime factors."
- **Many primes in bounded intervals.** For every $m$, infinitely many bounded-length intervals contain at least $m$ primes (Maynard, Tao).
- **Upper bounds.** Brun's sieve gives $\pi_2(x) = O(x/(\ln x)^2)$, matching the conjectured order of magnitude up to a constant.

## Strongest conditional results

- Under the **generalized Elliott–Halberstam conjecture** (GEH), the gap bound drops to $\le 6$ (Polymath8b). Notably, even GEH yields $6$, **not** $2$ — a direct manifestation of the parity barrier.
- The **Hardy–Littlewood** asymptotic $\pi_2(x)\sim 2C_2\int_2^x dt/(\ln t)^2$, with $C_2\approx 0.6601618$, is overwhelmingly supported numerically but unproved.

## What a full resolution would require

Closing the gap from $246$ (or conditionally $6$) to exactly $2$ is not a matter of further optimization within current sieve technology. The decisive obstruction is the **parity problem** of sieve theory: weighted sieves cannot distinguish integers with one prime factor from those with an odd number of prime factors, so they cannot force $p+2$ to be *prime* rather than $P_2$. A proof seems to demand one of:

1. a **parity-breaking** arithmetic input — e.g. a distribution result for primes in progressions strong and structured enough to evade the parity obstruction;
2. an essentially **non-sieve** method that detects prime pairs directly (no such method is known); or
3. an unexpected reduction to a tractable problem (e.g. via automorphic forms, the Möbius function's correlations, or progress on the more general $k$-tuple conjecture).

## Plausible routes

The most-watched directions are: deeper equidistribution estimates beyond Bombieri–Vinogradov (the path Zhang opened); structural results on multiplicative functions and Möbius correlations (Matomäki–Radziwiłł-type theory); and any genuine theoretical attack on the parity barrier itself, which remains the central conceptual gap. Absent such an advance, the consensus is that bounded gaps will continue to improve toward small constants while the leap to $2$ stays out of reach.

## Related problems

- [Polignac's Conjecture](../polignac-conjecture/README.md) — the general statement of which twin primes is the case $2k=2$.
- [Hardy–Littlewood k-tuple Conjecture](../hardy-littlewood-k-tuple/README.md) — the quantitative generalization predicting densities of all admissible prime constellations.
- [Goldbach Conjecture](../goldbach-conjecture/README.md) — the other great additive-prime problem, sharing sieve and circle-method machinery.
- [Legendre Conjecture](../legendre-conjecture/README.md) — a sibling question on the distribution and spacing of primes.
- [Riemann Hypothesis](../riemann-hypothesis/README.md) — governs prime distribution error terms central to all of the above.
