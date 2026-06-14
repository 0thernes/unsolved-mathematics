# Status & Frontier — The Dixmier Conjecture

_Where the problem stands and what a resolution would require._

**Status: open**, in every dimension $n \ge 1$, including the original first Weyl algebra $A_1$. There is no accepted proof and no counterexample. Metadata flags it open, and that reflects the consensus.

## What is known

**Unconditional.**
- $A_1$ is a simple Noetherian domain (Dixmier, 1968), so every nonzero endomorphism is injective; the entire problem is the surjectivity of injective endomorphisms.
- The conjecture holds for endomorphisms compatible with the Bernstein filtration and for bounded-degree images — the "tame" regime.
- $\mathrm{Aut}(A_1)$ is fully understood (tame, an analogue of Jung–van der Kulk for $\mathrm{Aut}(\mathbb{A}^2)$).

**Conditional / equivalence.**
- The **stable Dixmier conjecture is equivalent to the stable Jacobian conjecture**: $\mathrm{DC}_n$ corresponds to $\mathrm{JC}_{2n}$. This was proved by **Yoshifumi Tsuchimoto** (2005; full version, *Osaka J. Math.*, 2008) and independently by **Alexei Belov-Kanel and Maxim Kontsevich**, *"The Jacobian conjecture is stably equivalent to the Dixmier conjecture,"* Moscow Mathematical Journal 7 (2007), 209–218 (preprint arXiv:math/0512171, needs-verification on exact number). Consequently, a proof of the Jacobian conjecture in dimension $2n$ would prove $\mathrm{DC}_n$, and conversely.

So the Dixmier conjecture is now exactly as open — and as hard — as the Jacobian conjecture, which is unresolved even for $\mathbb{A}^2$.

## What a full resolution requires

A complete proof must control the **non-filtered, unbounded-degree** endomorphisms — precisely the case that special-case methods do not reach and that, via the equivalence, encodes the missing degree bounds of the Jacobian conjecture. Equivalently, one must show that any $P,Q \in A_1$ with $[P,Q]=1$ generate all of $A_1$, with no a-priori degree hypothesis. A counterexample, conversely, would furnish (by the equivalence) a counterexample to the Jacobian conjecture in some dimension — widely believed not to exist.

## Plausible routes

1. **Prove the Jacobian conjecture** (any dimension $2n$) by commutative-algebra or degree-reduction methods; Dixmier follows in dimension $n$.
2. **Symplectomorphism / tropical-limit program** (Belov-Kanel–Kontsevich–Elishev–Yu): establish $\mathrm{Aut}(A_n)\cong\mathrm{Aut}(P_n)$ and extend the control from automorphisms to endomorphisms via augmentation topology and lifting.
3. **Mathieu–Zhao subspace / image-conjecture route** (Zhao): resolve the vanishing-trace reformulation of invertibility.
4. **Holonomic / $p$-curvature refinements** that extract an effective degree bound directly on the Weyl-algebra side.

No route currently yields an unconditional proof, and all funnel into the same hard core.

## Related problems

- [Jacobian Conjecture](../jacobian-conjecture/) — stably equivalent twin; the central related open problem.
- [Zariski Cancellation Problem](../zariski-cancellation-problem/) — sibling rigidity/cancellation question in affine algebra.
- [Köthe Conjecture](../kothe-conjecture/) — a major open problem in noncommutative ring theory.
- [Invariant Subspace Problem](../invariant-subspace-problem/) — companion structural question on operators.
- [Connes Embedding Aftermath](../connes-embedding-aftermath/) — adjacent operator-algebra frontier in Dixmier's own tradition.
