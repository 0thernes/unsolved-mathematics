# Attempts — Sendov's Conjecture

The conjecture has accumulated a long record of partial proofs, degree-by-degree verifications, and a few episodes of overreach. Nothing approaching a full proof exists; the established results are genuinely partial, and the literature is unusually careful about the gap between "verified for $n \le N$" and "true in general."

## Low-degree verifications (real progress, incremental)

The earliest confirmed cases were small degrees. The case $n = 2$ is trivial (the single critical point is the average of the two roots), and $n = 3$ was settled cleanly by **Z. Rubinstein (1968)**. Through the late 1960s and 1970s, **A. Meir and A. Sharma**, **D. Phelps and R. S. Rodriguez**, **A. W. Goodman, Q. I. Rahman, and J. S. Ratti**, and **G. Schmeisser** pushed verified degrees upward. By the 1990s, work by **J. E. Brown** (and later **Brown–Xiang**) reached approximately $n \le 6$ and beyond, and consolidated estimates eventually established the conjecture rigorously for degrees up to roughly $n \le 8$. These are correct but narrow: each new degree required heavier and heavier case analysis, signaling that the method could not reach all $n$.

## Asymptotic breakthroughs (correct, regime-limited)

**Jérôme Dégot (2014)** proved the conjecture for sufficiently large degree when the distinguished root is bounded away from the unit circle. This is a genuine, accepted result, but it deliberately excludes the boundary regime, which is where the conjecture is sharpest. It reframed the open problem rather than closing it.

**Terence Tao (2020)**, "Sendov's conjecture for sufficiently high degree polynomials," proved the conjecture for all sufficiently large $n$ via a limiting-measure / compactness argument. This is the most celebrated partial result and is widely regarded as correct. Its acknowledged limitation is non-effectivity: the threshold degree is not made explicit at a usable scale, so it does not connect to the small-degree verifications to yield a complete proof.

## Near-misses and the "boundary obstruction"

A recurring pattern in failed or stalled attempts is an argument that controls the interior of the disk but loses all slack as the distinguished root approaches $|a| = 1$. Because the extremal example $z^n - 1$ achieves equality exactly on the boundary, any proof must be sharp there; numerous estimation-based attempts have foundered at precisely this point. This is less a single famous near-miss than a structural reason many plausible approaches stop just short.

## Disputed / withdrawn claims

Over the decades several **claimed complete proofs** circulated, particularly as preprints, asserting resolution for all degrees. The consistent objection raised by specialists is that such arguments **fail in the boundary-sharp regime** (the distinguished root near the unit circle) or rely on inequalities that are not in fact uniform in $n$ — the same gap that limits the rigorous estimation program. The community's standard, neutral position is that **no complete, fully verified proof of Sendov's conjecture currently exists**; the strongest accepted results remain Tao's large-$n$ theorem and the finite small-degree verifications. (Specific informal claims are not catalogued here precisely because none has survived expert scrutiny; this dossier records the dispute pattern rather than endorsing or naming any individual claim as proven.)

## Related "Sendov-type" problems

Attempts have also branched into variants — the conjecture for the *second* derivative, "Sendov for higher-order critical points," quantitative versions asking how close the nearest critical point must be on average, and analogues for rational functions or polynomials over other fields. Partial results exist in these directions, but they are auxiliary; the core conjecture stands open.
