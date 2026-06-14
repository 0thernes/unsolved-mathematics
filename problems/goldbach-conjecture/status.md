# Status & Frontier — Goldbach's Conjecture

_Where the problem stands and what a resolution would require._

## Current status: OPEN (strong/binary form)

The **strong (binary) Goldbach conjecture** — every even integer $n>2$ is a sum of two primes — remains **unproven**. Its sibling, the **weak (ternary) conjecture**, is settled: every odd $n>5$ is a sum of three primes (Helfgott, 2013, building on Vinogradov 1937). The binary form is strictly harder and does **not** follow from the ternary result.

## What is known (unconditional)

- **Almost all even numbers** satisfy Goldbach: the exceptional set $E(X)=\#\{n\le X \text{ even}: n\neq p+q\}$ satisfies $E(X)=O(X^{1-\delta})$ with an explicit power saving (Montgomery–Vaughan 1975; later $\delta\approx0.7$ via Pintz and others).
- **Chen's theorem (1973):** every sufficiently large even $n$ is $p+P_2$, where $P_2$ has at most two prime factors. This is the best structural approximation to $p+p$.
- **Bounded number of primes:** every even integer is a sum of at most **4 primes** (a corollary of Helfgott's ternary theorem; Ramaré's earlier bound was $\le 6$).
- **Computational verification:** the conjecture holds for all even $n\le 4\times10^{18}$ (Oliveira e Silva–Herzog–Pardi).
- **Heuristic support:** the Hardy–Littlewood asymptotic predicts the representation count $r(n)\sim 2\Pi_2\big(\prod_{p\mid n,\,p>2}\tfrac{p-1}{p-2}\big)\tfrac{n}{(\log n)^2}$, so representations are abundant and grow — the conjecture is expected to hold with overwhelming margin.

## What is known (conditional)

Under the **Generalized Riemann Hypothesis**, major-arc estimates sharpen and exceptional-set bounds improve, and the ternary theorem becomes elementary for all $n$ — but GRH **does not** yield the binary conjecture. No standard hypothesis (GRH, GLH, even pair-correlation assumptions) is currently known to imply $p+p$ for every even $n$.

## What a full resolution would require

The crux is the **binary minor-arc problem**. In the circle method, $r_2(n)=\int_0^1 S(\alpha)^2 e(-n\alpha)\,d\alpha$ is dominated by the minor arcs, where the available square-mean cancellation of $S(\alpha)=\sum_{p\le n}e(p\alpha)$ is too weak to guarantee a positive main term for *every* $n$ (it suffices only on average). A proof would need either (i) a genuinely new way to control binary exponential sums over primes pointwise in $n$, or (ii) a sieve that defeats **Selberg's parity barrier** — classical sieves provably cannot separate "two primes" from "two almost-primes," which is exactly why Chen stalls at $1+2$. Closing $E(X)$ from a power-saving set to the empty set is, in effect, equivalent to the conjecture itself.

## Plausible routes

None is currently credible for the binary form. The realistic near-term targets are: pushing the exceptional-set exponent $\delta\to1$; lowering explicit constants; transferring ideas from the bounded-gaps revolution (Zhang/Maynard/Tao) and from additive-combinatorics transference principles to additive prime problems. A resolution likely awaits a structural insight beyond the circle method and sieve theory rather than incremental sharpening.

## Related problems

- [Twin Prime Conjecture](../twin-prime-conjecture/README.md) — the multiplicative-additive dual; shares the parity barrier and Hardy–Littlewood heuristics.
- [Riemann Hypothesis](../riemann-hypothesis/README.md) — its generalization controls the major arcs and exceptional-set bounds.
- [Polignac Conjecture](../polignac-conjecture/README.md) — every even number as a prime gap; same circle of sieve methods.
- [Hardy–Littlewood k-tuple Conjecture](../hardy-littlewood-k-tuple/README.md) — the general quantitative framework predicting Goldbach's singular series.
- [Legendre Conjecture](../legendre-conjecture/README.md) — a sibling additive-distributional question about primes in short intervals.
