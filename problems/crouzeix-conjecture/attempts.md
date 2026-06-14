# Attempts — Crouzeix's Conjecture

_Notable attempts, near-misses, retracted proofs._

**The progression of universal constants.** The defining storyline of the conjecture is a sequence of decreasing absolute constants, each a genuine theorem, none yet reaching the conjectured $2$.

- Crouzeix's own qualitative result (2004) established finiteness with a large constant.
- Crouzeix (2007, J. Funct. Anal.) obtained the first clean explicit value, $\|p(A)\|\le 11.08\,\|p\|_{W(A)}$. This was the reference bound for a decade.
- **Crouzeix–Palencia (2017)** is the celebrated near-miss: $\|p(A)\|\le (1+\sqrt 2)\,\|p\|_{W(A)} \approx 2.4142$. It is widely regarded as the single most important step, bringing the constant within $21\%$ of the target by an elegant boundary-pairing argument. It is *not* a proof of the conjecture, and the authors were explicit that the factor $1+\sqrt 2$ is an artifact of their symmetrization rather than the true value.

**Refinements of Crouzeix–Palencia.** Ransford and Schwenninger (2018, and subsequent work) re-derived and analyzed the $1+\sqrt 2$ bound, clarifying exactly where the slack enters. A key cautionary finding is that the *unmodified* Crouzeix–Palencia mechanism cannot be pushed below a constant near $2.4$: the natural inequalities it relies on are essentially tight at that value, so improvements require structurally new ingredients, not just sharper estimates within the same scheme. Several authors have since obtained small unconditional improvements or conditional bounds approaching $2$ under extra hypotheses on $A$ or on $\partial W(A)$, but no unconditional value strictly between the conjectured $2$ and roughly $2.4$ has displaced $1+\sqrt 2$ in full generality.

**Settled special cases (genuine partial results, not over-claims).**

- **$2\times 2$ matrices:** fully proved with the sharp constant $2$. The numerical range is an ellipse, and an explicit conformal map plus a Blaschke-product computation closes the case. This both confirms the conjecture and certifies that $2$ is optimal, since these examples approach the ratio $2$.
- **Matrices with circular (disc) numerical range:** the constant $2$ holds and is sharp, recovered cleanly via the Okubo–Ando dilation.
- **Nilpotent Jordan blocks** and certain **tridiagonal Toeplitz** families: verified.
- **Various $3\times 3$ classes:** confirmed, though a fully general $3\times 3$ proof has been notably stubborn, with the hardest configurations involving boundary contact and near-coalescing eigenvalues.

**Disputed or retracted claims.** Crouzeix's conjecture is unusual among famous open problems in that it has *not* attracted a notable corpus of publicized, formally retracted "proofs." Its difficulty is granular — the obstacle is the last factor between $2$ and $2.414$, not a binary all-or-nothing barrier — which discourages sweeping false claims. From time to time preprints announce improvements on the universal constant or claim the full result; the responsible reading is that, as of the latest reliable literature, **no general proof of the constant $2$ has been accepted by the community**, the best unconditional theorem remains in the neighborhood of $1+\sqrt 2$, and any claim to the contrary should be checked against the published record. We flag such claims neutrally rather than endorse them.

**Computational near-misses.** Extensive numerical optimization (Greenbaum–Overton, Choi, and collaborators) has searched for a matrix–polynomial pair violating the constant $2$. None has been found; the observed supremum of $\|p(A)\|/\|p\|_{W(A)}$ sits at or just below $2$, and extremal-seeking runs converge to nearly degenerate matrices saturating $2$ in the limit. This is strong evidence for optimality and against any constant below $2$, but it is evidence, not proof.
