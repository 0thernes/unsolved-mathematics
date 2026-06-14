# History — The Hadwiger Covering Conjecture

_Origin, formulation, and timeline._

## Origin and statement

Let $K \subset \mathbb{R}^n$ be a convex body (compact, convex, with nonempty interior). A *homothet* of $K$ is a set of the form $\lambda K + t$ with $\lambda > 0$ and $t \in \mathbb{R}^n$; it is *smaller* if $0 < \lambda < 1$. Define the *covering number* $c(K)$ as the least number of smaller homothetic copies of $K$ whose union contains $K$. The conjecture asserts
$$
c(K) \le 2^n \quad \text{for every convex body } K \subset \mathbb{R}^n,
$$
with equality **iff** $K$ is an $n$-dimensional parallelepiped. For the cube the $2^n$ smaller copies sit at the corners, and the bound is sharp.

The conjecture is most famous in three equivalent disguises. Hadwiger and, independently, Levi posed the *covering* form. Boltyanski (1960) proved the equivalence with the *illumination* form: $c(K)$ equals the minimum number of directions (or, equivalently, external light sources) needed so that every boundary point of $K$ is illuminated. Gohberg and Markus posed the same quantity as a covering problem in 1960. The three numbers — covering by homothets, illumination number, and minimum number of translates of $\operatorname{int} K$ covering $K$ — coincide, so the literature treats them interchangeably.

## Timeline

- **1955** — Friedrich (Frigyes) Levi solves the planar case for the boundary-illumination viewpoint, showing $c(K) \le 4$ in $\mathbb{R}^2$ with equality only for parallelograms.
- **1957** — Hugo Hadwiger poses the covering problem for general $n$ in his work on combinatorial geometry, conjecturing the $2^n$ bound. The problem is often dated to this formulation.
- **1960** — Israel Gohberg and Alexander Markus independently state the covering-by-homothets version (the "Gohberg–Markus" formulation), giving the conjecture its alternate name.
- **1960** — Vladimir Boltyanski introduces the *illumination* number and proves its equivalence with the covering number, reframing the problem geometrically.
- **1960s** — The planar case is fully settled: every plane convex body needs at most $4$ homothets, exactly $4$ only for parallelograms. Smooth bodies in any dimension are shown to require only $n+1$ illuminating directions (the easy "smooth" case).
- **1982** — Martin Lassak proves $c(K) \le 8$ for centrally symmetric bodies in $\mathbb{R}^3$ and refines low-dimensional bounds.
- **1988** — Vojislav Boltyanski and collaborators connect the illumination number to the *Helly dimension* / belt bodies, settling several special classes.
- **1990s** — K. Bezdek and others verify the conjecture for specific families (zonotopes/belt polytopes, bodies of constant width in $\mathbb{R}^3$), but the general $3$-dimensional case remains open.
- **2003** — Marton Naszódi initiates a fractional/volumetric program; later work (with Artstein-Avidan, Naszódi, Brazitikos) sharpens covering estimates via measure concentration.
- **2010** — Károly Bezdek and collaborators verify the conjecture for several broad classes and popularize the modern "$X$-ray / illumination" survey framing.
- **2012–2016** — The Boltyanski–Martini–Soltan monograph and the Bezdek–Khan survey consolidate the state of the art; the best general upper bound remains far from $2^n$.
- **2021** — Han Huang, Boaz Slomka, Tomasz Tkocz, and Beatrice-Helen Vritsiou prove $c(K) \le \binom{2n}{n}(n\ln n + n\ln\ln n + 5n)$ for symmetric bodies and an improved bound in general, the best asymptotic improvement over the longstanding $\binom{2n}{n} n \ln n$ estimate.
- **2023–present** — Refinements for specific classes (1-symmetric bodies, bodies with many symmetries) continue, but the conjectured $2^n$ bound is unproven for all $n \ge 3$, and the equality characterization is open in general.

The gap between the conjectured $2^n$ and the best general upper bound (super-exponential, of order $4^n$ up to polynomial factors) remains the central quantitative scandal of the field.
