# History — The Twin Prime Conjecture

_Origin, formulation, and timeline._

## How the problem arose

The twin prime conjecture asserts that there are infinitely many primes $p$ for which $p+2$ is also prime — pairs such as $(3,5)$, $(5,7)$, $(11,13)$, $(17,19)$, $(29,31)$. Its roots reach back to Greek antiquity. Euclid's *Elements* (c. 300 BCE) proved the infinitude of primes, and although Euclid never recorded the twin question explicitly, the problem is its natural and ancient sibling: once one knows primes never stop, one asks whether primes that are *as close together as possible* never stop. For primes larger than $2$, the minimal possible gap is $2$, so twin primes are the tightest admissible pairs.

The first crisp modern formulation is attributed to **Alphonse de Polignac**, who in **1849** stated the broad conjecture that for every even number $2k$ there are infinitely many pairs of consecutive primes differing by exactly $2k$. The twin prime conjecture is precisely the case $k=1$ of **Polignac's conjecture**. De Polignac framed it within a search for regularities among prime gaps; the special case had certainly been contemplated earlier in the folklore of number theory, but 1849 is the conventional date of record.

The decisive **quantitative reformulation** came from **G. H. Hardy and J. E. Littlewood** in their 1923 memoir *Partitio Numerorum III*. Their circle-method heuristic predicts not merely infinitude but a precise density: the number $\pi_2(x)$ of twin primes up to $x$ should satisfy
$$\pi_2(x) \sim 2\,C_2 \int_2^x \frac{dt}{(\ln t)^2}, \qquad C_2 = \prod_{p>2}\frac{p(p-2)}{(p-1)^2} \approx 0.6601618.$$
This *first Hardy–Littlewood conjecture* upgraded a yes/no question into a sharp asymptotic, and $C_2$ is now called the twin prime constant. The conjecture is also a special case of the more general **Hardy–Littlewood $k$-tuple conjecture** and is bound up with the admissibility of prime constellations.

## Timeline

- **c. 300 BCE** — Euclid proves the infinitude of primes; the twin question is its informal antecedent.
- **1849** — Alphonse de Polignac states the general conjecture on prime gaps $2k$; the case $k=1$ is the twin prime conjecture.
- **1915–1919** — Viggo Brun introduces his sieve and proves that $\sum 1/p$ summed over twin primes converges (**Brun's constant** $B_2 \approx 1.902$), showing twins are sparse even if infinite.
- **1919–1920** — Brun's sieve yields the first non-trivial upper bound: the number of twin primes up to $x$ is $O\!\big(x/(\ln x)^2\big)$.
- **1923** — Hardy and Littlewood publish *Partitio Numerorum III*, giving the conjectural asymptotic and the constant $C_2$.
- **1940** — Erdős shows $\liminf_n (p_{n+1}-p_n)/\ln p_n < 1$, opening the small-gaps program.
- **1947–1950** — Atle Selberg develops his sieve, sharpening upper-bound technology for twins.
- **1973** — Chen Jingrun publishes the full proof that there are infinitely many primes $p$ with $p+2$ a product of at most two primes (a **$P_2$** "almost-twin").
- **1986** — Bombieri, Friedlander, and Iwaniec extend Bombieri–Vinogradov-type distribution results, foundational for later breakthroughs.
- **2005–2009** — Goldston, Pintz, and Yıldırım (GPY) prove $\liminf_n (p_{n+1}-p_n)/\ln p_n = 0$, a watershed in small gaps.
- **2013 (April)** — Yitang Zhang proves the first finite bound: $\liminf_n (p_{n+1}-p_n) < 7\times 10^7$.
- **2013 (autumn)** — The Polymath8a project, refining Zhang's method, lowers the bound to $4680$.
- **2013–2014** — James Maynard and (independently) Terence Tao introduce a multidimensional GPY sieve, proving bounded gaps for any fixed number of primes.
- **2014** — Polymath8b, combining Maynard's sieve with Zhang-type estimates, drives the gap bound to **246** (and to $6$ under the generalized Elliott–Halberstam conjecture).
- **Present** — Unconditionally, infinitely many prime pairs differ by at most $246$; the gap $2$ remains out of reach. The **parity barrier** of sieve theory obstructs the final step to genuine twins.
