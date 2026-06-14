# Status & Frontier — Lehmer's Mahler Measure Conjecture

_Where the problem stands and what a resolution would require._

**Status: open.** The conjecture — that $\inf\{M(\alpha) : M(\alpha)>1,\ \alpha \text{ algebraic integer}\} \ge c$ for some absolute $c>1$, conjecturally $c = \lambda_0 = 1.17628081\ldots$ (Lehmer's number) — has been open since 1933 and is not resolved as of mid-2026.

**Strongest unconditional results.** The best general lower bound remains **Dobrowolski's (1979)** inequality, in Voutier's clean explicit form: for non-cyclotomic $\alpha$ of degree $d \ge 2$,

$$M(\alpha) \ge 1 + \frac{1}{4}\left(\frac{\log\log d}{\log d}\right)^3.$$

This tends to $1$ as $d \to \infty$, so it does *not* furnish the degree-independent constant the conjecture demands. Complete unconditional resolution exists only for restricted classes: **Smyth (1971)** for non-reciprocal polynomials ($M \ge \theta_0 = 1.3247\ldots$); **Borwein–Dobrowolski–Mossinghoff (1999)** for polynomials with odd coefficients; and various bounded-height or few-term families. The general case reduces to **reciprocal** polynomials, where Salem numbers concentrate.

**Strongest "conditional" / structured results.** Under Galois constraints the full uniform bound is known: **Amoroso–Dvornicich (2000)** proved $h(\alpha) \ge (\log 5)/12$ for non-torsion $\alpha$ in any abelian extension of $\mathbb{Q}$; extensions cover numbers with controlled local degrees (Amoroso–Zannier) and the higher-dimensional toral analogue (Amoroso–David). These are genuine theorems, but they exploit special ramification structure absent in the general reciprocal case.

**A resolved sibling.** The closely related **Schinzel–Zassenhaus conjecture** (a gap above $1$ for the *house*, the largest conjugate modulus) was **proved by Vesselin Dimitrov in 2019** (arXiv:1912.12545, Acta Mathematica), via a Pólya-type integral/metric inequality refined with Habegger. This is a real breakthrough on a neighbouring problem, but bounding the house is strictly weaker than bounding the measure, and the method has **not** transferred to Lehmer's conjecture, which remains open.

**What a full resolution would require.** One must produce a constant $c>1$ with $M(\alpha) \ge c$ for *every* non-cyclotomic algebraic integer, uniformly in degree — equivalently a lower bound $h(\alpha) \ge c'/\deg(\alpha)$ on the Weil height. The central obstruction is that the auxiliary-polynomial machinery is intrinsically degree-sensitive; defeating it needs an idea that is uniform across degrees. Plausible routes: (i) extending Dimitrov-type metric/equidistribution inequalities from the house to the full measure; (ii) pushing height bounds from abelian/structured fields to arbitrary Galois groups; (iii) a dynamical-systems or arithmetic-equidistribution argument forcing a quantitative gap from the clustering of conjugates (Bilu equidistribution); (iv) new transcendence-theoretic auxiliary constructions. Computationally, exhaustive searches past degree $40$ continue to leave $\lambda_0$ unchallenged as the smallest measure exceeding $1$, lending strong empirical support to the strong form without proving it.

## Related problems

- [Lehmer's Totient Problem](../lehmer-totient-problem/README.md) — Lehmer's other famous open question.
- [Schanuel's Conjecture](../schanuel-conjecture/README.md) — sibling in transcendence and height theory.
- [Four Exponentials Conjecture](../four-exponentials-conjecture/README.md) — related Diophantine/transcendence circle.
- [Littlewood Conjecture](../littlewood-conjecture/README.md) — a Diophantine-approximation companion with similar metric flavour.
- [Artin's Primitive Root Conjecture](../artin-primitive-root-conjecture/README.md) — kindred classical number-theory problem on algebraic structure.
