# History — The Dirichlet Divisor Problem

_Origin, formulation, and timeline._

In 1849, Peter Gustav Lejeune Dirichlet proved via his famous hyperbola method that the average order of the divisor function $d(n) = \sum_{m \mid n} 1$ satisfies
$$D(x) = \sum_{n \le x} d(n) = x \log x + (2\gamma - 1) x + \Delta(x), \qquad \Delta(x) = O(x^{1/2}),$$
where $\gamma$ is the Euler–Mascheroni constant. Geometrically, $D(x)$ counts integer lattice points $(a, b) \in \mathbb{Z}_{>0}^2$ under the hyperbola $ab \le x$, making the Dirichlet divisor problem the hyperbolic sibling of Gauss's circle problem ($a^2 + b^2 \le x$).

Over the ensuing 177 years, lowering the upper bound on the error exponent $\theta = \inf\{\alpha : \Delta(x) = O(x^\alpha)\}$ has served as the canonical proving ground for every major advance in exponential-sum estimation — from Voronoi's summation formula (1903) and van der Corput's method (1922) to Bombieri–Iwaniec's discrete Hardy–Littlewood method (1986), Huxley's refinements (2003), and Bourgain–Watt's decoupling/exponential-sum record (2017). Hardy (1916) proved $\theta \ge 1/4$, and the conjecture $\theta = 1/4$ remains completely open.

## Timeline

- **1849** — Dirichlet proves $\Delta(x) = O(x^{1/2})$ via the hyperbola method.
- **1903** — Georgy Voronoi proves $\Delta(x) = O(x^{1/3} \log x)$ and derives his exact Bessel-function summation formula for $\Delta(x)$.
- **1916** — G. H. Hardy proves $\Delta(x) = \Omega(x^{1/4})$ (specifically $\theta \ge 1/4$) and establishes the mean-square asymptotic $\int_1^X \Delta(x)^2\,dx \sim C X^{3/2}$, strongly pointing to $\theta = 1/4$.
- **1922–1950** — van der Corput ($33/100$, then $27/82$) and Titchmarsh / Chih / Richert push $\theta$ below $1/3$ via Weyl–van der Corput differencing.
- **1969** — Kolesnik achieves $\theta \le 12/37 \approx 0.3243$, later $35/108$ (1982).
- **1988** — Iwaniec and Mozzochi adapt the Bombieri–Iwaniec method to break $7/22 \approx 0.3182$.
- **2003** — Martin Huxley proves $\theta \le 131/416 \approx 0.31490$.
- **2017** — Jean Bourgain and Nigel Watt prove $\theta \le 517/1648 \approx 0.31371$ (`arXiv:1709.04340`), the current world record.
- **2024–2026** — Sharp new $\Omega$-results via the resonance method (Soundararajan 2003; Lamzouri 2026; Mahatab 2026) and generalized divisor refinements (Bellotti–Yang 2024).
