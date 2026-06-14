# History — The Moving Sofa Problem

_Origin, formulation, and timeline._

The moving sofa problem is the most famous instance of a class of "motion-planning under rigid constraints" questions in plane geometry. The everyday picture is exact: a planar region (the "sofa") must be slid through an L-shaped hallway whose two arms each have unit width, meeting at a right-angled corner. The constraint is purely kinematic — the shape is rigid, may be translated and rotated continuously, but at every instant must lie entirely within the hallway. The question is to find the **sofa constant** $\mu$, the supremum of the areas of regions admitting such a motion.

The problem was posed in print by **Leo Moser** in 1966, in the American Mathematical Monthly's problem column (and circulated among combinatorial geometers earlier). Moser's formulation already fixed the modern setting: corridor of width 1, single $90^\circ$ turn, area to be maximized. The challenge is genuinely two-sided. An *upper bound* requires proving that no shape can exceed a given area — a statement about all possible motions of all possible regions. A *lower bound* requires exhibiting one explicit shape and a valid motion. The gap between the best constructions and the best impossibility proofs has remained the substance of the problem for six decades.

A crucial early simplification, due to **John Michael Hammersley** (1968), is that one may equivalently track the *intersection of the hallway, over all positions, in the sofa's own moving frame*. Equivalently, fix the sofa and slide the rotating corridor over it; the sofa must lie in the intersection of all corridor placements. This reframing converts the dynamic constraint into a description of an envelope of moving lines, and it underlies essentially every later construction. Hammersley produced a concrete shape — a rectangle with a semicircular bite removed — of area $\pi/2 + 2/\pi \approx 2.2074$, and conjectured (wrongly, as it turned out) that this might be optimal.

The decisive lower-bound advance came from **Joseph Gerver** in 1992 (published in *Geometriae Dedicata*, 1992). Gerver constructed a shape whose boundary is assembled from 18 analytic pieces — straight segments, arcs of circles, and arcs of involutes — determined by requiring that the boundary be the envelope of the swept inner corner. His sofa has area $\mu_G \approx 2.219531669$. Gerver's shape remains the conjectured optimum, and no larger shape has ever been found.

On the upper-bound side, simple arguments give $\mu \le 2\sqrt{2} \approx 2.8284$ (Hammersley). This was improved by **Yoav Kallus and Dan Romik** (2018), who used a rigorous, computer-assisted analysis of a finite set of rotation angles to certify $\mu \le 2.37$. Romik (2017) had separately re-derived Gerver's construction and solved the closely related **ambidextrous sofa** problem — shapes that turn both left and right through right angles — finding an optimal piecewise-analytic shape (the "Romik sofa") of area $\approx 1.6449$.

The current frontier is a 2024 claimed resolution by **Jineon Baek**, who posted a preprint asserting a proof that Gerver's sofa is in fact optimal, $\mu = \mu_G$. The argument is under community verification; the problem's status here is best described as a claimed proof rather than a settled theorem (see status.md).

### Timeline

- **1966** — Leo Moser poses the moving sofa problem in the *American Mathematical Monthly*.
- **1968** — J. M. Hammersley reformulates via the corridor-intersection picture; gives the lower bound $\pi/2 + 2/\pi \approx 2.2074$ and the upper bound $2\sqrt{2}$.
- **1976** — Surveys (notably in Croft, Falconer, Guy's problem collections) cement the problem as a canonical open question in plane geometry.
- **1992** — Joseph Gerver constructs the 18-piece shape of area $\approx 2.2195$; conjectures it is optimal.
- **1994** — The problem features prominently in *Unsolved Problems in Geometry* (Croft–Falconer–Guy).
- **2017** — Dan Romik re-derives Gerver's sofa with modern symbolic tools and solves the ambidextrous variant.
- **2018** — Kallus and Romik prove the rigorous upper bound $\mu \le 2.37$ via computer assistance.
- **2024** — Jineon Baek posts a preprint claiming a proof that $\mu = \mu_G \approx 2.2195$, asserting Gerver's sofa is optimal; the proof is undergoing verification.
