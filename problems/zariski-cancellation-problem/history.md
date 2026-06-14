# History — The Zariski Cancellation Problem

_Origin, formulation, and timeline._

## Origin and motivation

The cancellation problem grows out of a deceptively elementary question about affine space. Write $\mathbb{A}^n_k$ for affine $n$-space over a field $k$, with coordinate ring the polynomial algebra $k[x_1,\dots,x_n]$. The **Zariski Cancellation Problem (ZCP)** asks: if a variety $X$ satisfies
$$X \times \mathbb{A}^1_k \cong \mathbb{A}^{n+1}_k,$$
must $X \cong \mathbb{A}^n_k$? Equivalently, in algebraic language: if $A$ is a finitely generated $k$-algebra and $A[t]\cong k[x_1,\dots,x_{n+1}]$ as $k$-algebras, must $A\cong k[x_1,\dots,x_n]$? The name reflects the desire to "cancel" the common factor $\mathbb{A}^1$. The terminology and the popularization of the problem trace to Oscar Zariski; the question circulated orally in the late 1940s, and Zariski is reported to have raised it in seminars around 1949, in connection with his program on the birational and biregular structure of algebraic varieties.

A closely related, even older instinct is the *cancellation of indeterminates* in ring theory: does $A[t]\cong B[t]$ force $A\cong B$? This fails in general (Hochster's 1972 counterexample with non-trivial vector bundles), so ZCP is special to the case where the larger ring is itself a polynomial ring — the rigidity of affine space is what makes the question subtle and important.

## Reformulations

Several equivalent or adjacent formulations shaped the field. The **biregular** (variety-theoretic) version asks for an isomorphism of varieties; the **stable** version concerns $X\times\mathbb{A}^m$. A central reformulation passes through **invariants**: to distinguish a candidate $X$ from $\mathbb{A}^n$ one seeks computable algebraic invariants of $A$ that are insensitive to adding a polynomial variable. The Makar-Limanov invariant (the ring of absolute constants of all locally nilpotent derivations) became the decisive such tool. A second reformulation is **fibration-theoretic**: $\mathbb{A}^1$-fibrations and the behaviour of additive group ($\mathbb{G}_a$) actions on $A$.

## Timeline

- **1949** — Oscar Zariski raises the cancellation question for affine space in seminar discussions.
- **1972** — Mel Hochster gives a counterexample to *general* algebra cancellation ($A[t]\cong B[t]$, $A\not\cong B$), sharpening why ZCP is special.
- **1972–75** — Abhyankar, Eakin, Heinzer establish $n=1$: a curve whose cylinder is a plane is the line.
- **1976** — Fujita, Miyanishi, Sugie prove ZCP for surfaces in characteristic $0$ ($n=2$): $X\times\mathbb{A}^1\cong\mathbb{A}^3 \Rightarrow X\cong\mathbb{A}^2$.
- **1980** — Russell, and independently work extending Miyanishi–Sugie, address $n=2$ in positive characteristic via $\mathbb{A}^1$-fibration techniques.
- **1987** — Kambayashi–Russell and related work develop the framework of locally nilpotent derivations for the problem.
- **1996** — Makar-Limanov introduces the AK (Makar-Limanov) invariant, showing the Russell cubic threefold $x+x^2y+z^2+t^3=0$ is *not* $\mathbb{A}^3$.
- **2003** — Kaliman–Makar-Limanov, and Crachiola, refine ML-invariant methods; the Russell cubic is shown to be an exotic $\mathbb{A}^3$-form, central to threefold cancellation.
- **2014** — **Neena Gupta** proves ZCP is **FALSE** in positive characteristic for $n\ge 3$: she constructs $A$ with $A[t]\cong k[x_1,\dots,x_{n+1}]$ yet $A\not\cong k[x_1,\dots,x_n]$, using the Asanuma threefolds and a sharpened Makar-Limanov invariant.
- **2014** — Gupta further settles the characteristic-$p$ case for $\dim X = 3$ definitively, drawing on Asanuma's 1987 deformation constructions.
- **2010s–present** — Characteristic $0$ remains **open** for $n\ge 3$; the threefold case (does $X\times\mathbb{A}^1\cong\mathbb{A}^4$ in char $0$ imply $X\cong\mathbb{A}^3$?) is the live frontier, studied via $\mathbb{G}_a$-actions, the Russell-type threefolds, and exponential maps.

The state of the art is thus sharply bifurcated: **resolved negatively in positive characteristic** (Gupta), **resolved positively for $n\le 2$ in characteristic $0$**, and **open for $n\ge 3$ in characteristic $0$**.
