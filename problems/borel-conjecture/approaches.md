# Approaches — The Borel Conjecture

_Major strategies, partial results, and barriers._

## Surgery theory and the structure set

**Core idea.** The Browder–Novikov–Sullivan–Wall surgery program reduces classification of manifolds homotopy equivalent to a fixed $M^n$ ($n\geq 5$) to the **surgery structure set** $\mathcal S^{\mathrm{TOP}}(M)$, which sits in the surgery exact sequence
$$ \cdots \to L_{n+1}(\mathbb Z\pi) \to \mathcal S^{\mathrm{TOP}}(M) \to [M,G/\mathrm{TOP}] \xrightarrow{\;\sigma\;} L_n(\mathbb Z\pi). $$
The Borel Conjecture for $M$ is *equivalent* to $\mathcal S^{\mathrm{TOP}}(M)=\{*\}$ (rigidity) together with vanishing of the relevant Whitehead group (so $h$-cobordisms are products). For aspherical $M$ the normal invariants $[M,G/\mathrm{TOP}]$ are governed by $H^*(M;\mathbf L)$, and triviality of $\mathcal S$ follows once the **assembly map** is an isomorphism.

**Best result.** A complete reduction: Borel rigidity in dimensions $\geq 5$ ⇔ the $L$-theoretic Farrell–Jones isomorphism plus $\mathrm{Wh}(\pi)=0$, $\widetilde K_0(\mathbb Z\pi)=0$.

**Barrier.** Surgery requires $n\geq 5$ (Whitney trick). Dimensions **3 and 4** lie outside; dimension 4 needs Freedman's topological surgery, which works only for "good" fundamental groups (a constrained class).

## Farrell–Jones via controlled topology and flows

**Core idea.** Farrell and Jones attack the assembly map directly using the dynamics of the **geodesic flow** on nonpositively curved manifolds, combined with **controlled $h$-cobordism** and **boundedness control** to split or invert assembly. The flow expands distances, allowing surgery obstructions to be pushed to infinity and absorbed.

**Best result.** The Borel Conjecture holds for closed Riemannian manifolds of **nonpositive sectional curvature** in dimensions $\neq 3,4$ (Farrell–Jones, 1989–1993), and for many word-hyperbolic and crystallographic groups. They also showed the *smooth* Borel statement is **false**, exhibiting homeomorphic-but-not-diffeomorphic negatively curved manifolds.

**Barrier.** The original method needs an actual nonpositively curved metric (geometry), excluding general aspherical manifolds whose groups carry no such structure.

## The Farrell–Jones Conjecture (assembly via $E_{\mathcal{VCyc}}\Gamma$)

**Core idea.** Reformulate everything as: the $K$- and $L$-theoretic assembly maps relative to the family $\mathcal{VCyc}$ of virtually cyclic subgroups,
$$ H_n^{\Gamma}(E_{\mathcal{VCyc}}\Gamma;\mathbf K/\mathbf L) \to K_n/L_n(\mathbb Z\Gamma), $$
are isomorphisms. The $L^{\langle-\infty\rangle}$-version **implies the Borel Conjecture** for closed aspherical manifolds with $\pi_1=\Gamma$ in dimension $\geq 5$; FJC is the central modern target because it is **inheritance-closed** (passes to subgroups, extensions, directed colimits, finite products, free/amalgamated products).

**Best result.** Bartels–Lück–Reich (2008–2012) proved FJC for **word-hyperbolic** groups; Bartels–Lück and Wegner for **CAT(0)** groups; later for lattices in virtually connected Lie groups, $\mathrm{GL}_n(\mathbb Z)$, $\mathrm{Out}(F_n)$-related and many relatively hyperbolic / solvable groups. This delivers Borel rigidity for an enormous family.

**Barrier.** No known proof for arbitrary groups; obstructions include groups with **no nonpositive-curvature geometry** (e.g. some amenable or exotic groups) and the difficulty of controlling flow spaces without geometric input. Key open targets: general **mapping class groups**, $\mathrm{Out}(F_n)$, and arbitrary residually finite or sofic groups.

## Controlled and bounded topology (Quinn, Chapman–Ferry)

**Core idea.** Replace geometric control by *abstract* metric control: the controlled $h$-cobordism and $\alpha$-approximation theorems (Chapman–Ferry) and Quinn's homology theory of $\mathbf{L}$-spectra let one prove local triviality of structure sets when obstructions can be shrunk below any $\varepsilon$.

**Best result.** The engine inside Farrell–Jones; yields rigidity whenever sufficient contraction toward a controlled space exists. Quinn's obstruction theory pins the assembly to a generalized homology theory.

**Barrier.** Producing the requisite contractions for groups without geometric models remains the central unsolved technical problem.

## Topological rigidity in dimension 4 (Freedman–Quinn)

**Core idea.** Use Freedman's topological surgery and the disk-embedding theorem for **good groups** (groups of subexponential growth / amenable, where Casson handles convert to embedded disks).

**Best result.** Borel-type rigidity for aspherical 4-manifolds with **good** $\pi_1$ — e.g. for poly-(finite or cyclic) and many solvable groups.

**Barrier.** The **disk-embedding conjecture** in dimension 4 is open for general (e.g. free, hyperbolic) groups; without it, 4-dimensional surgery — and hence Borel rigidity in dimension 4 — stalls. This is the same wall as the smooth 4D Poincaré problem.

## Geometrization in dimension 3

**Core idea.** In dimension 3 a closed aspherical manifold is irreducible with infinite $\pi_1$; Perelman's proof of **geometrization** (with the $K(\pi,1)$ structure) yields that such manifolds are determined by $\pi_1$.

**Best result.** Borel rigidity holds in dimension 3 as a **consequence of geometrization** (Perelman, 2003), modulo standard $3$-manifold topology (Waldhausen rigidity for Haken manifolds was the classical antecedent).

**Barrier.** This is special to dimension 3 and gives no leverage on the general conjecture; it is logically independent of the surgery/Farrell–Jones machinery.
