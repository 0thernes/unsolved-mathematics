# History — The Birch and Swinnerton-Dyer Conjecture

_Origin, formulation, and timeline._

The Birch and Swinnerton-Dyer (BSD) conjecture was born from numerical experiment, not abstract speculation. In the early 1960s, working in Cambridge, Bryan Birch and Peter Swinnerton-Dyer used the EDSAC 2 computer — one of the first machines available to academic mathematicians — to count the number $N_p$ of points modulo $p$ on a fixed elliptic curve $E/\mathbb{Q}$, for many primes $p$. Their guiding intuition was that an elliptic curve with many rational points should also have, on average, many points modulo $p$. They examined the partial products
$$
\prod_{p \le X} \frac{N_p}{p},
$$
and observed empirically that this grew like $C(\log X)^r$, where $r$ appeared to equal the rank of the Mordell–Weil group $E(\mathbb{Q})$. Through the analytic class number formula and the work of Hasse, this product is heuristically tied to the behaviour of the Hasse–Weil $L$-function $L(E,s)$ near $s=1$. Reorganized in the language of $L$-functions, the data suggested the now-canonical statement: the order of vanishing of $L(E,s)$ at $s=1$ (the analytic rank) equals the algebraic rank of $E(\mathbb{Q})$.

The **weak** form asserts equality of analytic and algebraic ranks. The **strong** (refined) form, formulated through the 1960s and sharpened by Tate, gives the leading Taylor coefficient explicitly:
$$
\lim_{s\to 1}\frac{L(E,s)}{(s-1)^r} = \frac{\#\Sha(E)\cdot \Omega_E \cdot \mathrm{Reg}(E)\cdot \prod_p c_p}{(\#E(\mathbb{Q})_{\mathrm{tors}})^2},
$$
involving the (conjecturally finite) Tate–Shafarevich group $\Sha$, the real period $\Omega_E$, the regulator, Tamagawa numbers $c_p$, and torsion. At the time of formulation, the very analytic continuation of $L(E,s)$ to $s=1$ was itself conjectural, contingent on modularity.

A foundational subtlety: BSD presupposes machinery proven only decades later. The analytic continuation and functional equation of $L(E,s)$ for $E/\mathbb{Q}$ follow from the modularity theorem (Wiles, Taylor–Wiles, then Breuil–Conrad–Diamond–Taylor, 2001). Before modularity, BSD's left-hand side was not even known to be defined for general $E/\mathbb{Q}$.

**Timeline**

- **1922** — Mordell proves $E(\mathbb{Q})$ is finitely generated (the Mordell–Weil theorem for $\mathbb{Q}$), giving meaning to "rank."
- **1928** — Weil generalizes Mordell's theorem to abelian varieties over number fields.
- **1958–1965** — Birch and Swinnerton-Dyer run EDSAC computations; conjecture announced and published (Crelle, 1965).
- **1965** — Tate formulates the refined conjecture and the BSD formula for the leading coefficient.
- **1967** — Tate's "On the conjectures of Birch and Swinnerton-Dyer and a geometric analog" surveys and clarifies the statement.
- **1977** — Coates and Wiles prove that for CM elliptic curves with $L(E,1)\ne 0$, the rank is $0$ (first major theoretical evidence).
- **1983** — Gross and Zagier prove their formula relating $L'(E,1)$ to heights of Heegner points.
- **1986** — Kolyvagin's method of Euler systems shows analytic rank $0$ or $1$ implies equal algebraic rank (modular curves), with $\Sha$ finite in those cases.
- **1995–2001** — Modularity of all elliptic curves over $\mathbb{Q}$ established (Wiles; Taylor–Wiles; Breuil–Conrad–Diamond–Taylor), validating analytic continuation of $L(E,s)$.
- **2000** — BSD named one of the seven Clay Millennium Prize Problems ($1,000,000).
- **2010s** — Bhargava–Shankar bound average ranks; Bhargava–Skinner–Zhang show BSD holds for a positive proportion of curves. Skinner–Urban and others advance Iwasawa Main Conjectures, controlling $\Sha$ via $p$-adic $L$-functions.
- **Present** — Weak BSD remains open in rank $\ge 2$; the conjecture is a theorem only in analytic rank $0$ and $1$ (with finiteness of $\Sha$ proven only there, prime-by-prime in the refined form).
