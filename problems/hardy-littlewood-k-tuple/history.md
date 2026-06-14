# History — The Hardy–Littlewood k-tuple Conjecture

_Origin, formulation, and timeline._

The $k$-tuple conjecture grew out of the most ambitious paper of the early twentieth-century theory of primes: G. H. Hardy and J. E. Littlewood's 1923 memoir *"Some problems of 'Partitio numerorum'; III: On the expression of a number as a sum of primes."* Working in the framework they had just built with their **circle method** (developed jointly with Ramanujan for partitions and additive problems), Hardy and Littlewood produced heuristic asymptotic formulas — and a whole hierarchy of conjectures — for the number of representations of integers by sums of primes and for the frequency of prime patterns. The $k$-tuple conjecture (their "Conjecture B," more precisely the general pattern underlying it) emerges from applying the singular-series heuristic of the circle method to the simplest possible additive question: how often a fixed tuple of linear forms is *simultaneously* prime.

**Precise formulation.** Fix distinct integers $\mathcal{H}=\{h_1,\dots,h_k\}$. The set is **admissible** if for every prime $p$ the residues $h_i \bmod p$ do not cover all of $\mathbb{Z}/p\mathbb{Z}$ — i.e. $\mathcal{H}$ does not occupy every congruence class modulo any $p$. (Inadmissibility forces some prime to divide one of $n+h_i$ for all $n$, killing the pattern beyond finitely many cases.) The conjecture asserts that for admissible $\mathcal{H}$,
$$\pi_{\mathcal{H}}(x) := \#\{n \le x : n+h_1,\dots,n+h_k \text{ all prime}\} \sim \mathfrak{S}(\mathcal{H}) \frac{x}{(\log x)^k},$$
where the **singular series** is
$$\mathfrak{S}(\mathcal{H}) = \prod_{p}\left(1-\tfrac{1}{p}\right)^{-k}\left(1-\tfrac{\nu_{\mathcal{H}}(p)}{p}\right),$$
$\nu_{\mathcal{H}}(p)$ being the number of distinct residues of $\mathcal{H}$ modulo $p$. Admissibility is exactly the condition $\mathfrak{S}(\mathcal{H})\neq 0$. The $k=2$, $\mathcal{H}=\{0,2\}$ case is the quantitative twin-prime conjecture; $k=1$ recovers the prime number theorem.

**Reformulations.** The conjecture has equivalent guises: as a special case of the **Bateman–Horn conjecture** (1962) for systems of irreducible polynomials; as a consequence of the **Dickson conjecture** (1904, qualitative) plus the right density; and, for many purposes, as a prediction subsumed by the **Hardy–Littlewood / Schinzel "Hypothesis H"** machinery. The qualitative core — infinitely many admissible $k$-tuples of primes — is itself wide open for every $k\ge 2$.

## Timeline

- **1849** — Polignac conjectures that every even gap occurs infinitely often between consecutive primes, an early qualitative ancestor.
- **1904** — L. E. Dickson formulates the qualitative prime $k$-tuple statement (Dickson's conjecture).
- **1919** — V. Brun introduces the Brun sieve, proving the twin-prime sum $\sum 1/p$ (twins) converges — the first hard quantitative result on prime pairs.
- **1923** — Hardy and Littlewood publish *Partitio Numerorum III*, giving the singular-series asymptotic and posing the $k$-tuple conjecture.
- **1940s–50s** — Selberg develops his sieve; upper bounds of the correct order of magnitude $\pi_{\mathcal{H}}(x) \ll \mathfrak{S}(\mathcal{H}) x/(\log x)^k$ become standard.
- **1962** — Bateman and Horn generalize the asymptotic to arbitrary irreducible polynomial systems, unifying Hardy–Littlewood with Bunyakovsky.
- **1965** — Bombieri–Vinogradov theorem gives primes in arithmetic progressions "on average," a key sieve input.
- **1973** — Chen Jingrun proves every large even number is $p + P_2$ and there are infinitely many primes $p$ with $p+2 = P_2$ — the parity-barrier near-miss for twins.
- **2005** — Goldston, Pintz, Yıldırım (GPY) achieve $\liminf (p_{n+1}-p_n)/\log p_n = 0$, conditionally tying small gaps to the conjecture.
- **2013** — Yitang Zhang proves bounded gaps: infinitely many primes within $7\times 10^7$.
- **2013–14** — Maynard and (independently) Tao introduce the multidimensional GPY sieve, lowering bounds and proving infinitely many $m$-tuples in admissible sets near correct width; the Polymath8 project drives the gap below 246.
- **Present** — The full asymptotic remains unproven for every $k\ge 2$; only upper bounds, the bounded-gaps qualitative shadow, and conditional results are known.
