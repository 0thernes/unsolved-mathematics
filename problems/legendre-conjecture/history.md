# History — Legendre's Conjecture

Legendre's conjecture is one of the four classical **Landau problems** — open questions on the distribution of primes that Edmund Landau, in his 1912 address to the Fifth International Congress of Mathematicians in Cambridge, singled out as "unattackable at the present state of science." It remains unsettled today.

## Origin and formulation

The conjecture is attributed to Adrien-Marie Legendre, who stated it in connection with his study of prime distribution in the early editions of his *Essai sur la théorie des nombres* (around 1808). The assertion is strikingly simple:

> For every positive integer $n$, there exists at least one prime $p$ with $n^2 < p < (n+1)^2$.

Equivalently, each interval between consecutive perfect squares contains a prime. Because the gap between consecutive squares is $(n+1)^2 - n^2 = 2n+1$, the conjecture is essentially a statement about short-interval prime gaps: if $p_k$ denotes the $k$-th prime, a near-equivalent form is that consecutive prime gaps satisfy $p_{k+1} - p_k < (2+o(1))\sqrt{p_k}$, i.e. gaps are $O(\sqrt{p_k})$ uniformly.

The conjecture sits in a hierarchy of square-root-spacing statements. It is **stronger** than the Bertrand–Chebyshev postulate (a prime between $m$ and $2m$) and is **implied by** several deeper conjectures: Oppermann's conjecture (a prime in each of $(n^2-n, n^2)$ and $(n^2, n^2+n)$), Andrica's conjecture ($\sqrt{p_{k+1}}-\sqrt{p_k}<1$), and Brocard's conjecture. It would also follow from the Cramér heuristic, which predicts maximal gaps of size $O((\log p)^2)$. Crucially, **the Riemann Hypothesis alone is not known to imply Legendre's conjecture** — RH yields $p_{k+1}-p_k = O(\sqrt{p_k}\log p_k)$, which carries an extra logarithmic factor and so falls just short. This single $\log$ is a large part of why the problem is hard.

## Why it resists standard tools

The prime number theorem gives $\pi(x)\sim x/\log x$, so heuristically $(n^2,(n+1)^2)$, of length $\approx 2n$, should contain about $n/\log n\to\infty$ primes. The difficulty is entirely one of **uniformity**: proving a prime in *every* such interval requires controlling primes in windows of length $x^{1/2}$ around $x$, while all unconditional short-interval results stop short of that exponent.

## Timeline

- **c. 1808** — Adrien-Marie Legendre states the conjecture in his work on prime distribution (*Essai sur la théorie des nombres*).
- **1845/1852** — Bertrand's postulate (prime between $m$ and $2m$), conjectured by Joseph Bertrand and proved by Pafnuty Chebyshev, secures the weaker constant-ratio interval result.
- **1896** — The Prime Number Theorem (Hadamard; de la Vallée Poussin) makes the heuristic prime count in $(n^2,(n+1)^2)$ precise but not uniform.
- **1912** — Edmund Landau lists Legendre's conjecture among four "unattackable" prime problems at the ICM in Cambridge.
- **1930** — Guido Hoheisel proves the first nontrivial short-interval result: primes in $(x, x+x^\theta)$ for $\theta = 1 - 1/33000$.
- **1937** — Albert Ingham, via zero-density estimates, deduces a prime between $n^3$ and $(n+1)^3$ for large $n$ — but cannot reach consecutive squares.
- **1972** — Hugh Montgomery's zero-density and pair-correlation work sharpens the available exponents.
- **1979** — Martin Huxley obtains primes in $(x, x+x^\theta)$ for $\theta = 7/12 + \varepsilon$, a durable benchmark.
- **2001** — Roger Baker, Glyn Harman, and János Pintz establish the standing unconditional record: a prime in $(x, x+x^{0.525})$ for large $x$.
- **2014–2015** — Yitang Zhang, James Maynard, and Polymath8 revolutionize *small* prime gaps; the tools illuminate but do not deliver the short-interval uniformity Legendre needs.
- **Present (2026)** — The conjecture remains open. The exponent $0.525$ is still distant from the required $0.5$, and closing that gap is widely viewed as beyond current technology.
