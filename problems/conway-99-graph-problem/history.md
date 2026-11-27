# History — Conway's 99-Graph Problem

_Origin, formulation, and timeline._

A **strongly regular graph** $\mathrm{srg}(v, k, \lambda, \mu)$ is a $k$-regular graph on $v$ vertices where every pair of adjacent vertices shares $\lambda$ common neighbors and every pair of non-adjacent vertices shares $\mu$ common neighbors. Consider the family with $\lambda = 1$ (every edge lies in a unique triangle) and $\mu = 2$ (every non-edge is the diagonal of a unique $4$-cycle). Elementary feasibility conditions (the integrality of adjacency-matrix eigenvalues and the parity of $k$, since each neighborhood is a union of disjoint edges!) restrict the possible parameter sets $(v, k, 1, 2)$ to **only five** candidates:
- $(v, k) = (9, 4)$ — **exists** (the $3 \times 3$ rook's graph / Paley(9));
- $(v, k) = (99, 14)$ — **OPEN** (Conway's 99-graph!);
- $(v, k) = (243, 22)$ — **exists** (the Berlekamp–van Lint–Seidel graph from the ternary Golay code!);
- $(v, k) = (6273, 112)$ — **OPEN**;
- $(v, k) = (494019, 994)$ — **OPEN**.

Around 1970 (and famously publicized in his 2017 *Five \$1,000 Problems* list), John Horton Conway offered **\$1,000** for deciding whether $\mathrm{srg}(99, 14, 1, 2)$ exists. Despite passing **every** known algebraic, spectral, Krein, and local-subgraph feasibility test — and sitting right between two extraordinarily symmetric existing graphs ($v = 9$ and $v = 243$) — neither an explicit construction nor a non-existence proof has ever been found.

## Timeline

- **1970s** — Conway poses the existence of $\mathrm{srg}(99, 14, 1, 2)$ (the "99-graph") as a test case for strongly regular graph feasibility.
- **1973** — Berlekamp, van Lint, and Seidel construct $\mathrm{srg}(243, 22, 1, 2)$ via the ternary Golay code, proving the $(1, 2)$ family does not terminate at $v = 9$.
- **1984–2010** — Wilbrink, Makhnev, Minakova, and Brouwer heavily restrict any putative automorphism group of a 99-graph: it cannot be vertex-transitive, and any prime dividing $|\mathrm{Aut}(G)|$ must lie in $\{2, 3\}$ (no element of order $5, 7, 11$ can act on it!).
- **2014–2017** — Conway renews his **\$1,000 prize** in *Five \$1,000 Problems* (published 2017).
- **2017** — Zehavi and de Olivera explore algebraic and computational obstructions (`arXiv:1707.08047`).
- **2022** — Brouwer and Van Maldeghem summarize the complete state of knowledge in *Strongly Regular Graphs* (`10.1017/9781009057226`): $|\mathrm{Aut}(G)|$ is severely constrained (orders of involutions and 3-elements almost exhaustively ruled out), making any surviving 99-graph nearly asymmetric!
- **2026** — Active structural/computational attacks continue (e.g., Natal & Al-saadi, `arXiv:2610.16266`, analyzing spanning subgraphs of Conway's 99-graph), while existence remains completely open.
