# Approaches — The Baum–Connes Conjecture

_Major strategies, partial results, and barriers._

The conjecture is naturally split into **injectivity** (which yields the Novikov conjecture and is governed by coarse geometry) and **surjectivity** (the hard, "exotic K-theory" half). Almost all positive results factor the assembly map through a richer category — Kasparov's $KK$-theory or a Banach analogue — and exhibit a homotopy or factorization that forces it to be an isomorphism.

## Dirac–dual-Dirac method (Kasparov)

The dominant technique. One seeks a proper $G$-space $X$ with a "Dirac" element $\alpha \in KK^G(C_0(X), \mathbb{C})$ and a "dual-Dirac" element $\beta \in KK^G(\mathbb{C}, C_0(X))$ whose Kasparov product $\gamma = \beta\otimes\alpha$ is an idempotent in the representation ring $KK^G(\mathbb{C},\mathbb{C})$. If $\gamma = 1$, the assembly map is an isomorphism. **Best result:** proves the conjecture (with coefficients) for all groups acting properly isometrically on a complete Riemannian manifold of nonpositive curvature, on Bruhat–Tits buildings, on bolic spaces, and on Hilbert space — covering closed subgroups of connected Lie groups, hyperbolic groups, and amenable groups. **Barrier:** for groups with **Property (T)**, $\gamma \neq 1$ in $C^*$-theory — the "$\gamma$-element" obstruction is genuine, and the method cannot reach surjectivity without leaving the $C^*$-algebraic world.

## Haagerup property / a-T-menability (Higson–Kasparov)

If $G$ acts properly and affinely-isometrically on a Hilbert space (the Haagerup property), a Dirac–dual-Dirac argument in infinite dimensions, using the Bott periodicity of an infinite-dimensional Clifford/oscillator construction, forces $\gamma = 1$. **Best result (Higson–Kasparov, 2001):** the full conjecture **with coefficients** for all a-T-menable groups — all amenable, free, one-relator with torsion, Coxeter, and many discrete groups. **Barrier:** Property (T) is exactly the negation of the Haagerup property, so this route is structurally blind to higher-rank lattices.

## Banach $KK$-theory and Property (T) (Lafforgue)

Lafforgue's breakthrough was to replace $C^*$-algebra $KK$-theory by a version built on Banach algebras and unconditional completions, in which the Property-(T) obstruction to $\gamma = 1$ dissolves because the relevant representations need not be unitary. **Best result:** the conjecture (without coefficients) for cocompact lattices in $SL_2(\mathbb{Q}_p)$, $Sp(n,1)$, rank-one Lie groups, and — after his 2012 work on **strong Property (T)** — for all hyperbolic groups and their lattices. **Barrier:** higher-rank lattices such as $SL_3(\mathbb{Z})$, $SL_n(\mathbb{Z})$ ($n\ge 3$), and lattices in higher-rank $p$-adic groups satisfy strong forms of Property (T) that obstruct even the Banach approach; surjectivity here is open.

## Controlled / coarse geometry and Property A (Yu, Skandalis–Tu–Yu)

For the **injectivity** half (hence Novikov), Yu's coarse Baum–Connes machinery shows that any group that **coarsely embeds into Hilbert space** — in particular every group with **Property A / exactness** — satisfies the strong Novikov conjecture and injectivity of assembly. **Best result:** injectivity / Novikov for an enormous class of finitely generated groups. **Barrier:** Gromov's randomly-constructed **monster groups** contain expanders and do **not** coarsely embed into Hilbert space; on them the *maximal* coarse assembly map behaves very differently from the *reduced* one.

## Going-Down / restriction and almost-connected groups (Chabert–Echterhoff–Nest)

A homological/permanence strategy: verify the conjecture on compact-open or maximal-compact subgroups and propagate via the **Going-Down principle**, the **Mayer–Vietoris** and **continuity** properties of the Kasparov category, and the structure theory of locally compact groups. **Best result:** the conjecture for **almost-connected groups** and for the group of rational points of a linear algebraic group over a local field of characteristic zero (Chabert–Echterhoff–Nest, building on Connes–Kasparov). **Barrier:** the method needs the conjecture as input on building blocks and good structural reductions; it does not by itself crack the residually-finite higher-rank discrete lattices.

## Categorical / homological algebra (Meyer–Nest)

Meyer and Nest recast assembly as a derived functor: the Baum–Connes assembly map is the localization of the equivariant Kasparov category at the subcategory of compactly-induced (weakly contractible) objects, with a spectral sequence converging to $K_*(C^*_r G)$. This clarifies *why* the conjecture can fail with coefficients and isolates the precise obstruction class. **Best result:** a conceptual framework that reproves permanence properties and frames the counterexamples; it explains the failure-with-coefficients as a non-vanishing derived term. **Barrier:** it reorganizes rather than removes the analytic difficulty for Property-(T) groups.

## Negative results and the central obstruction

The **Higson–Lafforgue–Skandalis counterexamples (2003)** show the conjecture **with coefficients** is false: Gromov monster groups containing expanders make the reduced crossed product fail exactness, breaking surjectivity. This rules out any proof of the plain conjecture that passes through the coefficient version in full generality and pinpoints **expanders / non-exactness / Property (T)** as the true obstruction to a uniform method.
