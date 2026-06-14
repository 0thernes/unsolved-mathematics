# Approaches — Legendre's Conjecture

The conjecture is a short-interval prime problem: it asks for a prime in $(x, x+y)$ with $y \approx 2\sqrt{x}$ for *every* $x$ of the form $n^2$. Equivalently, it demands that the maximal prime gap below $X$ is $O(\sqrt{X})$. All serious lines of attack therefore target the function $\pi(x+y)-\pi(x)$, or the corresponding sum $\sum_{x<n\le x+y}\Lambda(n)$, and try to push the interval length $y$ down to $x^{1/2}$. The recurring obstacle is that the best unconditional methods stall at $y = x^{0.525}$, a hair above the required $x^{0.5}$.

## Zero-density estimates and the classical short-interval program

**Core idea.** Via Perron's formula, the count of primes in $(x, x+y)$ is governed by zeros of the Riemann zeta function $\zeta(s)$. If $\zeta(s)$ had no zeros to the right of $\Re s = \sigma$, primes would be evenly distributed in intervals of length $x^{\sigma+\varepsilon}$. Since we cannot prove such zero-free regions are wide enough, one instead uses **zero-density theorems** — bounds of the form $N(\sigma, T) \ll T^{A(\sigma)(1-\sigma)+\varepsilon}$ on the number of zeros with real part $\ge \sigma$ — to show that the *aggregate* contribution of zeros near the critical line is small enough to leave primes in short intervals.

**Best result.** This program yields the standing unconditional record of Baker, Harman, and Pintz (2001): a prime in $(x, x+x^{0.525})$ for all sufficiently large $x$. Earlier milestones in the same lineage are Hoheisel's $1-1/33000$ (1930), Ingham's deduction of primes between consecutive cubes (1937), and Huxley's $7/12$ (1979). Recent improvements to Ingham-type zero-density bounds (Guth–Maynard, 2024) sharpen related exponents but do not yet move the Legendre-relevant constant to $1/2$.

**Barrier.** The exponent $0.525$ sits above $0.5$, and reaching $1/2$ exactly — let alone going below it with the necessary uniformity — appears to require essentially the full strength of the Riemann Hypothesis *and more*. Even on RH, the implied gap bound is $O(\sqrt{x}\log x)$, which **fails** to give Legendre's conjecture by a factor of $\log x$. This logarithmic deficit is the crux: no known density argument removes it.

## Sieve methods and the parity barrier

**Core idea.** Sieves estimate how many integers in a short interval survive removal of multiples of small primes, producing lower bounds on the count of "almost primes" or genuine primes. Harman's sieve and Chen-type bilinear decompositions of $\Lambda$ are central to the Baker–Harman–Pintz argument.

**Best result.** Sieves are responsible for the constant $0.525$ and for results like the existence of *almost-primes* (numbers with few prime factors) in even shorter intervals.

**Barrier.** Pure sieve methods are obstructed by the **parity problem** (Selberg): a sieve cannot, by itself, distinguish integers with an even number of prime factors from those with an odd number, and so cannot detect primes alone without an external "arithmetic" input. This caps what sieves can prove about short intervals and is a fundamental reason they cannot be pushed to the $x^{1/2}$ threshold unaided.

## Conditional approaches: RH and beyond

**Core idea.** Assume strong hypotheses and see how close one gets. Under RH, $\pi(x+y)-\pi(x) \sim y/\log x$ for $y = x^{1/2+\varepsilon}$, and the prime gap bound $p_{k+1}-p_k = O(\sqrt{p_k}\log p_k)$ follows (Cramér, 1919/1936).

**Best result.** RH gives gaps $O(\sqrt{p}\log p)$; the stronger Cramér probabilistic model predicts $O((\log p)^2)$; the Hardy–Littlewood $k$-tuple conjecture and Montgomery's pair-correlation conjecture sharpen the statistics further. All of these comfortably imply Legendre's conjecture.

**Barrier.** None of these is proved, and the gap between RH ($O(\sqrt{x}\log x)$) and Legendre ($O(\sqrt{x})$) is genuine — Legendre is *not* a formal consequence of RH. So even resolving the Riemann Hypothesis would leave Legendre open.

## Small-gap technology (Zhang–Maynard–Tao / GPY)

**Core idea.** The Goldston–Pintz–Yıldırım method and Maynard–Tao multidimensional sieve produce infinitely many bounded gaps between primes.

**Best result.** Bounded gaps ($p_{k+1}-p_k \le 246$ infinitely often, conditionally smaller). This is spectacular for *small* gaps.

**Barrier.** Legendre concerns *large* gaps and requires a prime in *every* window, an essentially orthogonal demand: bounded-gap results say nothing about the rare long stretches with no primes, which is exactly where Legendre could fail.

## Computational verification

**Core idea.** Directly check that $(n^2,(n+1)^2)$ contains a prime, and study maximal prime gaps to confirm they stay below $\sqrt{x}$.

**Best result.** The conjecture has been verified well past $n = 10^9$ and beyond; records of maximal prime gaps (Nicely, Oliveira e Silva, and others) remain consistent with gaps far smaller than $\sqrt{x}$.

**Barrier.** Computation can never prove a universal statement; it only raises confidence and guards against a small counterexample.
