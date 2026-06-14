# Approaches — The 1/3–2/3 Conjecture

_Major strategies, partial results, and barriers._

## Convex geometry and Brunn–Minkowski (the Kahn–Saks method)

**Core idea.** Encode the linear extensions of $P$ via a polytope: the *chain polytope* / order polytope, or the family of "stochastically ordered" probability measures on extensions. Counting extensions in which an element $x$ sits in position $i$ defines a sequence; the Kahn–Saks insight is that an appropriate such sequence is **log-concave**, a consequence of the **Brunn–Minkowski inequality** applied to slices of a convex body. Log-concavity of the position distribution forces the existence of a pair whose betweenness probability is bounded away from $0$ and $1$.

**Best result reached.** Kahn and Saks (1991) obtained the first universal balance constant: every non-chain poset has a pair with $\Pr[x\prec y]\in[\tfrac{3}{11},\tfrac{8}{11}]$. Brightwell, Felsner, and Trotter (1995) pushed the same circle of ideas to $\tfrac12-\tfrac{\sqrt5}{10}\approx 0.2764$, the current record for general posets.

**Known barrier.** The Brunn–Minkowski route is "lossy": the log-concavity it delivers controls a single element's position distribution, but the conjecture needs a *pair* with a two-sided bound, and the geometric inequality does not see the extremal V-poset configuration tightly. There is no known way to squeeze the convex-geometry argument past $\approx 0.276$ up to $1/3$; the gap appears to be intrinsic to using a one-parameter slice rather than the full combinatorial structure.

## Entropy and the comparability graph (Kahn–Kim)

**Core idea.** Associate to $P$ the entropy $H(P)$ of its comparability graph (graph entropy / the entropy of the order polytope). A balanced comparison corresponds to a large entropy *drop*. Kahn and Kim (1994) showed one can always find a comparison whose resolution decreases $\log_2 e(P)$ by a constant factor, and that such a comparison is computable in polynomial time.

**Best result reached.** A constructive, polynomial-time guarantee of a constant-factor reduction — strong enough to prove that sorting with partial information needs only $O(\log e(P))$ comparisons, settling the *algorithmic* consequence of the conjecture up to the constant. This is the resolution of "the information-theoretic bound is good" even though the sharp $1/3$ remains open.

**Known barrier.** Entropy is a smoothed, averaged quantity; it controls totals but not the *worst* incomparable pair, and the constant it yields is again below $1/3$. The method certifies the algorithmic payoff without delivering the extremal combinatorial constant.

## Structural / class-by-class verification

**Core idea.** Prove the conjecture outright on restricted classes where extensions can be counted or compared directly: induct on structure, exhibit an explicit balanced pair, or reduce to lattice-path counting.

**Best results reached.**
- **Width 2** (Linial, 1984): full conjecture with the sharp constant $\tfrac12-\tfrac{\sqrt5}{10}$, via Fibonacci-type counting of interleavings.
- **Height 2** and **semiorders** (Brightwell; Brightwell–Felsner–Trotter): full conjecture.
- **$N$-free, series–parallel** posets: verified by decomposition.
- **Small posets**: confirmed exhaustively by computer for all posets up to a moderate number of elements, and the extremal cases catalogued.
- **Forests / trees**: partial results (Zaguia and collaborators), with the natural balanced pair identified for several subfamilies.

**Known barrier.** Each class exploits special structure (a chain decomposition, a forbidden subposet, a recursive build) absent in general. There is no uniform inductive scheme: deleting or contracting an element can change all betweenness probabilities unpredictably, so class results do not compose into a general proof. The "generic" poset — wide, of large height, highly tangled — is precisely where every structural handle disappears.

## Correlation inequalities (FKG / XYZ-type)

**Core idea.** Use correlation inequalities on the distributive lattice of down-sets (the XYZ inequality of Shepp, and FKG-type inequalities) to compare betweenness probabilities of related pairs and to rule out configurations in which *every* pair is unbalanced.

**Best result reached.** These inequalities constrain the joint behavior of comparisons (e.g. the XYZ inequality: conditioning on $x\prec y$ cannot make $x\prec z$ less likely) and are used as lemmas inside the structural and geometric proofs, sharpening bounds on specific families.

**Known barrier.** Correlation inequalities give *qualitative* monotonicity, not the quantitative two-sided $[\frac13,\frac23]$ window. They are auxiliary tools, not a standalone route to the constant.

## Computational search and extremal analysis

**Core idea.** Enumerate posets, compute exact betweenness probabilities (counting linear extensions is $\#\mathrm P$-hard in general, but feasible for small $n$), and search for any poset violating $1/3$ or for new tight families.

**Best result reached.** No counterexample has ever been found; the conjecture is verified for all small posets and the known extremal cases (V/Λ gadgets and their disjoint unions, certain "$2+2$"-type posets) realize the bound exactly, supporting that $1/3$ is the true threshold.

**Known barrier.** $\#\mathrm P$-hardness of counting extensions caps the reach of brute force; computation can refute or reassure but cannot prove the universal statement. It also has not surfaced a richer extremal family that might suggest the right invariant.

## Synthesis of obstructions

The two analytic methods (Brunn–Minkowski, entropy) plateau near $0.276$ and seem structurally incapable of reaching $1/3$; the structural method proves $1/3$ but only where extra structure is present and does not generalize. A full proof likely needs a genuinely new idea that sees the *pairwise* extremal configuration as sharply as Brunn–Minkowski sees a single position distribution — perhaps a stronger geometric inequality, a tailored entropy with the correct extremizer, or a global structural dichotomy.
