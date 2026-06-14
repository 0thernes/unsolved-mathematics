# Status & Frontier — Singmaster's Conjecture

_Where the problem stands and what a resolution would require._

## Current status: open, with active analytic progress

Singmaster's conjecture — that the multiplicity $N(a) = \#\{(n,k):\binom{n}{k}=a\}$ is bounded by an absolute constant for all $a>1$ — remains **unproven**. It is classified as *active-progress*: the headline modern result is genuinely strong, but it controls multiplicity on average rather than pointwise, so the conjecture itself is untouched at the level of a single worst-case $a$.

## What is known

**Unconditional, uniform (all $a$).** The benchmark is the 1974 Abbott–Erdős–Hanson bound
$$N(a) = O\!\left(\frac{\log a}{\log\log a}\right),$$
still essentially unimproved for general $a$. This is exponentially weaker than the conjectured $O(1)$.

**Per-equation finiteness.** For each fixed pair $(k,\ell)$ the equation $\binom{n}{k}=\binom{m}{\ell}$ has finitely many solutions (Siegel/Faltings), and in many low cases — e.g. $\binom{n}{2}=\binom{m}{4}$ — the solution set has been *completely enumerated* via Baker's effective methods (de Weger and others). These give $N(a) \le 8$ for all $a$ outside a controlled set, but the bounds are not uniform across $(k,\ell)$.

**Strongest current result (2021).** Matomäki, Radziwiłł, Shao, Tao, and Teräväinen (arXiv:2106.03335) prove a power-saving bound on the number of nontrivial solutions $\binom{n}{k}=a$ with $a \le N$ and $k \ge 3$, of the form $O(N^{2/3})$ against the trivial $O(N\log N)$. Consequently the conjecture holds **on average**, and the set of $a$ with anomalously large multiplicity is very sparse. This is conditional on nothing — it is unconditional — but it is an *averaged* statement.

**Empirical.** No integer is known to occur more than six times in Pascal's triangle; $3003$ is the unique known sextuple occurrence, and exhaustive searches to large bounds find no septuple. Erdős conjectured the true maximum is $\le 8$ and attained only finitely often.

## What a full resolution would require

A proof must control a **single, arbitrary, potentially very rare $a$** — exactly the case that averaged and sparse-exceptional-set methods cannot reach. Concretely, one would need either (i) a uniform-in-$(k,\ell)$ bound on integral points of the curves $\binom{n}{k}=\binom{m}{\ell}$, which runs into the ineffectivity of Faltings's theorem and the lack of uniformity in known effective methods; or (ii) a structural reason — perhaps via abc-type smoothness obstructions — forbidding an integer from lying on too many of these curves at once. Neither is currently in reach.

## Plausible routes

- **Uniform Diophantine bounds.** A uniform version of the Bombieri–Lang / Caporaso–Harris–Mazur philosophy bounding the number of rational points on curves of bounded genus would, if unconditional, likely settle Singmaster. This is itself a deep open program.
- **abc-conditional smoothness arguments.** Repeated binomial coefficients force unusually structured integers; strong enough abc-type input could rule out high multiplicity, transferring the difficulty to abc.
- **Pushing the analytic method to pointwise control.** Extending the 2021 sieve-theoretic framework from averages to individual $a$ would require defeating the standard barrier that large-sieve/large-value methods are blind to a single sparse exception.

## Related problems

- [abc Conjecture](../abc-conjecture/README.md) — a natural conditional input for ruling out high multiplicity.
- [Erdős–Straus Conjecture](../erdos-straus-conjecture/README.md) — another deceptively elementary Erdős-circle number-theory problem about representations.
- [Brocard's Problem](../brocard-problem/README.md) — a sibling Diophantine equation ($n!+1=m^2$) attacked by similar finiteness/effective methods.
- [Grimm's Conjecture](../grimm-conjecture/README.md) — a Pascal/factorization-adjacent elementary conjecture resistant to current tools.
- [Twin Prime Conjecture](../twin-prime-conjecture/README.md) — shares the analytic-sieve toolkit (Matomäki–Radziwiłł methods) used in the 2021 advance.
