# Attempts — Sarnak's Möbius Disjointness Conjecture

_Notable attempts, near-misses, retracted proofs._

The conjecture has never been claimed in full, and — unlike the Riemann Hypothesis or $abc$ — it has not attracted high-profile *disputed* proof announcements. The history is instead one of accumulating partial conquests, each settling a substantial class of zero-entropy systems. The following are the most important milestones and near-misses.

## Confirmed special cases (genuine partial results)

- **Circle rotations and Kronecker systems.** Davenport's 1937 bound $\sum_{n\le N}\mu(n)e(n\alpha)=O_A(N(\log N)^{-A})$, uniform in $\alpha$, settles disjointness from all rotations — the historical prototype and a clean unconditional win.
- **Nilsystems and nilsequences.** Green–Tao's quantitative nilsequence estimates, combined with the Bourgain–Sarnak–Ziegler criterion (2013), prove disjointness for every nilsystem, the largest "algebraic" class.
- **Horocycle flows.** Bourgain–Sarnak–Ziegler (2013) verified disjointness for the horocycle flow on $\mathrm{SL}_2(\mathbb{R})/\Gamma$, a key homogeneous-dynamics case.
- **Automatic / substitution sequences.** Mauduit–Rivat's resolution of the Gelfond problems gives $\sum\mu(n)t(n)=o(N)$ for the Thue–Morse and Rudin–Shapiro sequences; later work (Müllner) extends to all automatic sequences.
- **Countably-many-ergodic-measure systems.** Frantzikinakis–Host (2018) is the strongest general theorem, covering all such systems in logarithmic average — widely regarded as the deepest near-miss toward the universal statement.

## Near-misses on Chowla (the harder sibling)

- **Logarithmic two-point Chowla.** Tao (2016) proved $\frac1{\log N}\sum_{n\le N}\frac{\lambda(n)\lambda(n+h)}{n}\to 0$, a genuine breakthrough — but only in *logarithmic* density. The corresponding ordinary-average statement $\frac1N\sum\lambda(n)\lambda(n+h)=o(N)$ remains **open**, the most famous gap in the area.
- **Higher-order log-Chowla.** Tao–Teräväinen (2017–2019) extended to odd orders and, conditionally on local-uniformity inputs, toward even orders. Even-order ordinary Chowla is still unresolved.
- **Sign-change and short-interval results.** Matomäki–Radziwiłł (2016) proved multiplicative functions do not have constant sign in almost all short intervals — not a disjointness proof, but the analytic engine behind nearly every subsequent advance.

## Frequently encountered subtleties (where naive attempts fail)

- **Entropy is essential.** Attempts to drop or weaken the zero-entropy hypothesis fail outright: full shifts and other positive-entropy systems support observables that correlate with $\mu$. Any claimed proof not using entropy crucially is suspect.
- **Logarithmic vs. ordinary averaging.** Several arguments inadvertently prove only the log-averaged version; promoting this to Cesàro averaging is a real obstacle, not a formality. Conflating the two is the most common error in informal attempts.
- **"Almost every $x$" vs. "every $x$."** Averaged or generic-point results are strictly weaker than the conjecture's demand of disjointness for *every* point and *every* continuous observable; exceptional orbits cannot be discarded.

## Status of claimed full proofs

As of the present, there is **no claimed proof of the full conjecture** in the literature, and consequently no dispute to adjudicate. The community treats the universal Cesàro-average statement, and full (ordinary-average) Chowla, as decidedly open. Caution is warranted only around the standard pitfalls above — particularly the logarithmic-average gap, which separates what is proven from what is conjectured.
