# Approaches — The Eilenberg–Ganea Conjecture

_Major strategies, partial results, and barriers._

The conjecture is binary: a group $G$ with $\operatorname{cd}(G)=2$ has $\operatorname{gd}(G)\in\{2,3\}$, and one must either show $3$ never occurs or build a group where it does. Attacks split into "prove it" lines (verify on ever-larger classes) and "break it" lines (engineer a counterexample). Both confront a sharp algebraic core.

## Algebraic core: $D(2)$ and the relation module

The geometric content reduces to a question about chain complexes. If $\operatorname{cd}(G)=2$, the trivial module $\mathbb{Z}$ has a length-$2$ projective resolution. To get a $2$-dimensional $K(G,1)$ one needs this realized by a **free**, geometrically-realizable resolution coming from a presentation $2$-complex whose attaching maps kill all of $\pi_2$. The obstruction is exactly whether a stably-free relation module can be replaced by a free one of the same rank realizing the presentation.

- **Core idea.** Translate $\operatorname{gd}\le 2$ into the existence of a finite aspherical $2$-complex, i.e. an algebraic **$D(2)$-condition**: a $3$-dimensional complex with the (co)homology of a $2$-complex must be homotopy equivalent to a $2$-complex.
- **Best result.** Wall's $D(2)$ program and its modern form (developed extensively by F.E.A. Johnson) verify the $D(2)$-property for many finite and infinite groups, converting Eilenberg–Ganea-type questions into computations in $K$-theory and the stable module category.
- **Barrier.** The reduction can fail to be free even when projective: the gap is governed by $\widetilde{K}_0(\mathbb{Z}G)$ and units/torsion phenomena. For $\operatorname{cd}=2$ the relevant modules need not be free, and no general argument forces freeness.

## Stallings–Swan analogy (dimension 1 as template)

- **Core idea.** Imitate the clean dimension-$1$ result: Stallings (f.g. case) and Swan (general) proved $\operatorname{cd}(G)=1 \iff G$ free $\iff \operatorname{gd}(G)=1$, via ends of groups and the structure of $\mathbb{Z}G$-modules of projective dimension $1$.
- **Best result.** A complete, clean classification in dimension $1$; it is the proof that $\operatorname{cd}=\operatorname{gd}$ in the only other "boundary" case.
- **Barrier.** The dimension-$1$ proof uses Stallings' theorem on ends and the fact that submodules of free $\mathbb{Z}G$-modules of pd $\le 0$ are free. No analogous structure theorem exists for pd-$2$ modules; the JSJ/accessibility tools that power dimension $1$ have no dimension-$2$ counterpart that controls $\pi_2$.

## Bestvina–Brady Morse theory (the counterexample engine)

- **Core idea.** From a flag simplicial complex $L$, build the Bestvina–Brady group $H_L$ as the kernel of a height map on a right-angled Artin group, and read its finiteness/dimension properties off the topology of $L$. Choosing $L$ acyclic but not simply connected separates $\mathrm{FP}_2$ from finite presentability.
- **Best result (1997).** Bestvina and Brady produced groups of cohomological dimension $2$ that are $\mathrm{FP}_2$ but not finitely presented. Crucially, they proved a **dichotomy**: at least one of the Eilenberg–Ganea conjecture and the Whitehead asphericity conjecture must be false. A suitable $H_L$ is the natural candidate counterexample.
- **Barrier.** The candidate groups are not finitely presented, so they do not directly contradict the (finitely-presented) Eilenberg–Ganea question; and computing their exact geometric dimension confronts the same $\pi_2$/relation-module obstruction. The dichotomy shows a counterexample exists *somewhere*, without locating it.

## Duality groups and $\ell^2$ / profinite invariants

- **Core idea.** Restrict to $2$-dimensional duality groups, Poincaré-duality groups in dimension $2$ (surface-like), or groups with strong finiteness, where extra structure may force a $2$-dimensional model. Use $\ell^2$-Betti numbers, deficiency, or profinite completions as obstructions.
- **Best result.** For $\mathrm{PD}_2$ groups the answer is known (they are surface groups, realized by surfaces, so $\operatorname{gd}=2$). Deficiency arguments confirm Eilenberg–Ganea for one-relator groups and many groups of small deficiency.
- **Barrier.** These methods need the relation module's rank to match the deficiency exactly; for general $\operatorname{cd}=2$ groups the deficiency may be strictly below what a $2$-complex requires, and $\ell^2$-invariants do not detect the difference between $\operatorname{gd}=2$ and $3$.

## Stable/algebraic $K$-theory of $\mathbb{Z}G$

- **Core idea.** Encode the obstruction to de-stabilizing a stably-free relation module to a genuinely free one as a class in $\widetilde{K}_0(\mathbb{Z}G)$ or in $SK_1$; vanishing of the relevant class yields $\operatorname{gd}=2$.
- **Best result.** For groups with trivial reduced projective class group and good Whitehead group ($\widetilde{K}_0(\mathbb{Z}G)=0$), the algebraic obstruction vanishes and Eilenberg–Ganea holds. This covers free, surface, and many polycyclic-by-finite cases.
- **Barrier.** $\widetilde{K}_0(\mathbb{Z}G)$ is nonzero for many infinite groups, and even when the algebraic obstruction vanishes, *realizing* the free resolution by attaching maps requires solving the $D(2)$ realization problem, which is not automatic.

## Summary of obstructions

Every successful line verifies the conjecture on classes where the **relation module is provably free** and the **$D(2)$-realization** goes through. Every attempted counterexample lands among **non-finitely-presented** groups or stalls at computing $\operatorname{gd}$ exactly. The two failure modes are precisely the two halves of the Bestvina–Brady dichotomy, which is why the problem has resisted resolution in either direction.
