# History — Erdős Problem 142 (Asymptotic Density of $k$-AP-Free Sets)

_Origin, formulation, and timeline._

For integers $k \ge 3$ and $N \ge 1$, let $r_k(N)$ denote the maximum cardinality of a subset $A \subseteq \{1, 2, \dots, N\}$ containing no non-trivial $k$-term arithmetic progression ($a, a+d, \dots, a+(k-1)d$ with $d > 0$). In 1936, Paul Erdős and Pál Turán conjectured that $r_k(N) = o(N)$ for every fixed $k \ge 3$. Klaus Roth proved the $k=3$ case in 1953 via the circle method, Endre Szemerédi proved $k=4$ in 1969, and Szemerédi settled all $k \ge 3$ in 1975 through his regularity lemma.

Once qualitative density vanishing was settled, Erdős posed **Problem #142** (carrying his highest open cash prize of **\$10,000**): find a genuine asymptotic formula for $r_k(N)$ — or at least narrow the vast exponential-vs-logarithmic gulf separating lower bounds from upper bounds. Even the weaker target of proving $r_3(N) = o(N / \log N)$ (which implies the $k=3$ case of the \$5,000 Erdős–Turán conjecture on divergent reciprocal sums $\sum_{a \in A} 1/a = \infty$) stood open for 67 years until Bloom and Sisask (2020), followed by the landmark quasi-polynomial breakthrough of Kelley and Meka (2023).

## Timeline

- **1936** — Erdős and Turán formulate the density conjecture $r_k(N) = o(N)$ and introduce the extremal function $r_k(N)$.
- **1946** — Felix Behrend constructs 3-AP-free sets via high-dimensional spheres, proving $r_3(N) \ge N \exp(-c\sqrt{\log N})$ (later generalized by Rankin, 1961, for all $k \ge 3$).
- **1953** — Klaus Roth proves $r_3(N) \ll N / \log\log N$ using Fourier-analytic density increment.
- **1969–1975** — Endre Szemerédi proves $r_4(N) = o(N)$ (1969) and $r_k(N) = o(N)$ for all $k$ (1975), with tower-type bounds.
- **1973–1981** — Erdős elevates the asymptotic determination of $r_k(N)$ to a \$10,000 prize problem (recorded as Erdős Problem #142).
- **2001** — Timothy Gowers introduces higher-order uniformity norms $U^{k-1}$ and proves the first doubly-exponential-type quantitative bound $r_k(N) \ll N / (\log\log N)^{c_k}$.
- **2008** — Ben Green and Terence Tao prove the primes contain arbitrarily long arithmetic progressions via transference, and establish inverse theorems for $U^3$.
- **2020** — Thomas Bloom and Olof Sisask break the logarithmic barrier for $k=3$, proving $r_3(N) \ll N / (\log N)^{1+c}$.
- **2023** — Zander Kelley and Raghu Meka achieve a breakthrough matching Behrend's shape up to the exponent of $\log N$: $r_3(N) \le N \exp(-c (\log N)^{1/12})$ (refined to $1/9$ by Bloom–Sisask 2023).
- **2024** — James Leng, Ashwin Sah, and Mehtaab Sawhney prove the first quasipolynomial-in-log-log breakthrough for all $k \ge 5$: $r_k(N) \le N \exp(-(\log\log N)^{c_k})$.
