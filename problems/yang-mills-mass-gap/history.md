# History — Yang–Mills Existence and Mass Gap

_Origin, formulation, and timeline._

## How the problem arose

The problem grows out of two distinct strands: the physics of non-abelian gauge theory and the mathematics of constructive quantum field theory (CQFT). In 1954 Chen Ning Yang and Robert Mills generalized Maxwell's $U(1)$ electromagnetism to a non-abelian gauge group (originally $SU(2)$), producing a classical field theory with self-interacting gauge potentials $A_\mu$ valued in a Lie algebra and curvature $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + g[A_\mu, A_\nu]$. The classical equations are scale-invariant and the gauge bosons are massless, which initially seemed to doom the theory as a model of the short-range strong force.

Two later developments transformed this picture. First, the discovery of **asymptotic freedom** by Gross, Wilczek, and Politzer (1973) showed that the running coupling of non-abelian Yang–Mills decreases at high energy, making the theory weakly coupled in the ultraviolet and strongly coupled in the infrared. Second, the physical expectation of **confinement** and a **mass gap**: although the classical Lagrangian contains no mass term, the quantized theory (pure $SU(3)$ gauge theory, or QCD without quarks) is believed to have a lowest excitation — the lightest glueball — with strictly positive mass $\Delta > 0$, so that correlation functions decay exponentially. Lattice Monte-Carlo simulations have confirmed this numerically since the 1980s, but no rigorous proof exists.

The mathematical obligation is sharper still. The very **existence** of four-dimensional interacting quantum field theory is unestablished. The CQFT program of Glimm, Jaffe, Nelson, Symanzik, Osterwalder, Schrader and others succeeded in rigorously constructing scalar theories in spacetime dimensions $d=2$ and $d=3$, but $d=4$ remained out of reach. Yang–Mills is the natural candidate for a non-trivial $d=4$ construction because asymptotic freedom suppresses the ultraviolet divergences that defeat, e.g., $\phi^4_4$ (believed to be trivial).

## Precise formulation

The official problem, written by Arthur Jaffe and Edward Witten for the Clay Mathematics Institute (2000), asks: for any compact simple gauge group $G$, prove that a quantum Yang–Mills theory exists on $\mathbb{R}^4$ satisfying the **Wightman axioms** (or equivalently the **Osterwalder–Schrader axioms** for the Euclidean theory), and that it has a **mass gap** $\Delta > 0$, i.e. the spectrum of the energy–momentum operator has an isolated lowest eigenvalue $0$ (the vacuum) with a gap to the rest of the spectrum. Existence requires a nontrivial measure / Hilbert space with the correct symmetries; the mass gap requires exponential clustering of correlations.

## Timeline

- **1954** — C. N. Yang and Robert Mills publish the non-abelian gauge theory in *Physical Review*.
- **1967–1971** — Faddeev–Popov quantization; 't Hooft proves renormalizability of non-abelian gauge theories with spontaneous symmetry breaking.
- **1973** — Gross–Wilczek and Politzer discover asymptotic freedom, making QCD a viable theory of the strong interaction.
- **1975–1977** — Belavin–Polyakov–Schwartz–Tyupkin instantons; first nonperturbative signals of vacuum structure.
- **1973–1987** — Glimm–Jaffe, Osterwalder–Schrader, and others build constructive QFT in $d=2,3$; Balaban, Magnen–Sénéor–Rivasseau, and Federbush develop rigorous renormalization-group machinery for gauge theories in finite volume.
- **1979–1980s** — Wilson's lattice gauge theory and Monte-Carlo simulations give strong numerical evidence for confinement and a positive glueball mass.
- **2000** — Clay Mathematics Institute names "Yang–Mills Existence and Mass Gap" a Millennium Prize Problem; official statement by Jaffe and Witten.
- **2003–2010** — Magnen–Rivasseau and collaborators, Dimock, and others pursue partial constructive results; supersymmetric and topologically twisted variants studied.
- **2010s–2020s** — Continued rigorous work on lattice continuum limits (e.g. abelian Higgs, 2D and 3D Yang–Mills), stochastic quantization of the Yang–Mills measure (Chandra–Chevyrev–Hairer–Shen) in $d=2,3$, and Chatterjee's rigorous results on lattice gauge theory and Wilson loops.
- **Present** — The full four-dimensional construction with a mass gap remains open; no claimed complete proof is accepted.
