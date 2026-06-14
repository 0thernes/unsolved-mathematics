# Approaches — The Zariski Cancellation Problem

_Major strategies, partial results, and barriers._

The problem splits by dimension $n$ and by the characteristic of the base field $k$. Strategies divide into (i) *positive-direction* methods that prove cancellation in low dimension, and (ii) *invariant-theoretic* methods that detect failure by distinguishing a cylinder's base from $\mathbb{A}^n$. Gupta's theorems show the latter actually win in characteristic $p$.

## $\mathbb{A}^1$-fibrations and the theory of affine surfaces

**Core idea.** In characteristic $0$, a smooth affine variety that admits enough $\mathbb{A}^1$-fibrations and has the homology and topology of affine space can often be shown to *be* affine space. For surfaces, Miyanishi's structure theory of affine rational surfaces, combined with the classification of $\mathbb{A}^1$- and $\mathbb{A}^1_*$-fibrations, gives an essentially complete picture.

**Best result.** Fujita, Miyanishi, and Sugie (1976–80) proved cancellation for $n=2$ in characteristic zero: $X\times\mathbb{A}^1\cong\mathbb{A}^3 \Rightarrow X\cong\mathbb{A}^2$. The Abhyankar–Eakin–Heinzer theorem (1972) settles $n=1$ over any field: a curve with $C\times\mathbb{A}^1\cong\mathbb{A}^2$ is the affine line.

**Barrier.** The fibration method relies on the fine classification of surfaces (Mori theory of open surfaces, logarithmic Kodaira dimension), which has no equally complete analogue in dimension $\ge 3$. It also leans on characteristic-zero phenomena (e.g. integrability of vector fields, generic smoothness) that fail in characteristic $p$.

## Locally nilpotent derivations and the Makar-Limanov invariant

**Core idea.** A locally nilpotent derivation (LND) $D$ on a $k$-algebra $A$ is the infinitesimal generator of a $\mathbb{G}_a$-action; $\ker D$ is the ring of invariants. The **Makar-Limanov (ML) invariant** is $\mathrm{ML}(A)=\bigcap_D \ker D$, the intersection over all LNDs. For a polynomial ring $\mathrm{ML}(k[x_1,\dots,x_n])=k$. Because $\mathrm{ML}$ behaves controllably under adding a variable, computing it on a candidate base $X$ can prove $X\not\cong\mathbb{A}^n$ even when $X\times\mathbb{A}^1\cong\mathbb{A}^{n+1}$ — exactly a cancellation failure.

**Best result.** Makar-Limanov (1996) used this to show the **Russell cubic threefold** $V=\{x+x^2y+z^2+t^3=0\}\subset\mathbb{A}^4$ has $\mathrm{ML}(V)\ne k$, hence $V\not\cong\mathbb{A}^3$, although $V$ is a smooth contractible affine threefold that looks like $\mathbb{A}^3$ to homology. Kaliman–Makar-Limanov and Crachiola refined the invariant (including a positive-characteristic variant). Gupta's 2014 breakthrough deploys exactly an ML-type invariant on Asanuma threefolds.

**Barrier.** In characteristic $0$ the ML invariant of any known $X$ with $X\times\mathbb{A}^1\cong\mathbb{A}^4$ has so far come out trivial, so this exact tool has *not* produced a char-$0$ counterexample. The invariant is also hard to compute in general and can be insensitive (e.g. it is trivial whenever $A$ carries two independent $\mathbb{G}_a$-actions with different invariant rings).

## Asanuma deformations and the positive-characteristic resolution

**Core idea.** Asanuma (1987) constructed affine threefolds in characteristic $p$ as deformations $A_m=k[x,y,z,t]/(x^m y + z^{p^e}+ t + t^{sp})$-type rings whose cylinders are polynomial rings but whose own structure is anomalous. The subtlety is purely characteristic-$p$: Frobenius and inseparability allow "fake" coordinate systems.

**Best result.** **Neena Gupta (2014)** proved that for $k$ of characteristic $p>0$ and $n\ge 3$, ZCP is **false**: there exist $A$ with $A^{[1]}\cong k^{[n+1]}$ but $A\not\cong k^{[n]}$. Her proof computes a characteristic-$p$ Makar-Limanov-type invariant on the Asanuma threefolds to separate them from $\mathbb{A}^3$. This was the first counterexample in *any* setting and resolved the long-open positive-characteristic problem completely for $\dim\ge 3$.

**Barrier (for char 0).** The construction is intrinsically characteristic-$p$: it exploits $p$-th power maps and inseparable subextensions that simply do not exist in characteristic zero, where the relevant rings turn out to be genuine polynomial rings. Thus Gupta's method, decisive though it is, gives no information about the open char-$0$ case.

## Homological / topological characterizations of affine space

**Core idea.** Characterize $\mathbb{A}^n$ among smooth affine varieties by contractibility, triviality of the Picard group, and other cohomological vanishing, then show cylinders force these properties on the base. This connects to the (still-open) **Zariski–Lipman** and characterization-of-$\mathbb{A}^n$ programs and to motivic/$\mathbb{A}^1$-homotopy methods.

**Best result.** Such methods recover the surface case and constrain candidate threefolds, and motivic-homotopy invariants (e.g. $\mathbb{A}^1$-homotopy sheaves) have been used to study cancellation and the related $\mathbb{A}^1$-contractibility of the Koras–Russell threefolds.

**Barrier.** Contractibility and trivial invariants are *necessary* but provably *not sufficient*: the Russell cubic is contractible yet is not $\mathbb{A}^3$. Topology alone cannot decide cancellation, which is why finer algebraic ($\mathbb{G}_a$-action) data is unavoidable.
