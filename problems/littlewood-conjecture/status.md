# Status & Frontier — The Littlewood Conjecture

_Where the problem stands and what a resolution would require._

## Current status: open (active progress)

The Littlewood conjecture remains **unproven**. It is not a Millennium Prize problem, but it is a touchstone of Diophantine approximation and homogeneous dynamics. The state of knowledge can be summarized in three layers.

### What is known unconditionally

- The conjecture is **trivial unless both $\alpha$ and $\beta$ are badly approximable** (bounded partial quotients). If either has unbounded partial quotients, the corresponding factor $\lVert n\alpha\rVert$ is small along convergent denominators and the product tends to $0$.
- It holds for **explicit structured pairs**: when $1,\alpha,\beta$ are $\mathbb{Q}$-linearly dependent, for many pairs tied to cubic fields (Cassels–Swinnerton-Dyer), and similar special families.
- **Strongest unconditional result (Einsiedler–Katok–Lindenstrauss, 2006):** the set of exceptions has **Hausdorff dimension $0$**. Thus *almost every* pair (indeed all but a dimension-zero set) satisfies the conjecture. This used measure rigidity for the diagonal $A$-action on $\mathrm{SL}_3(\mathbb{R})/\mathrm{SL}_3(\mathbb{Z})$ and is the work cited in Lindenstrauss's 2010 Fields Medal. Reference: Einsiedler, Katok, Lindenstrauss, *Annals of Mathematics* **164** (2006), 513–560.

### What is known conditionally

- Under Margulis's conjectured **rigidity of bounded diagonal orbits** (no bounded $A$-orbit of the exceptional type exists), the conjecture follows immediately.
- Under suitable **positive-entropy hypotheses** on putative invariant measures, EKL-type arguments already exclude counterexamples; the conditional gap is precisely the zero-entropy case.

### What a full resolution requires

A proof must dispose of the **dimension-zero exceptional set** that EKL cannot reach. Concretely, one must exclude a hypothetical bounded $A$-orbit in $X_3$ whose only invariant measures have **zero entropy** — the regime where measure-rigidity machinery currently has no leverage. Two broad routes are considered plausible:

1. **A stronger rigidity / equidistribution theorem** removing the positive-entropy hypothesis, i.e. classifying *all* bounded diagonal orbits (not just those of positive entropy), possibly via effective equidistribution and effective measure-rigidity techniques now under active development.
2. **A new arithmetic/analytic input** special to the real homogeneous setting — necessarily *not* a soft general principle, since several mixed, inhomogeneous, and $p$-adic analogues are now known to be **false** (Shapira and others), proving that any valid argument must exploit a feature unique to the original problem.

The honest assessment: the conjecture is "true for all practical purposes" (only a dimension-zero set could fail), yet a complete proof appears to need genuinely new ideas about zero-entropy diagonal dynamics. No claimed elementary proof has survived expert scrutiny.

## Related problems

- [Hardy–Littlewood $k$-tuple Conjecture](../hardy-littlewood-k-tuple/README.md) — another Littlewood-associated conjecture, in prime distribution rather than approximation.
- [Schanuel's Conjecture](../schanuel-conjecture/README.md) — a deep transcendence conjecture interacting with Diophantine structure of real numbers.
- [abc Conjecture](../abc-conjecture/README.md) — a central Diophantine conjecture constraining integer/rational arithmetic.
- [Riemann Hypothesis](../riemann-hypothesis/README.md) — the flagship analytic-number-theory problem whose techniques and ethos overlap the Hardy–Littlewood school.
