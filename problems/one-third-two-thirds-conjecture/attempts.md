# Attempts — The 1/3–2/3 Conjecture

_Notable attempts, near-misses, retracted proofs._

## Linial's width-2 theorem (1984) — the sharp base case

Linial proved the conjecture for posets of **width 2** with the optimal constant $\tfrac12-\tfrac{\sqrt5}{10}\approx 0.2764$, the golden-ratio value forced by counting interleavings of two chains (a Fibonacci/lattice-path computation). This is not a near-miss but a complete result on a key class, and it fixed the *expected* extremal constant for the whole problem: any general proof must be consistent with width-2 posets achieving exactly this value, and the conjectured global constant $1/3$ is larger, so width-2 is in fact the "hardest looking" thin case.

## Kahn–Saks (1991) — the breakthrough that stopped short of $1/3$

The Kahn–Saks theorem — a balanced pair always exists with probability in $[\tfrac{3}{11},\tfrac{8}{11}]$ — is the single most important partial result. Its Brunn–Minkowski argument is widely admired but is understood to be **inherently unable to reach $1/3$**: it controls the position distribution of one element, not the worst pair. The $3/11 \approx 0.273$ constant was the first proof that *some* universal balance holds, converting the conjecture from "is there any constant?" to "is the constant exactly $1/3$?".

## Brightwell–Felsner–Trotter (1995) — the current record

Improving the geometric method, Brightwell, Felsner, and Trotter raised the universal constant to $\tfrac12-\tfrac{\sqrt5}{10}\approx 0.2764$ — numerically just above the Kahn–Saks value and matching Linial's width-2 constant. This remains, three decades later, the **best known general lower bound**. The fact that the universal record exactly equals the width-2 extremal constant is suggestive but has not been leveraged into a proof of $1/3$.

## Class results as accumulating evidence

Full verification on **height-2 posets**, **semiorders**, **$N$-free** and **series–parallel** posets (Brightwell; Felsner; Trotter) and exhaustive **computer checks of all small posets** constitute a long sequence of confirmations with no counterexample. These are genuine theorems, but each leans on structure unavailable in general, so none extends to the full statement; collectively they raise confidence that the conjecture is true.

## Forests and trees — an active, partly open sub-front

Trees and forests have proven unexpectedly stubborn: the obvious candidate balanced pair is not always balanced, and several papers (Zaguia and collaborators, 2010s) establish the conjecture for subfamilies of forests while leaving the general forest case as a recognized smaller open problem. This is a near-miss zone where partial progress keeps appearing.

## On claimed full proofs

As of the present record, **no proof of the full conjecture has been accepted**, and there is no widely-circulated, seriously-debated *retracted* claim attached to it on the scale of disputes seen for some other famous conjectures. The problem's status has stayed cleanly "open with strong partial results," and surveys (Brightwell 1999; Trotter's order-theory expositions) consistently report the $\approx 0.276$ bound as the frontier rather than announcing any contested resolution. Any specific online or preprint claim to have settled it should be treated with caution and checked against the published constant $\tfrac12-\tfrac{\sqrt5}{10}$, which no peer-reviewed work has surpassed for general posets.

## Net assessment

The pattern is characteristic of a "true but resistant" conjecture: two powerful analytic methods plateau just below the target, structural methods confirm it wherever they apply, computation never refutes it, and the remaining gap from $0.276$ to $1/3$ for arbitrary posets has resisted every technique tried since 1991.
