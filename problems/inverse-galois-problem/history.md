# History — The Inverse Galois Problem

_Origin, formulation, and timeline._

## How the problem arose

Galois theory, born from Évariste Galois's 1830–1832 work on the solvability of polynomial equations, attaches to each separable polynomial (or field extension) a finite group encoding the symmetries of its roots. The *direct* problem—given a polynomial, compute its Galois group—was understood in principle by the mid-nineteenth century. The *inverse* problem reverses the arrow: given an abstract finite group $G$, does there exist a Galois extension $L/\mathbb{Q}$ with $\mathrm{Gal}(L/\mathbb{Q}) \cong G$? Equivalently, is every finite group realizable as a Galois group over the rationals?

The question crystallized in the late nineteenth century. The decisive impetus was **David Hilbert's 1892 paper** on irreducibility, which introduced what is now the *Hilbert Irreducibility Theorem*. Hilbert showed that if a group can be realized "regularly" over $\mathbb{Q}(t)$—as the Galois group of an extension of the rational function field with $\mathbb{Q}$ algebraically closed in the base—then by specializing the parameter $t$ to suitably chosen rational values, one obtains infinitely many realizations over $\mathbb{Q}$ itself. This reduced the arithmetic problem to a geometric one: realize $G$ over $\mathbb{Q}(t)$. Using this machinery, Hilbert realized the symmetric groups $S_n$ and alternating groups $A_n$.

The standard precise formulation is therefore twofold. The **arithmetic IGP** asks for $\mathrm{Gal}(L/\mathbb{Q}) \cong G$. The stronger **regular IGP (RIGP)** asks for a regular Galois extension of $\mathbb{Q}(t)$ with group $G$; via Hilbert irreducibility, RIGP for $G$ implies the arithmetic version. A connected reformulation, pursued by Emmy Noether around 1918, is the **Noether problem**: is the field of $G$-invariants $\mathbb{Q}(x_g : g \in G)^G$ purely transcendental (rational) over $\mathbb{Q}$? A positive answer yields a regular—indeed generic—realization, but the Noether problem can fail (Swan, 1969).

## Timeline

- **1830–1832** — Galois develops the group-theoretic theory of equations, supplying the language in which the problem is later posed.
- **1892** — Hilbert proves the Irreducibility Theorem and realizes $S_n$ and $A_n$ over $\mathbb{Q}$; this is the conventional birth of the inverse problem.
- **1918** — Emmy Noether formulates the rationality (Noether) problem, reducing realization to a question about invariant fields.
- **1937** — Arnold Scholz and Helmut Reichardt realize all finite $p$-groups of odd order over $\mathbb{Q}$.
- **1954** — Igor Shafarevich announces the realization of every finite **solvable** group as a Galois group over $\mathbb{Q}$ (the proof, involving subtle embedding problems, was later corrected for the prime $2$).
- **1969** — Richard Swan shows the Noether problem fails for the cyclic group $C_{47}$, severing rationality from realizability.
- **1977–1984** — The **rigidity method** matures (Belyi, Fried, Matzat, Thompson, Shih), realizing many simple groups via covers of $\mathbb{P}^1$.
- **1979** — Belyi realizes many finite simple groups of Lie type using rigidity and Belyi maps.
- **1984** — John Thompson realizes the **Monster** sporadic simple group over $\mathbb{Q}$ via rigid triples of rational conjugacy classes.
- **1984–1989** — Matzat, Fried, and others develop the theory of the algebraic fundamental group and braid-group action (Hurwitz spaces) systematizing rigidity.
- **1996** — Helmut Völklein's monograph and the Malle–Matzat treatise consolidate the field; most sporadic groups (with the persistent exception of $M_{23}$) are realized.
- **2000s–present** — Harbater–Pop "patching" methods extend realizability over other fields; the general problem over $\mathbb{Q}$ remains open, with $M_{23}$ and many non-solvable groups still unconfirmed.
