# History — Montgomery's Pair Correlation Conjecture

_Origin, formulation, and timeline._

The conjecture grew out of Hugh Montgomery's doctoral and early postdoctoral work on the distribution of the non-trivial zeros of the Riemann zeta function $\zeta(s)$. Writing the zeros (under the Riemann Hypothesis) as $\tfrac12 + i\gamma$, Montgomery studied the statistics of the differences $\gamma - \gamma'$ between ordinates after normalizing them to have unit mean spacing near height $T$, where the local density of zeros is $\tfrac{1}{2\pi}\log\tfrac{T}{2\pi}$.

**Precise formulation.** Montgomery introduced the function
$$F(\alpha, T) = \left(\frac{T}{2\pi}\log T\right)^{-1} \sum_{0 < \gamma,\gamma' \le T} T^{i\alpha(\gamma-\gamma')} \, w(\gamma-\gamma'),\quad w(u)=\frac{4}{4+u^2}.$$
Assuming RH, he proved that $F(\alpha) \sim |\alpha|$ for $|\alpha| < 1$ and $F(\alpha)\to 1$ as $\alpha$ grows, but the behavior for $|\alpha|\ge 1$ was conjectural. His **Strong Pair Correlation Conjecture** asserts $F(\alpha,T)\to 1$ uniformly for $1 \le |\alpha| \le A$ for any fixed $A$. Fourier transforming this yields the asymptotic
$$\frac{1}{N(T)}\#\Big\{(\gamma,\gamma'): 0<\gamma,\gamma'\le T,\ \tfrac{2\pi a}{\log T}\le \gamma-\gamma' \le \tfrac{2\pi b}{\log T}\Big\} \to \int_a^b\!\Big(1-\Big(\frac{\sin\pi u}{\pi u}\Big)^2\Big)\,du.$$
The kernel $1-\big(\tfrac{\sin\pi u}{\pi u}\big)^2$ is precisely the **pair correlation density of the Gaussian Unitary Ensemble (GUE)** of random matrix theory — the eigenvalue statistics of large random Hermitian matrices.

**The Dyson connection.** The link to random matrices was not in Montgomery's original derivation; it emerged in a now-legendary 1972 tea-time conversation at the Institute for Advanced Study, where Freeman Dyson recognized Montgomery's form factor $\min(|\alpha|,1)$ and the sine-kernel density as exactly the quantities he and Mehta had computed for GUE. This identification transformed an isolated result on zeta zeros into the founding observation of the "spectral interpretation" program and the Montgomery–Odlyzko law.

**Timeline.**

- **1972** — Montgomery derives $F(\alpha)$ and the pair correlation density under RH; Dyson identifies the GUE connection at Princeton.
- **1973** — Montgomery publishes "The pair correlation of zeros of the zeta function" (Proc. Sympos. Pure Math. 24, AMS), the founding paper.
- **1975** — Hejhal and others begin extending correlation ideas to higher-order statistics and to $L$-functions.
- **1987** — Andrew Odlyzko's large-scale numerical computation of zeros near height $10^{12}$ shows striking agreement with the GUE pair correlation, giving the conjecture overwhelming empirical support (the "Montgomery–Odlyzko law").
- **1994** — Zeev Rudnick and Peter Sarnak prove the $n$-level correlations for zeros of $\zeta$ (and general $L$-functions) match GUE for test functions with restricted support, generalizing Montgomery's result to all correlations.
- **1996** — Nicholas Katz and Peter Sarnak prove function-field analogues unconditionally and articulate the broader symmetry-type philosophy (unitary/symplectic/orthogonal).
- **1999** — Conrey–Ghosh, and later work, connect pair correlation to moments and to the proportion of zeros on the critical line.
- **2000s** — Bogomolny–Keating, Conrey–Snaith and others derive lower-order terms via the ratios conjecture / CUE moments, refining the leading GUE prediction with arithmetic corrections.
- **2013** — Odlyzko extends numerics to zeros near $10^{22}$; agreement persists to extraordinary precision.
- **2010s–present** — The conjecture remains open for $|\alpha|\ge 1$ unconditionally; effort focuses on extending the support of $F(\alpha)$, conditional consequences (gaps, simplicity of zeros), and the broader Katz–Sarnak/RMT framework.
