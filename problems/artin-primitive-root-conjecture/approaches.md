# Approaches — Artin's Primitive Root Conjecture

_Major strategies, partial results, and barriers._

## The Chebotarev / GRH approach (Hooley's method)

The dominant approach reformulates "$a$ is a primitive root mod $p$" as a sieve over the auxiliary number fields $k_q = \mathbb{Q}(\zeta_q, a^{1/q})$. For a prime $p$, $a$ is a primitive root mod $p$ iff for **every** prime $q \mid p-1$, $a$ is a non-$q$-th-power residue, which (for $p$ unramified) holds iff $p$ does **not** split completely in $k_q$. Writing $N_a(x)$ for the count of primes $p \le x$ with $a$ a primitive root, inclusion–exclusion over squarefree $q$ gives
$$
N_a(x) = \sum_{q \text{ squarefree}} \mu(q)\,\pi_a(x, q),
$$
where $\pi_a(x,q)$ counts $p \le x$ splitting completely in $k_q$. Each term is estimated by the **Chebotarev density theorem**, whose effective error term is controlled by the zeros of the Dedekind zeta function $\zeta_{k_q}$.

**Best result.** In **1967 Christopher Hooley** proved that, *assuming the Generalized Riemann Hypothesis* for all the fields $k_q$, the conjecture holds in full quantitative form: $N_a(x) \sim A(a)\, c_a \,\frac{x}{\log x}$ with the corrected constant. This remains the definitive conditional theorem.

**Barrier.** The unconditional Chebotarev error term (Lagarias–Odlyzko, effective Chebotarev) is too weak: summing $\pi_a(x,q)$ over $q$ up to a usable range requires power-saving error uniform in the degree of $k_q$, which only GRH currently delivers. The "tail" of large $q$ cannot be controlled unconditionally without a zero-free region for $\zeta_{k_q}$ that we cannot prove.

## The sieve approach (Gupta–Murty–Heath-Brown)

To go unconditional, one restricts the sieve so that only finitely many $q$ matter, trading the exact density for a *lower-bound* count. The key innovation (Gupta–Murty, then sharpened by Heath-Brown) combines a **lower-bound sieve** with results on the rank of certain multiplicative groups and with the **large sieve / Brun–Titchmarsh** inequalities to handle the contributions of small primes $q$ simultaneously for several candidate bases.

**Best result.** **D. R. Heath-Brown (1986)** proved unconditionally that Artin's conjecture (qualitative form) can fail for **at most two** prime values of $a$. Concretely: among any three multiplicatively independent integers (e.g. $2, 3, 5$), at least one is a primitive root for infinitely many primes; among the primes, at most two exceptions exist. Earlier, **Gupta–Murty (1984)** established it for an infinite (but thin, density-zero) set of $a$, of size $\gg x/(\log x)^2$ up to $x$.

**Barrier.** The method cannot identify *which* $a$ are the possible exceptions, nor can it handle a *single specified* base. It is a "non-effective dichotomy": it proves the conjecture for all but $\le 2$ bases without naming any. Removing the last exceptions appears to require essentially GRH-strength input.

## The character-sum / entanglement framework (Lenstra–Stevenhagen–Moree)

A more conceptual line, developed from the 1970s onward and systematized by **H. W. Lenstra, Peter Stevenhagen, and Pieter Moree**, recasts the correction factor $c_a$ through the **entanglement** of the Kummer extensions: the fields $k_q$ are not linearly disjoint, and their pairwise intersections (governed by the discriminant of $\mathbb{Q}(\sqrt{a})$ and quadratic reciprocity) produce the rational correction. This framework yields clean, uniform formulas for many *variants* — near-primitive roots, primitive roots in arithmetic progressions, the "$k$-th power" and matrix/$\mathrm{GL}_n$ versions, and elliptic-curve analogues.

**Best result.** Exact, GRH-conditional densities for a vast family of generalizations, and a transparent derivation of the corrected constant. Unconditional *average* results: e.g. averaging over $a$ in a range, the conjectured density holds (Goldfeld 1968; Stephens 1969; later refinements).

**Barrier.** Still GRH-conditional for individual densities; the framework reorganizes the analytic difficulty but does not remove the dependence on zero-free regions.

## Average and statistical results

A robust unconditional strand proves the conjecture **on average** over $a$. **Goldfeld (1968)** and **Stephens (1969)** showed that for almost all $a$, the density exists and equals the predicted value; the exceptional set is small. **P. J. Stephens (1976)** computed averaged constants. These results are unconditional but say nothing about any *particular* base.

**Barrier.** Averaging smooths out the dependence on individual zero-free regions, which is exactly why it succeeds — and exactly why it cannot resolve the conjecture for a named $a$.

## Function-field analogue

Over $\mathbb{F}_q(t)$, the relevant zeta functions are those of curves over finite fields, where the **Riemann Hypothesis is a theorem (Weil)**. Consequently the function-field analogue of Artin's conjecture has been established unconditionally (Bilharz 1937, modulo Weil's RH, completed once Weil proved it in 1948). This is the strongest evidence that GRH is the *right* sufficient hypothesis: the only missing ingredient in the number-field case is an analytic input that is already a theorem in the geometric case.
