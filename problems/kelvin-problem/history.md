# History — The Kelvin Problem (Optimal Space Partition)

_Origin, formulation, and timeline._

## Origin and formulation

In 1887 Sir William Thomson (Lord Kelvin) asked, in the pages of the _Philosophical Magazine_, for the partition of three-dimensional Euclidean space $\mathbb{R}^3$ into cells of equal volume that minimizes the average surface area per cell. The question grew out of his attempt to model the luminiferous aether as a fine-grained elastic foam: he wanted the "least-energy" arrangement of equal compartments, energy being proportional to interfacial area. The problem is the natural $3$D analogue of the planar honeycomb question (which tiling of the plane into equal areas minimizes perimeter — answered by the regular hexagon, rigorously only in 1999 by Thomas Hales).

Kelvin's candidate is a relaxed **bitruncated cubic honeycomb**: cells are slightly curved truncated octahedra (Kelvin cells), each with $6$ square and $8$ hexagonal faces, packed on a body-centered cubic lattice. Crucially, Kelvin recognized that the flat-faced truncated octahedron is _not_ optimal; the faces must curve and edges relax so that every triple of films meets at $120°$ and every quadruple of edges meets at the tetrahedral Maraldi angle $\approx 109.47°$. These are **Plateau's laws** for soap films, so Kelvin's structure is a candidate **minimal partition**: a stable foam, not merely a polyhedral tiling.

The modern formulation: among all partitions of $\mathbb{R}^3$ into regions of unit volume, minimize the surface-area density $\sigma$ (area per unit volume). Kelvin's structure achieves $\sigma \approx 5.306$ (in units where each cell has volume $1$), or isoperimetric quotient about $0.757$ relative to the sphere.

## Timeline

**1873** — Joseph Plateau publishes _Statique expérimentale et théorique des liquides_, codifying the geometric laws of soap films that any optimal foam must obey.

**1887** — Lord Kelvin, "On the Division of Space with Minimum Partitional Area," _Phil. Mag._ Ser. 5, vol. 24. He proposes the relaxed truncated-octahedron foam and constructs physical and stereoscopic models.

**1929** — F. W. Schwarz and later workers revisit Kelvin's cell; the structure is reproduced in crystallography (the bcc Wigner–Seitz cell is the flat truncated octahedron).

**1942–1970s** — Cyril Stanley Smith and metallurgists study real foam topology (Plateau borders, vertex statistics), giving empirical context. No structure beating Kelvin is found; many conjecture his is optimal.

**1976** — Fred Almgren and collaborators advance the regularity theory of $(M,\varepsilon,\delta)$-minimal sets and area-minimizing currents, the analytic backbone for foam minimality.

**1993** — Denis Weaire and Robert Phelan (Trinity College Dublin), using the Surface Evolver software of Ken Brakke, discover a partition with surface-area density about $0.3\%$ **lower** than Kelvin's. The **Weaire–Phelan (WP) structure** uses two cell types of equal volume — irregular pentagonal dodecahedra ($12$ faces) and tetrakaidecahedra ($14$ faces, $2$ hexagons + $12$ pentagons) — in an $8$-cell unit cell modeled on the A15 / $\beta$-tungsten ($\mathrm{Cr_3Si}$) clathrate structure. This refutes Kelvin's conjecture of optimality.

**1994** — Weaire and Phelan publish further analysis; the foam community confirms numerically that no flat-faced relaxation of Kelvin beats WP.

**1996** — John M. Sullivan and others place the problem in the language of minimal surfaces and explore related "tetrahedrally close-packed" (TCP) candidates (A15, C15, Z, etc.).

**1990s–2000s** — Surface Evolver computations refine WP's value; searches over hundreds of TCP and Frank–Kasper structures find none better than WP.

**2008** — The aquatic centre ("Water Cube") for the Beijing Olympics is built on the Weaire–Phelan geometry, bringing the problem wide public attention.

**2010s–present** — The problem remains open: WP is the conjectured optimum, but no proof exists that WP (or any explicit structure) is the global minimizer; even Kelvin's structure has not been proven to be a local minimizer in full generality. Work by Hales (honeycomb, 2001), Morgan, and the GMT community frames what a rigorous $3$D resolution would demand, but the partition problem in $\mathbb{R}^3$ stays unresolved as of 2026.
