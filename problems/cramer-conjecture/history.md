# History — Cramér's Conjecture on Prime Gaps

_Origin, formulation, and timeline._

How large can the gap $g_n = p_{n+1} - p_n$ between consecutive prime numbers be? In 1936, Swedish probabilist and statistician Harald Cramér introduced a random model of the primes in which each integer $n \ge 3$ is independently declared "prime" with probability $1/\log n$. By the Borel–Cantelli lemma, the maximal gap in Cramér's random sequence satisfies $\limsup g_n / (\log p_n)^2 = 1$ almost surely, leading Cramér to conjecture that $p_{n+1} - p_n = O((\log p_n)^2)$ (with $\limsup = 1$).

Cramér's conjecture lies vastly beyond the Riemann Hypothesis itself: even assuming RH, Cramér (1920/1936) could only prove $p_{n+1} - p_n = O(\sqrt{p_n} \log p_n)$! Meanwhile, Andrew Granville (1995) showed via Maier's matrix method that the naive Cramér model misses local divisibility by small primes, predicting that the true $\limsup$ should be **at least $2 e^{-\gamma} \approx 1.1229$** rather than $1$. Thus while the quadratic scale $O((\log p_n)^2)$ is universally expected, Cramér's original constant $1$ is widely doubted.

## Timeline

- **1920** — Cramér proves under RH that $p_{n+1} - p_n = O(\sqrt{p_n} \log p_n)$ (and later $\sum_{p_n \le x} (p_{n+1}-p_n)^2 / p_n \ll (\log x)^4$).
- **1936** — Cramér publishes his random model in *Acta Arithmetica* and formulates the $(\log p_n)^2$ conjecture.
- **1938** — Robert Rankin proves lower bounds for large prime gaps of order $(\log x \log\log x \log\log\log\log x) / (\log\log\log x)^2$.
- **1985** — Helmut Maier proves that primes exhibit unexpected irregularities in short intervals of length $(\log x)^A$, revealing subtle defects in Cramér's naive independent model.
- **1995** — Andrew Granville combines Maier's method with Cramér's model to conjecture $\limsup (p_{n+1}-p_n)/(\log p_n)^2 \ge 2 e^{-\gamma} \approx 1.1229$.
- **2001** — Baker, Harman, and Pintz prove the best unconditional upper bound $p_{n+1} - p_n \ll p_n^{0.525}$.
- **2014–2018** — Ford, Green, Konyagin, Maynard, and Tao break Erdős's \$10,000 large-gap barrier (2016 *Annals* / 2018 *JAMS*), proving arbitrarily large constants $c$ in Rankin's formula (still only $\approx \log x \cdot \log\log x$, far below $(\log x)^2$).
- **2018** — Exhaustive computation by Oliveira e Silva / Nicely / Pintz-era projects verifies all maximal prime gaps up to $4 \times 10^{18}$; the largest observed ratio $(p_{n+1}-p_n)/(\log p_n)^2$ remains $< 0.921$ (for $p_n = 1693182318746371$, gap $1132$, ratio $\approx 0.9206$).
