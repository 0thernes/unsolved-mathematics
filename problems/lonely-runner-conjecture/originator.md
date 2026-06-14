# Originator(s) — The Lonely Runner Conjecture

_Biography, background, and the ideas that led here._

The conjecture carries two originators of record, reflecting its dual birth in the geometry of numbers and in Diophantine approximation.

## Jörg M. Wills

**Jörg Michael Wills** (born 1937) is a German mathematician long associated with the **University of Siegen**, where he held a chair in mathematics and built a research group in discrete and convex geometry. His mathematical home is the **geometry of numbers** in the tradition of Hermann Minkowski, together with combinatorial convexity, lattice-point enumeration, and the theory of polytopes. Wills is widely known beyond this problem for foundational work on **lattice points in convex bodies**, the **Wills functional** (a lattice-point analogue of the intrinsic-volume sum that bears his name), and for co-editing influential handbooks of convex and discrete geometry.

The Lonely Runner Conjecture emerged from his 1967–1968 investigations into **simultaneous Diophantine approximation**. The governing question there is: given real numbers (or, after reduction, integers) $v_1,\dots,v_n$, how large can one force $\min_i \|t v_i\|$ to be by choosing $t$ well? Wills studied the quantity
$$ \kappa(v_1,\dots,v_n) = \sup_t \min_i \|t v_i\|, $$
and the worst-case value over all admissible speed systems. He conjectured that this worst case is always at least $\tfrac{1}{n+1}$, attained by the arithmetic progression $1,2,\dots,n$. His motivation was internal to the geometry of numbers: he sought sharp inhomogeneous approximation constants and recognized that the extremal configurations had a clean, conjecturally universal form. Wills proved the bound for the first few values of $n$, establishing the conjecture as a precise, tantalizingly tight statement rather than a vague heuristic.

## T. W. Cusick

**Thomas W. Cusick** (born 1943) is an American number theorist, for most of his career a professor at the **University at Buffalo (SUNY)**. Trained in analytic and Diophantine number theory, Cusick worked broadly on **continued fractions, Diophantine approximation, the Markoff spectrum**, and later on **Boolean functions and cryptography**. Around 1971–1974, independently of Wills, he arrived at the same extremal problem from a strikingly geometric angle, which he named the **view-obstruction problem**.

Cusick's picture: place a closed axis-aligned cube of side $1/(k+1)$ centered at every point of the lattice $\mathbb{Z}^k$ shifted by $(\tfrac12,\dots,\tfrac12)$ in the open positive orthant. A ray from the origin in a generic direction will, he conjectured, always be "obstructed" — it must pierce one of these cubes. Translating the ray's direction into the speed vector and the time of obstruction into $t$, this is exactly the Lonely Runner statement. The cube formulation places the problem squarely in the **geometry of numbers and convex geometry**, and it is the lens through which many subsequent advances (Cusick–Pomerance for $n=4$, Barajas–Serra for $n=5$) were obtained.

## Two formulations, one problem

Wills's root is **analytic/Diophantine** — a sharp constant in inhomogeneous approximation. Cusick's root is **geometric** — a covering/obstruction property of cubes along rays. The two are equivalent by an elementary dictionary, and both predate the runners metaphor (Goddyn, 1990s), which reframed the same inequality as a kinematics problem and gave the conjecture its memorable name.

## Legacy

Wills's broader legacy is the modern interface of lattice-point theory and convex geometry; Cusick's spans Diophantine approximation and, later, cryptographic Boolean functions. The conjecture they posed has since become a hub connecting Diophantine approximation, the geometry of numbers, graph colouring, and combinatorics — a single inequality that refuses to yield even as the surrounding machinery has grown enormously sophisticated.
