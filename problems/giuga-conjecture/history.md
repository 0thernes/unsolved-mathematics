# History — Giuga's Conjecture

_Origin, formulation, and timeline._

## Origin and statement

In 1950 the Italian mathematician Giuseppe Giuga, then at the University of Rome, observed a striking power-sum criterion for primality. Writing $S_n = \sum_{k=1}^{n-1} k^{\,n-1}$, he conjectured that for every integer $n>1$,
$$
n \text{ is prime} \iff S_n \equiv -1 \pmod n .
$$
The "$\Rightarrow$" direction is an immediate consequence of Fermat's little theorem: if $p$ is prime, each of the $p-1$ summands $k^{p-1}\equiv 1\pmod p$, so $S_p\equiv p-1\equiv -1\pmod p$. The content — and the open part — is the converse: that **no composite $n$ satisfies the congruence**. A composite $n$ for which $S_n\equiv -1\pmod n$ would be a *counterexample*, and Giuga's conjecture asserts none exists.

## Reformulations

Giuga himself reduced the converse to an elementary divisibility condition. A composite $n$ violates the conjecture (is a *Giuga number* / counterexample candidate) precisely when $n$ is squarefree and **for every prime $p\mid n$ one has $p\mid \big(\tfrac{n}{p}-1\big)$**, equivalently
$$
\sum_{p\mid n}\frac{1}{p}-\prod_{p\mid n}\frac{1}{p}\in\mathbb{Z}.
$$
This couples two conditions: each prime factor $p$ of $n$ must satisfy $p^2\mid (n-p)$, i.e. $n$ is both a *Carmichael-like* "Giuga number" **and** a *weak prime / Lehmer-type* object. Counterexamples must therefore be simultaneously Carmichael numbers (for the $a^{n-1}$ behavior) and satisfy the stronger $\sum 1/p - \prod 1/p\in\mathbb Z$ relation.

A second, equivalent formulation runs through **Bernoulli numbers**. Since $S_n=\sum_{k=1}^{n-1}k^{n-1}$ relates to $B_{n-1}$ via Faulhaber's formula, Giuga's congruence is equivalent to
$$
n\,B_{n-1}\equiv -1 \pmod n \quad(\text{for primes}),
$$
which Takashi Agoh independently conjectured around 1990. The combined statement — $p$ is prime iff $pB_{p-1}\equiv -1\pmod p$ — is the **Agoh–Giuga conjecture**, and the equivalence of the Agoh and Giuga forms is a theorem (Borwein–Borwein–Borwein–Girgensohn).

## Timeline

- **1950** — Giuseppe Giuga states the conjecture and proves the prime direction; reduces a counterexample to the squarefree divisibility condition $p\mid(n/p-1)$ for all $p\mid n$.
- **1950** — Giuga verifies computationally that no counterexample exists below $10^{1000}$ (by hand-bounded arguments on the number of prime factors).
- **1985** — Bedocchi studies the conjecture, sharpening bounds and clarifying the structure of hypothetical counterexamples; pushes the no-counterexample bound far higher.
- **c. 1990** — Takashi Agoh formulates the Bernoulli-number criterion $nB_{n-1}\equiv-1\pmod n$.
- **1996** — D. Borwein, J. M. Borwein, P. B. Borwein, and R. Girgensohn publish "Giuga's Conjecture on Primality" (*Amer. Math. Monthly*), proving the Agoh–Giuga equivalence and showing any counterexample must have at least 13 prime factors and exceed $10^{1700}$.
- **1996** — They introduce *Giuga sequences* and *Giuga numbers* as a combinatorial relaxation, separating the two halves of the condition.
- **2009** — José María Grau and Antonio Oller-Marcén, and collaborators, generalize Giuga numbers and study density/finiteness questions for the relaxed objects.
- **2012–2013** — Computational verification extends the lower bound on any counterexample beyond roughly $10^{13{,}800}$ (counterexample must have $>13{,}000$ digits and a large number of distinct prime factors).
- **Present** — The conjecture remains **open**. No counterexample is known and none can be small; the converse direction is unproven, and it is unknown whether infinitely many *Giuga numbers* (the relaxed counterexample objects) exist.
