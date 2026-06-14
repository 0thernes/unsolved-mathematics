# Status & Frontier — The Erdős–Straus Conjecture

_Where the problem stands and what a resolution would require._

## Current status

The conjecture is **open** (metadata status: *active-progress*). It is known to be true for "almost all" $n$ in a strong quantitative sense and has been verified computationally for all $n$ up to at least $\sim 10^{17}$, yet no proof exists for general $n$, and no single counterexample is known. The problem is widely believed to be true.

## What is known (unconditional)

- **Reduction.** It suffices to prove $4/p = 1/a+1/b+1/c$ for primes $p$; solutions for divisors scale up to all composites.
- **Residue classes (Mordell, 1967).** $4/n$ is soluble for every $n$ outside the six classes $n \equiv 1, 121, 169, 289, 361, 529 \pmod{840}$ — the squares of $1,11,13,17,19,23$. Only primes in these sparse progressions remain open.
- **Exceptional set (Vaughan, 1970).** The count of $n\le N$ that could fail satisfies $E(N) \ll N\exp\!\big(-c(\log N)^{2/3}\big)$ — exponentially few, if any.
- **Representation counts (Elsholtz–Tao, 2011).** Sharp average and higher-moment bounds for the number of solutions $f(n)$, including behavior on prime $n$ and on arithmetic progressions, plus the link to point-counts on associated cubic congruences. This is the strongest structural result to date.
- **Computation.** Verified for all $n$ to roughly $10^{17}$, with the number of representations growing.

## Conditional results

There are no clean "assuming RH/GRH it follows" theorems that close the conjecture. The relevant conditional flavor is heuristic: standard conjectures on the distribution of primes in arithmetic progressions (and the equidistribution of associated quadratic-residue conditions) make the existence of a counterexample appear extremely improbable, since for each hard prime $p$ the density of admissible $(a,b,c)$ grows. But these heuristics, like the analytic bounds, cannot exclude an individual exceptional $p$.

## What a full resolution would require

A proof must handle the six square residue classes modulo $840$ *uniformly over all primes in them*. The decisive obstruction is that any finite collection of parametric identities solves a given prime only when a fixed quadratic-residue condition holds, and by quadratic reciprocity and Dirichlet's theorem the "bad" residues recur with positive density in each class — so **no finite identity list can suffice**. A resolution therefore needs a genuinely new mechanism that produces a solution for *every* prime in a square class without depending on a fixed Legendre-symbol condition. Equally, any disproof must exhibit a specific prime $p$ for which $4abc = p(ab+bc+ca)$ has no positive integral solution — something the computational and analytic evidence makes look very unlikely.

## Plausible routes

- **Beyond finite identities.** Constructions whose validity depends on a *varying* divisor of $p\pm$(small) rather than a fixed modulus, perhaps drawing on the geometry of the cubic surface and descent/Brauer–Manin analysis of the family.
- **Analytic forcing.** Strengthening Elsholtz–Tao-type lower bounds for $f(p)$ to a guarantee $f(p)\ge 1$ for all large $p$ in the hard classes — currently out of reach because the methods average and cannot pin a single prime.
- **Character-sum input.** New estimates for the relevant character/exponential sums that would force solubility pointwise in the square classes.

No route is close to completion; the square classes modulo $840$ remain the hard, open core, exactly where Mordell's reduction left them.

## Related problems

- [Goldbach Conjecture](../goldbach-conjecture/README.md) — another elementary additive statement over the integers, resistant despite overwhelming numerical and almost-all evidence.
- [Odd Perfect Numbers](../odd-perfect-numbers/README.md) — a classical Diophantine existence question with strong constraints but no resolution, sibling in the "elementary yet unyielding" family.
- [Singmaster Conjecture](../singmaster-conjecture/README.md) — an Erdős-flavored finiteness/representation problem from combinatorial number theory.
- [Lonely Runner Conjecture](../lonely-runner-conjecture/README.md) — another deceptively simple Diophantine statement open across residue/parameter ranges.
- [Brocard Problem](../brocard-problem/README.md) — an elementary Diophantine equation, open with only finite verification, paralleling the status of $4/n$.
