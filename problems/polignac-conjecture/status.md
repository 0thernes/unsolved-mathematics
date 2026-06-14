# Status & Frontier — Polignac's Conjecture

_Where the problem stands and what a resolution would require._

**Status: open, with major partial progress.** No individual case of Polignac's conjecture is proved or disproved—including the twin prime case $k=2$. What *is* proved, since 2013, is a genuine but qualitative weakening: at least one even number $k$ occurs as a gap between consecutive primes infinitely often, with $k$ bounded by an explicit constant.

**Strongest unconditional results.**

- **Bounded gaps (Zhang 2013; Maynard, Tao 2013–2014; Polymath8b 2014).** $\liminf_n (p_{n+1}-p_n) \le 246$. Equivalently, some even $k \le 246$ is a Polignac gap. The proof does not identify which $k$; it shows that among a finite admissible set, at least one value recurs infinitely often.
- **Many primes in short intervals (Maynard–Tao).** For every $m$, there are infinitely many bounded-length intervals containing at least $m$ primes—far stronger than mere pairs.
- **Chen-type (Chen 1973).** Infinitely many primes $p$ with $p+k$ prime or semiprime, for every fixed even $k$. The "semiprime" alternative is exactly what the parity barrier prevents removing.
- **Small relative gaps (GPY 2005/2009).** $\liminf_n (p_{n+1}-p_n)/\log p_n = 0$.

**Strongest conditional results.** Under the Elliott–Halberstam conjecture (primes equidistributed in arithmetic progressions to level $\theta \to 1$), the Maynard–Tao method gives $\liminf_n(p_{n+1}-p_n) \le 12$; a generalized Elliott–Halberstam input lowers this to $\le 6$. Even full Elliott–Halberstam does **not** reach $k=2$: a residual factor of the parity barrier blocks the step from $\le 6$ to $2$.

**What a full resolution requires.** Polignac in full demands, for *every* even $k$, infinitely many consecutive-prime gaps equal to $k$. Two distinct obstructions stand in the way. (1) **The parity barrier**: pure sieve methods cannot produce the lower bound that distinguishes "prime" from "product of two primes," so any proof of a specific gap must inject genuinely new arithmetic input. (2) **Level of distribution**: the available equidistribution of primes in progressions tops out near $\theta = 1/2$ (Bombieri–Vinogradov), or marginally past it over special moduli (Zhang); pinning down individual gaps would need distribution of a uniformity that currently exceeds even what the Riemann Hypothesis supplies.

**Plausible routes.** Realistic near-term progress is incremental: lowering 246 toward the conditional floor of 6, and proving stronger distribution estimates over restricted moduli à la Zhang. A resolution of any single case (say $k=2$) would likely require either a method that genuinely breaks parity—none is known—or a Hardy–Littlewood-strength input that no current technique approaches. The Hardy–Littlewood $k$-tuple conjecture would imply Polignac outright but is itself far out of reach. Most experts regard the full conjecture as no easier than the twin prime conjecture and expect it to remain open for the foreseeable future, even as the bounded-gaps record continues to be refined.

## Related problems

- [Twin Prime Conjecture](../twin-prime-conjecture/README.md) — the case $k=2$, the most famous instance.
- [Hardy–Littlewood k-tuple Conjecture](../hardy-littlewood-k-tuple/README.md) — the quantitative refinement implying Polignac in full.
- [Legendre's Conjecture](../legendre-conjecture/README.md) — a sibling question on the distribution and spacing of primes.
- [Goldbach Conjecture](../goldbach-conjecture/README.md) — the parallel binary additive prime problem driving Chen's and Brun's methods.
- [Bunyakovsky Conjecture](../bunyakovsky-conjecture/README.md) — prime values of polynomials, another irreducibility-and-density question beyond current sieve reach.
