# History — Bunyakovsky's Conjecture

_Origin, formulation, and timeline._

## How the problem arose

The conjecture grew out of the oldest question about prime-producing formulas. Euclid had shown the primes are infinite; Dirichlet's 1837 theorem on primes in arithmetic progressions settled the degree-one case completely, proving that any linear polynomial $ax+b$ with $\gcd(a,b)=1$ represents infinitely many primes. The natural next question — what happens for nonlinear polynomials — was left open, and remains open to this day for every single polynomial of degree $\ge 2$.

In 1857 the Russian mathematician **Viktor Yakovlevich Bunyakovsky**, in a memoir of the St. Petersburg Academy, isolated the precise conditions under which a single irreducible integer polynomial in one variable ought to represent infinitely many primes. His insight was that two obvious obstructions, and only those two, can prevent a polynomial from being prime-rich.

## Precise formulation

Let $f(x) \in \mathbb{Z}[x]$ have degree $d \ge 1$ and positive leading coefficient. Bunyakovsky conjectured that $f(n)$ is prime for infinitely many positive integers $n$ provided $f$ satisfies all three of the following necessary conditions:

1. **Irreducibility** — $f$ is irreducible over $\mathbb{Q}$ (equivalently over $\mathbb{Z}$, by Gauss's lemma);
2. **Positive leading coefficient** (so $f(n) \to +\infty$);
3. **No fixed prime divisor** — the set $\{f(n) : n \in \mathbb{Z}\}$ has greatest common divisor $1$; equivalently there is no prime $p$ dividing every value $f(n)$.

Condition 3 is essential: $f(x)=x^2+x+2$ is irreducible yet always even, so it produces no primes beyond $2$. The condition can be checked finitely: a prime $p$ dividing all values must satisfy $p \le d$, so one tests only finitely many residues.

The canonical open instance is $f(x)=x^2+1$: does it represent infinitely many primes? This is **Landau's fourth problem** (1912), still unresolved, and it is precisely the simplest nonlinear Bunyakovsky case.

## Reformulations and generalizations

- The **Hardy–Littlewood Conjecture F** (1923) sharpens Bunyakovsky by predicting the *asymptotic density* of prime values via a singular series $\mathfrak{S}(f)$, giving $\#\{n\le N : f(n)\text{ prime}\}\sim \frac{C(f)}{d}\,\frac{N}{\log N}$.
- The **Schinzel Hypothesis H** (1958, with Sierpiński) generalizes Bunyakovsky to several polynomials simultaneously: if $f_1,\dots,f_k$ are irreducible with positive leading coefficients and $\prod f_i$ has no fixed prime divisor, then all are simultaneously prime infinitely often. Bunyakovsky is the case $k=1$.
- The **Bateman–Horn Conjecture** (1962) supplies the quantitative form of Hypothesis H, unifying Hardy–Littlewood F, the twin-prime constant, and the prime $k$-tuple heuristics into one density formula.

## Timeline

- **1837** — Dirichlet proves infinitely many primes in arithmetic progressions, settling the degree-one case.
- **1857** — Bunyakovsky states the conjecture in a memoir of the Imperial St. Petersburg Academy of Sciences.
- **1904** — Dickson states an analogous conjecture for systems of linear forms (a precursor to Hypothesis H).
- **1912** — Landau, at the Fifth International Congress of Mathematicians (Cambridge), lists "$n^2+1$ prime infinitely often" among four hard problems on primes — the flagship Bunyakovsky case.
- **1922–1923** — Hardy and Littlewood, in *Partitio Numerorum III*, give the conjectural asymptotic density (Conjecture F).
- **1958** — Schinzel and Sierpiński publish Hypothesis H, generalizing Bunyakovsky to multiple polynomials.
- **1962** — Bateman and Horn formulate the quantitative density conjecture.
- **1998** — Friedlander and Iwaniec prove infinitely many primes of the form $a^2+b^4$ — a sparse two-variable result, not a single-variable Bunyakovsky case but a landmark for thin sequences.
- **2001** — Heath-Brown proves infinitely many primes of the form $a^3+2b^3$.
- **2014** — Maynard and (independently) Tao introduce new sieve weights for bounded gaps; the methods illuminate $k$-tuple/Hypothesis-H structure though they do not reach degree $\ge 2$ Bunyakovsky cases.
- **Present** — No polynomial of degree $\ge 2$ in one variable is known to represent infinitely many primes; the conjecture is fully open, with $x^2+1$ as the emblematic unsolved instance.
