# Status & Frontier — The Hardy–Littlewood k-tuple Conjecture

_Where the problem stands and what a resolution would require._

**Status: active-progress; open for every $k \ge 2$.** No admissible $k$-tuple ($k\ge 2$) has been proved to be all-prime infinitely often, let alone shown to satisfy the predicted asymptotic with constant $\mathfrak{S}(\mathcal{H})$. The conjecture is unproven in even its weakest qualitative form for $k=2$ (the twin-prime conjecture is the special case $\mathcal{H}=\{0,2\}$).

## What is known

**Unconditional upper bounds (right order, wrong constant).** Sieve theory gives
$$\pi_{\mathcal{H}}(x) \le \big(2^k k! + o(1)\big)\,\mathfrak{S}(\mathcal{H})\,\frac{x}{(\log x)^k},$$
i.e. the conjectured order of magnitude, off by a bounded factor. No matching unconditional lower bound of any positive order is known for $k\ge 2$.

**Almost-primes.** Chen's theorem (1973) gives infinitely many $n$ with $n$ prime and $n+2 = P_2$ — the conjecture "up to one extra prime factor," and only for the pair.

**Bounded gaps and many-primes-in-tuples.** Zhang (2013) proved infinitely many bounded prime gaps unconditionally; Maynard and Tao (2013–14) reproved this from Bombieri–Vinogradov and showed every admissible $k$-tuple contains $\gg \log k$ primes infinitely often, with $\liminf(p_{n+m}-p_n) < \infty$ for all $m$. Polymath8 reached gap $\le 246$. **This produces $m$ primes inside an admissible set, not the whole set, and yields no asymptotic.**

**Function fields.** Sawin–Shusterman proved strong Hardy–Littlewood-type asymptotics over $\mathbb{F}_q[t]$ for large $q$, confirming the predicted form in that model — but with no transfer to $\mathbb{Z}$.

**Conditional results.** Under the Elliott–Halberstam conjecture, Maynard–Tao gives gaps of 6; under generalized EH, sharper constellation results follow. Even full EH does not deliver the integer asymptotic — the parity barrier survives.

## What a full resolution requires

A proof must (i) produce a **lower bound** of the correct order $\gg \mathfrak{S}(\mathcal{H}) x/(\log x)^k$ for *genuine* primes simultaneously, not almost-primes, and (ii) pin the **constant** to $\mathfrak{S}(\mathcal{H})$. Achieving (i) means **breaking the parity barrier**: supplying arithmetic information (a Type-II / bilinear estimate, or an unconditional distribution input far beyond Bombieri–Vinogradov) strong enough to force exactly-prime values. No present technique does this; it is widely believed to demand a fundamentally new idea, comparable in novelty to the circle method or to the resolution of the Riemann hypothesis in the function-field analogue.

**Plausible routes.** (a) A dramatic strengthening of equidistribution (toward Elliott–Halberstam with power-saving and bilinear control) that, combined with a parity-defeating maneuver, yields lower bounds; (b) transfer of geometric/cohomological methods from the function-field proofs to $\mathbb{Z}$ — currently obstructed by the lack of an analogue of the Riemann hypothesis in the requisite form; (c) an entirely new analytic identity that sieves cannot see. None is close.

## Related problems

- [Twin Prime Conjecture](../twin-prime-conjecture/README.md) — the case $\mathcal{H}=\{0,2\}$.
- [Polignac's Conjecture](../polignac-conjecture/README.md) — every even gap recurs infinitely often.
- [Goldbach Conjecture](../goldbach-conjecture/README.md) — sister additive-prime problem via the same circle method.
- [Bunyakovsky Conjecture](../bunyakovsky-conjecture/README.md) — single-polynomial analogue, subsumed by Bateman–Horn.
- [Riemann Hypothesis](../riemann-hypothesis/README.md) — governs the prime-distribution inputs the conjecture relies on.
