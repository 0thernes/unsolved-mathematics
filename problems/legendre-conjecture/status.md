# Status & Frontier — Legendre's Conjecture

**Status: OPEN.** There is no accepted proof, and no announced resolution. The conjecture is one of Landau's four classical prime problems and is widely regarded as out of reach of present-day methods.

## What is known

The heuristic case for the conjecture is overwhelming. The prime number theorem predicts $\sim n/\log n$ primes in $(n^2,(n+1)^2)$, and computation has verified the existence of a prime in every such interval far beyond $n = 10^9$, with all observed maximal prime gaps lying well under $\sqrt{x}$. The conjecture is therefore believed to be **true**; the difficulty is purely in proving it for *every* $n$ with no exceptions.

## Strongest current results

**Unconditional.** The benchmark is the short-interval theorem of Baker, Harman, and Pintz (2001): for all sufficiently large $x$ there is a prime in
$$(x,\; x + x^{0.525}).$$
Applied at $x = n^2$, the interval $(n^2,\, n^2 + n^{1.05})$ contains a prime — but Legendre needs a prime already in $(n^2,\, n^2 + 2n+1)$, i.e. an interval of length $\Theta(n) = \Theta(x^{0.5})$. The exponent $0.525$ exceeds the required $0.5$, so the result **does not** establish Legendre's conjecture; it misses by the margin $x^{0.025}$.

**Conditional.** Under the Riemann Hypothesis, $p_{k+1}-p_k = O(\sqrt{p_k}\log p_k)$ (Cramér). This is *still insufficient*: the extra factor $\log p_k$ means RH alone does not imply a prime in every $(n^2,(n+1)^2)$. RH does yield that *almost all* such intervals contain a prime (Selberg, conditional), and stronger conjectures — Cramér's probabilistic model ($O((\log p)^2)$ gaps), the Hardy–Littlewood $k$-tuple conjecture, Montgomery's pair-correlation conjecture, Oppermann's and Andrica's conjectures — each comfortably imply Legendre's conjecture, but none is proved.

## What a full resolution would require

A proof must control $\pi(x+y)-\pi(x) \ge 1$ for $y \asymp \sqrt{x}$ **uniformly in $x$**, with no exceptional set. In zero-density language, it needs prime existence in intervals of length $x^{1/2}$ — pushing the admissible exponent from $0.525$ down past $0.5$. Because even RH leaves a $\log$ factor, a successful argument must either (i) prove RH *and* squeeze out the logarithm via additional structure (e.g. strong pair-correlation or twin-prime-type input), or (ii) find a genuinely new short-interval method that bypasses the zero-density bottleneck. The parity barrier blocks pure sieves from reaching primes at this scale, so new arithmetic input is essential.

## Plausible routes

The most credible near-term path is incremental improvement of **zero-density estimates** for $\zeta(s)$; the Guth–Maynard (2024) advance on large-value/Dirichlet-polynomial bounds has revived interest, though it does not yet move the Legendre-relevant exponent to $1/2$. Longer term, resolution likely waits on progress toward the Riemann Hypothesis together with finer correlation information. The small-gap revolution (Zhang–Maynard) is unlikely to apply directly, since Legendre concerns the rare *large*-gap regime.

## Related problems

- [Riemann Hypothesis](../riemann-hypothesis/README.md) — controls $\zeta$-zeros and hence short-interval prime distribution; necessary but, alone, not sufficient for Legendre.
- [Twin Prime Conjecture](../twin-prime-conjecture/README.md) — sister Landau problem on small gaps; complementary techniques.
- [Goldbach Conjecture](../goldbach-conjecture/README.md) — another of Landau's four problems.
- [Bunyakovsky Conjecture](../bunyakovsky-conjecture/README.md) — primes represented by polynomials; shares the "primes in thin sequences" flavor.
- [Andrica / Polignac-type gaps](../polignac-conjecture/README.md) — prime-gap conjectures that imply or refine the square-interval statement.
