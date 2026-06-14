# Status & Frontier — The Birch and Swinnerton-Dyer Conjecture

_Where the problem stands and what a resolution would require._

**Status: open.** BSD is one of the seven Clay Millennium Prize Problems and remains unsolved in general. It is a theorem only in low analytic rank, and even the refined (strong) form is established only prime-by-prime there.

**What is known (unconditional).**
- *Analytic rank $0$:* If $L(E,1)\ne 0$ then $E(\mathbb{Q})$ has rank $0$ and $\Sha(E)$ is finite (Kolyvagin, building on Gross–Zagier; valid for all $E/\mathbb{Q}$ via modularity).
- *Analytic rank $1$:* If $\mathrm{ord}_{s=1}L(E,s)=1$ then the algebraic rank is $1$ and $\Sha(E)$ is finite (Gross–Zagier supplies a non-torsion Heegner point; Kolyvagin bounds the Selmer group).
- *Statistical:* The average rank of elliptic curves over $\mathbb{Q}$ is bounded (Bhargava–Shankar), and BSD holds for a **positive proportion** (over $66\%$) of all curves ordered by height (Bhargava–Skinner–Zhang).
- *Refined formula:* For many curves of analytic rank $\le 1$, the $p$-part of the exact leading-coefficient formula is verified for individual primes $p$ via the Iwasawa Main Conjecture (Skinner–Urban, Kato, Rubin in the CM case).

**What is known (conditional).** Granting finiteness of $\Sha$, descent algorithms compute the rank in practice and the BSD formula has been numerically confirmed for vast tables (Cremona, LMFDB) with no counterexample. Granting the relevant Iwasawa main conjectures and $p$-adic comparison results, the strong form follows in additional cases. The parity conjecture (that the analytic and algebraic ranks have the same parity) is known in considerable generality.

**What a full resolution requires.**
1. **Rank $\ge 2$, weak form.** No method produces two independent rational points from the vanishing $L^{(2)}(E,1)\ne 0$. A resolution needs either a *higher Euler system* controlling Selmer groups in higher rank, or a *higher Gross–Zagier formula* expressing $L^{(r)}(E,1)$ as a regulator of $r$ independent cohomological/cycle classes that are provably rational and independent.
2. **Finiteness of $\Sha$ in general.** Unproven for rank $\ge 2$; without it there is no terminating rank algorithm. This is arguably the deepest sub-problem.
3. **Strong form for all primes simultaneously.** Even in rank $\le 1$, the exact leading coefficient is verified prime-by-prime; assembling all primes (including bad-reduction and exceptional-zero cases) into the full rational identity remains incomplete.

**Plausible routes.** (a) Anticyclotomic Iwasawa theory and **Darmon / Stark–Heegner points** extended beyond rank $1$; (b) the **Gan–Gross–Prasad / arithmetic theta** circle and generalized Gross–Zagier (Yuan–Zhang–Zhang, Disegni) pushing height formulas to higher-dimensional cycles; (c) advances in the geometry of numbers raising the proven proportion toward $100\%$ while never settling individual high-rank curves; (d) entirely new input from the Langlands programme or motivic cohomology (Beilinson–Bloch–Kato), of which BSD is the genus-1 case. None is near completion; the rank-$\ge 2$ barrier is regarded as requiring a fundamentally new idea.

## Related problems

- [Riemann Hypothesis](../riemann-hypothesis/README.md) — both concern special values and zeros of $L$/zeta functions; BSD is the prototypical "special value at $s=1$" statement.
- [Hodge Conjecture](../hodge-conjecture/README.md) — sibling Millennium problem in arithmetic/algebraic geometry; both relate algebraic cycles to cohomological/analytic data.
- [Hardy–Littlewood k-tuple Conjecture](../hardy-littlewood-k-tuple/README.md) — like BSD, born from heuristic/numerical reasoning about local-to-global densities (here Euler products of $N_p/p$).
- [abc Conjecture](../abc-conjecture/README.md) — neighbouring problem in Diophantine arithmetic with strong consequences for rational points and heights on curves.
