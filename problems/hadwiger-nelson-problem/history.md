# History — The Hadwiger–Nelson Problem

_Origin, formulation, and timeline._

The Hadwiger–Nelson problem asks for the **chromatic number of the plane**, denoted $\chi(\mathbb{R}^2)$ or simply $\chi$: the minimum number of colors needed to color every point of the Euclidean plane so that no two points at distance exactly $1$ receive the same color. Equivalently, it is the chromatic number of the infinite **unit-distance graph** $G(\mathbb{R}^2)$, whose vertices are all points of the plane and whose edges join pairs at distance $1$. The problem lies at the crossroads of combinatorial geometry, graph coloring, and Euclidean Ramsey theory.

The problem was first formulated in 1950 by **Edward Nelson**, then an 18-year-old student, who asked how many colors are needed and quickly observed a lower bound of $4$. **John Isbell**, a fellow student, supplied the upper bound of $7$ shortly thereafter using a hexagonal tiling. Thus from the outset it was known that $4 \le \chi \le 7$. The problem circulated by word of mouth — through Paul Erdős, who popularized it widely, and Hugo Hadwiger, whose work on tilings and whose later expository writing attached his name to the geometric circle of ideas. The first published appearances are usually credited to **Martin Gardner's** October 1960 *Scientific American* "Mathematical Games" column and to a 1961 paper by Hadwiger. Erdős repeatedly advertised the problem and offered small prizes, cementing its status as a celebrated open question.

For 68 years the bounds $4 \le \chi \le 7$ stood unimproved, despite intense effort and the problem's deceptive simplicity. The lower bound $\chi \ge 4$ follows from the **Moser spindle**, a 7-vertex unit-distance graph (introduced by Leo and William Moser in 1961) that requires $4$ colors. The upper bound $\chi \le 7$ follows from coloring a tiling by regular hexagons of diameter slightly less than $1$ with $7$ colors in a repeating pattern. Whether the true value was $4$, $5$, $6$, or $7$ remained completely open.

The decisive event came in **April 2018**, when **Aubrey de Grey** — better known for work in biogerontology, but an accomplished amateur combinatorialist — posted "The chromatic number of the plane is at least 5" on the arXiv. De Grey exhibited an explicit unit-distance graph with $1581$ vertices that is not $4$-colorable, raising the lower bound to $\chi \ge 5$ for the first time. The construction was verified by SAT solvers and by independent researchers within days. Almost immediately a **Polymath project (Polymath16)** formed online to digest, simplify, and extend the result; it succeeded in driving down the vertex count of $5$-chromatic unit-distance graphs dramatically. The current bracket is $5 \le \chi \le 7$, and which of $5$, $6$, $7$ is correct remains the open frontier.

### Timeline

- **1945** — Hugo Hadwiger publishes work on coverings and tilings of the plane that later informs the geometric framing of the problem.
- **1950** — Edward Nelson poses the problem and proves $\chi \ge 4$; John Isbell proves $\chi \le 7$ via a hexagonal $7$-coloring.
- **1960** — Martin Gardner publicizes the problem in *Scientific American* ("Mathematical Games", October), reaching a wide audience.
- **1961** — Hugo Hadwiger's expository writing discusses the question; Leo and William Moser introduce the **Moser spindle**, giving a clean $7$-vertex proof of $\chi \ge 4$.
- **1981** — Paul Erdős repeatedly features the problem in problem collections, offers prizes, and speculates the answer may be sensitive to set-theoretic axioms.
- **1991** — Kenneth Falconer proves that any **measurable** coloring of the plane requires at least $5$ colors, hinting the answer might depend on regularity assumptions.
- **2008** — Alexander Soifer publishes *The Mathematical Coloring Book*, the definitive historical and mathematical account, documenting the origins and the "Nelson–Isbell" attribution.
- **2018 (April)** — Aubrey de Grey posts a $1581$-vertex unit-distance graph proving $\chi \ge 5$, the first improvement in 68 years.
- **2018 (April–onward)** — Polymath16 launches, verifies de Grey's graph, and drives the minimal vertex count of $5$-chromatic examples down toward a few hundred vertices.
- **2018–present** — Search continues for a $6$-chromatic unit-distance graph (which would give $\chi \ge 6$); no example is known, and $5 \le \chi \le 7$ stands.
