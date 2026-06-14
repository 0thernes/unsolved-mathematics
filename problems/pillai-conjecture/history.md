# History — Pillai's Conjecture

_Origin, formulation, and timeline._

## Origin and motivation

Pillai's conjecture grew out of the centuries-old study of consecutive perfect powers. The list of perfect powers $1, 4, 8, 9, 16, 25, 27, 32, \dots$ (numbers of the form $x^p$ with $p \ge 2$) thins out as it climbs, and a natural question is how the gaps between successive powers behave. Eugène Charles Catalan in 1844 had conjectured that $8$ and $9$ are the only consecutive perfect powers, i.e. that $x^p - y^q = 1$ has only the solution $3^2 - 2^3 = 1$ in integers $\ge 2$. The Indian mathematician **Subbayya Sivasankaranarayana Pillai** generalized this from the difference $1$ to an arbitrary fixed difference $k$.

In a sequence of papers in the early 1930s, Pillai studied the number of solutions of $a x^p - b y^q = k$. The clean modern statement attached to his name is: **for every fixed integer $k \ge 1$, the equation $x^p - y^q = k$ has only finitely many solutions in integers $x, y, p, q$ with $x, y > 0$ and $p, q \ge 2$.** Equivalently, if one orders the perfect powers $1 < 4 < 8 < 9 < \dots$ as $a_1 < a_2 < \dots$, then the gap $a_{n+1} - a_n \to \infty$. The case $k = 1$ is exactly Catalan's conjecture, so Pillai's conjecture is a strict generalization of Catalan's.

## Reformulations

Several equivalent or closely related phrasings circulate. The "gaps tend to infinity" form is the most geometric. The "finiteness for each $k$" form is the Diophantine statement. A stronger quantitative version, also due in spirit to Pillai, asks for an effective lower bound: $x^p - y^q \gg \max(x^p, y^q)^{\delta}$ for some absolute $\delta > 0$ once the power is large, which would follow from the $abc$ conjecture. The conjecture is intimately tied to the $abc$ conjecture and to bounds on linear forms in logarithms.

## Timeline

- **1844** — Catalan conjectures that $8, 9$ are the only consecutive perfect powers ($k = 1$ case).
- **1931–1936** — Pillai publishes a series of papers on $a x^p - b y^q = k$, proving finiteness of solutions when the exponents $p, q$ are **fixed** and conjecturing finiteness in general; he establishes asymptotics for the count of solutions in fixed-exponent cases.
- **1945** — Pillai dies in an air crash near Cairo en route to the Institute for Advanced Study in Princeton; the conjecture survives him.
- **1976** — Tijdeman proves an effective bound for Catalan's equation $x^p - y^q = 1$, showing solutions are bounded — a major step for the $k=1$ case using Baker's theory of linear forms in logarithms.
- **1982** — Stroeker and Tijdeman survey the problem; the case of fixed $k$ with two consecutive powers receives effective treatment in many subcases.
- **2002–2004** — Preda Mihăilescu proves Catalan's conjecture using the theory of cyclotomic fields (Wieferich pairs, Stickelberger's theorem), settling $k = 1$ completely.
- **2004** — Bennett proves that for fixed $p, q \ge 2$ with the equation $|x^p - y^q| = k$, there are at most a small bounded number of solutions; e.g. $x^n - y^n$-type and many two-fixed-exponent results are made explicit.
- **2006–2018** — Numerical work (Pinch, and later large-scale searches) tabulates "Pillai numbers," differences $k$ achieved by few or many power pairs; the $abc$ conjecture is shown to imply Pillai's conjecture in full.
- **Present** — The general conjecture (variable exponents $p, q$) remains **open**. Only when both exponents are fixed, or for $k = 1$ (Catalan), is finiteness known unconditionally.

The frontier today is the variable-exponent regime: no unconditional proof exists that $x^p - y^q = k$ has finitely many solutions when $p$ and $q$ are allowed to grow, for any single $k \ge 2$.
