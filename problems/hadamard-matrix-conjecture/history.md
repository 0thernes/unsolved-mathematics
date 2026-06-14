# History — The Hadamard Matrix Conjecture

_Origin, formulation, and timeline._

## How the problem arose

A **Hadamard matrix** of order $n$ is an $n \times n$ matrix $H$ with entries in $\{+1,-1\}$ whose rows are pairwise orthogonal, equivalently $H H^{\top} = n I_n$. Such matrices attain, with equality, **Hadamard's determinant bound**: among all real matrices with entries bounded by $1$ in absolute value, $|\det| \le n^{n/2}$, and equality holds precisely for $\{\pm1\}$ matrices with orthogonal rows.

The objects predate Hadamard. **James Joseph Sylvester** constructed them in 1867 under the name "anallagmatic pavements," giving the recursive doubling $H \mapsto \begin{psmallmatrix} H & H \\ H & -H \end{psmallmatrix}$ that produces matrices of every order $2^m$. In 1893 **Jacques Hadamard** studied the determinant-maximization problem directly, proved the bound, and showed that equality forces $n = 1$, $n = 2$, or $n \equiv 0 \pmod 4$. He exhibited examples in orders $12$ and $20$ and asked whether such matrices exist for **every** multiple of $4$. That question is the conjecture.

The **order-$4k$ divisibility** is the only known necessary condition, and the conjecture asserts it is also sufficient: a Hadamard matrix of order $4k$ exists for every positive integer $k$. The second originator credited in the metadata, **Raymond Paley**, supplied in 1933 the first systematic infinite families via finite fields, dramatically enlarging the set of orders known to be achievable and reframing the problem as a number-theoretic existence question rather than a case-by-case search.

## Reformulations

The conjecture has several equivalent guises. Existence of a Hadamard matrix of order $4k$ is equivalent to existence of a symmetric **$2$-$(4k-1,\,2k-1,\,k-1)$ design** (a Hadamard design), and to existence of certain **regular two-graphs** and conference-type structures. Via the substitution of $\pm1$ rows by codewords, it is equivalent to existence of specific binary codes meeting the Plotkin bound. These dictionaries route attacks through design theory, finite geometry, group theory (difference sets and group-developed matrices), and algebraic number theory.

## Timeline

- **1867** — Sylvester constructs $\{\pm1\}$ orthogonal matrices of order $2^m$ ("anallagmatic pavements"), the first infinite family.
- **1893** — Hadamard proves the determinant bound, shows equality requires order $1$, $2$, or $4k$, gives examples in orders $12$ and $20$, and poses the existence question.
- **1898** — Scarpis gives early constructions tied to orders $p+1$.
- **1933** — Raymond Paley introduces the **Paley constructions** from quadratic residues in finite fields, yielding Hadamard matrices of orders $q+1$ and $2(q+1)$ for prime powers $q$, and lists the smallest unsettled orders.
- **1944** — **John Williamson** introduces the array method producing matrices of order $4n$ from four symmetric circulant blocks, the dominant tool for sporadic orders for decades.
- **1962** — **Baumert, Golomb, and Hall** construct a Hadamard matrix of order $92$ by computer via Williamson's method, eliminating the smallest then-open order.
- **1965** — **Goethals and Seidel** develop constructions via association schemes and strongly regular graphs.
- **1970s** — **Turyn** advances multiplicative use of **Baumert–Hall arrays** and launches the asymptotic-existence program.
- **1976** — Turyn proves an asymptotic theorem: a Hadamard matrix of order $2^t m$ exists once $t$ is large enough relative to odd $m$.
- **1985** — **Jennifer Seberry (Wallis)** proves that for every odd $m$ a Hadamard matrix of order $2^t m$ exists for all $t \ge 2\log_2(m-3)$, an explicit asymptotic bound.
- **2004–2005** — **Hadi Kharaghani and Behruz Tayfeh-Rezaie** construct a Hadamard matrix of order $428$, the smallest open order at the time.
- **2008** — Sharper asymptotic-existence results appear (de Launey, Craigen, Smith); after $428$ is settled the smallest open order becomes $668$.
- **2010s–present** — Order **$668$** remains the smallest undecided order; cocyclic and SAT/computational approaches advance, and the exponent in Seberry-type bounds is improved (e.g. by de Launey–Gordon under number-theoretic hypotheses).

The problem remains open: divisibility by $4$ is necessary and conjecturally sufficient, but no construction or argument covers all $k$.
