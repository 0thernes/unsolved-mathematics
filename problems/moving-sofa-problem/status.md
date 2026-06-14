# Status & Frontier — The Moving Sofa Problem

_Where the problem stands and what a resolution would require._

**Status: active progress, with a claimed (unverified) resolution.** The official problem — determine the sofa constant $\mu$, the largest area of a rigid planar region that can be maneuvered around a right-angled corner in a unit-width corridor — is, in the strict sense, still open, because the strongest claim of full resolution is a recent preprint not yet accepted by the community.

## What is known (unconditional)

- **Lower bound (best, unbeaten since 1992):** $\mu \ge \mu_G \approx 2.219531669$, realized by **Gerver's sofa**, a shape whose boundary consists of 18 analytic pieces (segments, circular arcs, and arcs of involutes of circles). No larger admissible shape has ever been exhibited.
- **Upper bound (best rigorous, published):** $\mu \le 2.37$, proved by **Yoav Kallus and Dan Romik (2018)** by a computer-assisted analysis bounding the area of the intersection of finitely many corridor placements. This superseded Hammersley's classical $\mu \le 2\sqrt 2 \approx 2.8284$.
- Thus, unconditionally, $2.2195 \le \mu \le 2.37$, and it is widely conjectured that the lower bound is exact: $\mu = \mu_G$.

## The current frontier (conditional / claimed)

In November 2024, **Jineon Baek** posted *Optimality of Gerver's Sofa* (arXiv:2411.19826, identifier needs-verification), claiming a complete proof that $\mu = \mu_G$ — i.e. that Gerver's sofa is the true maximizer. The argument reportedly upgrades the variational/optimization characterization of the optimal boundary into a rigorous matching upper bound. If correct, it closes the six-decade gap and resolves the problem.

Honest characterization: this is a **claimed proof under verification**, not an accepted theorem. It is a long, technical, single-author manuscript settling a famous problem, and such results require independent scrutiny and (typically) peer review before the community treats them as established. There is no recorded refutation or retraction; equally, there is not yet confirmation. Until that process concludes, the dossier records the lower bound $\mu_G$ and the upper bound $2.37$ as the standing *unconditional* facts, with $\mu = \mu_G$ as the conjectured — and now claimed — value.

## What a full resolution requires

A complete, accepted solution must do one of two things:
1. **Confirm $\mu = \mu_G$** by an upper-bound argument matching Gerver's value — exactly what Baek's preprint attempts. This requires showing no admissible shape (smooth or not, symmetric or not) exceeds $\mu_G$, i.e. that Gerver's local/variational optimum is the *global* maximizer over all rigid regions and motions.
2. **Or exhibit a larger shape**, which would refute the long-standing conjecture. This is regarded as unlikely given the stability of Gerver's value across decades of attempts.

## Plausible routes

- **Verification of Baek (2024):** the dominant near-term route — careful checking of the claimed optimality proof by independent experts.
- **Closing the analytic upper-bound gap independently:** strengthening the finite-angle / linear-programming relaxation, or a fresh variational argument bounding area from above by $\mu_G$.
- **Variant-informed structure theory:** leveraging the fully solved ambidextrous sofa (Romik, 2017) and corridor-width generalizations to constrain the structure of any optimizer.

## Related problems

- [Inscribed Square Problem](../inscribed-square-problem/README.md) — another deceptively elementary plane-geometry question about curves and embedded shapes.
- [Kakeya Conjecture](../kakeya-conjecture/README.md) — extremal geometry of regions swept by moving/rotating segments.
- [Hadwiger–Nelson Problem](../hadwiger-nelson-problem/README.md) — a sibling Moser-associated planar problem (the Moser spindle), elementary to state and stubborn to resolve.
- [Unit Distance Problem](../unit-distance-problem/README.md) — combinatorial plane geometry in the same problem-collection lineage (Croft–Falconer–Guy).
