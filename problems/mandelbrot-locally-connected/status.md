# Status & Frontier — The MLC Conjecture (Mandelbrot Locally Connected)

_Where the problem stands and what a resolution would require._

**Status: open, with active progress.** MLC is unproven in full generality but established on large, explicitly characterized subsets of parameter space. It is universally believed true.

## What is known (unconditional)

- **Connectivity and the model.** $M$ is compact, connected, and full (Douady–Hubbard, 1982); its complement carries a conformal Riemann map, so MLC is equivalent to that map extending continuously to the boundary — i.e. **every parameter ray lands continuously**.
- **Finitely renormalizable parameters.** $M$ is locally connected at every **non-renormalizable** and **finitely renormalizable** parameter (Yoccoz, 1990), via the puzzle/parapuzzle and principal-nest modulus estimates. The same holds for the corresponding Julia sets.
- **Bounded-type infinitely renormalizable parameters.** Local connectivity holds at infinitely renormalizable parameters of **bounded combinatorial type** with *a priori* bounds (Lyubich, Sullivan, McMullen).
- **Primitive decorations.** Complex bounds, hence MLC, hold for broad classes of **primitive** infinitely renormalizable maps outside the "molecule" (Kahn 2006; Kahn–Lyubich, via the Quasi-Additivity Law and Covering Lemma).
- **Hardness signal.** $\partial M$ has Hausdorff dimension $2$ (Shishikura, 1998), excluding any naive metric-regularity proof.

## What is known (conditional)

The standing reduction is: **uniform *a priori* bounds (uniform lower bounds on moduli of renormalization annuli) at a parameter $\Rightarrow$ rigidity $\Rightarrow$ MLC at that parameter.** Thus MLC for the residual class is *equivalent*, in practice, to establishing such bounds for **all infinitely renormalizable combinatorics**, including the unbounded-satellite ("molecule") regime where bounded geometry is known to fail. MLC also implies — and this is its headline corollary — **density of hyperbolicity in the quadratic family**; the real-line case of that corollary is an unconditional theorem (Lyubich; Graczyk–Świątek, 1997), but it does not control the transverse complex directions.

## What a full resolution requires

A proof of MLC must supply *a priori* bounds **uniformly across the molecule** — the closure of parameters with satellite renormalization of unbounded type (Feigenbaum-like accumulation). Equivalently, it must show that the principal nest shrinks to a point at every infinitely renormalizable parameter, despite the failure of summable moduli and of bounded geometry there. This is the precise and well-localized obstruction.

## Plausible routes

1. **Near-parabolic / Inou–Shishikura renormalization** (Shishikura, Cheraghi, Buff, Chéritat): obtain satellite-regime *a priori* bounds where the linear Yoccoz theory degenerates — the most actively pursued path.
2. **Extending the Quasi-Additivity / Covering-Lemma estimates** (Kahn–Lyubich) to remain uniform up to and on the molecule.
3. **Renormalization-operator rigidity**: prove hyperbolicity/contraction of renormalization on the full infinitely renormalizable locus, closing the parameter-transfer step.

No accepted full proof exists as of the knowledge cutoff; claimed results are assessed on whether their estimates stay uniform as parameters approach the molecule.

## Related problems

- [P versus NP](../p-versus-np/README.md) — by way of the broader landscape of central open problems (here only as an Atlas sibling).
- [Riemann Hypothesis](../riemann-hypothesis/README.md) — comparably load-bearing conjecture whose resolution would settle a web of consequences.
- [Collatz Conjecture](../collatz-conjecture/README.md) — another iteration/dynamics problem where orbit behavior resists global control.
- [Birkhoff Conjecture](../birkhoff-conjecture/README.md) — rigidity in a dynamical setting, methodologically adjacent.
- [Weinstein Conjecture](../weinstein-conjecture/README.md) — frontier dynamics conjecture in the same Atlas neighborhood.
