# History — The Jacobian Conjecture

_Origin, formulation, and timeline._

## How the problem arose

The conjecture grew out of the study of polynomial automorphisms — invertible maps $F\colon \mathbb{C}^n \to \mathbb{C}^n$ whose components are polynomials and whose inverse is again polynomial. A necessary condition for invertibility is that the Jacobian determinant $\det DF$ be a nonzero constant: by the chain rule, $\det DF \cdot \big(\det DF^{-1}\big)\!\circ\! F = 1$, and since both factors are polynomials, each must be a nonzero constant. The Jacobian Conjecture asks whether this evidently necessary condition is also *sufficient*.

The problem entered the literature in 1939 through a short note by **Ott-Heinrich Keller**, who studied invertibility of polynomial maps with unit Jacobian (the so-called "ganze Cremona-Transformationen"). Keller's original concern was with integral/unimodular polynomial transformations; the now-standard formulation over a field of characteristic zero — most often $\mathbb{C}$ — is a later distillation of his question.

## Precise formulation and reformulations

**Standard statement (characteristic 0).** If $F = (F_1,\dots,F_n)\colon \mathbb{C}^n \to \mathbb{C}^n$ is a polynomial map with $\det\!\big(\partial F_i/\partial x_j\big) \in \mathbb{C}^\times$ (a nonzero constant), then $F$ is bijective and $F^{-1}$ is also polynomial.

Several equivalent reformulations have shaped the field:

- **Reduction to degree 3 (cubic case).** Bass, Connell, and Wright (1982), and independently Yagzhev (around 1980), proved that it suffices to treat maps of the special form $F = X + H$ where $H$ is homogeneous of degree 3, in all dimensions. Thus the *cubic homogeneous* case captures the full conjecture.
- **Nilpotency reformulation.** For cubic-homogeneous maps the conjecture is equivalent to the assertion that the Jacobian matrix $DH$ is nilpotent.
- **Cubic-linear reduction.** Drużkowski (1983) sharpened the target further to maps whose cubic part has the form $((a_1 \cdot x)^3,\dots,(a_n\cdot x)^3)$.
- **Vanishing conjecture / Mathieu–Zhao spaces.** Wenhua Zhao recast the conjecture in terms of differential operators and "Mathieu subspaces," linking it to statements about powers of the Laplacian annihilating certain functions.

The conjecture is sharply sensitive to hypotheses: it is **false in positive characteristic** (e.g., $x \mapsto x - x^p$ on $\mathbb{F}_p$ has Jacobian $1$ but is not injective), and false if "polynomial" is relaxed to "holomorphic." The dimension-1 case is elementary (a polynomial with constant nonzero derivative is affine).

## Timeline

- **1939** — Ott-Heinrich Keller poses the question of invertibility of polynomial maps with unit Jacobian ("Ganze Cremona-Transformationen," *Monatshefte für Mathematik und Physik*).
- **1939–1960s** — The two-dimensional case attracts attention; numerous flawed proofs circulate; the problem gains a reputation for treachery.
- **1971** — Connections to the structure of $\mathrm{Aut}(\mathbb{C}[x_1,\dots,x_n])$ are clarified; the tame/wild automorphism question takes shape alongside.
- **c. 1980** — A. V. Yagzhev establishes reduction to cubic maps (work in Russian).
- **1982** — Hyman Bass, Edwin Connell, and David Wright publish the landmark survey "The Jacobian conjecture: reduction of degree and formulation of equations," establishing the cubic reduction in the Western literature and standardizing terminology.
- **early 1980s** — Degree-2 maps are settled: any quadratic map with constant Jacobian is invertible (Wang).
- **1983** — Tzuong-Tsieng Moh proves the two-dimensional conjecture for maps of degree $\le 100$.
- **1983** — Ludwik Drużkowski reduces the problem to "cubic-linear" maps.
- **1998** — Steven Smale lists the Jacobian Conjecture among his "Mathematical problems for the next century."
- **2000s** — Wenhua Zhao develops the vanishing-conjecture / Mathieu-subspace framework; Michiel de Bondt and Arno van den Essen prove new structural results on nilpotent Jacobians and symmetric maps.
- **2005** — Arno van den Essen's monograph *Polynomial Automorphisms and the Jacobian Conjecture* consolidates the modern theory.
- **2012** — Bass–Connell–Wright-style ideas extended; Belov-Kanel and Kontsevich relate the conjecture to the Dixmier conjecture on the Weyl algebra (stable equivalence in suitable dimension).
- **2010s–2020s** — Continued partial progress (symmetric maps, special structural classes, formal-inverse degree bounds); numerous announced general proofs appear and are subsequently retracted or found incomplete. The conjecture remains **open** in all dimensions $n \ge 2$.
