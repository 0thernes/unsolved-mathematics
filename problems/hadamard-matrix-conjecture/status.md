# Status & Frontier — The Hadamard Matrix Conjecture

_Where the problem stands and what a resolution would require._

## Current status: open (active progress)

The conjecture — **a Hadamard matrix of order $4k$ exists for every positive integer $k$** — remains unproven. The necessary condition $4 \mid n$ (for $n > 2$) is classical and is the *only* known obstruction; the conjecture asserts its sufficiency. No counterexample exists and none is expected: heuristic counts suggest the number of inequivalent Hadamard matrices of order $4k$ grows super-exponentially in $k$, so the difficulty is purely **constructive**, not a suspected impossibility.

## What is known (unconditional)

- **Infinite families.** Sylvester doubling (all $2^m$), the **Paley constructions** (orders $q+1$ and $2(q+1)$ for prime powers $q$), Williamson/Goethals–Seidel/base-sequence families, and **cocyclic** constructions together settle a set of orders of positive density and, in particular, all "small" orders up to the current frontier.
- **The smallest open order is $668 = 4 \cdot 167$.** Every multiple of $4$ below $668$ is known to admit a Hadamard matrix; $668$ has resisted Paley reach, Williamson search, base-sequence methods, and SAT/algebraic search. (The previous frontier, **order $428$**, was settled by **Kharaghani and Tayfeh-Rezaie**, *A Hadamard matrix of order 428*, J. Combin. Designs, 2005.)
- **Asymptotic existence (strongest general theorem).** For every odd $m$, a Hadamard matrix of order $2^t m$ exists for all $t \ge 2\log_2(m-3)$ (**Seberry/Wallis, 1985**), with the exponent later reduced by **Craigen** and by **de Launey–Gordon**. Equivalently: a Hadamard matrix of order $4m$ exists for *almost every* $m$, once a sufficient power of two is permitted.

## What is known (conditional)

Under number-theoretic hypotheses on the distribution of primes — for instance assuming strong forms of prime-gap estimates, sometimes Riemann-Hypothesis-flavored — the asymptotic exponent improves, narrowing the gap between "for large $t$" and the conjectural "$t = 2$." The **cocyclic Hadamard conjecture** (de Launey–Horadam) is a structured strengthening: it asserts a *cocyclic* Hadamard matrix exists at every order $4k$. It is open and at least as hard, but provides a cohomological target with its own conditional partial results.

## What a full resolution requires

A proof must produce, or prove the existence of, a $\{\pm1\}$ matrix with orthogonal rows at **every** order $4k$ — crucially including the infinitely many $k$ where $4k$ is far from any prime power and where doubling cannot help. Plausible routes:

1. **A universal construction** covering all residue classes, perhaps via cocyclic/relative-difference-set machinery that subsumes Paley and Williamson simultaneously.
2. **Lowering the asymptotic exponent to $t = 2$** outright, turning Seberry-type theorems into "for all $m$" via better number theory (primes in short intervals) plus combinatorial amplification.
3. **A probabilistic or entropy-counting existence proof** showing the family is non-empty at every order without explicit construction — none is currently known to work for orthogonality constraints this rigid.

The realistic expectation in the community is incremental: clearing $668$ and the next open orders, and shrinking the asymptotic exponent, rather than a single decisive theorem. The problem is regarded as genuinely hard but "morally true."

## Related problems

- [Riemann Hypothesis](../riemann-hypothesis/README.md) — prime-distribution estimates underlie the conditional asymptotic-existence bounds.
- [Goldbach Conjecture](../goldbach-conjecture/README.md) — a sibling additive/number-theoretic existence statement believed true with overwhelming numerical support but no proof.
- [Odd Perfect Numbers](../odd-perfect-numbers/README.md) — like the Hadamard conjecture, a single divisibility/structure condition whose sufficiency (or impossibility) has resisted constructive settlement.
- [Mersenne Primes Infinitude](../mersenne-primes-infinitude/README.md) — another existence-for-all-cases question entangled with prime powers.
