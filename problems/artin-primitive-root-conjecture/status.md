# Status & Frontier — Artin's Primitive Root Conjecture

_Where the problem stands and what a resolution would require._

## Current status: active progress, conditionally resolved

Artin's primitive root conjecture is **open** in its primary form: for **no single specified integer** $a$ (not $2$, not $3$, not $10$) is it known unconditionally that $a$ is a primitive root for infinitely many primes. Yet the problem is unusually well understood — it is "morally solved," with the only missing ingredient being a deep analytic hypothesis.

## Strongest conditional result

**Hooley (1967)**, assuming the **Generalized Riemann Hypothesis** for the Dedekind zeta functions of the Kummer fields $\mathbb{Q}(\zeta_q, a^{1/q})$, proved the conjecture in full quantitative form. For $a$ not $-1$ and not a perfect square, the number of primes $p \le x$ with $a$ a primitive root is
$$
N_a(x) \sim c_a \cdot A(a) \cdot \frac{x}{\log x}, \qquad A(a) = \prod_q \left(1 - \tfrac{1}{q(q-1)}\right) \approx 0.3739558,
$$
where $c_a \in \mathbb{Q}$ is an explicit correction factor (equal to $1$ for generic $a$) depending on the squarefree part of $a$. This is universally accepted and remains the benchmark; the GRH dependence is the entirety of what stands between it and an unconditional theorem.

## Strongest unconditional results

- **Heath-Brown (1986):** Artin's conjecture (qualitative) fails for **at most two** prime values of $a$. Hence among any three multiplicatively independent integers — e.g. $\{2,3,5\}$ — at least one is a primitive root for infinitely many primes. The exceptions cannot be identified.
- **Gupta–Murty (1984):** the conjecture holds for an infinite, density-zero set of bases.
- **Goldfeld (1968), Stephens (1969):** the conjecture holds **on average** over $a$ and for **almost all** $a$, unconditionally.
- **Function-field case:** fully proved unconditionally (Bilharz 1937 + Weil's RH for curves, 1948).

## What a full resolution would require

Two routes are plausible. **(1) Prove enough of GRH** — specifically, sufficiently strong zero-free regions (or density estimates for zeros) for the family $\zeta_{\mathbb{Q}(\zeta_q, a^{1/q})}$, uniformly in $q$ — to make Hooley's argument unconditional for a named base. This is essentially as hard as GRH itself for the relevant fields. **(2) A new sieve or "GRH-avoiding" input** that controls the tail $\sum_{q \text{ large}} \mu(q)\,\pi_a(x,q)$ without zero-free regions, perhaps via additive-combinatorial or large-sieve advances that extend the Gupta–Murty–Heath-Brown method to a single specified $a$ and remove the two-exception ambiguity. No such input is currently on the horizon.

The function-field success (where RH is a theorem) is strong evidence that GRH is exactly the right and sufficient hypothesis, and that no counterexample exists — the conjecture is believed true with very high confidence; only the unconditional proof for individual bases is missing.

## Related problems

- [Riemann Hypothesis](../riemann-hypothesis/README.md) — the analytic engine; Artin's conjecture for any single base follows from its generalized form.
- [Schinzel's Hypothesis H](../schinzel-hypothesis-h/README.md) — another density/prime-structure conjecture provable on average but open in specifics.
- [Twin Prime Conjecture](../twin-prime-conjecture/README.md) — a sibling in analytic number theory where sieve methods give partial, GRH-free progress.
- [Lehmer's Totient Problem](../lehmer-totient-problem/README.md) — a related multiplicative-order / $(\mathbb{Z}/n)^\times$-structure question.
- [Bunyakovsky Conjecture](../bunyakovsky-conjecture/README.md) — prime values of polynomials, sharing the "true on heuristic grounds, hard in specifics" character.
