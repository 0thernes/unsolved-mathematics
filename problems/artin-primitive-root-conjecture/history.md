# History — Artin's Primitive Root Conjecture

_Origin, formulation, and timeline._

## How the problem arose

A *primitive root* modulo a prime $p$ is an integer $a$ whose powers $a, a^2, \dots, a^{p-1}$ run through every nonzero residue class mod $p$; equivalently, $a$ generates the cyclic group $(\mathbb{Z}/p\mathbb{Z})^\times$. The question of whether a *fixed* integer $a$ is a primitive root for infinitely many primes — and, if so, how often — is a natural sequel to Gauss's study of primitive roots in the *Disquisitiones Arithmeticae* (1801). Gauss famously asked whether $10$ is a primitive root infinitely often, a question motivated by the decimal expansion of $1/p$ having maximal period $p-1$.

The conjecture in its modern form was posed by **Emil Artin** in a conversation with **Helmut Hasse on 27 September 1927**, recorded in Hasse's diary. Artin asserted that any integer $a$ which is neither $-1$ nor a perfect square is a primitive root modulo infinitely many primes. More strikingly, he proposed a *quantitative* form: the set of such primes has a positive natural density among all primes.

## The precise formulation

For $a \neq -1$ and $a$ not a perfect square, Artin conjectured that the density of primes $p$ for which $a$ is a primitive root equals
$$
A(a) = \prod_{q \text{ prime}} \left(1 - \frac{1}{q(q-1)}\right) \quad (\approx 0.3739558\ldots)
$$
when $a$ is "generic," where the displayed product is **Artin's constant**. The heuristic: $a$ is a primitive root mod $p$ iff for every prime $q \mid p-1$, $a$ is not a $q$-th power mod $p$. The "probability" that $q \mid p-1$ and $a$ is a $q$-th power is $\frac{1}{q(q-1)}$, and assuming independence gives the product.

## Reformulation and the correction

Artin's original heuristic contained a subtle error. In **1957**, computations by the **Lehmers (Derrick H. Lehmer and Emma Lehmer)** revealed that for certain $a$ the predicted density disagreed with numerical data. Artin and others realized the events "$q \mid p-1$" and "$a$ is a $q$-th power mod $p$" are not always independent: when $a$ has a nontrivial structure (e.g. $a = b^k$, or the discriminant of $\mathbb{Q}(\sqrt{a})$ has specific divisibility), entanglement between the $q$-th power residue conditions and the splitting of $p$ in $\mathbb{Q}(\sqrt{a})$ forces a *correction factor*. The corrected density, established under hypothesis by Hooley, is $A(a)$ times an explicit rational factor depending on the squarefree part of $a$.

## Timeline

- **1801** — Gauss, in *Disquisitiones Arithmeticae*, studies primitive roots and the period of decimal fractions; implicitly raises the case $a=10$.
- **1927** — Emil Artin formulates the conjecture (and its density form) in conversation with Helmut Hasse (recorded 27 Sept 1927).
- **1957** — D. H. and Emma Lehmer's numerical computations expose a discrepancy, prompting the correction factor for the density.
- **1965** — Christopher Hooley proves the conjecture (qualitative and quantitative, with the corrected constant) **conditionally on the Generalized Riemann Hypothesis** for Dedekind zeta functions of the fields $\mathbb{Q}(\zeta_q, a^{1/q})$.
- **1967** — Hooley's result published in *Crelle's Journal*; the GRH-conditional density becomes the benchmark.
- **1976** — P. J. Stephens and others refine the heuristic; the "Stephens constant" and average results appear.
- **1984** — Rajiv Gupta, M. Ram Murty (and independently the sieve circle) make the first unconditional progress: infinitely many primes for a thin set of $a$.
- **1986** — **Gupta–Murty** and, decisively, **D. R. Heath-Brown** prove unconditionally that Artin's conjecture (qualitative form) holds for all but at most **two exceptional primes** $a$ — so at least one of $2, 3, 5$ is a primitive root for infinitely many primes.
- **2000** — Pieter Moree begins systematic surveys; the "Artin constant" zoo and near-primitive-root variants are catalogued.
- **2002** — Moree and collaborators extend conditional results to function-field and matrix analogues.
- **2012–present** — Lenstra, Moree, Stevenhagen develop the character-sum / entanglement framework giving a uniform conceptual proof of the correction factor (still GRH-conditional for the density). The unconditional qualitative case for any *single specified* $a$ remains open.
