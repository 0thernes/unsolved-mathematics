# History — The Lonely Runner Conjecture

_Origin, formulation, and timeline._

## Origin

The conjecture grew out of two independent threads in the geometry of numbers and Diophantine approximation during the 1960s. The earlier root lies with **Jörg M. Wills**, who in 1967 studied problems of simultaneous Diophantine approximation and the question of how closely a system of multiples $n\alpha_1, \dots, n\alpha_k$ could simultaneously avoid the integers. In a 1967–1968 series of papers Wills proved results that, in modern language, establish the conjecture for small numbers of runners and posed the general question. Independently, **T. W. Cusick** arrived at an equivalent statement in the early-to-mid 1970s through a geometric reformulation he called the **view-obstruction problem**: given the closed cubes of side $1/(k+1)$ centered at the half-integer lattice points, does every ray from the origin into the open positive orthant meet one of them? Cusick's framing makes the link to the geometry of numbers explicit.

## Formulation

The now-standard "runners" picture, and the evocative name, are due to **Luis Goddyn** around 1998, who connected the problem to chromatic numbers of distance graphs and circular colourings. The statement: $k$ runners start together on a circular track of unit circumference and run forever at distinct constant speeds. The conjecture asserts that for each runner there is a moment at which that runner is at distance at least $\tfrac{1}{k}$ (along the track) from every other runner — i.e., each runner is, at some time, "lonely."

The standard reduction fixes the runner under study at speed $0$ and takes the others' speeds to be **distinct nonzero integers** $v_1,\dots,v_{n}$ (with $n = k-1$ moving runners). Writing $\|x\|$ for the distance from $x$ to the nearest integer, the claim becomes: there exists a real $t$ with
$$ \|t\,v_i\| \ge \frac{1}{n+1} \quad \text{for all } i. $$
The constant $\tfrac{1}{n+1}$ is tight: the speeds $1,2,\dots,n$ show it cannot be improved. The conjecture is invariant under scaling speeds, so one may assume the $v_i$ are distinct positive integers with $\gcd = 1$.

## Reformulations

Equivalent guises include: Cusick's **view-obstruction** for the cube; **covering systems** / restricted covers of the integers; **regular chromatic number** and **circular chromatic number of distance graphs** (Goddyn–Zhu); a question about **flows and nowhere-zero invariants** in matroid theory; and a statement about **maxima of certain exponential sums / trigonometric polynomials**. Bienia, Goddyn, Gvozdjak, Sebő and Tarsi (1998) crystallized several of these dictionaries.

## Timeline

- **1967** — Jörg M. Wills poses the conjecture in the context of simultaneous Diophantine approximation; proves small cases.
- **1968** — Wills publishes further bounds on $\max_t \min_i \|t v_i\|$, settling $n \le 3$.
- **1973** — T. W. Cusick independently introduces the **view-obstruction problem** for the cube, equivalent to the conjecture.
- **1974** — Cusick and others verify additional small-$n$ cases via the geometric formulation.
- **1984** — Cusick and Carl Pomerance settle the case $n = 4$ (five runners) by detailed analysis.
- **1998** — Bienia, Goddyn, Gvozdjak, Sebő, Tarsi give a unified treatment, coin the "lonely runner" name (Goddyn), and re-prove $n \le 4$; links to colouring established.
- **2001** — Chen and Cusick, and related work, push computational and geometric methods.
- **2008** — Barajas and Serra prove the case $n = 5$ (six runners), using a refined view-obstruction argument.
- **2011** — Renault gives a streamlined proof for $n=5$ and surveys the gap-of-divisors method.
- **2017** — Tao establishes the conjecture for $\tfrac{1}{n+1}$ replaced by a slightly smaller bound and proves it suffices to consider speeds bounded by an explicit polynomial in $n$, reducing the problem in principle to a finite check.
- **2021** — Beck, Hosten, Schymura and collaborators bring polyhedral/Ehrhart and computational geometry tools; partial results for structured speed sets.
- **2023–2024** — Work on the "shifted" and "rational" variants; intensive verification efforts and refinements of Tao's reduction; $n = 6$ remains the frontier of fully proven cases.
