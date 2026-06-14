# History — Hilbert's Sixteenth Problem (Second Part)

_Origin, formulation, and timeline._

Hilbert's sixteenth problem has two parts. The **first part** concerns the topology of real algebraic curves and surfaces — the mutual position ("Lage," whence the German title *"Problem der Topologie algebraischer Kurven und Flächen"*) of the ovals of a nonsingular real plane algebraic curve of degree $n$, building on Harnack's 1876 bound of $\tfrac{(n-1)(n-2)}{2}+1$ ovals. The **second part**, which this dossier treats, asks the analogous question for trajectories: to determine the maximum number and relative position of **limit cycles** of a planar polynomial differential system
$$\dot x = P(x,y),\qquad \dot y = Q(x,y),$$
where $P,Q$ are real polynomials of degree at most $n$. A limit cycle is an isolated periodic orbit in the phase plane. The quantity in question is the **Hilbert number** $H(n)$, the supremum over all degree-$n$ systems of the number of limit cycles.

Hilbert posed the problem in his address to the International Congress of Mathematicians in Paris on 8 August 1900, as the sixteenth of his famous twenty-three problems. He was motivated by Poincaré's qualitative theory of differential equations (1881–1886), which introduced limit cycles, and by the contemporaneous work on the location of ovals. Hilbert explicitly connected the two parts as questions about the topology of real solution sets — algebraic ones in the first part, transcendental (phase-portrait) ones in the second.

The problem has proven extraordinarily resistant. Even the **existence of a finite bound** for the simplest nonlinear case $n=2$ (quadratic systems) remains open; no one knows whether $H(2)$ is even finite. The closely related but logically distinct **finiteness problem** — whether a *single fixed* polynomial system can have infinitely many limit cycles — is known to have a negative answer (each individual system has finitely many), but this "individual finiteness" was itself the subject of a celebrated saga of flawed and repaired proofs.

## Timeline

- **1881–1886** — Henri Poincaré develops the qualitative theory of planar differential equations and defines the notion of a limit cycle (*cycle limite*).
- **1900** — David Hilbert poses the problem at the ICM in Paris; the second part asks for bounds on the number and configuration of limit cycles of degree-$n$ polynomial systems.
- **1923** — Henri Dulac publishes a proof that an individual analytic planar system has finitely many limit cycles ("Dulac's theorem"); the argument is later found to contain an essential gap.
- **1939–1952** — N. N. Bautin studies the cyclicity of foci/centers; his 1952 result bounds the number of small-amplitude limit cycles bifurcating from a focus or center of a quadratic system by **3**.
- **1955–1957** — Petrovskii and Landis announce a (false) proof that $H(2)=3$; the error is acknowledged in the early 1960s.
- **1979–1980** — Shi Songling and, independently, Chen Lansun and Wang Mingshu construct concrete quadratic systems with **4** limit cycles, disproving the Petrovskii–Landis claim and showing $H(2)\ge 4$.
- **1981** — Yu. S. Ilyashenko exposes the gap in Dulac's 1923 proof, reopening the individual finiteness question.
- **1985–1988** — Roussarie and others recast the problem via the **Hilbert–Arnold problem** and the cyclicity of limit periodic sets (polycycles).
- **1991–1992** — Ilyashenko (*Finiteness Theorems for Limit Cycles*) and, independently, J. Écalle, complete correct proofs that each fixed analytic system has finitely many limit cycles.
- **1994** — Yu. Ilyashenko and S. Yakovenko frame the **existential / infinitesimal Hilbert 16th problem** (uniform bounds via Abelian integrals).
- **2010** — Binyamini, Novikov, and Yakovenko prove an explicit uniform bound for the number of zeros of Abelian integrals on bounded distance from the boundary (a partial result on the infinitesimal problem).
- **2016–present** — Activity on the **restricted/tangential Hilbert problem**, Liénard systems, slow–fast (geometric singular perturbation) methods, and computer-assisted lower bounds (current records put $H(2)\ge 4$, $H(3)\ge 13$ and similar growth $\gtrsim n^2\log n$ for general $n$).
