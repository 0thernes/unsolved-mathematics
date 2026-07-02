# History — The Collatz Conjecture

_Origin, formulation, and timeline._

## How the problem arose

The Collatz conjecture concerns the deceptively elementary map on the positive integers
$$
T(n) = \begin{cases} n/2 & n \equiv 0 \pmod 2,\\ 3n+1 & n \equiv 1 \pmod 2.\end{cases}
$$
The conjecture asserts that for every $n \in \mathbb{Z}^{+}$, repeated application of $T$ eventually reaches $1$ (after which the trajectory enters the cycle $1 \to 4 \to 2 \to 1$). Because $3n+1$ is always even, many authors prefer the **accelerated (Syracuse) map** $T(n) = (3n+1)/2$ for odd $n$ and $n/2$ for even $n$, which makes the dynamics easier to analyze without changing the conjecture.

The problem traces to **Lothar Collatz**, who recorded iteration problems of this flavor in his notebooks beginning around **1937**, shortly after completing his doctorate. Collatz never published the $3n+1$ problem formally; it circulated orally and by correspondence, which is why the conjecture acquired an unusually large number of names: the **Syracuse problem**, the **Ulam conjecture** (after Stanisław Ulam, who discussed it at Los Alamos), **Kakutani's problem** (Shizuo Kakutani popularized it in the 1950s–60s), **Thwaites' conjecture** (Bryan Thwaites, who offered a prize in 1996), and the **Hasse algorithm** (after Helmut Hasse, who lectured on it). The folklore that it "circulated through every major mathematics department" dates to this mid-century oral spread.

## Reformulations

Several equivalent or closely related framings sharpened the problem over time. The **stopping-time** formulation asks whether every $n>1$ has a finite first time at which the trajectory drops below $n$. The **parity-vector / 2-adic** formulation (Hedlund, Lagarias) encodes a trajectory's odd/even pattern as a $2$-adic integer and recasts the question as a property of the extension of $T$ to $\mathbb{Z}_2$. The conjecture also splits into two logically independent claims: **(a)** no nontrivial cycles exist, and **(b)** no trajectory diverges to infinity.

## Timeline

- **1937** — Lothar Collatz formulates iteration problems including the $3n+1$ map in his notebooks; the problem begins to spread informally.
- **1950s** — Shizuo Kakutani circulates the problem widely; it becomes known as the "Syracuse problem"; Ulam discusses it at Los Alamos.
- **1972** — Early systematic computational checks confirm convergence for modest ranges; the problem gains broad notoriety.
- **1976** — Riho Terras proves that **almost all** integers (natural density $1$) have a finite stopping time, the first major density result.
- **1977** — C. J. Everett independently obtains analogous almost-all results.
- **1978** — Work of Robert Tijdeman, R. P. Steiner and others establishes nontrivial constraints on hypothetical cycles; Steiner rules out "$1$-cycles."
- **1985** — Jeffrey C. Lagarias publishes "The $3x+1$ problem and its generalizations," the survey that organizes the field and frames the modern questions.
- **1994** — Ilia Krasikov derives nonlinear-programming bounds on the count of integers reaching $1$; later refined by **Krasikov–Lagarias (2003)** to $\#\{n \le x : n \to 1\} \gg x^{0.84}$.
- **1996** — Bryan Thwaites publicly offers £1,000 for a proof or disproof.
- **1998–2011** — Tomás Oliveira e Silva runs large-scale distributed verification, pushing the verified bound past $10^{18}$ and beyond.
- **2007** — John H. Conway's earlier work on FRACTRAN-style generalizations is widely cited as evidence that the broader family of such maps is **algorithmically undecidable**.
- **2011** — Cycle-exclusion bounds (Shalom Eliahou's $3 \cdot 10^{8}$-style estimates and successors) push the minimal length of any nontrivial cycle into the hundreds of millions.
- **2019** — Terence Tao proves that **almost all** Collatz orbits (in a strong logarithmic-density sense) attain **almost bounded** values, the strongest unconditional progress to date.
- **2020** — Distributed verification (David Bařina, continuing the Oliveira e Silva project) confirms convergence for all $n \le 2^{68} \approx 2.95 \times 10^{20}$.
- **2023** — Christian Hercher proves there are no Collatz $m$-cycles with $m \le 91$ (*J. Integer Seq.* **26**, art. 23.3.5; arXiv:2201.00406), sharply extending the Simons–de Weger bounds.
- **2025** — Bařina's continued GPU verification reaches all $n < 2^{71} \approx 2.36 \times 10^{21}$ (*J. Supercomput.* **81**, 810); combined with Hercher's threshold this forces any nontrivial cycle to contain at least $1.375 \times 10^{11}$ odd terms.
- **2020s** — Active work on the cycle problem, $2$-adic and ergodic models, and undecidability connections; the conjecture remains open.
