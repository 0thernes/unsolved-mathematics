# Approaches — The Moving Sofa Problem

_Major strategies, partial results, and barriers._

Work on the sofa constant $\mu$ splits cleanly into **lower-bound** efforts (build a large shape that provably fits and moves) and **upper-bound** efforts (prove no shape can exceed a stated area). The conjectured truth, $\mu = \mu_G \approx 2.2195$ (Gerver's value), would be pinned down only when these two sides meet.

## Envelope / corridor-intersection method (lower bounds)

The foundational technique, due to Hammersley (1968), reframes the motion. Instead of moving the sofa, fix the sofa and slide the rotating L-corridor over it through a $90^\circ$ turn. A shape is admissible iff it lies inside *every* placement of the corridor, i.e. inside the intersection of a continuous family of corridors. The boundary of the maximal admissible shape is therefore an **envelope** of the moving inner-corner lines. This converts an intractable dynamic constraint into a problem in the differential geometry of envelopes.

**Best result.** Applied naively to a one-parameter rotation, the method yields Hammersley's shape (area $\pi/2 + 2/\pi \approx 2.2074$). Gerver (1992) applied it with a richer motion in which the sofa both translates and rotates, allowing the boundary to be built from segments, circular arcs, and **involutes of circles**; matching the 18 pieces analytically gives the area $\mu_G \approx 2.219531669$. Romik (2017) reconstructed this with symbolic computation, expressing the parameters via a system of transcendental equations.

**Barrier.** The method *constructs* candidates but does not certify *optimality*. Establishing that a given envelope is the global maximizer — rather than a local critical configuration — is exactly the open problem. The envelope is determined by a local matching condition; ruling out other, possibly non-smooth or asymmetric maximizers requires a global argument the method does not supply.

## Calculus-of-variations / Euler–Lagrange characterization

A natural strategy treats the boundary as an unknown function and seeks stationarity of area under the corridor constraint, producing Euler–Lagrange-type optimality conditions. Gerver's construction can be read as a solution to such conditions: each boundary piece satisfies a local extremality relation, and the pieces are glued at points where the contact structure changes.

**Best result.** This viewpoint explains *why* Gerver's shape has its particular structure (the appearance of involutes is forced by the contact geometry) and yields necessary conditions any optimizer must satisfy. Baek's 2024 claimed proof develops this into a rigorous variational framework.

**Barrier.** Necessary conditions for a smooth critical shape do not by themselves exclude the existence of a *larger* shape with different (e.g. asymmetric, or lower-regularity) contact structure. Promoting "Gerver's shape is the unique smooth critical point of this type" to "$\mu = \mu_G$" is the hard step; it requires showing the variational problem has no competing maximizer and that the maximizer has the assumed regularity.

## Linear-programming / finite-angle upper bounds (computer-assisted)

For upper bounds, the key idea (sharpened by Kallus and Romik, 2018) is to consider only a *finite* set of corridor rotation angles. Any admissible sofa must fit inside the intersection of the corridors at those finitely many angles; the maximal area of that intersection is an upper bound for $\mu$, and it is computable. Choosing the angles well and bounding the optimization rigorously (interval arithmetic / certified computation) yields validated numerical bounds.

**Best result.** Kallus–Romik proved $\mu \le 2.37$, the best rigorous unconditional upper bound prior to 2024. Earlier bounds came from Hammersley ($2\sqrt 2 \approx 2.828$) and intermediate refinements around $2.62$ (e.g. work attributed to Gerver and to others using a handful of constraints).

**Barrier.** Adding more angles drives the bound down toward $\mu_G$ only slowly; the intersection-of-finitely-many-corridors relaxation has a genuine gap from the true constant, and the gap closes asymptotically rather than in finitely many constraints. Pushing the finite-angle method from $2.37$ to $2.2195$ appears computationally infeasible by brute force — the number of constraints and the precision required both blow up. This motivated the search for a closed-form optimality proof rather than a numerical squeeze.

## Variant problems as testing grounds

Because the original is so resistant, several variants serve as proving grounds for techniques.

- **Ambidextrous sofa** (Romik, 2017): a shape that can navigate corners turning *both* left and right. Romik found the exact optimal shape (the "Romik sofa," area $\approx 1.6449$), giving a clean, completely solved analogue whose methods informed work on the main problem.
- **Unequal corridor widths** and **non-right-angle corners**: studied to understand how the optimal structure deforms; useful for stress-testing the envelope method.
- **Higher dimensions** (the "moving box/sofa in 3D"): largely open and far less developed; included mainly to delimit which 2D techniques are dimension-specific.

**Net barrier across all approaches.** Every lower bound has been Gerver's value since 1992, and every unconditional upper bound has stayed strictly above it. The defining obstruction was the absence of a single framework able to prove a matching upper bound equal to $\mu_G$ — precisely what Baek's 2024 preprint claims to supply, pending verification.
