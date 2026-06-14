# Approaches — The Volume Conjecture

_Major strategies, partial results, and barriers._

## Saddle-point / state-integral asymptotics

**Core idea.** Write $J_N(K;e^{2\pi i/N})$ as a finite multisum (or, after Poisson summation, an integral) whose summand is $\exp(N\cdot S(\mathbf{z}))$ for a "potential" $S$ built from quantum/Euler dilogarithms. As $N\to\infty$ the sum is dominated by critical points of $S$; the critical value of $S$ at the geometric saddle equals $\tfrac{1}{2\pi}(\mathrm{Vol}+i\,\mathrm{CS})$, because the critical-point equations reproduce Thurston's gluing/hyperbolicity equations for an ideal triangulation of $S^3\setminus K$. This is the most successful and most geometric line of attack.

**Best result.** Ohtsuki (2016, building on 2007–2011 work) gave a rigorous saddle-point proof for the figure-eight knot $4_1$, including the full asymptotic expansion (the $1$-loop term, an $N^{1/2}$ factor, and a power series), and the method has been pushed to $5_2$, $6_1$, and several other small hyperbolic knots, as well as some twist and double-twist knots by Ohtsuki–Yokota and collaborators.

**Barrier.** Controlling the asymptotics rigorously requires (a) writing the invariant as a genuine integral with controlled error, (b) certifying that the *geometric* critical point dominates (no other critical point has larger real part of $S$), and (c) deforming the integration contour onto the relevant steepest-descent/Lefschetz thimble. Step (c) — the Stokes phenomenon and contour deformation — is delicate and currently must be redone knot-by-knot. There is no general theorem that the dominant saddle is always the geometric one for arbitrary knots; this is the central analytic obstruction.

## Quantum-modularity and resurgence (Garoufalidis–Zagier)

**Core idea.** Treat the Kashaev invariant as the value at $1$ of a "quantum modular form"; its asymptotics are governed by a full transseries whose leading exponential is the complex volume and whose Stokes data encode all flat $\mathrm{SL}_2(\mathbb{C})$ connections. Resurgence organizes the perturbative series around each saddle and the connection (Borel) coefficients between them.

**Best result.** Detailed, internally consistent transseries and modularity conjectures verified numerically to very high precision for $4_1$, $5_2$ and other knots; a rigorous proof of quantum modularity for $4_1$ (Bettin–Drappeau and related work on Kashaev's function).

**Barrier.** The framework is largely conjectural/numerical for general knots; turning resurgent structure into a proof of the leading volume asymptotics for all knots is open.

## $q$-Holonomicity and the AJ / $A$-polynomial program (Garoufalidis–Lê, Gukov)

**Core idea.** Garoufalidis–Lê proved $N\mapsto J_N(K;q)$ satisfies a linear $q$-difference equation (it is $q$-holonomic). Its "classical limit" should be the $A$-polynomial of $K$, whose zero locus is the $\mathrm{SL}_2(\mathbb{C})$ character variety. Gukov's generalized Volume Conjecture predicts that asymptotics at $e^{2\pi i\hbar}$ are dictated by a path on the character variety, with the complex volume arising as a period; this ties the VC to the AJ conjecture.

**Best result.** $q$-holonomicity is a theorem; AJ is proved for many knots; the structural link to character varieties is well established and explains *why* volumes should appear.

**Barrier.** Knowing the recursion does not by itself control the $N\to\infty$ growth at the specific root $e^{2\pi i/N}$ (a confluence/coalescence limit); the AJ conjecture itself is open in general, so this route inherits an unproven dependency.

## TQFT / Reshetikhin–Turaev and Turaev–Viro reformulations (Chen–Yang)

**Core idea.** Chen–Yang (2015/2018) observed that evaluating Turaev–Viro and Reshetikhin–Turaev invariants at the *unusual* root $q=e^{2\pi i/r}$ (rather than the standard $e^{\pi i/r}$) produces exponential growth whose rate is the hyperbolic volume of the underlying $3$-manifold. This generalizes the knot statement to closed and cusped manifolds and reconnects it to honest TQFT.

**Best result.** Proved for fundamental shadow links (Belletti–Detcherry–Kalfagianni–Yang, 2018) and certain families and Dehn fillings; relation $|J_N(K)|^2$-type estimates to $\mathrm{TV}$ via Detcherry–Kalfagianni–Yang. Strong numerical support across census manifolds.

**Barrier.** Proofs again rely on explicit $6j$-symbol asymptotics (quantum Racah coefficients $\to$ volumes of hyperbolic tetrahedra) and on the link admitting controllable triangulations; extending to all hyperbolic $3$-manifolds, and pinning the exact subexponential factor, is open.

## Hyperbolic-geometric / gluing-variety methods

**Core idea.** Match the critical-point equations of the dilogarithm potential directly to Neumann–Zagier data of an ideal triangulation, proving the geometric saddle exists and yields the complete structure. Yokota's program constructs the potential function from a triangulation so that its critical value is manifestly the complex volume.

**Best result.** Clean identification of saddle value with complex volume for triangulated complements; foundational for all rigorous cases.

**Barrier.** Existence/uniqueness of a *positively oriented* (geometric) solution and dominance over other (e.g. parabolic, reducible) flat connections is not guaranteed for all knots — exactly the gap the analytic approaches must close.

## Negative / cautionary results

The naive conjecture fails outside its intended class. The original limit can fail to exist or fail to equal the volume for some links and for some non-hyperbolic configurations; Garoufalidis–Lê and others noted that for certain torus knots and specific cases the precise asymptotic form requires care (subtle subexponential and oscillatory corrections), motivating the use of $\limsup$ and of simplicial rather than hyperbolic volume. Detcherry–Kalfagianni found families where related growth-rate statements need additional hypotheses. These results do not refute the conjecture but sharpen its correct formulation and warn against over-generalization to all links and roots of unity.
