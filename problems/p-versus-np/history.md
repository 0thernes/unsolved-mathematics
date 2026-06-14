# History — P versus NP

_Origin, formulation, and timeline._

The $\mathrm{P}$ versus $\mathrm{NP}$ problem asks whether every decision problem whose "yes" instances admit a short, polynomial-time *verifiable* certificate can also be *solved* in polynomial time. In symbols: does the class $\mathrm{P}$ of problems decidable by a deterministic Turing machine in time $n^{O(1)}$ coincide with the class $\mathrm{NP}$ of problems solvable in nondeterministic polynomial time (equivalently, those with polynomially checkable witnesses)? It is the central open question of theoretical computer science and one of the seven Clay Millennium Prize Problems.

## Origins

The conceptual seed predates the formal definitions. In a now-famous 1956 letter to John von Neumann, Kurt Gödel asked, in essence, whether deciding the existence of a proof of length $n$ could be solved in time linear or quadratic in $n$ rather than by exhaustive search over $\sim 2^n$ possibilities. Gödel recognized the stakes: if brute force could be avoided, "the mental effort of the mathematician in the case of yes-or-no questions could be completely replaced by machines." The letter lay in obscurity until rediscovered and publicized in the 1980s.

The modern formulation crystallized independently on two sides of the Iron Curtain. In 1971 Stephen Cook, then at the University of Toronto, presented "The Complexity of Theorem-Proving Procedures" at the third ACM Symposium on Theory of Computing (STOC), proving that the Boolean satisfiability problem ($\mathrm{SAT}$) is $\mathrm{NP}$-complete: every problem in $\mathrm{NP}$ reduces to it in polynomial time. Almost simultaneously, Leonid Levin in the Soviet Union proved an equivalent universality result for a family of search problems; his work, circulated from 1971 and published in 1973, is why the foundational theorem is jointly called the **Cook–Levin theorem**. Richard Karp then showed in 1972 that 21 natural combinatorial problems are $\mathrm{NP}$-complete, demonstrating the phenomenon was ubiquitous rather than exotic. Earlier, Jack Edmonds (1965) had articulated the "good algorithm" $=$ polynomial-time thesis, and Alan Cobham and Michael Rabin had independently argued for polynomial time as the boundary of feasibility.

## Reformulations

The problem wears many equivalent faces: the existence of a polynomial-time algorithm for $\mathrm{SAT}$ or any single $\mathrm{NP}$-complete problem; a question about Boolean circuit size (does every $\mathrm{NP}$ language have polynomial-size circuits?—the stronger nonuniform variant $\mathrm{NP} \subseteq \mathrm{P}/\mathrm{poly}$); via descriptive complexity, where Fagin's theorem (1974) characterizes $\mathrm{NP}$ as exactly the properties expressible in existential second-order logic; and via proof complexity, where short propositional proofs of tautologies bear on $\mathrm{NP}$ vs. $\mathrm{coNP}$.

## Timeline

- **1956** — Kurt Gödel's letter to von Neumann poses the essential question of search vs. verification time.
- **1965** — Jack Edmonds frames polynomial time as the criterion for a "good" (efficient) algorithm; Hartmanis and Stearns inaugurate computational complexity as a field.
- **1971** — Stephen Cook proves $\mathrm{SAT}$ is $\mathrm{NP}$-complete (STOC); Leonid Levin's equivalent universality result circulates in the USSR.
- **1972** — Richard Karp's "Reducibility Among Combinatorial Problems" gives 21 $\mathrm{NP}$-complete problems.
- **1973** — Levin's paper formally published in *Problemy Peredachi Informatsii*.
- **1974** — Ronald Fagin characterizes $\mathrm{NP}$ in existential second-order logic.
- **1975** — Baker, Gill, and Solovay prove the **relativization barrier**: the question has opposite answers under different oracles, so no "black-box" argument can settle it; Ladner shows $\mathrm{NP}$-intermediate problems exist if $\mathrm{P} \neq \mathrm{NP}$.
- **1979** — Garey and Johnson's *Computers and Intractability* codifies $\mathrm{NP}$-completeness for a generation.
- **1985–87** — Razborov proves superpolynomial monotone circuit lower bounds for clique; circuit complexity surges.
- **1994** — Razborov and Rudich identify the **natural proofs barrier**.
- **2000** — The Clay Mathematics Institute names $\mathrm{P}$ vs. $\mathrm{NP}$ a Millennium Prize Problem ($\$1{,}000{,}000$).
- **2008** — Aaronson and Wigderson formulate the **algebrization barrier**, extending relativization to algebraic techniques.
- **2010** — Vinay Deolalikar circulates a claimed proof that $\mathrm{P} \neq \mathrm{NP}$; the community identifies fatal gaps within weeks.
- **2010s–present** — Geometric Complexity Theory (Mulmuley–Sohoni) and proof-complexity programs continue; the problem remains open, widely conjectured to satisfy $\mathrm{P} \neq \mathrm{NP}$.
