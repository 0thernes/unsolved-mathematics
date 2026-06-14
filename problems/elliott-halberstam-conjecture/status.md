# Status & Frontier — The Elliott–Halberstam Conjecture

_Where the problem stands and what a resolution would require._

**Status: open (active progress).** The Elliott–Halberstam conjecture — that primes are equidistributed in arithmetic progressions, on average over the modulus, up to level of distribution $\theta < 1$ — remains unproved for every $\theta > 1/2$ in the uniform (maximum-over-residue-class) sense. It is *not* resolved, and no credible claim of resolution exists.

## What is known unconditionally

- **Level $\theta = 1/2$.** The Bombieri–Vinogradov theorem (1965) gives, for every $A>0$,
$$\sum_{q \le x^{1/2}/(\log x)^B} \max_{(a,q)=1} \Big| \psi(x;q,a) - \tfrac{x}{\varphi(q)} \Big| \ll_A \tfrac{x}{(\log x)^A}.$$
This matches what GRH yields for individual moduli and is the unconditional benchmark.
- **Past $1/2$ for fixed residue classes.** Bombieri, Friedländer, and Iwaniec (1986–89) reached $\theta = 4/7$ for a *fixed* class $a$, via the dispersion method and Kloosterman-sum bounds — but not uniformly in $a$.
- **Restricted EH for smooth/well-factorable moduli.** Zhang (2013) proved a Bombieri–Vinogradov-type estimate at $\theta = 1/2 + 1/584$ for smooth moduli; Polymath8a improved the exponent. These suffice for bounded prime gaps but do not establish general EH.

## What is known conditionally

- Under full **EH** ($\theta\to 1^-$), the Goldston–Pintz–Yıldırım sieve gives $\liminf_n (p_{n+1}-p_n) \le 16$.
- Under the **generalized** EH (GEH, covering Dirichlet convolutions), the Maynard–Tao multidimensional sieve (Polymath8b, 2014) gives $\liminf_n (p_{n+1}-p_n) \le 12$, plus bounds on $p_{n+2}-p_n$.
- Crucially, the **parity problem** (Selberg) shows that EH/GEH alone *cannot* deliver the twin-prime conjecture ($\le 2$); the best the EH-sieve framework reaches is $\le 6$ for certain configurations.

## What a full resolution requires

A proof of uniform EH for any $\theta > 1/2$ would need a source of cancellation in the relevant bilinear/exponential sums that goes genuinely beyond the large sieve — the large sieve being provably sharp at $x^{1/2}$. The fixed-class BFI results suggest the truth lies near $\theta = 1$, but converting those gains into a *uniform* statement (max over $a$) has resisted all attempts; the dispersion method intrinsically fixes the class. A full proof to $\theta < 1$ would essentially require GRH-strength control on average over the full admissible range, likely demanding new automorphic / spectral input or a fundamentally new bilinear estimate.

## Plausible routes

1. **Extend BFI uniformly** — remove the fixed-class restriction from the dispersion/Kloosterman approach, the most-studied but most-obstructed path.
2. **Sharper algebraic exponential sums** — better Weil/Deligne-type bounds to enlarge the smooth-moduli range, continuing the Zhang–Polymath line (gains so far are tiny).
3. **New large-sieve-type inequalities** capturing arithmetic structure the classical one misses.

The practical payoff of any progress flows through the bounded-gaps program: the conjecture's modern significance is that it is the cleanest hypothesis controlling how small prime gaps can provably be.

## Related problems

- [Twin Prime Conjecture](../twin-prime-conjecture/README.md)
- [Polignac's Conjecture](../polignac-conjecture/README.md)
- [Hardy–Littlewood k-tuple Conjecture](../hardy-littlewood-k-tuple/README.md)
- [Grand Riemann Hypothesis](../grand-riemann-hypothesis/README.md)
- [Chowla Conjecture](../chowla-conjecture/README.md)
