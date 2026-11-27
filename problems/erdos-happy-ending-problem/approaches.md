# Approaches — The Happy Ending Problem (Erdős–Szekeres Conjecture)

_Major strategies, partial results, and barriers._

1. **Cups-and-Caps Dynamic Programming (Erdős–Szekeres 1935).** Define $f(k, \ell)$ as the minimum number of points guaranteeing either a $k$-cup (convex upward chain) or an $\ell$-cap (convex downward chain). Exact induction gives $f(k, \ell) = \binom{k + \ell - 4}{k - 2} + 1$, which is sharp for cups/caps alone yet wastes a factor of $2^n$ when one only asks for *any* convex $n$-gon.
2. **Positive-Fraction & Container / Partition Method (Suk 2017; Holmsen–Mojarrad–Pach–Tardos 2020).** Combining the Pór–Valtr positive-fraction Erdős–Szekeres theorem (extracting $m$ well-separated convex clusters of positive size) with a careful cups-and-caps argument across clusters reduces the upper bound from $\approx 4^n$ all the way to $2^{n + O(\sqrt{n \log n})}$.
3. **SAT / Realizable Order-Type Enumeration (Szekeres–Peters 2006; Scheucher).** Encoding oriented matroids / triple orientations of $N$ planar points into SAT solvers settled $\mathrm{ES}(6) = 17$ and yields structural bounds on empty $k$-gons (Horton sets), though $N = 33$ ($n = 7$) currently lies far beyond direct combinatorial search.

## Core Barrier
Suk's and Holmsen–Mojarrad–Pach–Tardos's proofs determine $\log_2 \mathrm{ES}(n) = n + o(n)$, confirming the base $2$ of the exponential! However, removing the $O(\sqrt{n \log n})$ error in the exponent — down to the exact constant $-2$ in $2^{n-2} + 1$ — requires overcoming the loss incurred when partitioning into convex clusters via the positive-fraction theorem, where sub-exponential overhead appears intrinsic.
