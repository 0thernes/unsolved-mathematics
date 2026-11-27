# Status & Frontier — The Bateman–Horn Conjecture

_Where the problem stands and what a resolution would require._

**Overall status: `open`.**

## What is known

- **Only proved case:** $k = 1, \deg f_1 = 1$ (Dirichlet's theorem on primes in arithmetic progressions, 1837, with prime number theorem in progressions).
- **Completely open cases:** Every single nonlinear polynomial ($k=1, \deg \ge 2$, including $n^2 + 1$) and every multi-polynomial system ($k \ge 2$, including Twin Primes $n, n+2$).
- **Numerical evidence:** Vast computational checks agree with the Bateman–Horn constant $C(f_1, \dots, f_k)$ to high accuracy across linear, quadratic, and cyclotomic families.
- **Formal tracking:** Formalized in Lean 4 in `google-deepmind/formal-conjectures` as `BatemanHornConjecture.bateman_horn_conjecture` (`kind: open`).

## What a resolution requires

A fundamental breakthrough bypassing the Selberg sieve parity barrier for both linear prime tuples and sparse single-variable polynomial sequences — likely requiring deep new equidistribution or automorphic / $L$-function cancellation theorems far beyond GRH and Elliott–Halberstam.

## Related problems

- [Schinzel's Hypothesis H](../schinzel-hypothesis-h/README.md)
- [The Hardy–Littlewood k-tuple Conjecture](../hardy-littlewood-k-tuple/README.md)
- [Bunyakovsky's Conjecture](../bunyakovsky-conjecture/README.md)
- [The Twin Prime Conjecture](../twin-prime-conjecture/README.md)
