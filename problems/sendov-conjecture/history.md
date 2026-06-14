# History — Sendov's Conjecture

The conjecture concerns the geometry of polynomials: the relationship between the location of a polynomial's zeros and the location of its critical points (the zeros of its derivative). Its ancestry lies in the classical **Gauss–Lucas theorem** (early 19th century), which states that all critical points of a complex polynomial lie in the convex hull of its zeros. Sendov's conjecture sharpens this from a global containment statement to a *local* one attached to each individual root.

## Precise formulation

Let $p(z) = \prod_{k=1}^n (z - z_k)$ be a polynomial of degree $n \ge 2$ with all zeros in the closed unit disk, $|z_k| \le 1$. The conjecture asserts that for **every** root $z_j$, the disk $\{ z : |z - z_j| \le 1 \}$ contains at least one zero of the derivative $p'$. Equivalently, for each $j$,
$$\min_{w : p'(w)=0} |z_j - w| \le 1.$$
The constant $1$ is sharp: $p(z) = z^n - 1$ has all roots on the unit circle while $p'(z) = n z^{n-1}$ has its only critical point at the origin, exactly distance $1$ from each root. By scaling, the statement is equivalent to: if all roots lie in a disk of radius $r$, then within distance $r$ of each root lies a critical point.

A standard reduction (rotation, and treating each root in turn) lets one fix the distinguished root and study the **"extremal"** configurations. Much of the literature normalizes the chosen root to be real and considers the worst case where roots cluster on the unit circle.

## Provenance and the naming question

The problem was posed by **Blagovest Sendov** around **1959** and circulated privately. It first appeared in print in **1967**, in Walter K. Hayman's *Research Problems in Function Theory*, where it was mistakenly attributed to **Ljubomir Iliev** (Sendov had communicated it to Iliev). For this reason it was long known as the **Ilieff conjecture** (or **Ilyeff–Sendov conjecture**) before Sendov's priority became standard. This attribution tangle is itself a notable historical feature of the problem.

## Timeline

- **1959** — Blagovest Sendov formulates the conjecture and communicates it to colleagues in Sofia.
- **1967** — The problem appears in print in Hayman's *Research Problems in Function Theory*, attributed to Iliev; the "Ilieff conjecture" name takes hold.
- **1969** — Early confirmations for low degree and special cases; A. Meir and A. Sharma, and independently others, verify the conjecture for $n \le 5$.
- **1969** — Z. Rubinstein proves the case $n = 3$ cleanly; D. Phelps and R. S. Rodriguez contribute partial results.
- **1972** — A. Joyal establishes a quantitative bound; Goodman, Rahman, and Ratti, and separately Schmeisser, push verified degrees upward.
- **1991** — Brown verifies $n \le 6$; subsequent work (Brown, Xiang) reaches higher degrees via heavy estimation.
- **1996** — Borcea proves several structural results and partial cases; the "Borcea variance conjecture" relatives appear.
- **1999** — Bojanov, Rahman, and Szynal, and related authors, sharpen estimates for roots on the circle.
- **2002** — **Gerald Schmeisser** and collaborators consolidate the degree-by-degree program; verification reaches roughly $n \le 8$.
- **2014** — **Jérôme Dégot** proves the conjecture holds for all sufficiently large $n$ *when the distinguished root is fixed away from the unit circle* (root modulus bounded below $1$), an asymptotic-in-degree breakthrough.
- **2020** — **Terence Tao** proves Sendov's conjecture for **all sufficiently large degree $n$** (an effective but astronomically large threshold), using a compactness/limiting argument and analysis of the equilibrium measure. This is the landmark modern result.
- **2020–present** — Active work by Chalebgwa, Hohn, and others refines Tao's method, studies roots on the unit circle, and attacks the remaining *finite* gap between small verified degrees and Tao's large-$n$ threshold. The conjecture remains **open** for the intermediate range of degrees.

The frontier is now unusual: the statement is known for all small degrees and for all sufficiently large degrees, yet unproven across a vast, finite, intermediate band.
