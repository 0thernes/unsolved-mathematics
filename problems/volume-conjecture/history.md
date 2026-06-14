# History — The Volume Conjecture

_Origin, formulation, and timeline._

## Origin

The Volume Conjecture sits at the junction of two developments that, for most of the twentieth century, had little to do with each other. On one side stands hyperbolic geometry: Thurston's geometrization program (late 1970s) showed that the complement $S^3 \setminus K$ of a "generic" knot $K$ carries a complete hyperbolic metric of finite volume, and that this volume $\mathrm{Vol}(S^3\setminus K)$ is a topological invariant. On the other side stands quantum topology: the Jones polynomial (1984) and its colored refinements — the colored Jones polynomials $J_N(K;q)$ extracted from the $N$-dimensional irreducible representation of $U_q(\mathfrak{sl}_2)$ — are combinatorial invariants with no manifest geometric meaning.

In the mid-1990s Rinat Kashaev defined, for each $N\ge 2$, a complex-valued knot invariant $\langle K\rangle_N$ built from the quantum dilogarithm (Faddeev–Kashaev). In 1997 he conjectured, on the basis of the examples $4_1$, $5_2$, $6_1$, that for a hyperbolic knot
$$2\pi \lim_{N\to\infty}\frac{\log|\langle K\rangle_N|}{N}=\mathrm{Vol}(S^3\setminus K).$$
The decisive reformulation came in 2001, when Hitoshi Murakami and Jun Murakami proved that Kashaev's invariant equals the colored Jones polynomial evaluated at the root of unity $q=e^{2\pi i/N}$, i.e. $\langle K\rangle_N=J_N(K;e^{2\pi i/N})$ (in the normalization $J_N(\text{unknot})=1$). This identification converted Kashaev's geometric guess into a statement about a mainstream quantum invariant and gave the conjecture its modern form.

## Modern statement

For any knot $K$,
$$2\pi\lim_{N\to\infty}\frac{\log\bigl|J_N(K;e^{2\pi i/N})\bigr|}{N}=\mathrm{Vol}(S^3\setminus K),$$
where $\mathrm{Vol}$ denotes the simplicial (Gromov) volume of the complement: for hyperbolic knots this is the hyperbolic volume, for torus knots it is $0$, and in general it is the sum of volumes of the hyperbolic pieces of the geometric decomposition. Murakami–Murakami's "complexified" version conjectures that the full limit recovers $\mathrm{Vol}+\sqrt{-1}\,\mathrm{CS}$, the complex volume packaging volume and Chern–Simons invariant. Gukov's generalization (2003) embedded this into the asymptotics at $q=e^{2\pi i\hbar}$ for $\hbar$ near rational points, linking it to the $A$-polynomial and the AJ (quantum volume) conjecture.

## Timeline

- **1984** — V. Jones defines the Jones polynomial; colored versions follow from $U_q(\mathfrak{sl}_2)$ representation theory.
- **c. 1977–1982** — Thurston establishes hyperbolic structures on knot complements; hyperbolic volume becomes a knot invariant.
- **1994–1995** — Kashaev introduces the quantum-dilogarithm invariants $\langle K\rangle_N$.
- **1997** — Kashaev states the conjecture relating his invariant's growth to hyperbolic volume (*Letters in Mathematical Physics*).
- **2001** — H. Murakami and J. Murakami identify $\langle K\rangle_N$ with $J_N(K;e^{2\pi i/N})$ and propose the general (colored-Jones) Volume Conjecture.
- **2002** — Murakami–Murakami–Okamoto–Takata–Yokota study the complexified version with Chern–Simons.
- **2003** — Gukov proposes the generalized Volume Conjecture tying asymptotics to the $A$-polynomial.
- **2004** — Kashaev–Tirkkonen prove the conjecture for torus knots (volume $0$).
- **2007** — Garoufalidis–Lê prove the colored Jones is $q$-holonomic, grounding the AJ conjecture.
- **2008** — Ohtsuki–Yokota and others develop saddle-point/state-integral techniques.
- **2011** — Ohtsuki proves the conjecture for the figure-eight knot $4_1$ with full asymptotic expansion (later extended to $5_2$ and other small knots).
- **2015** — Detcherry–Kalfagianni–Yang relate Kashaev-type limits to Turaev–Viro invariants of $3$-manifolds.
- **2018** — Chen–Yang's Turaev–Viro volume conjecture (numerically verified widely) reframes the program for closed and cusped $3$-manifolds.
- **2018–2024** — Ohtsuki, Wong–Yang, Belletti–Detcherry–Kalfagianni–Yang and others extend partial proofs (fundamental shadow links, certain Dehn fillings); the conjecture for general hyperbolic knots remains open.
