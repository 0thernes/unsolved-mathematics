# History — The Bateman–Horn Conjecture

_Origin, formulation, and timeline._

In 1962, Paul T. Bateman and Roger A. Horn unified nearly every classical conjecture on prime values of integer polynomials into a single quantitative asymptotic law. While **Schinzel's Hypothesis H** (1958) predicts qualitatively that any admissible finite family of irreducible polynomials $f_1, \dots, f_k \in \mathbb{Z}[x]$ takes simultaneous prime values infinitely often, Bateman and Horn gave the exact conjectured asymptotic count:
$$Q(f_1, \dots, f_k; x) \sim \frac{C(f_1, \dots, f_k)}{\prod_{i=1}^k \deg f_i} \int_2^x \frac{dt}{(\log t)^k}, \qquad C(f_1, \dots, f_k) = \prod_p \frac{1 - \omega_f(p)/p}{(1 - 1/p)^k},$$
where $\omega_f(p)$ is the number of roots of $f_1 \cdots f_k \equiv 0 \pmod p$.

Bateman–Horn simultaneously subsumes **Dirichlet's theorem on primes in arithmetic progressions** (the *only* case $k=1, \deg f_1 = 1$ proved!), the **Twin Prime Conjecture** ($x, x+2$), **Sophie Germain primes** ($x, 2x+1$), the **Hardy–Littlewood $k$-tuple conjecture** (all linear $f_i$), and **Landau's fourth problem / Bunyakovsky's conjecture** ($x^2 + 1$, and all single higher-degree irreducible polynomials).

## Timeline

- **1837** — Dirichlet proves the sole solved case ($k = 1, \deg f_1 = 1$: primes in arithmetic progressions $an + b$).
- **1857** — Viktor Bunyakovsky states the qualitative conjecture for a single irreducible polynomial of degree $\ge 2$.
- **1923** — Hardy and Littlewood formulate the quantitative $k$-tuple conjecture (all linear $f_i$) and Conjecture F ($ax^2 + bx + c$).
- **1958** — Andrzej Schinzel and Wacław Sierpiński formulate qualitative Hypothesis H for arbitrary admissible polynomial families.
- **1962** — Paul Bateman and Roger Horn publish the unified quantitative asymptotic formula and Euler product in *Mathematics of Computation* (`10.1090/s0025-5718-1962-0148632-7`).
- **1998–2001** — Friedlander–Iwaniec ($a^2 + b^4$) and Heath-Brown ($a^3 + 2b^3$) prove prime asymptotics for sparse *two-variable* polynomials, highlighting how far single-variable degree $\ge 2$ polynomials remain out of reach.
- **2013–2014** — Zhang, Maynard, and Tao prove bounded prime gaps and show that for sufficiently large $k$, at least $m$ out of $k$ linear forms are simultaneously prime infinitely often — still without proving even a single $k=2$ pair or any $\deg \ge 2$ case.
- **2020–2025** — Function-field analogues over $\mathbb{F}_q[t]$ for large fixed $q$ see substantial progress (Entin; Sawin–Shusterman), while the integer case remains completely open beyond $k = 1, \deg = 1$.
