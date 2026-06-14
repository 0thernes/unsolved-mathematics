# History — The Caccetta–Häggkvist Conjecture

_Origin, formulation, and timeline._

The Caccetta–Häggkvist conjecture is a central open problem of extremal digraph theory. It links two parameters of a directed graph: the minimum out-degree, which measures how dense out-neighbourhoods are, and the *girth*, the length of a shortest directed cycle. The intuition is simple: if every vertex points to many others, the digraph ought to be forced to close up into a short directed cycle. The conjecture makes this quantitative — and, more than four decades on, the precise threshold remains stubbornly out of reach.

## Origin and formulation

The problem was introduced by **Louis Caccetta** and **Roland Häggkvist** in their 1978 paper *"On minimal digraphs with given girth"*, presented at the Ninth Southeastern Conference on Combinatorics, Graph Theory, and Computing in Boca Raton, Florida. They studied digraphs of girth $g$ and asked how small the minimum out-degree could be forced to be — a Turán-type extremal question transplanted into the directed setting, where comparatively little machinery existed.

The conjecture in its now-standard form states:

> Every digraph $D$ on $n$ vertices in which every vertex has out-degree at least $n/k$ contains a directed cycle of length at most $k$.

Equivalently, a digraph of girth greater than $k$ must contain a vertex of out-degree at most $\lceil n/k\rceil - 1$. The directed cycle $\vec{C}_n$, with all out-degrees equal to $1 = n/n$, shows the bound $n/k$ cannot in general be lowered, so the threshold is conjectured to be exactly tight. The case $k=2$ is trivial; the first genuinely hard and most-studied case is **$k=3$**: any digraph on $n$ vertices with minimum out-degree $\ge n/3$ must contain a directed triangle. The triangle case admits an equivalent counting form: a digraph with no directed triangle and minimum out-degree $d$ should have at least $3d$ vertices.

The conjecture sits inside a wider family of girth problems for regular digraphs, notably a 1970 conjecture of Behzad, Chartrand, and Wall on the order of $d$-regular digraphs of girth $g$, which the Caccetta–Häggkvist statement generalizes. The triangle case in particular became prominent through the interest of **Paul Seymour**, and it is closely related to (though logically distinct from) Seymour's Second Neighbourhood Conjecture.

## Timeline

- **1970** — Behzad, Chartrand, and Wall conjecture that a $d$-regular digraph of girth $g$ has at least $d(g-1)+1$ vertices; later recognized as a special case of the broader picture.
- **1978** — Louis Caccetta and Roland Häggkvist pose the conjecture at the Boca Raton conference; the proceedings paper *"On minimal digraphs with given girth"* appears, with partial bounds and small-case verification.
- **1985** — **Chvátal and Szemerédi** prove that every digraph with minimum out-degree $d$ has a directed cycle of length at most $n/d + 2500$, an additive-constant approximation.
- **2000** — **Nathanson, Hamidoune** and others connect the triangle case to additive-combinatorial and Cayley-digraph formulations.
- **2003** — **Shen Jian** proves the triangle case ($k=3$) holds whenever minimum out-degree is at least $0.3532\,n$, pushing the constant toward the conjectured $1/3 \approx 0.3333$.
- **2006** — **Hladký, Král', and Norin** begin the flag-algebra attack on the triangle case; their work ultimately yields the bound $\approx 0.3465\,n$, the best unconditional result for $k=3$.
- **2007** — **Bondy** surveys the conjecture and its many equivalent forms in *"Counting subgraphs: a new approach to the Caccetta–Häggkvist conjecture"*-style discussions.
- **2008** — **Chudnovsky, Seymour, and Sullivan** prove results on a "local" version and on triangle-free digraphs, relating the problem to the Second Neighbourhood Conjecture.
- **2013** — **Lichiardopol** establishes results for digraphs with prescribed minimum out- and in-degree and for vertex-disjoint short cycles.
- **2010s–2020s** — Probabilistic, spectral, and entropy/compression methods, plus extended computer-assisted verification of small cases; the gap between $0.3465\,n$ and $n/3$ for the triangle case remains unclosed.

The conjecture is open for every $k \ge 3$. Its resilience against extremal, probabilistic, algebraic, and computer-assisted attacks marks its difficulty as structural rather than merely technical.
