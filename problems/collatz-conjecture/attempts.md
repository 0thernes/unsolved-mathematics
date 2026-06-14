# Attempts — The Collatz Conjecture

_Notable attempts, near-misses, retracted proofs._

## Genuine partial results (near-misses)

- **Terras (1976) / Everett (1977).** The first real theorems: almost all $n$ have finite stopping time. These remain the template for every "density" attack and fall short only in that "almost all" cannot be promoted to "all."
- **Krasikov inequalities (1989) and Krasikov–Lagarias (2003).** Nonlinear programming on the difference inequalities of the iteration yields $\#\{n \le x : n \to 1\} \gg x^{0.84}$. A genuine unconditional lower bound on the convergent set, but $0.84 < 1$ leaves a positive-exponent gap to full density.
- **Steiner (1977); Simons (2005); Simons–de Weger (2005).** Exclusion of $1$-cycles and, more generally, $m$-cycles for $m \le 68$, combining transcendence theory with computation. A near-miss on the cycle half of the problem — but only for bounded cycle complexity.
- **Tao (2019).** "Almost all Collatz orbits attain almost bounded values." Widely regarded as the closest anyone has come. It proves $\min_k T^k(n) < f(n)$ for almost all $n$ and any $f \to \infty$. Tao himself emphasized that the result, while strong, "falls well short" of the conjecture because logarithmic density misses a thin exceptional set and "almost bounded" is not "bounded."

## Computational verification

Tomás Oliveira e Silva's long-running distributed search, continued by **David Bařina (2020)**, has verified convergence for all $n \le 2^{68}$. This is not a proof but provides the empirical floor under cycle-exclusion bounds and rules out any small counterexample. No counterexample has ever been found.

## Disputed and retracted claimed proofs

The Collatz conjecture is notorious for attracting claimed solutions; the overwhelming majority are erroneous. A few episodes are notable for the stature of those involved or the public attention they drew. These are stated neutrally, with the standing mathematical objection.

- **Bryan Thwaites (1996 and later).** Thwaites, who offered a £1,000 prize, also circulated arguments he believed established the conjecture. These were not accepted by the community; the proposed reasoning did not control the full orbit structure and was regarded as a heuristic rather than a proof.
- **Gerhard Opfer (2011 preprint, University of Hamburg).** Opfer — from Collatz's own institution — posted a manuscript ("An analytic approach to the Collatz $3n+1$ problem") claiming a proof via complex analysis and a holomorphic mapping argument. It was quickly disputed: reviewers identified that the argument, in effect, assumed a property equivalent to the conjecture (the relevant function-theoretic statement presupposed the very non-divergence it sought to prove), so the proof was **circular**. Opfer withdrew/acknowledged the gap and the paper was never published as a proof.
- **Recurring arXiv and preprint claims (ongoing).** Numerous individual claimants post purported proofs each year. The standard failure modes, repeatedly diagnosed by the community, are: (i) proving an "almost all" statement and silently treating it as "all"; (ii) bounding cycles only up to a finite length; (iii) a hidden circularity in which a convergence assumption enters a fixed-point or analytic-continuation step; or (iv) probabilistic heuristics presented as rigorous. None has survived expert scrutiny.

## Why attempts fail in a characteristic way

Paul Erdős's verdict — *"Mathematics is not yet ready for such problems"* — captures the pattern. The map's behavior is empirically pseudorandom with negative drift, so heuristically the conjecture is "obviously true," and this very plausibility lures attempts that quietly substitute the average behavior for the worst case. The genuine difficulty is the absence of any conserved quantity, algebraic structure, or monotone invariant that distinguishes the integers' orbits from the measure-typical orbits the heuristics describe.
