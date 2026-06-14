# Status & Frontier — Bunyakovsky's Conjecture

_Where the problem stands and what a resolution would require._

## Current status: open

Bunyakovsky's conjecture is **completely open for every polynomial of degree $\ge 2$**. There is not a single irreducible integer polynomial of degree two or higher that is *proven* to represent infinitely many primes. The degree-one case is Dirichlet's theorem (1837) and is settled; everything beyond it is conjectural. The emblematic unsolved instance is $f(x)=x^2+1$ (Landau's fourth problem, 1912).

## What is known (unconditional)

- **Almost-primes.** Iwaniec (1978): every admissible irreducible quadratic represents a $P_2$ (product of $\le 2$ primes) infinitely often. For $x^2+1$ this is the strongest unconditional result toward primality. Higher-degree polynomials admit $P_r$ results with $r$ growing in the degree (Halberstam–Richert weighted sieves).
- **Correct upper bounds.** Sieves give the conjecturally-sharp upper bound $\#\{n\le N : f(n)\text{ prime}\}\ll \frac{N}{\log N}$ with the right constant order; only the matching lower bound is missing.
- **Multivariate primes (not single-variable).** Friedlander–Iwaniec (1998), $a^2+b^4$; Heath-Brown (2001), $a^3+2b^3$ — genuine primes for *thin two-variable* polynomial sequences, achieved by breaking the parity barrier with bilinear sums. These do not cover any one-variable degree-$\ge 2$ polynomial.

## What is known (conditional)

- The **Bateman–Horn conjecture** gives the exact predicted density and is numerically confirmed to high precision; it implies Bunyakovsky. It is not proven.
- Under sufficiently strong and uniform forms of the prime $k$-tuple / Elliott–Halberstam-type hypotheses, Bunyakovsky-type conclusions follow — but those hypotheses are themselves open, and ordinary GRH is not known to suffice.
- **Function fields:** over $\mathbb{F}_q[t]$, Bunyakovsky/Hypothesis-H statements are *theorems* (Sawin–Shusterman for large $q$; Pollack and others), unconditionally — strong evidence the integer statement is true.

## What a full resolution would require

Two obstructions must both be overcome for a single-variable polynomial:

1. **Defeat the parity problem (Selberg).** No classical sieve can certify primality; one must inject a genuinely new arithmetic input (a Type-II / bilinear estimate, or an "asymptotic sieve for primes" with a usable error term) for the one-dimensional sequence $\{f(n)\}$.
2. **Supply RH-strength equidistribution without a second variable.** The function-field proofs lean on the Riemann hypothesis for curves and monodromy; the integer analogue would need comparable control over the distribution of $f(n)$ in residue classes with no extra variable to provide bilinear structure.

## Plausible routes

The most credible avenues are: (a) extending the Friedlander–Iwaniec asymptotic-sieve technology to recover a single-variable case (no one has found the required bilinear input); (b) a transfer of the function-field successes to $\mathbb{Z}$, which would likely require a major new equidistribution theorem; and (c) deductions from a proven fragment of the prime $k$-tuple conjecture strong enough to imply the $k=1$ case. All three are widely regarded as out of reach with present methods; even $x^2+1$ is expected to remain open for the foreseeable future.

## Related problems

- [Landau's / Legendre Conjecture](../legendre-conjecture/README.md)
- [Hardy–Littlewood k-tuple Conjecture](../hardy-littlewood-k-tuple/README.md)
- [Twin Prime Conjecture](../twin-prime-conjecture/README.md)
- [Polignac's Conjecture](../polignac-conjecture/README.md)
- [Goldbach Conjecture](../goldbach-conjecture/README.md)
