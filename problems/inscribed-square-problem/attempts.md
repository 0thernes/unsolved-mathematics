# Attempts — The Inscribed Square Problem (Toeplitz)

_Notable attempts, near-misses, retracted proofs._

The history of the square peg problem is one of steadily widening special cases rather than dramatic failed proofs. There is no famous retracted "complete solution," but several episodes of imprecision, gaps, and over-claimed generality are worth recording neutrally.

## Emch's pioneering proofs (1913–1916)

Arnold Emch gave the first rigorous results, proving the conjecture for smooth convex curves and then for a class of piecewise-analytic curves. These are genuine theorems, but Emch's arguments rely on tangency and median-chord constructions that implicitly assume regularity; they do not extend to general curves, and Emch himself framed them as partial. They are best read as foundational special cases, not as attempts at the full conjecture.

## Schnirelmann's smoothness hypothesis (1929) and its correction

Lev Schnirelmann's celebrated 1929 argument proved the conjecture for sufficiently smooth curves via a parity (mod-2) count of inscribed squares. The original statement and proof contained imprecisions about exactly how much smoothness was required and about the transversality of the auxiliary map. The result was later cleaned up and the smoothness hypothesis made explicit (a $C^2$-type condition suffices, with refinements by Guggenheimer and others). This is a near-miss in the sense that the *method* tantalizingly suggests a count that "should" survive to continuous curves, but the parity is exactly what can collapse under degeneration.

## The persistent degeneration gap

The most common error in informal or amateur attempts is to prove inscribed squares for smooth approximations $\gamma_n \to \gamma$ and then assert that the limiting configuration is a non-degenerate square. As emphasized in Stromquist's and Matschke's writings, the inscribed squares $S_n$ can shrink to a point in the limit; without a uniform size bound the argument is incomplete. Many proposed "elementary proofs" of the full conjecture circulating in the literature and online founder precisely here. The neutral statement of the objection is: *uniform non-degeneracy of inscribed squares under approximation has not been established for arbitrary continuous Jordan curves.*

## Stromquist's locally monotone theorem (1989) — a genuine high-water mark

Stromquist proved the conjecture for locally monotone curves, covering all piecewise-$C^1$ curves. This is a correct and influential result, not a disputed claim. It is a near-miss only in that the hypothesis (local monotonicity) is the precise feature that wild curves lack — so it brings the smooth/tame world fully into the fold while leaving the fractal frontier untouched.

## Modern conditional results (Matschke; Tao)

Benjamin Matschke (2014) surveyed the field and obtained results under explicit metric/smoothness conditions, carefully flagging the boundary of what is proved. Terence Tao (2017) proved a square-peg-type theorem for curves that decompose as unions of Lipschitz graphs (a "two graphs" condition), with the honest caveat that the fully general continuous case is not implied. These are correct partial theorems whose authors are explicit about their limitations — exemplary in distinguishing what is proved from what is conjectured.

## Greene–Lobb (2020) — resolved the smooth case, not the general one

The symplectic-geometry breakthrough of Greene and Lobb settled inscribed rectangles of every aspect ratio for **smooth** curves. It was widely and correctly reported as a major advance, but some popular coverage blurred "smooth Jordan curve" into "every Jordan curve." For the record: the general continuous (non-smooth) square problem remained open after Greene–Lobb and remains open today.

**Bottom line.** There is no accepted solution to the full problem and no notorious fraudulent proof; the recurring methodological pitfall is the unjustified limiting argument, and the recurring reporting pitfall is conflating the solved smooth case with the open general case.
