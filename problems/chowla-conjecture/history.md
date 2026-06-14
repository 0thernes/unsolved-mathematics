# History — The Chowla Conjecture

_Origin, formulation, and timeline._

## Origin and formulation

The Liouville function $\lambda(n) = (-1)^{\Omega(n)}$, where $\Omega(n)$ counts prime factors with multiplicity, encodes the parity of the prime factorization. Its close cousin is the Möbius function $\mu$, which agrees with $\lambda$ on squarefree integers. Heuristically, $\lambda$ behaves like a random $\pm 1$ sequence: the single-average statement $\sum_{n\le x}\lambda(n)=o(x)$ is equivalent to the Prime Number Theorem (Landau, 1899), and the bound $\sum_{n\le x}\lambda(n)=O(x^{1/2+\varepsilon})$ is equivalent to the Riemann Hypothesis.

Sarvadaman Chowla, in his 1965 monograph *The Riemann Hypothesis and Hilbert's Tenth Problem*, formulated the natural generalization to higher-order correlations. In modern notation, the **Chowla conjecture** asserts that for any distinct non-negative integers $h_1,\dots,h_k$ and any choice of exponents $a_i\in\{1,2\}$ (not all even),
$$\sum_{n\le x}\lambda(n+h_1)^{a_1}\cdots\lambda(n+h_k)^{a_k}=o(x).$$
Equivalently, the sign pattern of $\lambda$ along shifts is asymptotically balanced — a precise statement that the Liouville/Möbius function is "pseudorandom." The two-point case $\sum_{n\le x}\lambda(n)\lambda(n+h)=o(x)$ is the simplest open instance; the conjecture also implies the infinitude of sign patterns and is intimately tied to questions on consecutive values of $\lambda$ (the Chowla–Erdős sign-pattern problem). A logarithmically-averaged variant replaces $\sum_{n\le x}$ by $\sum_{n\le x}\frac1n$.

A historical root predating the multiplicative framing is **Chowla's problem on $\sum_{n\le x}\mu(n)\mu(n+1)$**, sometimes traced to questions of Chowla and others in the 1930s–40s. The conjecture acquired renewed structural meaning through Sarnak's 2010 reformulation linking $\mu$-randomness to dynamical disjointness; the **Sarnak conjecture** on Möbius orthogonality to zero-entropy systems is implied by (logarithmic) Chowla.

## Timeline

**1899** — Landau: $\sum\mu(n)=o(x)$ ⇔ PNT, fixing the one-point baseline.

**1937** — Hua and others study averages of multiplicative functions; sign-change questions for $\lambda$ circulate.

**1965** — Chowla states the higher-correlation conjecture in his monograph.

**1968** — Cassels, Chowla and others note connections to sign patterns; the two-point case is recognized as central and unreachable.

**1977** — Hildebrand and later work establishes all eight sign patterns of length 3 occur with positive density — far from balance.

**2010** — Sarnak proposes the Möbius disjointness conjecture, recasting Chowla in ergodic-theoretic language and igniting a decade of cross-field activity.

**2015** — Matomäki and Radziwiłł prove a landmark theorem on multiplicative functions in short intervals, controlling averages on intervals $[x,x+h]$ with $h\to\infty$ arbitrarily slowly.

**2016** — Matomäki, Radziwiłł and Tao establish the two-point Chowla conjecture *on average* over $h$; Tao proves the **logarithmically-averaged two-point Chowla conjecture** $\sum_{n\le x}\frac{\lambda(n)\lambda(n+h)}{n}=o(\log x)$, using the entropy decrement argument.

**2017** — Tao and Teräväinen extend the logarithmic result to all odd-order correlations; Frantzikinakis–Host and others develop the ergodic structure of multiplicative functions.

**2018** — Tao–Teräväinen prove the logarithmically-averaged Chowla conjecture for all odd $k$ unconditionally.

**2019** — Tao's solution of the Erdős discrepancy problem (2015) and subsequent work cement entropy-decrement and Gowers-norm methods as the central toolkit.

**2023–2024** — Quantitative refinements (Tao–Teräväinen, Helfgott–Radziwiłł and others) sharpen error terms; the **even-order** correlations and the **non-logarithmic** (natural-density) Chowla conjecture remain open, marking the present frontier. No unconditional proof of even the natural-density two-point case is known.
