# Status & Frontier — Schinzel's Hypothesis H

_Where the problem stands and what a resolution would require._

**Status: open.** No instance of Hypothesis H is proved. Not a single nonlinear case is known — it is unproven that $n^2+1$ takes infinitely many prime values — and no prescribed multiple-polynomial (twin-type) case is known either. What exists is a dense band of partial results that approach the conjecture from several directions without reaching any concrete instance.

## What is known (unconditional)

- **Upper bounds of the right order.** Sieve methods (Brun, Selberg) bound the count of $n\le x$ with all $f_i(n)$ prime by $O\big(\mathfrak{S}\,x/(\log x)^k\big)$, matching the Bateman–Horn main term up to a constant. The conjecture cannot fail by overcounting.
- **Almost-primes.** Chen's theorem (1973) gives infinitely many $p$ with $p+2$ prime or $P_2$; analogous $P_r$ results hold for general systems. These stop one prime factor short by the **parity barrier**.
- **Thin-sequence primes.** Friedlander–Iwaniec ($a^2+b^4$, 1998) and Heath-Brown ($a^3+2b^3$, 2001) prove primality for sparse *two-variable* polynomials, breaking parity using bilinear structure absent in the one-variable case.
- **Linear systems of finite complexity.** Green–Tao (2008) and Green–Tao–Ziegler (2010–2012) prove the Hardy–Littlewood asymptotic for any system of linear forms of finite complexity — a large unconditional fragment of Dickson's conjecture, excluding the infinite-complexity twin pattern.
- **Bounded gaps / existential tuples.** Zhang (2014), Maynard (2015), and Polymath8 give infinitely many bounded prime $m$-tuples for every $m$ (prime gaps $\le 246$), proving that *some* admissible tuple recurs — but not any specified one.
- **Function-field analogue.** Sawin–Shusterman established Hypothesis H, twin-prime, and Bateman–Horn analogues over $\mathbb{F}_q[t]$ for suitable $q$, with power-saving error terms — the only setting where a full analogue is a theorem.

## What is known (conditional)

Under the Elliott–Halberstam conjecture, Maynard's sieve yields prime gaps $\le 12$; under generalized Elliott–Halberstam, $\le 6$. Hypothesis H itself implies twin primes, infinitely many $n^2+1$ primes, the Sophie Germain conjecture, and innumerable prescribed prime constellations — it is a standard hypothesis from which such consequences are derived. No known conjecture of comparable plausibility is known to *imply* Hypothesis H.

## What a full resolution would require

A proof must break the parity problem in the **one-variable** setting — currently the single hardest known obstacle. Sieves and the GPY/Maynard machinery cannot, on their own, force the number of prime factors of $F(n)$ down to exactly one for a prescribed configuration; the bilinear (Type II) information that rescued $a^2+b^4$ has no one-variable analogue. A resolution likely needs a fundamentally new arithmetic input — an equidistribution statement for $\mu$ or $\Lambda$ against polynomial values strong enough to defeat parity — or a transfer principle making the function-field success rigorous over $\mathbb{Z}$, which would in turn seem to require an unconditional substitute for the Riemann Hypothesis over $\mathbb{Z}$.

## Plausible routes

1. **Higher-order Fourier analysis extended past finite complexity** — the most direct attack on the linear (twin) heart, currently blocked at infinite complexity.
2. **New bilinear/dispersion inputs for one variable** — a one-variable analogue of the Friedlander–Iwaniec breakthrough; no candidate is known.
3. **Function-field-to-integer transfer** — making the Sawin–Shusterman geometry rigorous over $\mathbb{Z}$; presently heuristic only.

The consensus is that Hypothesis H is far from resolution; tractability is rated low precisely because the parity barrier is a structural theorem about current methods, not a removable gap.

## Related problems

- [Twin Prime Conjecture](../twin-prime-conjecture/README.md) — the canonical two-form linear instance.
- [Bunyakovsky Conjecture](../bunyakovsky-conjecture/README.md) — the single-polynomial special case.
- [Hardy–Littlewood k-tuple Conjecture](../hardy-littlewood-k-tuple/README.md) — the quantitative linear precursor.
- [Polignac's Conjecture](../polignac-conjecture/README.md) — prime gaps of every even size, a sibling consequence.
- [Legendre's Conjecture](../legendre-conjecture/README.md) — a related prime-distribution problem in short intervals.
