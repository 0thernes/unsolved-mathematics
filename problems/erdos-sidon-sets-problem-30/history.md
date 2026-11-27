# History — The Erdős–Turán Sidon Set Conjecture (Erdős Problem 30)

_Origin, formulation, and timeline._

A subset $A \subseteq \{1, 2, \dots, N\}$ is a **Sidon set** (or $B_2$-sequence) if all pairwise sums $a + b$ ($a, b \in A$, $a \le b$) are distinct. Let $h(N)$ denote the maximum cardinality of a Sidon set in $\{1, \dots, N\}$. Using James Singer's 1938 construction of perfect difference sets from finite projective planes $\mathrm{PG}(2, q)$, one immediately obtains $h(N) \ge (1 - o(1)) \sqrt{N}$ (more sharply, $\sqrt{N} - O(N^{0.2625})$ via prime-gap estimates).

In 1941, Paul Erdős and Pál Turán proved the upper bound $h(N) \le \sqrt{N} + O(N^{1/4})$ by counting differences inside sliding sub-intervals. Remarkably, the exponent $1/4$ in the error term $N^{1/4}$ has **never been improved** in 85 years! Erdős offered a **\$1,000** prize (**Erdős Problem #30**) simply to prove $h(N) = \sqrt{N} + O_\varepsilon(N^\varepsilon)$ for all $\varepsilon > 0$ — or even $h(N) \le \sqrt{N} + O(1)$ in its strongest form.

## Timeline

- **1932** — Simon Sidon asks Erdős for the maximum density of sets with distinct pairwise sums, motivated by lacunary Fourier series.
- **1938** — James Singer constructs modular Sidon sets of size $q+1$ in $\mathbb{Z}/(q^2+q+1)\mathbb{Z}$ for every prime power $q$, giving $h(N) \ge (1-o(1))\sqrt{N}$.
- **1941** — Erdős and Turán prove $h(N) \le \sqrt{N} + O(N^{1/4})$ and conjecture that the error term is $O(1)$ (later offering \$1,000 for $O_\varepsilon(N^\varepsilon)$).
- **1962** — Bose and Chowla generalize Singer's projective construction to affine planes and higher-order $B_h$ sequences.
- **1969** — Bernt Lindström tightens the Erdős–Turán constant to $h(N) \le \sqrt{N} + N^{1/4} + 1$.
- **2010** — Javier Cilleruelo gives a sleek proof recovering $h(N) \le \sqrt{N} + N^{1/4} + 1/2$.
- **2021** — József Balogh, Zoltán Füredi, and Souktik Roy break the half-century leading-constant barrier at $N^{1/4}$, proving $h(N) \le \sqrt{N} + 0.998 N^{1/4}$ (`arXiv:2103.15850`).
- **2023–2025** — Carter, Hunter, and O'Bryant tighten the constant further to $h(N) \le \sqrt{N} + 0.98183 N^{1/4}$, yet the exponent $1/4$ itself remains unbroken.
