# Attempts — The Erdős Unit Distance Problem

_Notable attempts, near-misses, retracted proofs._

## The successive upper bounds (the real progress)

The honest narrative of the problem is a short chain of *upper-bound* improvements that then stalled:

- **Erdős (1946):** $u(n) = O(n^{3/2})$ via the $K_{2,3}$-free incidence graph (Kővári–Sós–Turán). This is the trivial ceiling.
- **Józsa–Szemerédi (1972):** the first improvement, $u(n) = o(n^{3/2})$ — superficially small, but it broke the $3/2$ barrier and signaled that the truth is much smaller.
- **Beck; Spencer–Szemerédi–Trotter (1984):** $u(n) = O(n^{4/3})$. This remains the record more than four decades later. Every subsequent "improvement" has been a constant-factor sharpening or a reproof (notably Székely's 1997 crossing-number argument and Pach–Tardos refinements), **not** a new exponent.

The lower bound side has been even more static: Erdős's grid construction $n^{1+c/\log\log n}$ (1946) has never been improved. So the famous gap — between $n^{1+o(1)}$ and $n^{4/3}$ — is essentially the gap as it stood in 1984.

## Near-misses via the polynomial method

After Guth and Katz's 2010 resolution of the distinct-distances problem, several groups attempted to port polynomial partitioning to the unit-distance count. These produced genuine partial results — sharper bounds for points on a bounded number of lines or circles, for sets of bounded algebraic complexity, and in three dimensions — but the general planar exponent did not move. The consensus, articulated repeatedly by Sheffer, Solymosi, Zahl and others, is that the distinct-distances method counts distinct *values* (and reduces to a rigid-motion incidence problem with a low-degree structure), whereas the unit-distance lattice extremizer has no comparable algebraic backbone to partition. This is a structural near-miss, not a flawed proof.

## Structured-set results (partial, correct)

A productive body of work proves the conjecture *conditionally* or for restricted inputs: points in convex position admit only $O(n\log n)$ unit distances (a clean, tight-up-to-constants result), and points on the integer grid, on few lines, or with small additive doubling satisfy near-linear or otherwise improved bounds. These are correct and important, but they sidestep the worst case rather than resolve it.

## Disputed and erroneous claims

The unit distance problem has, fortunately, not been plagued by high-profile false "solutions" of the kind that surround, say, $P$ vs $NP$. There is **no widely circulated, seriously entertained claimed proof** of either the $n^{1+o(1)}$ upper bound or a matching lower bound that the community treats as a live dispute. Periodic preprints claiming to settle the problem appear on arXiv and elsewhere; none has survived expert scrutiny, and they are generally found either to (i) re-derive the known $O(n^{4/3})$ bound while *claiming* to beat it, (ii) silently assume the extremal set is grid-like, or (iii) misapply incidence bounds past their tightness threshold (which Valtr-type norm constructions show cannot be beaten by general convex-distance arguments). In keeping with house policy, no specific claimed proof is endorsed here; readers should treat any announcement of a resolution as unverified until it passes refereeing by the discrete-geometry community.

## The barrier that frames all attempts

The single most cited reason the problem resists is the **norm barrier**: there exist (non-Euclidean) norms for which the maximum number of unit distances genuinely is $\Theta(n^{4/3})$. Any correct proof of Erdős's conjecture must therefore invoke a property special to the round Euclidean circle — its strict, uniform convexity together with the two-intersection rigidity of congruent circles. Every attempt that uses only combinatorial or topological features common to all "nice" convex bodies is, by this barrier, doomed to stop at $n^{4/3}$.
