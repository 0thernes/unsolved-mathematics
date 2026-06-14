# History — The Eilenberg–Ganea Conjecture

_Origin, formulation, and timeline._

## Origin and setting

The conjecture grows out of the theory of Eilenberg–MacLane spaces and the cohomology of groups, a subject Samuel Eilenberg helped found in the 1940s. To a discrete group $G$ one associates the classifying space $K(G,1)$ — an aspherical CW complex with $\pi_1 \cong G$ and all higher homotopy groups vanishing. Two integer invariants measure the minimal complexity of such a model:

- the **cohomological dimension** $\operatorname{cd}(G)$, the projective dimension of the trivial module $\mathbb{Z}$ over the group ring $\mathbb{Z}G$ (equivalently the largest $n$ with $H^n(G;M)\neq 0$ for some $\mathbb{Z}G$-module $M$);
- the **geometric dimension** $\operatorname{gd}(G)$, the minimal dimension of an aspherical CW model $K(G,1)$.

One always has $\operatorname{cd}(G) \le \operatorname{gd}(G)$. In their 1957 *Annals of Mathematics* paper "On the Lusternik–Schnirelmann category of abstract groups," Eilenberg and Ganea proved a near-coincidence of the two invariants. The clean statement of what they established is the **Eilenberg–Ganea theorem**: for $n \ge 3$, $\operatorname{cd}(G) = n$ implies $\operatorname{gd}(G) = n$. Combined with later work in dimensions $0$ and $1$, this leaves a single open case, $n = 2$.

## The precise statement

> **Eilenberg–Ganea Conjecture.** If $\operatorname{cd}(G) = 2$ then $\operatorname{gd}(G) = 2$; equivalently, every group of cohomological dimension $2$ admits a $2$-dimensional aspherical CW model.

The sole obstruction is the possible gap between $\operatorname{cd} = 2$ and $\operatorname{gd} = 3$. A potential counterexample would be a group $G$ with $\operatorname{cd}(G) = 2$ but $\operatorname{gd}(G) = 3$. By the Eilenberg–Ganea theorem together with a theorem of Wall (and the general inequality $\operatorname{gd}(G)\le\max(3,\operatorname{cd}(G))$), one has $\operatorname{gd}(G) \in \{2,3\}$ whenever $\operatorname{cd}(G) = 2$, so the question is genuinely binary.

A tightly related circle of problems — connecting Eilenberg–Ganea to the **Whitehead asphericity conjecture** and to the Stallings–Swan characterization of dimension $1$ — was sharpened by Bestvina and Brady (1997): under their constructions, the Eilenberg–Ganea conjecture and the Whitehead conjecture cannot both be true, tying the problem logically to another central open question.

## Timeline

- **1945–1953** — Eilenberg and MacLane develop $K(\pi,n)$ spaces and group cohomology, fixing the framework of $\operatorname{cd}$ and $\operatorname{gd}$.
- **1957** — Eilenberg and Ganea prove $\operatorname{cd}(G)=n \Rightarrow \operatorname{gd}(G)=n$ for $n\ge 3$; the $n=2$ case is isolated as the open conjecture.
- **1966–1968** — Stallings characterizes finitely generated groups of cohomological dimension $1$ as free groups.
- **1969** — Swan removes the finite-generation hypothesis: $\operatorname{cd}(G)=1 \iff G$ is free, settling dimension $1$ fully and confirming $\operatorname{cd}=\operatorname{gd}$ there.
- **1970s** — Wall, Brown, and others sharpen the relationship between algebraic and geometric finiteness, framing the $\operatorname{gd}\le\operatorname{cd}+1$ phenomenon and the role of the $\mathrm{FP}_n$ conditions.
- **1997** — Bestvina and Brady introduce discrete Morse theory on cube complexes, producing groups that distinguish the finiteness properties $\mathrm{FP}_2$ and finite presentability, and prove that not both the Eilenberg–Ganea and Whitehead conjectures can hold.
- **2000s** — Survey treatments (Brown's textbook, Bestvina's "Questions") crystallize the consensus that the conjecture is plausibly true but that no current method addresses the $\operatorname{cd}=2$ case directly.
- **2010s–present** — Work on duality groups, $\mathrm{FP}_2$ groups, right-angled and Artin-type structures, and profinite/$\ell^2$ invariants keeps the question active. The conjecture remains **open**: no group exhibiting $\operatorname{cd}=2,\ \operatorname{gd}=3$ has been found, and no proof that none exists is known.
