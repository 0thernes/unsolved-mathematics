# Attempts — The Erdős–Straus Conjecture

_Notable attempts, near-misses, retracted proofs._

## Congruence-class clearing (the main partial program)

The most productive line, pursued from the 1950s onward by Rosati, Bernstein, Yamamoto, Hagedorn, and others, resolves the conjecture residue class by residue class modulo $840$ and its refinements. These attempts collectively reduced the open cases to the six square classes $n \equiv r^2 \pmod{840}$, $r\in\{1,11,13,17,19,23\}$, and cleared many sub-progressions inside them. They are genuine partial results, not failed proofs, but they share a fundamental near-miss character: each new identity removes some primes from the hard classes, yet by quadratic reciprocity a positive-density residual always survives, so the program cannot terminate. This is the recurring "so close, yet provably not enough" pattern of the subject.

## Vaughan's exceptional-set theorem (1970)

R. C. Vaughan's bound $E(N) \ll N\exp(-c(\log N)^{2/3})$ is the landmark analytic near-miss: it shows that *if* counterexamples exist they are vanishingly rare. Many readers have mistaken such results for near-proofs, but they are categorically unable to exclude a single bad prime. Vaughan's work is correct and celebrated; the gap between "almost all $n$" and "all $n$" is exactly where the conjecture lives.

## Elsholtz–Tao representation bounds (2011)

Christian Elsholtz and Terence Tao gave the most complete modern analysis, controlling the number of solutions $f(n)$ on average and in arithmetic progressions, and tying $4/n$ solubility to counts of points on related cubic congruences and to character-sum estimates. Their paper is widely regarded as the current state of the art and explicitly frames why the problem resists resolution. It is not a claimed proof of the conjecture and makes no such claim; it sharpens the statistical picture and the structural obstruction.

## The general $a/n$ analogues

Sierpiński's $5/n$ conjecture and the Erdős–Straus–Sierpiński program for general $a/n$ (Schinzel) were attacked with the same congruence machinery. Schinzel observed that for *fixed* numerator $a$, the $a/n$ conjecture is soluble for all sufficiently large $n$ outside finitely many residue classes — an attractive uniformity — but again the finitely many classes are exactly the hard ones, mirroring the $4/n$ obstruction. These are honest theorems with the same ceiling.

## Disputed and erroneous claimed proofs

Because the statement is elementary, the conjecture attracts frequent claimed solutions, almost all from outside the professional literature; none has survived scrutiny. The characteristic flaw is **covering only a density-1 set of $n$ while implicitly assuming the residual square classes are also covered** — that is, conflating "all but finitely many residue classes" with "all residue classes." A second common error is an **unjustified interchange of quantifiers**, asserting that a single parametric identity works for every prime in a progression when, for the square classes, the required quadratic residue fails infinitely often. No retraction in the refereed literature is associated with the problem because no peer-reviewed full proof has ever been accepted; the appropriate neutral statement is that **the conjecture remains open**, and any document claiming a complete elementary proof should be checked specifically against the six square residue classes modulo $840$ and against the quadratic-reciprocity obstruction that defeats finite identity lists.

## Computational "verifications"

Large searches (Allan Swett and others) confirming $4/n$ for all $n$ up to $\sim 10^{17}$ are sometimes informally cited as if they settled the matter. They do not: they are strong confirmatory evidence and useful for pruning heuristics, but verification over a finite range is logically incapable of proving a statement quantified over all integers. Their real value is in establishing that no small counterexample exists and that the number of representations grows, consistent with the conjecture holding robustly.
