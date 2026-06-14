# History — Self-Avoiding Walk (Scaling & Connective Constant)

_Origin, formulation, and timeline._

The self-avoiding walk (SAW) is a lattice path that visits no vertex more than once. On the hypercubic lattice $\mathbb{Z}^d$, let $c_n$ denote the number of $n$-step SAWs from the origin. The model originated not in pure mathematics but in polymer chemistry: a long-chain molecule in dilute solution cannot self-intersect (the excluded-volume effect), so its conformations are modeled by SAWs. The two governing questions are (i) the asymptotics of $c_n$, controlled by the **connective constant** $\mu = \lim_{n\to\infty} c_n^{1/n}$, and (ii) the **scaling exponents** $\gamma$ (susceptibility) and $\nu$ (mean-square displacement), conjectured to be universal and to take simple rational values in low dimension.

The central conjectures are sharp. One expects $c_n \sim A\,\mu^n n^{\gamma-1}$ and $\mathbb{E}|\omega_n|^2 \sim D\, n^{2\nu}$, with $\nu = 3/4$, $\gamma = 43/32$ in $d=2$; $\nu \approx 0.588$ in $d=3$; and mean-field values $\nu = 1/2$, $\gamma = 1$ with logarithmic corrections at the critical dimension $d=4$. Existence of $\mu$ is classical and elementary (submultiplicativity, $c_{m+n}\le c_m c_n$); essentially everything quantitative about the exponents in $d=2,3$ remains conjectural.

**Timeline**

**1947** — W. J. C. Orr studies excluded-volume statistics of polymer chains, introducing the combinatorial counting of non-self-intersecting configurations.
**1949–1953** — Paul Flory develops mean-field "Flory theory," predicting $\nu = 3/(d+2)$ (giving $3/4$ in 2D, $3/5$ in 3D), set out fully in *Principles of Polymer Chemistry* (1953).
**1954** — J. M. Hammersley and K. W. Morton formalize SAWs probabilistically and introduce importance sampling ("Poor man's Monte Carlo").
**1957** — Hammersley proves existence of the connective constant $\mu$ via subadditivity, founding the rigorous theory.
**1959–1962** — Hammersley and D. J. A. Welsh sharpen bounds and convergence rates for $c_n$.
**1972** — P.-G. de Gennes' "$n\to 0$" insight maps SAWs onto the $O(n)$ spin model in the $n\to0$ limit, embedding the problem in statistical field theory and explaining universality.
**1982** — B. Nienhuis, via Coulomb-gas methods, predicts exact 2D exponents $\nu=3/4$, $\gamma=43/32$ and the honeycomb connective constant $\mu=\sqrt{2+\sqrt2}$ (non-rigorous, now canonical).
**1989–1992** — T. Hara and G. Slade prove, via the **lace expansion**, mean-field behavior ($\nu=1/2$, $\gamma=1$) for SAWs in dimensions $d \ge 5$ — the deepest rigorous result on exponents.
**1993** — N. Madras and G. Slade publish *The Self-Avoiding Walk*, the field's standard monograph.
**2000** — O. Schramm introduces SLE and conjectures that the 2D SAW scaling limit is chordal $\mathrm{SLE}_{8/3}$, giving a precise conformally invariant target.
**2004** — G. Lawler, O. Schramm, W. Werner show that *if* the SAW has a conformally invariant scaling limit it must be $\mathrm{SLE}_{8/3}$, whose exponents reproduce Nienhuis' predictions — conditional but decisive.
**2010–2012** — H. Duminil-Copin and S. Smirnov prove the honeycomb-lattice connective constant is exactly $\sqrt{2+\sqrt 2}$ (published 2012, *Ann. of Math.*), confirming Nienhuis — a rare exact rigorous theorem, using a discrete holomorphic parafermionic observable.
**2014–2016** — Duminil-Copin, Glazman, Hammond, Manolescu and collaborators establish structural results: continuity of $\mu$ in the lattice, sharpness, and absence of an infinite SAW measure with sub-ballistic behavior in certain regimes.
**2020s** — Conformal-bootstrap and Monte Carlo work refines 3D estimates to $\nu \approx 0.58759700(40)$; rigorous conformal invariance and the exact 2D exponents remain open — the central frontier.
