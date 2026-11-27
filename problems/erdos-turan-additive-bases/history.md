# History — The Erdős–Turán Conjecture on Additive Bases

_Origin, formulation, and timeline._

In their landmark 1941 paper *On a Problem of Sidon in Additive Number Theory, and on some Related Problems*, Paul Erdős and Pál Turán asked whether an asymptotic additive basis $A \subseteq \mathbb{N}$ of order 2 can have a uniformly bounded number of representations $r_A(n) = |\{(a,b) \in A^2 : a + b = n\}|$. They conjectured that if $r_A(n) \ge 1$ for all sufficiently large $n$, then necessarily $\limsup_{n \to \infty} r_A(n) = \infty$.

Erdős later offered a **\$500** prize for its resolution (recorded as **Erdős Problem #28**). Despite its elementary one-sentence statement — and despite the fact that the *multiplicative* analogue was proved by Erdős himself in 1964, and the *signed-integer* analogue over $\mathbb{Z}$ is **false** (Nathanson 2003 constructed a basis of $\mathbb{Z}$ with $r_A(n) = 1$ for all $n \in \mathbb{Z}$!) — the natural-number conjecture has resisted every analytic, probabilistic, and combinatorial attack for more than 85 years.

## Timeline

- **1941** — Erdős and Turán publish the conjecture alongside their foundational upper bound on Sidon sets.
- **1956** — Erdős proves via the probabilistic method that there exists an asymptotic basis $A \subseteq \mathbb{N}$ with $c_1 \log n \le r_A(n) \le c_2 \log n$, showing that $\limsup r_A(n)$ can grow as slowly as $\log n$.
- **1964** — Erdős proves the multiplicative analogue: every multiplicative basis of $\mathbb{N}$ has unbounded multiplicative representation function (via Ramsey's theorem on prime-exponent vectors).
- **1985** — Paul Erdős and András Sárközy conjecture the stronger form: even if $A \subseteq \mathbb{N}$ merely satisfies $a_k \ll k^2$ (the density of a basis without requiring full coverage), $r_A(n)$ must still be unbounded.
- **2003** — Grekos, Haddad, Helou, and Pihko prove that any asymptotic basis of order 2 satisfies $\limsup r_A(n) \ge 6$ (and $\ge 8$ for unordered representations under refined analysis; Borwein–Choi–Chu 2006).
- **2003** — Melvyn Nathanson proves that the conjecture **fails over $\mathbb{Z}$**, constructing a subset $A \subseteq \mathbb{Z}$ where every integer has a unique representation $a + b$ with $a \le b$.
- **2025–2026** — Formalized in Lean 4 in `google-deepmind/formal-conjectures` as `Erdos28.erdos_28` (`kind: open`, prize `$500`); conjecture remains completely open.
