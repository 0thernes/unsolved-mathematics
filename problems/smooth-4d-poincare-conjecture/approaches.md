# Approaches — The Smooth 4-Dimensional Poincaré Conjecture

_Major strategies, partial results, and barriers._

SPC4 sits at a peculiar methodological impasse: the techniques that *prove* Poincaré in every other dimension (the $h$-cobordism theorem, Ricci flow) are unavailable in the smooth 4-dimensional category, while the techniques that *detect* exotic 4-manifolds (gauge theory) systematically fail to see homotopy 4-spheres. The major lines of attack fall into two camps — constructing a counterexample (an exotic $S^4$) and proving none exists — with most modern energy on the first.

## Gauge theory and Floer-type invariants

**Core idea.** Donaldson and Seiberg–Witten invariants distinguish smooth structures on closed 4-manifolds by counting solutions to elliptic PDEs (anti-self-dual or monopole equations) on instanton/monopole moduli spaces.

**Best result.** These invariants have produced a flood of exotic 4-manifolds — exotic $\mathbb{C}P^2 \# k\overline{\mathbb{C}P^2}$, exotic $K3$'s, infinitely many exotic structures on many manifolds with $b_2^+ > 1$.

**Barrier.** This is the central obstruction in the subject: gauge-theoretic invariants *vanish identically* on a homotopy 4-sphere. With $b_2 = 0$ there is no second cohomology to support a basic class; both Donaldson and Seiberg–Witten invariants of any homotopy $S^4$ equal those of $S^4$. The most powerful tools in 4-manifold topology are structurally blind to exactly the manifolds SPC4 concerns. Any successful detection must use an invariant that survives at $b_2 = 0$.

## Khovanov homology and the Rasmussen $s$-invariant

**Core idea.** Rasmussen's $s$-invariant, extracted from Khovanov homology, bounds the smooth slice genus of a knot $K$ and is a *combinatorial* invariant — not a gauge-theoretic one — so it can survive where Donaldson/SW vanish. Freedman–Gompf–Morrison–Walker (2010) proposed using $s$ to certify that a knot is *not* smoothly slice even when it is topologically slice; embedding such a knot appropriately would manufacture an exotic 4-ball or 4-sphere.

**Best result.** Manolescu–Piccirillo (2020) reduced the existence of an exotic $S^4$ (and the related $4$-dimensional Schoenflies setting) to finding a knot, topologically slice in a homotopy 4-ball, with $s(K) \neq 0$. They produced explicit candidate knots; Piccirillo's celebrated resolution of the Conway knot's sliceness (2020) demonstrated the trace-embedding lens that powers the approach.

**Barrier.** Every candidate examined has, on closer inspection, turned out to be smoothly slice (so $s = 0$) or otherwise standard. The method is a *potential* counterexample detector that has not yet caught one, and there is no proof that an $s \neq 0$ topologically-slice knot of the required type exists. Recent work (e.g. on whether $s$ can detect exoticity at all) raises the possibility that $s$ is insufficient.

## Skein lasagna modules and 4-category invariants

**Core idea.** Morrison–Walker–Wedrich's skein-lasagna modules ($\mathfrak{gl}_N$ homology of 4-manifolds) and related categorified invariants aim for genuinely 4-dimensional invariants sensitive at $b_2 = 0$.

**Best result.** Computations (Manolescu–Neithalath, Ren–Willis, and others) have evaluated these invariants on Gluck twists and 2-handlebodies, showing they sometimes distinguish smooth structures relative to boundary.

**Barrier.** Whether they can distinguish a closed homotopy $S^4$ from $S^4$ is unresolved; computations on closed candidates remain extremely difficult, and no exotic detection has been achieved.

## Reducing the candidate pool: Cappell–Shaneson and Gluck twists

**Core idea.** Rather than a general theory, attack specific families. Cappell–Shaneson spheres (from punctured mapping tori) and Gluck twists (re-gluing along a 2-knot) are the two canonical sources of *potential* exotic 4-spheres.

**Best result.** Gompf (1991, 2010) and Akbulut (2009–2010) proved the most prominent infinite families of Cappell–Shaneson spheres are standard. Many Gluck twists are known to be standard (e.g. on ribbon and 0-concordant 2-knots, work of Gluck, Gordon, Sunukjian, and others).

**Barrier.** The reductions are case-by-case and rely on producing explicit handle moves; they do not generalize to all members, and the general Gluck-twist problem (is every Gluck twist on $S^4$ standard?) remains open. Eliminating candidates narrows the search but cannot, by itself, prove SPC4.

## Trisections and combinatorial 4-manifold theory

**Core idea.** Gay–Kirby trisections decompose a 4-manifold into three standard pieces, reducing smooth 4-manifold classification to the combinatorics of trisection diagrams and the (notoriously hard) mapping class group of $\#^k(S^1 \times S^2)$.

**Best result.** A clean combinatorial framework; trisection genus is a new smooth invariant and any homotopy 4-sphere has a trisection.

**Barrier.** The relevant stabilization and Powell-conjecture questions are themselves open and as hard as SPC4; trisections reframe the problem without yet cracking it.

## Why $h$-cobordism and Ricci flow fail

For $n \geq 5$, Smale's smooth $h$-cobordism theorem finishes the job via the Whitney trick. In dimension four the Whitney trick fails smoothly (embedded Whitney disks cannot be found), which is precisely why Freedman needed infinite topological constructions and why no *smooth* $h$-cobordism theorem exists. Perelman's Ricci-flow proof of the 3-dimensional case has no 4-dimensional analogue: 4-dimensional Ricci flow develops uncontrolled singularities and there is no surgery theory adequate to a homotopy 4-sphere. Both master strategies are structurally blocked, leaving the field dependent on the partial, unproven tools above.
