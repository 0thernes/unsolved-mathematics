# Status & Frontier — Giuga's Conjecture

_Where the problem stands and what a resolution would require._

**Status: open.** Giuga's conjecture — that $n>1$ is prime if and only if $\sum_{k=1}^{n-1}k^{\,n-1}\equiv-1\pmod n$ — remains unproven after more than seventy years. The forward direction (primes satisfy the congruence) is an elementary consequence of Fermat's little theorem. The open content is the **converse**: that no composite $n$ satisfies it.

## What is known (unconditional)

- **The reduction.** Any composite counterexample is squarefree and satisfies $p\mid(n/p-1)$ for every prime $p\mid n$; equivalently it is a **Giuga number** ($\sum_{p\mid n}1/p-\prod_{p\mid n}1/p\in\mathbb Z$) that is *also* a Carmichael number. (Giuga 1950.)
- **Size and factor bounds.** Borwein–Borwein–Borwein–Girgensohn (1996, *Amer. Math. Monthly* 103) proved any counterexample has at least **13 distinct prime factors** and exceeds $10^{1700}$. Later computation raised the floor to roughly $10^{13{,}800}$, requiring thousands of distinct primes.
- **Equivalence.** The Giuga congruence is equivalent to the **Agoh–Giuga** Bernoulli criterion $nB_{n-1}\equiv-1\pmod n$ (Borwein et al. 1996; Agoh c. 1990).
- **Relaxed objects exist.** Genuine **Giuga numbers** exist — $30, 858, 1722, 66198,\dots$ — but none is a counterexample, because each fails the Carmichael condition.

## What is known (conditional / contextual)

- Carmichael numbers are infinite (Alford–Granville–Pomerance 1994), so the ambient class of a hypothetical counterexample is infinite; the Giuga sub-condition prunes it drastically.
- Whether **infinitely many Giuga numbers** exist is itself open; even a positive answer would not yield a Giuga *counterexample*.

## What a full resolution requires

A proof must show the **converse is unconditional**: no composite $n$, however large or however many prime factors it has, satisfies the congruence. The counting/size arguments produce ever-larger lower bounds but **no finiteness mechanism** — they cannot exclude an astronomically large $n$ with enough prime factors. A resolution therefore needs a genuinely new idea that converts the simultaneous Carmichael + Giuga conditions into an outright contradiction, rather than merely a larger bound.

## Plausible routes

1. **Bernoulli/$p$-adic obstruction** — exploit von Staudt–Clausen and Kummer-type congruences on $B_{n-1}$ to force the Agoh form to fail for composites.
2. **Structural impossibility for Carmichael ∩ Giuga** — prove the two conditions are jointly unsatisfiable using the multiplicative constraints $\sum 1/p_i\approx$ integer together with Korselt's criterion.
3. **Density/sieve methods** — show the count of candidate counterexamples below $x$ is $o(1)$ unconditionally, not merely below current bounds.

No route is close to completion; the most realistic near-term progress is continued raising of the verification floor and partial results on generalized Giuga numbers.

## Related problems

- [Carmichael's totient-function conjecture](../carmichael-totient-conjecture/) — Carmichael-number machinery underlies any counterexample.
- [Lehmer's totient problem](../lehmer-totient-problem/) — a sibling "composite-with-strong-congruence" problem.
- [Odd perfect numbers](../odd-perfect-numbers/) — another easy-to-state, computationally-unfalsified squarefree/divisor problem.
- [Mersenne primes infinitude](../mersenne-primes-infinitude/) — a parallel open question on the multiplicative structure of integers.
- [Goldbach's conjecture](../goldbach-conjecture/) — a comparison case of an elementary, verified-far, unproven number-theory statement.
