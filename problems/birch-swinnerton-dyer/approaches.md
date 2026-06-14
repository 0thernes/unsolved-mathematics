# Approaches — The Birch and Swinnerton-Dyer Conjecture

_Major strategies, partial results, and barriers._

## Heegner points and the Gross–Zagier formula

The most successful concrete attack constructs rational points directly. **Heegner points** are images of CM points on modular curves; under modular parametrization $X_0(N)\to E$ they yield rational (or near-rational) points on $E$. The **Gross–Zagier formula** (1986) computes the canonical (Néron–Tate) height of a Heegner point in terms of the derivative $L'(E,1)$ of the $L$-function. Its decisive consequence: when the analytic rank is exactly $1$, the Heegner point is non-torsion, so the algebraic rank is at least $1$. Combined with Kolyvagin's bound below, this establishes BSD (weak form) in analytic rank $1$. **Barrier:** Heegner points live in the rank-$1$ eigenspace and produce a *single* independent point. The method is structurally incapable of generating two independent points, so it does not reach rank $\ge 2$. Generalizations (Stark–Heegner / Darmon points, $p$-adic and higher-dimensional analogues) remain largely conjectural.

## Euler systems and Kolyvagin's method

Kolyvagin (1988–1990) introduced **Euler systems** — compatible families of cohomology classes built from Heegner points — to bound the Selmer group and hence the Tate–Shafarevich group $\Sha$ from above. He proved: if the analytic rank is $0$ or $1$, then the algebraic rank equals it *and* $\Sha(E)$ is finite. This is the deepest unconditional structural result toward BSD. **Best result:** full weak BSD plus finiteness of $\Sha$ in analytic ranks $0$ and $1$. **Barrier:** the Euler system derived from Heegner points encodes information only up to rank $1$. No Euler system is known that controls Selmer groups in analytic rank $\ge 2$; constructing one is a central open problem.

## Iwasawa theory and Main Conjectures

Iwasawa theory studies how Selmer groups and $p$-adic $L$-functions vary up a tower of cyclotomic (or anticyclotomic) extensions. The **Iwasawa Main Conjecture** equates a characteristic ideal of a Selmer module with a $p$-adic $L$-function, packaging the arithmetic of $\Sha$ and the BSD leading term $p$-adically. **Best results:** Rubin proved the CM case; Kato's Euler system gave one divisibility for modular forms; **Skinner–Urban** (2014) proved the reverse divisibility for a large class of curves, yielding the full main conjecture for many $E$. This lets one verify the $p$-part of the *refined* BSD formula for individual primes $p$ in ranks $0$ and $1$. **Barrier:** controls only one prime at a time and presupposes analytic rank $\le 1$ for the strongest conclusions; the $p$-adic and complex $L$-values are linked but not identical, and exceptional ("trivial zero") cases need separate treatment.

## Average ranks and the geometry of numbers

Rather than a single curve, **Bhargava–Shankar** (2010s) bound the *average* size of $n$-Selmer groups over all elliptic curves ordered by height, using orbit-counting in representations of arithmetic groups (geometry of numbers). They proved the average rank is bounded (below $1$), so a positive proportion of curves have rank $0$ and a positive proportion have rank $1$. **Bhargava–Skinner–Zhang** combined this with Gross–Zagier–Kolyvagin to show **BSD holds for a positive proportion (over 66%) of elliptic curves over $\mathbb{Q}$**. **Barrier:** these are statistical statements; they do not resolve any individual curve of rank $\ge 2$, and the methods say nothing about the high-rank tail.

## $p$-adic $L$-functions and $p$-adic BSD

A parallel programme (Mazur–Tate–Teitelbaum, Perrin-Riou) formulates BSD-type statements for $p$-adic $L$-functions $L_p(E,s)$, where the order of vanishing and leading coefficient are more accessible. **Best result:** strong evidence and many proven cases of the $p$-adic main conjecture; exceptional-zero phenomena governed by the $\mathcal{L}$-invariant. **Barrier:** transferring $p$-adic conclusions to the complex (archimedean) BSD requires comparison results that are themselves deep and partly conjectural.

## Descent and explicit computation

Classical **$n$-descent** computes Selmer groups $\mathrm{Sel}^{(n)}(E)$, giving an upper bound for the rank and a lower bound via found points; the gap is exactly the $n$-part of $\Sha$. Modern algorithms (Cremona's tables, magma/pari implementations, visualization of $\Sha$, second/higher descents) verify BSD numerically for vast databases of curves and detect non-trivial $\Sha$. **Barrier:** descent is conditional on the finiteness of $\Sha$ to terminate as a rank algorithm — and that finiteness is itself a (proven only in rank $\le 1$) special case of BSD. There is no unconditional, provably terminating algorithm to compute the rank of a general $E/\mathbb{Q}$.

**Overarching obstruction.** Every known unconditional route to the algebraic rank passes through Heegner-point / Euler-system technology that saturates at rank $1$. Breaking into rank $\ge 2$ — producing arithmetic objects that certify two or more independent rational points from analytic data — is the recognized fundamental barrier, and no current method overcomes it.
