# Approaches — Brocard's Problem

_Major strategies, partial results, and barriers._

Brocard's problem — finiteness of solutions to $n! + 1 = m^2$ — has attracted four broad lines of attack: elementary/congruence methods, the abc conjecture and Diophantine-approximation transfer, effective methods from transcendence theory, and large-scale computation. None has resolved it unconditionally; the structural reason is that $n!$ supplies almost no usable arithmetic *structure* (it is not a polynomial in $n$, nor a value of an elliptic/Thue form), so the powerful effective machinery that solves polynomial Diophantine equations does not directly apply.

## Elementary and congruence methods

The core idea is to write $n! = m^2 - 1 = (m-1)(m+1)$ and exploit the factorization. The two factors $m-1, m+1$ differ by $2$, so $\gcd(m-1,m+1) \in \{1,2\}$; since $n!$ is even for $n \ge 2$, one analyzes how the prime factorization of $n!$ (whose exponents are given by Legendre's formula $v_p(n!) = \sum_{k\ge1}\lfloor n/p^k\rfloor$) can split into two near-equal coprime-ish halves. Congruence obstructions modulo small primes and modulo squares rule out solutions in many residue classes and underlie the fast computational sieves. **Best result:** these methods confirm the three known solutions and supply efficient necessary conditions used in searches, but they cannot bound $n$. **Barrier:** factorials are "too smooth" — $n!$ has every small prime to high power, so square/congruence obstructions that kill generic Diophantine equations are automatically *satisfiable* here, and no single congruence forces $n!+1$ off the squares for large $n$.

## abc conjecture and Diophantine transfer

This is the most successful conditional approach. Applying the **abc conjecture** to the relation $1 + n! = m^2$ (i.e. $a=1$, $b=n!$, $c=m^2$) bounds $c = m^2$ in terms of the radical $\mathrm{rad}(abc) = \mathrm{rad}(n! \cdot m)$. Because $\mathrm{rad}(n!) = \prod_{p\le n} p = e^{(1+o(1))n}$ is exponentially smaller than $n! = e^{(1+o(1))n\log n}$, abc forces $n!$ to be bounded, yielding **finitely many solutions**. **Best result:** Overholt (and others) showed a weak form of abc implies Brocard's conjecture; this is the strongest known *finiteness* statement, and it extends to $n! + A = m^2$ and to $n! + 1 = m^k$. **Barrier:** the abc conjecture is itself open, and the argument is *ineffective in spirit* relative to what we want — it gives no explicit bound on $n$ without an explicit abc constant, and abc remains unproved (Mochizuki's claimed proof via inter-universal Teichmüller theory is not accepted by the broader community; see the abc dossier).

## Generalized equations and Dąbrowski's theorem

A productive strategy generalizes the constant: study $n! + A = m^2$ for fixed integer $A$. **Andrzej Dąbrowski (1996)** proved that for every fixed $A$ that is **not** a perfect square, the equation has only finitely many solutions, by combining factorization with growth/valuation estimates that fail precisely when $A$ is a square. **Best result:** complete finiteness for all non-square $A$, plus partial results for $n! + 1 = m^k$ and for products of consecutive factorials. **Barrier:** the case $A = 1$ — Brocard's original — is exactly the excluded square case. When $A$ is a square, $m^2 - A = (m-\sqrt A)(m+\sqrt A)$ factors over $\mathbb{Z}$, removing the obstruction Dąbrowski exploits, so his method gives no information about $A=1$.

## Effective methods: linear forms in logarithms and Pillai-type results

One hopes to import **Baker's theory of linear forms in logarithms**, which effectively solves equations like $a^x - b^y = c$ (Pillai's equation) and Thue–Mahler equations. **Best result:** Baker-type methods effectively bound solutions of many *fixed-base* exponential Diophantine equations and underlie Dąbrowski-style finiteness once the problem is reduced to a fixed shape. **Barrier:** $n!$ is not of the form $a^n$ or a value of a fixed polynomial/binary form — its "base" changes with $n$ — so Baker's machinery does not apply to $n!+1=m^2$ directly. There is no known reduction of the factorial to an object on which linear-forms-in-logarithms bounds bite, which is why no *effective* unconditional bound on Brown numbers exists.

## Probabilistic heuristics

A guiding (non-rigorous) approach models $n!+1$ as a random integer of its size; the chance it is a square near $m \approx \sqrt{n!}$ is $\sim m^{-1}$, and $\sum_n (n!)^{-1/2}$ converges extremely fast, predicting that the known list $\{4,5,7\}$ is almost certainly complete and that the *expected* number of solutions above any modest bound is essentially zero. **Best result:** strong support for the conjecture and quantitative predictions matching computation. **Barrier:** heuristics of this kind are not proofs and cannot distinguish "finitely many" from "no more"; they are explicitly inadmissible as evidence of finiteness in the rigorous sense.

## Summary of the obstruction

Across all approaches the recurring wall is the same: $n!$ has a huge, totally controlled set of small prime factors but no exploitable algebraic structure as a function of $n$. Congruences are too weak, effective transcendence methods do not engage, and the only argument that yields finiteness (abc) is conditional on a conjecture at least as hard as Brocard's problem itself. Computation closes off small $n$ but cannot close the problem.
