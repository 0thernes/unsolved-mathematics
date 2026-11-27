# Approaches — Cramér's Conjecture on Prime Gaps

_Major strategies, partial results, and barriers._

1. **Zero-Density & Explicit Formula Methods (Baker–Harman–Pintz 2001).** Combining Harman's sieve with zero-density estimates for $\zeta(s)$ yields $p_{n+1} - p_n \ll p_n^{0.525}$ unconditionally. Even assuming full RH only lowers the exponent to $1/2$ ($O(p_n^{1/2} \log p_n)$) because individual terms $x^\rho / \rho$ in the explicit formula have magnitude $x^{1/2}$.
2. **Pair Correlation & Higher Moments of Prime Gaps.** Montgomery's pair correlation conjecture plus RH improves *almost-all* intervals down to $(\log x)^{2+\varepsilon}$ (Heath-Brown / Selberg), showing that Cramér's bound holds for almost all primes — yet exceptional intervals cannot be excluded without controlling extreme cancellations among all $\zeta$-zeros simultaneously.
3. **Large-Gap Lower Bounds (Rankin; FGKMT 2016/2018).** Covering a long interval of integers by residue classes modulo small primes (via hypergraph packing / Rödl nibble + Maynard–Tao prime-tuple weights) produces gaps of size $\gg \frac{\log x \log\log x \log\log\log\log x}{\log\log\log x}$, still nearly a full factor of $\log x$ below $(\log x)^2$.

## Core Barrier
Cramér's conjecture is **strictly stronger than Legendre's conjecture** (a prime between $n^2$ and $(n+1)^2$, i.e. $O(\sqrt{p_n})$) and **does not follow from the Riemann Hypothesis**. Breaking even the $\sqrt{p_n}$ barrier unconditionally — or conditionally on RH! — requires understanding extreme correlations among the imaginary parts of zeta zeros well beyond current spectral or sieve theory.
