# History — The Tate Conjecture

_Origin, formulation, and timeline._

## How the problem arose

The Tate conjecture was born from the confluence of two developments of the late 1950s and early 1960s: Grothendieck's construction of $\ell$-adic étale cohomology, which supplied a Weil cohomology theory carrying a continuous action of the absolute Galois group $G_k = \mathrm{Gal}(\bar k / k)$; and the Weil conjectures, which tied the eigenvalues of Frobenius to the arithmetic of varieties over finite fields. John Tate, working on abelian varieties and class field theory, recognized that algebraic cycles ought to be detectable inside this Galois module. He proposed an arithmetic analogue of Lefschetz's $(1,1)$ theorem and of the then-recent Hodge conjecture: where Hodge predicts that rational $(p,p)$ classes are algebraic, Tate predicts that Galois-invariant $\ell$-adic classes are algebraic.

## Precise formulation

Let $X$ be a smooth projective variety over a finitely generated field $k$ of characteristic $\neq \ell$, with $\bar X = X \times_k \bar k$. For each $i$, the cycle-class map sends codimension-$i$ algebraic cycles into étale cohomology:
$$ \mathrm{CH}^i(X) \otimes \mathbb{Q}_\ell \;\longrightarrow\; H^{2i}_{\mathrm{\acute et}}(\bar X, \mathbb{Q}_\ell(i))^{G_k}. $$
The **Tate conjecture** $T^i(X,\ell)$ asserts this map is **surjective**: every Galois-invariant class (after a finite extension, fixed by an open subgroup) is a $\mathbb{Q}_\ell$-combination of cycle classes. Equivalently, the order of the pole of the $L$-function at the relevant point counts the rank of the cycle group (the "strong" form linking Tate to Beilinson–Bloch and Birch–Swinnerton-Dyer). Tate's first major instance — the **Tate conjecture for endomorphisms of abelian varieties** — states that $H^1$ of $A$ and $B$ have $G_k$-equivariant maps exactly given by isogenies: $\mathrm{Hom}(A,B)\otimes\mathbb{Z}_\ell \xrightarrow{\sim} \mathrm{Hom}_{G_k}(T_\ell A, T_\ell B)$.

## Timeline

- **1958–1960** — Grothendieck and M. Artin develop étale cohomology, providing the $\ell$-adic theory Tate needed.
- **1962–1963** — Tate poses the conjecture; the canonical reference is his ICM Stockholm address and the 1963 Woods Hole seminar notes "Algebraic cycles and poles of zeta functions."
- **1966** — Tate's "Endomorphisms of abelian varieties over finite fields" (Inventiones) proves the conjecture for divisors/endomorphisms of abelian varieties over **finite** fields.
- **1968** — Serre and Tate study good reduction; the formalism of Tate modules and $\ell$-adic representations matures.
- **1973–1974** — Pohlmann, and work surrounding Deligne's proof of the Weil conjectures, sharpen the finite-field picture; the conjecture is verified for many CM and Fermat varieties.
- **1983** — **Faltings** proves the Tate conjecture for abelian varieties (divisors) over **number fields** and finitely generated fields, en route to the Mordell conjecture — a landmark.
- **1983** — Zarhin extends results to abelian varieties over fields of positive characteristic ($> 2$, later all characteristics).
- **1994** — Tate's Motives (Seattle) survey "Conjectures on algebraic cycles in $\ell$-adic cohomology" restates the precise conjectures and their interrelations.
- **2003–2005** — Tate conjecture for $K3$ surfaces over finite fields established in special cases (e.g. ordinary, by Nygaard–Ogus earlier in 1985 for $p\geq 5$).
- **2012–2016** — **Madapusi Pera**, **Maulik**, **Charles**, and **Kim–Madapusi Pera** prove the Tate conjecture for $K3$ surfaces over finitely generated fields of characteristic $\neq 2$, exploiting the Kuga–Satake construction and Shimura varieties.
- **2017–present** — Progress on products, abelian-type Shimura varieties, and the relation to the Mumford–Tate conjecture; the general case over number fields remains **open**.
