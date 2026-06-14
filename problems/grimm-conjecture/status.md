# Status & Frontier — Grimm's Conjecture

**Status: open.** More than half a century after Grimm posed it in 1969, the conjecture is unresolved in general, and the strongest unconditional result remains essentially that of Ramachandra, Shorey, and Tijdeman (1976).

## What is known (unconditional)

- **Short blocks are settled.** Grimm's Conjecture holds for every block of consecutive composite integers $n+1,\dots,n+k$ with
$$k \;\le\; \exp\!\Big(c\,(\log n/\log\log n)^{1/2}\Big)$$
for an absolute constant $c>0$ (Ramachandra–Shorey–Tijdeman, 1976). Equivalently, the conjecture is true for all prime gaps that are short relative to $n$.
- **The reformulation is exact.** By Hall's marriage theorem, the existence of a distinct-prime assignment is equivalent to: every sub-block of $m$ of the integers has at least $m$ distinct prime factors. So the problem is *precisely* a lower bound on distinct prime factors of sub-blocks — no slack is lost in the translation.
- **Weak Grimm partial bounds.** Unconditional lower bounds for the number of distinct prime factors of $\prod_{i=1}^{k}(n+i)$ (Erdős, Pomerance, Shorey and others) are known and support, without proving, the full matching statement.
- **Computational verification.** No counterexample exists below large search bounds; explicit assignments have been constructed for all small prime gaps.

## What is known (conditional / structural)

- **Linkage to prime gaps (Erdős–Selfridge, 1971).** A strong general form of Grimm's Conjecture would imply prime-gap bounds of the shape $p_{m+1}-p_m \ll p_m^{1/2}/\log p_m$. This is stronger than what even the Riemann Hypothesis delivers ($p_{m+1}-p_m \ll p_m^{1/2}\log p_m$). Hence the conjecture is, in a precise sense, *harder than RH-level prime-gap control* in this direction.

## What a full resolution would require

A general proof must cover blocks as long as an **arbitrary** prime gap, not merely short ones. Because of the Erdős–Selfridge linkage, any such proof either (a) establishes prime-gap bounds beyond all current technology, or (b) finds a way to verify Hall's matching condition for long blocks *without* first proving those gap bounds — exploiting the fact that a maximal run of composites between consecutive primes has special multiplicative structure. No one knows how to do (b), and (a) is out of reach. The binding obstructions are the **parity/short-interval limitations of sieve theory** and our poor understanding of **smooth numbers in short intervals**, which is exactly where Hall's condition is most strained.

## Plausible routes

- **Improved distinct-prime-factor counts** for blocks, pushing the Ramachandra–Shorey–Tijdeman range upward via better sieve or smooth-number input.
- **Structural use of the prime-gap setting**: leveraging that the block lies strictly between two primes to gain extra distinct factors, potentially decoupling the result from generic gap bounds.
- **Advances on smooth numbers in short intervals**, which would directly relax the local failures of the matching condition.
- **Weak-Grimm-first strategies**, proving each $n+i$ has a large prime factor in wider ranges as a stepping stone.

There is currently **no claimed proof** of the general conjecture, disputed or otherwise, in the established record; the problem remains genuinely open and is widely regarded as requiring a new idea on prime spacing or smooth-number distribution.

## Related problems

- [Legendre's Conjecture](../legendre-conjecture/README.md) — primes in short intervals, directly governing the length of the composite blocks Grimm studies.
- [Twin Prime Conjecture](../twin-prime-conjecture/README.md) — small prime gaps, the opposite-extreme regime of prime spacing.
- [Polignac's Conjecture](../polignac-conjecture/README.md) — prescribed even prime gaps; shares the prime-spacing machinery.
- [Riemann Hypothesis](../riemann-hypothesis/README.md) — sets the conditional benchmark for prime-gap bounds that Grimm's strong form would have to exceed.
- [Cramér / Bunyakovsky-type questions](../bunyakovsky-conjecture/README.md) — multiplicative structure and prime values among consecutive-integer expressions.
