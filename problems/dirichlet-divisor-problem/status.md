# Status & Frontier — The Dirichlet Divisor Problem

_Where the problem stands and what a resolution would require._

**Overall status: `active-progress` (OPEN).**

## What is known (through November 2026)

- **Best upper bound:** $\theta \le 517/1648 \approx 0.3137136$ (Bourgain–Watt 2017, `arXiv:1709.04340`).
- **Best lower bound:** $\theta \ge 1/4$ (Hardy 1916), with refined logarithmic $\Omega$-bounds (`10.1112/plms.70230`, `10.1007/s11139-026-01368-8`, 2026).
- **Conjectured truth:** $\theta = 1/4$, supported overwhelmingly by mean-square and limiting-distribution theorems, yet still separated from the best upper bound by $> 0.0637$.
- **Formal tracking:** Formalized in Lean 4 in `google-deepmind/formal-conjectures` as `DirichletDivisorProblem.dirichlet_divisor_problem` (`kind: open`).

## What a resolution requires

Fundamentally new tools for cancellation in oscillatory nonlinear exponential sums $\sum e(2\sqrt{nx})$ that break past both the Bombieri–Iwaniec $3/10$ barrier and current decoupling limits.

## Related problems

- [The Riemann Hypothesis](../riemann-hypothesis/README.md)
- [The Restriction Conjecture](../restriction-conjecture/README.md)
- [The Kakeya Conjecture](../kakeya-conjecture/README.md)
