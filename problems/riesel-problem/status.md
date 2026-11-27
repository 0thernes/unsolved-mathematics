# Status & Frontier — The Riesel Problem

_Where the problem stands and what a resolution would require._

**Overall status: `active-progress` (OPEN; 41 odd candidates $k < 509{,}203$ remain uneliminated as of Wilfrid Keller's PrimeGrid tracking).**

## What is known

- **Smallest proven Riesel number:** $k = 509{,}203$ (Riesel 1956, covering primes $\{3,5,7,13,17,241\}$).
- **Remaining candidates:** Exactly **41** odd integers $k < 509{,}203$ remain without a known prime $k \cdot 2^n - 1$ (unchanged since late 2017) despite distributed LLR testing beyond $n > 10^7$ (PrimeGrid).
- **Covering-system constraints:** Hough (2015, `10.4007/annals.2015.181.1.6`) tightly constrained covering systems, reinforcing belief that no hidden covering-system Riesel number exists below $509{,}203$.
- **Formal tracking:** Formalized in Lean 4 in `google-deepmind/formal-conjectures` as `OeisA108129.conjecture` (`kind: open`, OEIS `A108129`).

## What a resolution requires

Either finding at least one prime $k \cdot 2^n - 1$ for each of the remaining 41 candidates below $509{,}203$ (which would settle the conjecture affirmatively by direct finite verification!), OR proving an extraordinary non-covering compositeness theorem for some remaining $k$.

## Related problems

- [Infinitude of Mersenne Primes](../mersenne-primes-infinitude/README.md)
- [The Bateman–Horn Conjecture](../bateman-horn-conjecture/README.md)
- [Schinzel's Hypothesis H](../schinzel-hypothesis-h/README.md)
