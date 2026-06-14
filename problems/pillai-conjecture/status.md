# Status & Frontier — Pillai's Conjecture

_Where the problem stands and what a resolution would require._

**Status: open.** For every $k \ge 2$, the full conjecture — that $x^p - y^q = k$ has only finitely many solutions with $p, q \ge 2$ and variable exponents — remains unproven. Equivalently, it is not known unconditionally that the gaps between consecutive perfect powers tend to infinity.

## What is known (unconditional)

- **Fixed exponents.** For any fixed pair $p, q \ge 2$, the equation $|x^p - y^q| = k$ has only finitely many solutions, and they are effectively computable (Baker's method, refined by Tijdeman, Mignotte, Bennett, Bugeaud). In many cases the exact count is $\le 2$ and the full solution set is known.
- **The case $k = 1$ (Catalan).** Completely solved: $3^2 - 2^3 = 1$ is the only nontrivial solution, with **all** exponents. This is Mihăilescu's theorem (P. Mihăilescu, *Primary cyclotomic units and a proof of Catalan's conjecture*, J. reine angew. Math. **572** (2004), 167–195), via cyclotomic field theory; Tijdeman (1976) had earlier given effective finiteness for $k=1$.
- **Many individual equations.** Modular (Frey-curve) methods have resolved numerous specific $x^p \pm y^q = k$ and Lebesgue–Nagell equations $x^2 + D = y^n$ unconditionally for fixed signatures (Bennett, Bugeaud, Mignotte, Siksek).
- **Recurrence-sequence variants.** "Pillai's problem" for Fibonacci and other linear recurrences (e.g. $F_n - 2^m = c$) is solved in many concrete families by the Luca school using Baker's method plus reduction.

## What is known (conditional)

- **Under the $abc$ conjecture, Pillai's conjecture holds in full** — for all $k$ simultaneously, including variable exponents, with an effective bound. This is the cleanest known route to the whole statement, but $abc$ is itself open. (Mochizuki's IUT claim for $abc$ is **not accepted** by the community following the 2018 Scholze–Stix objections, so it cannot be treated as resolving Pillai.)

## What a full resolution requires

The single missing ingredient is an unconditional bound on the **exponents** $p, q$ in terms of $k$ for $k \ge 2$. Every existing unconditional method controls $x, y$ once $p, q$ are fixed; none caps $p, q$ themselves outside the Catalan case. Concretely, a proof would need either:

1. a proof of the $abc$ conjecture (or of the weaker effective consequence sufficient to bound exponents), or
2. an extension of Mihăilescu's cyclotomic framework — which exploits the special arithmetic forced by the difference being exactly $1$ — to differences $k \ge 2$, or
3. a uniform modular/Galois-representation argument working across all exponent signatures for a fixed $k$, beyond the current case-by-case reach.

## Plausible routes

The $abc$-conditional implication is the most promising structurally, so progress on $abc$ (even partial, "$abc$-with-an-epsilon" type results, or the Stewart–Yu linear-forms bounds toward it) is the most-watched lever. The modular method continues to chip away at individual $k$ and signatures, and the recurrence-sequence program steadily extends the catalog of solved special cases — but none of these currently threatens the variable-exponent core for any $k \ge 2$.

## Related problems

- [Catalan / abc connection](../abc-conjecture/) — $abc$ implies Pillai in full.
- [Beal's conjecture](../beal-conjecture/) — sibling conjecture on perfect powers with a common-factor twist.
- [Brocard's problem](../brocard-problem/) — another sparse-perfect-power Diophantine question.
- [Hall's conjecture](../hall-conjecture/) — quantitative lower bound on $|x^3 - y^2|$, a sharp Pillai-type gap statement.
- [Schinzel's Hypothesis H](../schinzel-hypothesis-h/) — related conjectural structure governing values of polynomials, in the same $abc$-adjacent circle of Diophantine problems.
