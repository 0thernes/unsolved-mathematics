# Status & Frontier — Infinitude of Mersenne Primes

**Status: open.** It is not known whether there are infinitely many primes of the form $2^p - 1$, nor whether there are infinitely many composite $M_p$ with $p$ prime — though the latter is essentially certain and far easier in spirit. No conditional proof exists either: the statement does not follow from the Riemann Hypothesis, the Generalized Riemann Hypothesis, Schinzel's Hypothesis H, or any other standard conjecture known to be reducible to it.

## What is known (unconditional)

- **Necessary structure.** $M_n$ can be prime only if $n=p$ is prime. Every prime factor $q$ of $M_p$ satisfies $q \equiv 1 \pmod{2p}$ and $q \equiv \pm1 \pmod 8$. These constraints make $M_p$ disproportionately likely to be prime and underpin both the search and the heuristic.
- **A deterministic test.** The Lucas–Lehmer test decides primality of $M_p$ in $\tilde{O}(p^2)$ bit operations (near-linear in the number of digits per squaring, with $p$ squarings), which is why Mersenne numbers dominate the largest-known-prime record.
- **The empirical record.** Exactly **52 Mersenne primes** are known. The largest, and the largest known prime of any kind, is $M_{136279841} = 2^{136279841}-1$ (41{,}024{,}320 digits), found in October 2024 through GIMPS by Luke Durant on GPU hardware. As of this writing all exponents below roughly the high tens of millions have been checked at least once, and a large initial range has been double-checked.

## What is known (conditional / heuristic)

- The **Lenstra–Pomerance–Wagstaff heuristic** predicts that the number of Mersenne primes with exponent $\le x$ is $\sim \frac{e^\gamma}{\log 2}\log x$, hence infinitely many; the 52 known primes fit this model closely. This is a *prediction*, not a theorem.
- The **New Mersenne Conjecture** (Bateman–Selfridge–Wagstaff, 1989) constrains the joint behavior of $2^p-1$ and $(2^p+1)/3$ but is itself open and does not bound the count.
- Conditional results in adjacent territory (e.g. Hooley's GRH-conditional proof of Artin's primitive-root conjecture) show that even the conditional toolkit does not reach the Mersenne question.

## What a full resolution would require

A proof of infinitude would have to exhibit infinitely many primes in the **exponentially sparse deterministic sequence** $\{2^p - 1\}$. This demands a fundamentally new method: current analytic number theory cannot produce a single prime — let alone infinitely many — in *any* sequence growing as fast as $2^p$. The **parity barrier** blocks sieve approaches from yielding a positive lower bound on primes (as opposed to almost-primes) in such a thin set, and probabilistic heuristics, however accurate, cannot be promoted to lower bounds. A resolution would likely illuminate the entire class of "primes in thin sequences" problems (Fermat primes, primes $n^2+1$, etc.) simultaneously.

## Plausible routes

There is no route that experts regard as promising. The realistic near-term activity is: (i) continued GIMPS searches extending the record and tightening the empirical fit to the heuristic; (ii) sharper heuristics and partial results on the *density of composite* $M_p$ and on divisor distribution; and (iii) progress on enabling sub-questions (Artin's conjecture, the order of $2$ modulo $q$, sieve parity-breaking) that would be prerequisites for any eventual attack. A genuine proof, if it comes, is expected to require an advance in analytic number theory comparable to resolving primes in other thin families — a prospect generally judged decades or more away, if attainable at all.

## Related problems

- [Twin Prime Conjecture](../twin-prime-conjecture/README.md) — another infinitude-of-primes question in a thin set, blocked by the same parity barrier.
- [Odd Perfect Numbers](../odd-perfect-numbers/README.md) — directly linked via Euclid–Euler; even perfect numbers correspond to Mersenne primes.
- [Lehmer's Totient Problem](../lehmer-totient-problem/README.md) — kindred question on the multiplicative structure of $2^n-1$-type quantities.
- [Polignac's Conjecture](../polignac-conjecture/README.md) — generalized prime-gap infinitude facing analogous sieve obstructions.
- [Legendre's Conjecture](../legendre-conjecture/README.md) — primes in a thin range, sharing the difficulty of producing primes in sparse deterministic sets.
