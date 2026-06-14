# History — The Andrews–Curtis Conjecture

_Origin, formulation, and timeline._

The Andrews–Curtis Conjecture (AC) was posed in 1965 by James J. Andrews and Morton L. Curtis in a short, technically dense note in the *Proceedings of the American Mathematical Society* titled "Free groups and handlebodies." Its roots lie in low-dimensional topology — specifically in the theory of $2$-dimensional CW-complexes and the geometry of handle decompositions — but the statement itself is purely combinatorial-group-theoretic, which is the source of both its accessibility and its notorious intractability.

The setting is that of group presentations. A presentation $\langle x_1,\dots,x_n \mid r_1,\dots,r_m\rangle$ is called **balanced** if $n=m$, i.e. the number of generators equals the number of relators. The trivial group $\{1\}$ admits the obvious trivial balanced presentation $\langle x_1,\dots,x_n \mid x_1,\dots,x_n\rangle$. The conjecture asserts:

> Every balanced presentation of the trivial group can be transformed into the trivial presentation of the same deficiency by a finite sequence of **elementary Andrews–Curtis moves**.

The AC-moves on the relator tuple are: (1) replace a relator $r_i$ by $r_i^{-1}$; (2) replace $r_i$ by $r_i r_j$ ($j\neq i$); (3) replace $r_i$ by a conjugate $w r_i w^{-1}$ for any word $w$ in the generators; and (4) the stabilization/destabilization move that adds or removes a generator $x_{n+1}$ together with the relator $x_{n+1}$. The variant that forbids move (4) — keeping the number of generators fixed — is the **simple (or elementary) Andrews–Curtis Conjecture (AC')**, while the **stable** version permits it. The stable conjecture is implied by, and is formally weaker than, the simple one.

The deeper motivation is the connection between these Nielsen-type transformations and $3$-deformations of $2$-complexes (the Whitehead simple-homotopy equivalences that add or remove cells of dimension $\le 3$). Andrews and Curtis showed the question is equivalent to asking whether every contractible $2$-complex $3$-deforms to a point. It is therefore a combinatorial cousin of questions surrounding the Poincaré conjecture and is closely tied to the **Zeeman conjecture**. A potential counterexample would be a balanced presentation of the trivial group that is genuinely "knotted" — algebraically trivial yet combinatorially irreducible.

The history since 1965 is a story of accumulating candidate counterexamples on one side and ever-larger computational verifications on the other. The most famous candidates are the **Akbulut–Kirby presentations** $AK(n) = \langle x,y \mid x^n = y^{n+1},\ xyx = yxy\rangle$ (1985); $AK(2)$ was eventually shown to be AC-trivial, leaving $AK(3)$ as a long-standing open test case. Miller and Schupp introduced another influential family. Modern work is dominated by computer search — breadth-first search, genetic algorithms, and since 2021 deep reinforcement learning — which has trivialized many candidates and thereby reshaped, without resolving, expert belief.

### Timeline

- **1939** — J. H. C. Whitehead develops simple-homotopy theory and the theory of $3$-deformations of $2$-complexes, the topological backdrop for AC.
- **1965** — J. J. Andrews and M. L. Curtis pose the conjecture in "Free groups and handlebodies" (*Proc. AMS* 16).
- **1966** — Andrews and Curtis extend the framework, linking the problem to handlebody theory and $2$-complexes.
- **1975** — Connections between AC, the Zeeman conjecture, and Whitehead's deformation questions are clarified (Wright and others).
- **1979** — C. F. Miller III and P. E. Schupp produce balanced presentations conjectured to be potential counterexamples.
- **1984–1985** — S. Akbulut and R. Kirby introduce the $AK(n)$ family as candidate counterexamples arising from Dehn-surgery and $4$-manifold considerations.
- **1993** — R. G. Burns and O. Macedońska study AC-moves and balanced transformations algebraically.
- **1999** — A. D. Miasnikov applies genetic algorithms to search for AC-trivializations.
- **2006** — Miasnikov–Myasnikov and collaborators survey computational attacks; $AK(2)$ remains a focus.
- **2016** — M. R. Bridson constructs presentations with explicit (super-exponential) lower bounds on trivialization length, showing AC can be true yet astronomically hard.
- **2019** — D. Panteleev and A. Ushakov trivialize $AK(2)$ and several Miller–Schupp presentations via large-scale search.
- **2021–2024** — Reinforcement-learning approaches (including work by Shehper, Halverson, and collaborators) resolve large swaths of the Miller–Schupp family, shrinking the open candidate set.
- **Present** — $AK(3)$ and certain Miller–Schupp presentations remain open; the conjecture is unresolved in both stable and simple forms.
