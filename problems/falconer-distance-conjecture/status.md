# Status & Frontier — The Falconer Distance Conjecture

**Status: active progress, open in every dimension $d \ge 2$.** The conjecture states that a compact $E \subset \mathbb{R}^d$ with $\dim_H E > d/2$ has a distance set $\Delta(E)$ of positive Lebesgue measure. The sharp threshold $d/2$ has not been reached unconditionally in any dimension. What has happened over four decades is a steady compression of the gap between Falconer's 1985 sufficient threshold $(d+1)/2$ and his conjectured $d/2$.

**What is known (unconditional).**
- **$d = 2$:** Guth–Iosevich–Ou–Wang (2018) proved that $\dim_H E > 5/4$ implies $|\Delta(E)| > 0$, improving Wolff's long-standing $4/3$ (1999) and Bourgain-era bounds. The conjectured threshold is $1$, so a quarter of a dimension remains.
- **High dimensions:** the Du–Iosevich–Ou–Wang–Zhang and Du–Zhang program established thresholds of the form $d/2 + 1/4$ for the positive-measure statement, using weighted restriction estimates and sharp Schrödinger-maximal bounds — the best known in general $d$. There are slightly different constants for even versus odd dimensions in parts of this literature.
- **Necessity:** Falconer's dimension-$d/2$ examples show $d/2$ cannot be lowered, so the conjecture, if true, is sharp.
- **Refinements:** pinned-distance results (some point $x$ with $|\Delta_x(E)| > 0$) and dimension-of-distance-set results ($\dim_H \Delta(E)$ lower bounds) have advanced in parallel, in some regimes matching or nearly matching the measure thresholds.

**What is known (conditional).** The full conjecture follows in various ranges from the sharp restriction conjecture or from optimal Kakeya-type maximal estimates, but even granting restriction, the standard reductions do not always deliver $d/2$ outside the plane. This signals that Falconer may be strictly harder than restriction in high dimensions, or that a fundamentally different reduction is needed.

**What a full resolution would require.** A proof of the sharp $d/2$ threshold must extract more than the second-moment (spherical $L^2$-average) information at the heart of the Mattila integral, since that integral is known to be insufficient at the critical exponent for extremal Salem-type measures. Plausible routes: (i) optimal weighted restriction/decoupling estimates pushed to the endpoint, likely entangled with progress on the **Kakeya conjecture**; (ii) sharp radial-projection theorems robust in high dimensions; (iii) genuinely multilinear or incidence-geometric arguments in the spirit of the polynomial method that resolved Erdős distinct distances. Most experts expect the last increment to demand a new idea rather than a refinement of current estimates.

**Plausible near-term frontier.** Continued shaving of constants in the plane (toward $1$) and in high dimensions (toward $d/2$) via improved decoupling and radial-projection inputs; sharper pinned and dimension-of-distance-set theorems; and clarification of the precise logical relationship between Falconer, restriction, and Kakeya. A complete unconditional proof of the sharp threshold is not expected imminently.

## Related problems

- [Kakeya Conjecture](../kakeya-conjecture/README.md) — the Besicovitch/Kakeya tube-overlap problem that underlies the restriction estimates feeding Falconer.
- [Unit Distance Problem](../unit-distance-problem/README.md) — Erdős's incidence-geometry sibling counting repeated distances among finite point sets.
- [Hadwiger–Nelson Problem](../hadwiger-nelson-problem/README.md) — chromatic number of the plane under unit-distance constraints, another distance-driven combinatorial-geometric question.
- [Moving Sofa Problem](../moving-sofa-problem/README.md) — a fellow extremal problem in continuous geometry where sharp constants resist proof.
