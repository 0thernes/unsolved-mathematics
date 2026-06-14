# History — The Erdős–Straus Conjecture

_Origin, formulation, and timeline._

## Origin

The conjecture belongs to the modern study of *Egyptian fractions* — representations of a rational number as a sum of unit fractions $1/m$. The subject reaches back to the Rhind Mathematical Papyrus (c. 1650 BCE), whose $2/n$ table expresses fractions $2/n$ as sums of unit fractions, and to Fibonacci's greedy algorithm (1202, *Liber Abaci*), which guarantees that every rational in $(0,1)$ admits *some* finite unit-fraction expansion. The natural twentieth-century refinement asks how *few* terms a given family requires.

Around 1948, **Paul Erdős** and **Ernst G. Straus** asked whether, for the family $4/n$, three terms always suffice. The precise statement: for every integer $n \ge 2$ there exist positive integers $a,b,c$ with
$$\frac{4}{n} = \frac{1}{a} + \frac{1}{b} + \frac{1}{c}.$$
The unit fractions need not be distinct and are taken positive. (For $n=2$, $4/2 = 1/1 + 1/2 + 1/2$; for $n=3$, $4/3 = 1/1 + 1/4 + 1/12$; the interesting range is large $n$.) It is a paradigm of an "elementary but unyielding" problem: trivial to check for any single $n$, yet resistant to a uniform proof.

## Reformulations

Several equivalent forms organize the attack:

- **Reduction to primes.** A solution for a divisor of $n$ scales to one for $n$, so the conjecture for all $n$ follows from the conjecture for all primes $p$. All difficulty concentrates on prime denominators.
- **Reduction to residue classes.** Constructions resolve $n$ according to its residue modulo small moduli. Following Mordell, solubility holds for every $n$ outside a finite set of classes modulo $840$; the unresolved cases are essentially the primes $p \equiv 1, 121, 169, 289, 361, 529 \pmod{840}$ — the squares of $1, 11, 13, 17, 19, 23$ — a sparse union of arithmetic progressions.
- **Diophantine form.** Clearing denominators, $4/n = 1/a+1/b+1/c$ is equivalent to the cubic-surface point-count $4abc = n(ab+bc+ca)$, tying solubility to whether certain quantities are quadratic residues modulo the divisors involved.

## Timeline

- **c. 1650 BCE** — Rhind Papyrus $2/n$ table establishes the Egyptian-fraction tradition.
- **1202** — Fibonacci's greedy algorithm (*Liber Abaci*) proves finite unit-fraction expansions always exist.
- **1948** — Paul Erdős and Ernst G. Straus pose the conjecture for $4/n$ (traditional date; it circulated in Erdős's problem lists from the late 1940s).
- **1950** — Erdős publishes on dense Egyptian-fraction questions, popularizing the $4/n$ problem in his problem-collecting network.
- **1954** — Richard Obláth verifies small cases and records partial congruence results.
- **1956–1958** — Work by Rosati, Bernstein, and others constructs solutions for broad residue classes; the modulo-$840$ framework takes shape.
- **1962** — Andrzej Schinzel and Wacław Sierpiński study the general $a/n$ family; Sierpiński states the analogous conjecture for $5/n$.
- **1964–1965** — Hagedorn, Yamamoto, and others give further constructions; the six hard square residue classes are isolated.
- **1967** — Mordell's *Diophantine Equations* records the modulo-$840$ reduction in textbook form, the standard reference for the residue obstruction.
- **1970** — R. C. Vaughan proves the exceptional set is sparse: the number of $n \le N$ for which $4/n$ might fail is $O\!\big(N \exp(-c(\log N)^{2/3})\big)$.
- **1976** — W. A. Webb and collaborators sharpen exceptional-set and density estimates.
- **1990s–2000s** — Allan Swett and others verify the conjecture computationally to roughly $n \le 10^{14}$.
- **2011** — Christian Elsholtz and Terence Tao publish a definitive analytic study, bounding the number of representations $f(n)$ on average and over arithmetic progressions, and connecting the problem to character sums and primes in special progressions.
- **2019–2024** — Continued computation pushes verification past $n \sim 10^{17}$; refined heuristics support the conjecture, which remains open for general $n$.

The problem stands today essentially where Mordell left it in structure: everything reduces to a sparse set of prime residue classes, none known to be universally soluble, and no argument rules out a single recalcitrant prime.
