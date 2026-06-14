# Approaches — Giuga's Conjecture

_Major strategies, partial results, and barriers._

Throughout, a *counterexample* means a composite $n$ with $\sum_{k=1}^{n-1}k^{n-1}\equiv -1\pmod n$. By Giuga's reduction such an $n$ is squarefree with $p\mid(n/p-1)$ for every prime $p\mid n$. Equivalently $n$ is a **Giuga number** (satisfying $\sum_{p\mid n}1/p-\prod_{p\mid n}1/p\in\mathbb Z$) that is *also* a Carmichael number. The strategies below all attack this double condition.

## Elementary divisibility / counting prime factors

**Core idea.** A counterexample $n=p_1\cdots p_k$ is squarefree and satisfies, for each $i$, $p_i\mid \prod_{j\ne i}p_j - 1$. Summing the conditions yields the relation $\sum_i 1/p_i-1/n\in\mathbb Z$, which forces $\sum_i 1/p_i>1$ and hence a lower bound on $k$ (the more primes, the easier $\sum 1/p_i$ can exceed $1$, but each $p_i$ must then be large). Careful bookkeeping of these constraints bounds counterexamples from below.

**Best result.** Giuga (1950) already excluded counterexamples below $10^{1000}$; Bedocchi (1985) and then Borwein–Borwein–Borwein–Girgensohn (1996) showed any counterexample must have **at least 13 distinct prime factors** and exceed $10^{1700}$. Subsequent computation pushed this past $\sim 10^{13{,}800}$ with thousands of prime factors required.

**Barrier.** The counting argument gives ever-larger *lower bounds* but no finiteness: nothing in it forbids an enormous $n$ with sufficiently many factors. It cannot, by itself, prove that the set of counterexamples is empty.

## Carmichael-number structure

**Core idea.** Every counterexample is a Carmichael number, so the conjecture is a statement *about a thin subset of Carmichael numbers* — those additionally satisfying the Giuga relation. One hopes to import the rich structure theory of Carmichael numbers (Korselt's criterion, Alford–Granville–Pomerance infinitude) to constrain or exclude the Giuga subset.

**Best result.** Korselt's criterion characterizes Carmichael numbers cleanly, and the extra Giuga condition $p\mid(n/p-1)$ is strictly stronger than Korselt's $p-1\mid n-1$. This shows counterexamples are *much* rarer than Carmichael numbers.

**Barrier.** Alford–Granville–Pomerance (1994) proved there are infinitely many Carmichael numbers, so the ambient set is infinite; the Giuga sub-condition is not known to be satisfiable or unsatisfiable infinitely often. The structure theory constrains but does not close the gap.

## Bernoulli-number / Agoh formulation

**Core idea.** Reformulate via $nB_{n-1}\equiv -1\pmod n$ (Agoh–Giuga). Bernoulli numbers carry deep $p$-adic and Kummer-congruence structure, raising the hope that von Staudt–Clausen and Kummer-type tools could force the congruence to fail for composites.

**Best result.** Borwein–Borwein–Borwein–Girgensohn (1996) proved the Agoh and Giuga forms are *equivalent*, unifying the two literatures. The von Staudt–Clausen theorem gives exact control of the denominators of $B_{n-1}$, which feeds back into the divisibility analysis.

**Barrier.** The equivalence is a translation, not a resolution: the Bernoulli form inherits the same difficulty. No known $p$-adic congruence rules out the required composite behavior.

## Giuga numbers and the relaxed problem

**Core idea.** Split the double condition. A **Giuga number** satisfies only the multiplicative relation $\sum_{p\mid n}1/p-\prod_{p\mid n}1/p\in\mathbb Z$ (without the Carmichael/Fermat part). These *do* exist — the smallest is $30=2\cdot3\cdot5$, followed by $858$, $1722$, $66198$, and others. Studying their density and growth probes how close the relaxed objects come to genuine counterexamples.

**Best result.** Several Giuga numbers are known explicitly, and Borwein et al. and later Grau–Oller-Marcén characterized *Giuga sequences* combinatorially, constructing infinite families of the sequence objects. It is known that any Giuga number has at least three prime factors and grows rapidly.

**Barrier.** Known Giuga numbers are **not** counterexamples — they fail the Carmichael condition. Whether infinitely many Giuga numbers exist is itself open, and even an affirmative answer would not produce a Giuga *counterexample*. This separates the tractable combinatorial problem from the intractable primality one.

## Computational verification

**Core idea.** Directly rule out counterexamples up to a bound by exploiting the structural constraints (squarefree, many prime factors, $\sum 1/p_i$ near an integer) to make an exhaustive-in-structure search feasible far beyond naive ranges.

**Best result.** No counterexample exists below roughly $10^{13{,}800}$; any counterexample needs on the order of $13{,}000$+ digits and thousands of distinct prime factors.

**Barrier.** Verification is unbounded above and cannot constitute a proof. It only raises the floor a hypothetical counterexample must clear.
