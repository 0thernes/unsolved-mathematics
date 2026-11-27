# Status & Frontier — Resolution of Singularities in Positive Characteristic

_Where the problem stands and what a resolution would require._

**Overall status: `active-progress` (OPEN for all dimensions $d \ge 4$ over fields of characteristic $p > 0$).**

## What is known

- **Dimension $d \le 2$:** Resolved in all characteristics (Abhyankar 1956; Lipman 1978 for arbitrary excellent 2D schemes).
- **Dimension $d = 3$:** Resolved in all characteristics (Cossart–Piltant 2008/2009 `10.1016/j.jalgebra.2008.11.030`, and excellent arithmetical threefolds 2019).
- **Dimension $d \ge 4$, char $p > 0$:** Completely **OPEN** for birational resolution; only smooth alterations (de Jong 1996, Gabber) are known unconditionally.
- **Formal tracking:** Formalized in Lean 4 in `google-deepmind/formal-conjectures` as `AlgebraicGeometry.resolution_of_singularities` (`kind: open`).

## What a resolution requires

A genuinely characteristic-free induction invariant (or local uniformization + patching theorem) immune to wild $p$-ramification, failure of maximal contact, and Hauser's kangaroo invariant-jump obstructions in dimension $\ge 4$.

## Related problems

- [The Hodge Conjecture](../hodge-conjecture/README.md)
- [The Tate Conjecture](../tate-conjecture/README.md)
- [The Zariski Cancellation Problem](../zariski-cancellation-problem/README.md)
