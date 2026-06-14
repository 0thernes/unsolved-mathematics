# Approaches — The MLC Conjecture (Mandelbrot Locally Connected)

_Major strategies, partial results, and barriers._

The dominant philosophy is **rigidity via a priori bounds**: control the geometry of renormalized restrictions of $f_c$ (uniform moduli of annuli, bounded distortion), prove local connectivity of the relevant Julia sets, and transfer this to the parameter plane $M$ through holomorphic-motion / ray-landing arguments. Almost every line of attack is a variant of this transfer principle.

## The Yoccoz puzzle and parapuzzle

**Core idea.** Partition the dynamical plane by external rays landing at preperiodic points and equipotentials into *puzzle pieces*; the nested pieces around the critical point form the **principal nest**. If the moduli of the nesting annuli sum to infinity, the intersection is a point, forcing local connectivity at the critical value, hence (by combinatorial transfer) at the corresponding parameter. The parallel construction in parameter space is the **parapuzzle**.

**Best result.** Yoccoz (1990) proved that the moduli grow for **non-renormalizable** and **finitely renormalizable** quadratics, establishing local connectivity of those Julia sets and of $M$ at all such parameters — and as a corollary, density of hyperbolicity restricted to these parameters. This is the single largest unconditional advance.

**Barrier.** The summability of moduli fails for **infinitely renormalizable** maps: each renormalization level can return geometry of bounded modulus, so the nest need not shrink to a point by this mechanism alone. The puzzle reduces but does not resolve the infinitely renormalizable case.

## Renormalization and complex *a priori* bounds

**Core idea.** Douady–Hubbard's polynomial-like/straightening theory makes renormalization an operator on a space of maps; *complex bounds* (uniform lower bounds on the moduli of fundamental annuli of renormalizations) yield compactness, exponential contraction, and ultimately rigidity, which implies MLC at the parameter.

**Best result.** Sullivan, McMullen, and Lyubich established complex bounds and hyperbolicity of renormalization for **bounded combinatorial type** (e.g. Feigenbaum-type with bounded "returns"). Lyubich proved MLC at infinitely renormalizable parameters of **bounded type with a priori bounds**, and (with Graczyk–Świątek) density of hyperbolicity on the **real** line — the full real analogue of MLC's main consequence.

**Barrier.** For **unbounded** combinatorial type, especially **satellite (parabolic-like) renormalization**, complex bounds were long unavailable; the geometry can degenerate as one passes between satellite copies. This is the principal obstruction to general MLC.

## Quasi-Additivity Law and the Kahn–Lyubich machinery

**Core idea.** Kahn and Lyubich introduced the **Quasi-Additivity Law** and a "Covering Lemma" — quantitative estimates that bound how moduli can degrade under branched coverings — to obtain *a priori* bounds for large classes of **primitive** infinitely renormalizable maps with controlled "molecule" combinatorics.

**Best result.** Kahn (2006) and Kahn–Lyubich proved complex bounds, hence MLC, for **decorated/primitive** infinitely renormalizable quadratics outside the molecule, substantially enlarging the unconditional region of $M$ where local connectivity holds.

**Barrier.** The arguments require the renormalizations to stay away from the "molecule" — the closure of parameters with satellite combinatorics of unbounded type. Near the molecule the covering estimates lose uniformity.

## Near-parabolic / Inou–Shishikura renormalization

**Core idea.** Satellite combinatorics are governed by maps near parabolic, with rotation-number combinatorics resembling continued fractions. Inou and Shishikura constructed an invariant class for **near-parabolic renormalization**, giving analytic control where the linear (Yoccoz) theory of high type fails.

**Best result.** Cheraghi, Chéritat, Buff, and Shishikura used this to analyze the geometry of Julia sets and the boundary of $M$ for high-type and satellite rotation numbers (e.g. fine structure, hairiness, dimension results), and to attack *a priori* bounds in regimes inaccessible to puzzle methods.

**Barrier.** Translating dynamical control under near-parabolic renormalization into uniform parameter-plane bounds for *all* satellite types — closing MLC on the molecule — remains incomplete.

## Pinched-disk / lamination model (combinatorial side)

**Core idea.** Thurston's quadratic minor lamination and Douady's pinched-disk construct an *abstract* Mandelbrot set $M_{\mathrm{abs}}$ purely from rational external angles. There is a canonical continuous surjection $M_{\mathrm{abs}} \to M$; **MLC is equivalent to this map being a homeomorphism** (every ray landing, continuously).

**Best result.** The model is rigorously a topological model on the dense set of parameters where landing is known; it correctly predicts all combinatorics and is unconditionally valid wherever MLC is known.

**Barrier.** Establishing injectivity/continuity at infinitely renormalizable angles is precisely MLC — the model reformulates rather than resolves the conjecture.

## Negative and limiting results

There are no disproofs (MLC is widely believed true), but several **hardness signals** exist: (i) the boundary $\partial M$ has **Hausdorff dimension $2$** (Shishikura, 1998), so no naive metric-regularity argument can succeed; (ii) satellite/Feigenbaum geometry shows the renormalization fixed points can be **non-hyperbolic** in the relevant sense, blocking straightforward contraction arguments; and (iii) the failure of bounded geometry for unbounded-type rotation numbers rules out uniform puzzle estimates. These results delimit where the remaining difficulty lives: the **infinitely renormalizable, unbounded satellite ("molecule") parameters**.
