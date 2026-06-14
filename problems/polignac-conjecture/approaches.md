# Approaches — Polignac's Conjecture

_Major strategies, partial results, and barriers._

## Sieve methods (Brun, Selberg) and the parity barrier

The oldest serious line of attack is combinatorial sieve theory. Brun's sieve (1915) was the first to control the number of integers $n \le x$ for which both $n$ and $n+k$ avoid small prime factors, yielding the upper bound $\pi_k(x) \ll x/(\log x)^2$ for the count of prime pairs and proving Brun's theorem that $\sum 1/p$ over twin primes converges. The Selberg sieve (1940s) sharpened the constants. The decisive limitation is **Selberg's parity barrier**: a pure sieve cannot distinguish integers with an even number of prime factors from those with an odd number, so it cannot, by itself, produce a *lower* bound forcing infinitely many genuine prime pairs. Every unconditional approach to Polignac must inject non-sieve arithmetic information (typically equidistribution of primes in arithmetic progressions) to break parity. The best a sieve alone reaches is Chen-type results: infinitely many $p$ with $p+2$ having at most two prime factors.

## Chen's theorem (almost-prime companions)

Chen Jingrun (1973) combined a weighted sieve with Bombieri–Vinogradov-type inputs to prove that there are infinitely many primes $p$ such that $p+2$ is either prime or a product of two primes. This is the closest unconditional approach to the twin-prime ($k=2$) case and generalizes to every even $k$. It does not resolve Polignac because the "semiprime" alternative cannot be eliminated—removing it would again require crossing the parity barrier. Chen's result remains, fifty years on, the strongest statement of its kind.

## Small-gaps method: GPY and admissible tuples

Goldston, Pintz and Yıldırım (2005) introduced a higher-rank Selberg sieve weighting $k$-tuples, proving $\liminf_n (p_{n+1}-p_n)/\log p_n = 0$—gaps infinitely often much smaller than average. The method depends on the *level of distribution* $\theta$ of primes: the Bombieri–Vinogradov theorem gives $\theta = 1/2$ unconditionally, and GPY showed that any $\theta > 1/2$ would already yield bounded gaps. The barrier here was concrete: nobody could prove distribution beyond $1/2$ for the relevant moduli.

## Zhang's bounded gaps and Polymath8

Yitang Zhang (2013) broke the GPY barrier by proving a *restricted* Bombieri–Vinogradov estimate—equidistribution to level $\theta = 1/2 + 1/584$ over smooth ("$y$-friable") moduli—using deep inputs from algebraic geometry (the Weil/Deligne bounds for exponential sums via the work of Birch, Bombieri, Friedlander, Iwaniec). This forced $\liminf_n (p_{n+1}-p_n) < 7 \times 10^7$: **some** even gap $\le 7\times 10^7$ recurs infinitely often, a qualitative Polignac result. The Polymath8a collaboration optimized Zhang's distribution exponent and admissible-tuple combinatorics, lowering the bound to 4680.

## Maynard–Tao multidimensional sieve

James Maynard and, independently, Terence Tao (2013–2014) replaced the GPY one-dimensional weight with a fully multidimensional sieve, decoupling the result from any distribution level beyond Bombieri–Vinogradov. This both simplified Zhang's argument and proved much more: for any $m$, there are infinitely many intervals of bounded length containing $\ge m$ primes. Quantitatively it gave $\liminf_n (p_{n+1}-p_n) \le 600$, and the Polymath8b project pushed this to **246** unconditionally—the current record. Under the Elliott–Halberstam conjecture (level $\theta \to 1$) the method yields a gap $\le 12$, and a generalized Elliott–Halberstam input gives $\le 6$. None of these isolates a *specific* $k$: the sieve guarantees one of finitely many gaps occurs infinitely often without identifying which.

## Hardy–Littlewood / circle-method heuristics

The Hardy–Littlewood $k$-tuple conjecture (1923) predicts exact asymptotic densities for every even gap via a singular series, and would imply Polignac in full. The circle method underlying it works for ternary additive problems (e.g. Vinogradov's three-primes theorem) but fails for binary problems like twin primes because the minor arcs cannot be controlled. This is a structural obstruction: the binary additive problem lacks enough averaging. The heuristics are strongly supported numerically but provide no path to a proof.

## Why a full resolution remains out of reach

Every known unconditional route stops short for the same two reasons: the parity barrier blocks pure sieves from lower bounds, and the available level of distribution ($\theta = 1/2$, or slightly past it over special moduli) is insufficient to pin down individual gaps. Resolving even $k=2$ would require either a genuine breach of parity (no mechanism is known) or distribution estimates of a strength—uniform, to level approaching 1—that currently sit beyond the large sieve and the Riemann Hypothesis alike.
