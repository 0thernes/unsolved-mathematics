# Status & Frontier — Sarnak's Möbius Disjointness Conjecture

_Where the problem stands and what a resolution would require._

**Status: open, active progress.** The universal statement — $\frac1N\sum_{n\le N}\mu(n)f(T^n x)\to 0$ for *every* zero-entropy topological system $(X,T)$, every $f\in C(X)$, and every $x$ — is unproven. What exists is a large and growing collection of confirmed special classes plus strong results in the *logarithmically-averaged* setting.

## What is known (unconditional)

- **Algebraic / homogeneous classes.** Circle rotations and Kronecker systems (Davenport, 1937); all **nilsystems** and nilsequences (Green–Tao; Bourgain–Sarnak–Ziegler, 2012–2013); **horocycle flows** (BSZ, 2013).
- **Combinatorial sequences.** The Thue–Morse and Rudin–Shapiro sequences (Mauduit–Rivat) and, more generally, **all automatic sequences** (Müllner, 2017).
- **Low-complexity ergodic classes.** Discrete- and quasi-discrete-spectrum systems; many rank-one and interval-exchange systems; certain analytic skew products and smooth time-changes (Kanigowski–Lemańczyk–Radziwiłł and others).
- **The strongest general theorem.** Frantzikinakis–Host (2018) proved the conjecture (in **logarithmic average**) for **every system with countably many ergodic invariant measures** — the broadest class settled to date.

## What is known (conditional / log-averaged)

- Tao (2016) proved the **logarithmically-averaged two-point Chowla conjecture** via an entropy-decrement argument; Tao (2017) proved that **log-Sarnak $\iff$ log-Chowla**, so logarithmic-average progress transfers freely between the two. Tao–Teräväinen extended the log-Chowla picture to odd orders and, conditionally, beyond.
- These results are genuine but deliver only $\frac1{\log N}\sum_{n\le N}\frac{\cdot}{n}$ averaging, not the ordinary Cesàro mean the conjecture demands.

## What a full resolution requires

1. **Close the log-to-Cesàro gap.** Convert logarithmically-averaged disjointness into ordinary-average disjointness — equivalently, prove ordinary two-point Chowla, which no current method (entropy decrement included) achieves.
2. **Handle wild zero-entropy systems.** Extend beyond countably-many-ergodic-measure systems to those with uncountably many ergodic measures and sub-exponential but positive complexity, where structure theory is unavailable.
3. **A universal mechanism, not case-by-case.** A proof of the general statement likely needs a single principle linking multiplicativity of $\mu$ to zero entropy, rather than the present sequence of class-specific verifications.

## Plausible routes

- **Strengthen Matomäki–Radziwiłł** short-interval technology to break the logarithmic barrier — currently the most promising analytic avenue.
- **Joinings/structure theory** that classifies all zero-entropy systems disjoint from $\mu$, pushing the Frantzikinakis–Host method past its countability hypothesis.
- **Higher-order Fourier analysis** (Tao–Teräväinen) extended to even orders and to ordinary averaging, which would yield full Chowla and hence Sarnak.

No claimed proof of the full conjecture exists; the problem is firmly open, with the ordinary-average Chowla statement widely regarded as the crux.

## Related problems

- [Chowla Conjecture](../chowla-conjecture/README.md)
- [Riemann Hypothesis](../riemann-hypothesis/README.md)
- [Elliott–Halberstam Conjecture](../elliott-halberstam-conjecture/README.md)
- [Twin Prime Conjecture](../twin-prime-conjecture/README.md)
- [Grand Riemann Hypothesis](../grand-riemann-hypothesis/README.md)
