# History — Lehmer's Mahler Measure Conjecture

_Origin, formulation, and timeline._

Lehmer's conjecture arose not as an abstract question about heights but as a by-product of a concrete computational search for large primes. In 1933, Derrick Henry Lehmer, working in the tradition of factoring and primality testing, studied sequences of the form $\Delta_n = \prod_i (\alpha_i^n - 1)$, where the $\alpha_i$ are the roots of a fixed monic integer polynomial. Such sequences generalize the Pierce numbers and the Lucas–Lehmer machinery; Lehmer hoped to produce large primes by choosing polynomials whose associated products grew slowly, so that the ratios $\Delta_{n+1}/\Delta_n$ stayed small. The growth rate of $\Delta_n$ is governed precisely by the **Mahler measure**

$$M(P) = |a_d| \prod_{i=1}^{d} \max(1, |\alpha_i|),$$

the product of $|a_d|$ (the leading coefficient) and the moduli of those roots lying outside the unit circle. For a monic integer polynomial, $M(P) = 1$ exactly when $P$ is a product of cyclotomic polynomials and a power of $x$ — by Kronecker's 1857 theorem, all of whose roots are roots of unity. Lehmer asked whether non-cyclotomic polynomials could have measure arbitrarily close to $1$.

He found no example with measure strictly between $1$ and the largest root of his now-famous degree-$10$ polynomial

$$L(x) = x^{10}+x^9-x^7-x^6-x^5-x^4-x^3+x+1,$$

whose largest root is **Lehmer's number** $\lambda_0 = 1.17628081\ldots$, a Salem number. **Lehmer's conjecture** (in its modern phrasing) asserts that there is an absolute constant $c>1$ such that $M(P) \ge c$ for every non-cyclotomic integer polynomial $P$ — equivalently, that $\inf\{M(P) : M(P)>1\}$ is bounded away from $1$, with $\lambda_0$ the conjectured minimum. Lehmer himself stated the question cautiously and never claimed a conjecture; the strong form (that $\lambda_0$ is optimal) is folklore attribution.

The problem admits several equivalent reformulations. In terms of the **logarithmic Weil height** $h(\alpha) = \log M(P_\alpha)/\deg(\alpha)$, the conjecture says $h(\alpha) \ge c'/\deg(\alpha)$ for non-torsion algebraic numbers — a uniform lower bound on heights, and the toral ($\mathbb{G}_m$) case of a family of "Lehmer-type" problems (including the elliptic Lehmer problem of Laurent). Boyd recast the measure analytically and tied small measures to **Salem numbers**.

## Timeline

- **1857** — Kronecker proves that an algebraic integer all of whose conjugates lie in the closed unit disk is either zero or a root of unity, giving $M(P)=1 \iff P$ cyclotomic.
- **1933** — D. H. Lehmer publishes "Factorization of certain cyclotomic functions" (Ann. of Math.), exhibits $L(x)$ and $\lambda_0=1.176\ldots$, and poses the question.
- **1962–1964** — Salem develops the theory of Salem and Pisot numbers, clarifying the structure governing small measures.
- **1971** — Blanksby and Montgomery prove the first explicit unconditional bound: $M(\alpha) \ge 1 + 1/(52\,d\log 6d)$ for $\alpha$ of degree $d$.
- **1971** — Smyth proves Lehmer's conjecture for **non-reciprocal** polynomials: any such $\alpha$ has $M(\alpha) \ge \theta_0 = 1.32472\ldots$, the smallest Pisot number (plastic number).
- **1978–1980** — Boyd publishes systematic surveys and computational searches; "Reciprocal polynomials having small measure" (Math. Comp.) reinforces $\lambda_0$ as the conjectural minimum and links the problem to Salem numbers.
- **1979** — Dobrowolski's landmark bound: $M(\alpha) \ge 1 + (1-\varepsilon)(\log\log d/\log d)^3$, the best general unconditional result, essentially unimproved in form to this day.
- **1981** — Cantor–Straus and Louboutin give simplified proofs and refine the constant in Dobrowolski's inequality.
- **1996** — Amoroso–David prove a Dobrowolski-type lower bound for the height on $\mathbb{G}_m^n$ (the generalized Lehmer problem in higher dimension).
- **1999** — Borwein, Dobrowolski, and Mossinghoff prove Lehmer's conjecture for polynomials with all odd coefficients.
- **2000** — Amoroso–Dvornicich prove the conjecture for algebraic numbers lying in an abelian extension of $\mathbb{Q}$ (uniform $c$, independent of degree).
- **2004–2005** — Mossinghoff, Rhin, and collaborators push exhaustive searches to degree $\ge 40$; no measure in $(1,\lambda_0)$ is found.
- **2010s** — Connections to the metric Mahler measure (Dubickas, Fili, Samuels), to arithmetic dynamics, and to equidistribution deepen; the problem remains open with $\lambda_0$ untouched as a candidate minimum.
- **2020s** — Continued exhaustive verification and relative/equidistribution methods refine partial results, but the asymptotic shape of Dobrowolski's bound is still unbeaten and $\lambda_0$ stands as the smallest known measure exceeding $1$.
