# Approaches — The Hadamard Matrix Conjecture

_Major strategies, partial results, and barriers._

## Sylvester / Kronecker doubling

The oldest method exploits the **tensor (Kronecker) product**: if $H_a$ and $H_b$ are Hadamard of orders $a,b$, then $H_a \otimes H_b$ is Hadamard of order $ab$. Starting from $H_2 = \begin{psmallmatrix} 1 & 1 \\ 1 & -1 \end{psmallmatrix}$ this yields all orders $2^m$ (Sylvester, 1867). Combined with any seed matrix of order $4k$, doubling settles $2^t \cdot 4k$ for all $t \ge 0$.

**Barrier.** Multiplicativity alone cannot reach orders whose odd part is itself unreachable; it only propagates known orders upward by powers of $2$. It contributes nothing to a *first* construction at a new odd multiple.

## Paley constructions (finite-field / quadratic-residue)

Using the Legendre symbol over $\mathbb{F}_q$, Paley (1933) builds Hadamard matrices of order $q+1$ for $q \equiv 3 \pmod 4$ and order $2(q+1)$ for $q \equiv 1 \pmod 4$, $q$ a prime power. Together with doubling, the Paley families settle a positive-density set of orders and remain the backbone of existence tables.

**Barrier.** The reachable orders are constrained to neighborhoods of prime powers; many $4k$ (e.g. $4k = 4 \cdot 167 = 668$) lie outside all Paley-plus-doubling reach, leaving an infinite residue of orders the method cannot touch.

## Williamson's method and plug-in arrays

**Williamson (1944)** writes a Hadamard matrix of order $4n$ as a $4 \times 4$ array of symmetric circulant $n \times n$ blocks $A,B,C,D$ satisfying $A^2+B^2+C^2+D^2 = 4n\,I$. The search reduces to four $\pm1$ sequences with a sum-of-squares autocorrelation condition. **Baumert–Hall arrays** and **Goethals–Seidel arrays** generalize the plug-in to $T$-matrices and **base sequences**, decoupling the array from the sequences.

**Best result / barrier.** This machinery has produced most sporadic orders and famously cleared order $92$ (Baumert–Golomb–Hall, 1962). But Williamson matrices of certain orders **provably do not exist** (e.g. exhaustive search ruled out Williamson-type solutions at order $4 \cdot 35 = 140$ and others), so the method is not universal; it must be supplemented at infinitely many orders.

## Difference sets, group development, and cocyclic matrices

Many Hadamard matrices are **group-developed** or, more generally, **cocyclic**: $H_{g,h} = \psi(g,h)$ for a 2-cocycle $\psi$ over a finite group $G$ of order $4k$. The **cocyclic Hadamard conjecture** (de Launey–Horadam) posits that a cocyclic Hadamard matrix exists at every order $4k$; this is a sharper, more structured target equivalent in spirit to the main conjecture and amenable to **relative difference set** and **group-cohomology** techniques. Menon–Hadamard difference sets give regular (group-developed) Hadamard matrices of order $4m^2$.

**Best result / barrier.** Cocyclic methods unify Sylvester, Paley, and Williamson constructions and have produced new orders computationally, but proving the *cocyclic* conjecture is at least as hard, and the cohomological search space grows rapidly with $k$.

## Asymptotic existence

Rather than every order, one proves existence for all *sufficiently large* power-of-two multiples. **Turyn (1970s)** and then **Seberry/Wallis (1985)** showed: for each odd $m$, a Hadamard matrix of order $2^t m$ exists whenever $t \ge 2\log_2(m-3)$. Subsequent work (**Craigen**, **de Launey**, **de Launey–Gordon**) lowered the exponent; conditional on number-theoretic hypotheses (e.g. concerning primes in short intervals or the Riemann Hypothesis–flavored estimates), the bound improves further.

**Best result / barrier.** These are the strongest *general* theorems known: a definite Hadamard matrix exists in every order $2^t m$ for $t$ logarithmic in $m$. But the conjecture demands $t = 2$ (i.e. order $4m$ for *every* odd $m$), and the gap between "for large $t$" and "for $t=2$" is exactly the unsolved core. No asymptotic theorem reaches the $4m$ frontier.

## Computational and SAT/algebraic search

Exhaustive and heuristic searches — backtracking over Williamson sequences, **SAT solvers**, **Gröbner/algebraic** modeling, and metaheuristics — settle individual open orders one at a time. This route cleared $428$ (Kharaghani–Tayfeh-Rezaie, 2005).

**Barrier.** The search space is exponential in the order; computation resolves specific $k$ but yields no general theorem. Order $668$ has resisted all such efforts to date.

## Negative and structural obstructions

There are **no known obstructions** beyond $4 \mid n$: the conjecture has never been contradicted, and counting heuristics suggest the number of inequivalent Hadamard matrices of order $4k$ grows super-exponentially, making non-existence at any large order intuitively unlikely. The genuine barriers are *constructive*, not impossibility results: each method (Paley, Williamson, cocyclic) covers a structured but incomplete set of orders, and **no single framework is known to cover all residue classes simultaneously**. This is the analogue here of the "parity barrier" in sieve theory — not a proof of impossibility, but a structural reason every existing technique falls short of all $k$.
