# History — Lehmer's Conjecture on the Ramanujan Tau Function

_Origin, formulation, and timeline._

## Origin and formulation

The object at the center of the conjecture is the **Ramanujan tau function** $\tau(n)$, defined by the $q$-expansion of the discriminant modular form
$$
\Delta(z) = q\prod_{n=1}^{\infty}(1-q^n)^{24} = \sum_{n=1}^{\infty}\tau(n)\,q^n, \qquad q=e^{2\pi i z},
$$
the unique normalized cusp form of weight $12$ for the full modular group $\mathrm{SL}_2(\mathbb{Z})$. Srinivasa Ramanujan introduced $\tau(n)$ in his 1916 paper *On certain arithmetical functions*, conjecturing the three properties later proved central: multiplicativity $\tau(mn)=\tau(m)\tau(n)$ for $(m,n)=1$; the recursion $\tau(p^{r+1})=\tau(p)\tau(p^r)-p^{11}\tau(p^{r-1})$ at prime powers; and the size bound $|\tau(p)|\le 2p^{11/2}$. The first two were proved by Louis Mordell in 1917 via what are now recognized as Hecke operators; the third, the **Ramanujan–Petersson conjecture** for $\Delta$, was settled by Pierre Deligne in 1974 as a consequence of his proof of the Weil conjectures.

**Lehmer's question** is orthogonal to size: it asks whether $\tau(n)$ can ever equal zero. In his 1947 paper *The vanishing of Ramanujan's function $\tau(n)$* (Duke Math. J. 14), Derrick Henry Lehmer observed that by multiplicativity, $\tau(n)\ne 0$ for all $n$ if and only if $\tau(p)\ne 0$ for every prime $p$. He verified $\tau(n)\ne 0$ for all $n<33{,}333$, and remarked that the persistent non-vanishing "seems very remarkable." The statement — **$\tau(n)\ne 0$ for all $n\ge 1$** — is now known as Lehmer's conjecture on the tau function. It remains open.

A useful reformulation: since $\Delta$ is a Hecke eigenform, $\tau(p)$ is (up to normalization) the trace of Frobenius at $p$ on the associated $2$-dimensional $\ell$-adic Galois representation $\rho_{\Delta,\ell}$. Lehmer's conjecture is therefore the assertion that this trace of Frobenius is nonzero at every prime — a statement that resists the available analytic and Galois-theoretic tools, since the existing machinery controls $\tau(p)$ in distribution but cannot exclude a single sporadic zero.

## Timeline

**1916** — Ramanujan defines $\tau(n)$ and states his conjectures on it.

**1917** — Mordell proves multiplicativity and the prime-power recursion, implicitly using Hecke operators.

**1937** — Hecke develops the general theory of Hecke operators, placing $\tau$ in the framework of eigenforms.

**1947** — Lehmer poses the non-vanishing problem, reduces it to primes, and verifies $\tau(n)\ne 0$ for $n<33{,}333$.

**1947–1965** — Successive computational extensions (Lehmer and others) push the verified range upward into the hundreds of thousands.

**1968** — Serre's *Une interprétation des congruences relatives à la fonction $\tau$ de Ramanujan* frames $\tau$ congruences in modular terms, anticipating Galois representations.

**1972** — Serre's study of congruences of $\tau$ modulo the exceptional primes ($2,3,5,7,23,691$) crystallizes the image-of-Galois picture; Swinnerton-Dyer's analysis of $\ell$-adic representations attached to $\Delta$ appears.

**1974** — Deligne proves $|\tau(p)|\le 2p^{11/2}$ (Ramanujan–Petersson), but the bound is compatible with $\tau(p)=0$, so it does not resolve Lehmer.

**1973–1977** — Serre and Swinnerton-Dyer determine the image of $\rho_{\Delta,\ell}$ for all $\ell$, showing it is as large as possible (open in $\mathrm{GL}_2$) outside the exceptional primes; this constrains but does not forbid vanishing.

**1981** — Serre's *Quelques applications du théorème de densité de Chebotarev* gives density-zero statements for primes in prescribed Frobenius classes, bearing on how often $\tau(p)$ lands in small sets.

**1985–1997** — Effective congruence conditions for a hypothetical $\tau(p)=0$ are tabulated; any such $p$ must satisfy strong simultaneous congruences modulo the exceptional primes.

**2011** — Edixhoven, Couveignes and collaborators publish *Computational Aspects of Modular Forms and Galois Representations*, giving polynomial-time computation of $\tau(p)$.

**2013–2020** — Bosman, Derickx, Mascot and others compute $\tau(p)$ for very large primes, extending verification of non-vanishing far beyond earlier ranges.

**2021–2022** — Bennett, Gajović, Sengupta, Patel and others solve equations $\tau(n)=\pm\ell^m$ and study $|\tau(n)|$ taking prescribed values, sharpening the arithmetic of $\tau$ — but $\tau(p)=0$ remains untouched.

**Present** — No prime $p$ with $\tau(p)=0$ is known; the conjecture is verified well beyond any feasible search bound yet remains without proof.
