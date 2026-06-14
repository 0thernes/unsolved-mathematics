# History — Schinzel's Hypothesis H

_Origin, formulation, and timeline._

## How the problem arose

Hypothesis H is the natural endpoint of a century-long effort to predict when polynomials in one variable produce prime numbers. The single-polynomial case had already been isolated: in 1854 Viktor Bunyakovsky observed that an irreducible polynomial $f \in \mathbb{Z}[x]$ of degree $\ge 2$ should represent infinitely many primes provided it passes an obvious local test — namely that the set of values $\{f(1), f(2), f(3), \dots\}$ has no common factor greater than $1$ (equivalently, $f$ has no *fixed prime divisor*). The simplest open instance, whether $n^2+1$ is prime infinitely often, dates to this circle of ideas and remains unproven.

In parallel, L. E. Dickson in 1904 conjectured the analogous statement for *several linear* polynomials: a finite collection of forms $a_i n + b_i$ should be simultaneously prime infinitely often, again subject to the local non-obstruction condition. Dickson's conjecture already contains the twin-prime conjecture (take $n$ and $n+2$) and the Sophie Germain prime problem.

Andrzej Schinzel's insight, formalized with Wacław Sierpiński in 1958, was that Bunyakovsky's degree-$\ge 2$ case and Dickson's linear-but-multiple case are two shadows of one principle. **Hypothesis H** states: given irreducible polynomials $f_1, \dots, f_k \in \mathbb{Z}[x]$ with positive leading coefficients, if the product $F = f_1 \cdots f_k$ has no fixed prime divisor (i.e. for every prime $p$ there is an integer $n$ with $p \nmid F(n)$), then there are infinitely many integers $n$ for which $f_1(n), \dots, f_k(n)$ are all prime. The condition "no fixed divisor" is exactly the local obstruction $\prod_p$; Hypothesis H asserts that there is no global obstruction beyond it.

A quantitative refinement followed in 1962, when Paul T. Bateman and Roger A. Horn supplied an asymptotic prediction (the **Bateman–Horn conjecture**) for the *count* of such $n$ up to $x$, generalizing the Hardy–Littlewood prime $k$-tuple conjecture and giving Hypothesis H a precise density form. Hypothesis H is qualitative ("infinitely often"); Bateman–Horn is its asymptotic strengthening.

## Timeline

- **1854** — Viktor Bunyakovsky conjectures that a single irreducible polynomial with no fixed divisor represents infinitely many primes.
- **1904** — L. E. Dickson conjectures the simultaneous-prime statement for finitely many *linear* polynomials (Dickson's conjecture).
- **1923** — G. H. Hardy and J. E. Littlewood, in *Partitio Numerorum III*, give the quantitative $k$-tuple conjecture and the circle-method heuristics underpinning later density predictions.
- **1958** — Andrzej Schinzel and Wacław Sierpiński publish "Sur certaines hypothèses concernant les nombres premiers" (*Acta Arithmetica* 4), stating Hypothesis H and its quantitative companion Hypothesis $H_1$.
- **1962** — Paul Bateman and Roger Horn formulate the asymptotic density conjecture refining Hypothesis H (Bateman–Horn).
- **1965** — Sieve methods mature: the large sieve and Bombieri–Vinogradov theorem (1965) make "almost-prime" approximations to such problems possible.
- **1973** — Chen Jingrun proves that $n$ and $n+2$ are simultaneously prime-and-$P_2$ infinitely often — a landmark partial result toward the twin-prime case of Hypothesis H.
- **1997** — Greg Martin and others tabulate Bateman–Horn constants; computational confirmation of the predicted densities accumulates.
- **2004** — Ben Green and Terence Tao prove the primes contain arbitrarily long arithmetic progressions, settling a structured family of *linear* configurations.
- **2010** — Green, Tao, and Tamar Ziegler establish the Möbius–nilsequences and inverse theorems giving the asymptotics for systems of linear forms of *finite complexity* — Dickson-type problems are solved when no two forms are affinely dependent in a way the method cannot handle, but configurations of complexity involving two forms in one variable (twin primes) lie outside reach.
- **2013** — Yitang Zhang proves bounded gaps between primes; with the Polymath8 project and James Maynard (2013), the gap bound drops, yielding infinitely many bounded prime constellations — the first unconditional simultaneous-prime results for some admissible tuples, though not for any prescribed tuple.
- **2014** — Maynard and Tao's multidimensional sieve gives $m$-tuples of primes in bounded-length intervals for every $m$, a major structural advance on the linear case.
- **2018–present** — Function-field analogues (Sawin–Shusterman and others) prove strong forms of Hypothesis H over $\mathbb{F}_q[t]$ for large $q$, isolating where the difficulty in the integer case truly lies. The integer Hypothesis H remains open in every nonlinear instance and in every fixed twin-type instance.
