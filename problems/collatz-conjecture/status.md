# Status & Frontier — The Collatz Conjecture

_Where the problem stands and what a resolution would require._

**Status: OPEN.** No proof or disproof exists. The conjecture has been verified computationally for all $n \le 2^{68} \approx 2.95 \times 10^{20}$ (Bařina, 2020, continuing Oliveira e Silva's distributed project), and no counterexample — neither a divergent orbit nor a nontrivial cycle — has ever been found.

## What is known (unconditional)

- **Almost-all descent (density).** Terras (1976) and Everett (1977): natural density $1$ of integers have finite stopping time.
- **Counting bound.** Krasikov–Lagarias (2003): $\#\{n \le x : n \to 1\} \gg x^{0.84}$.
- **Tao's theorem (2019).** For any $f(n)\to\infty$, almost all $n$ (in logarithmic density) satisfy $\min_k T^k(n) < f(n)$ — "almost all orbits attain almost bounded values." This is the strongest known unconditional result and the current high-water mark. Reference: Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, arXiv:1909.03562 (2019).
- **Cycle constraints.** Nontrivial cycles, if any, must be enormously long (lower bounds in the hundreds of millions of terms, scaling with the verified range) and are excluded for small "cycle complexity" $m$ (Steiner 1977; Simons–de Weger 2005), via linear-forms-in-logarithms bounds on $|2^\ell - 3^k|$.

## What is known (conditional / heuristic)

The standard probabilistic model treats each odd step as multiplying by roughly $3/4$ on average (one $3n+1$ followed by an expected two halvings), giving multiplicative drift $\big(\tfrac{3}{4}\big)$ per cycle and hence almost-sure descent. This heuristic predicts that **(a)** no orbit diverges and **(b)** the only cycle is trivial — but it is a model, not a proof, and applies to typical rather than specific integers.

## What a full resolution would require

A complete proof must close two independent gaps simultaneously:

1. **No divergent orbit.** Upgrade Tao's *logarithmic-density, almost-bounded* statement to a *every-integer, genuinely-bounded* statement. This means controlling the thin exceptional set that all density methods discard — precisely where a divergent trajectory could hide.
2. **No nontrivial cycle.** Exclude cycles of *all* lengths, not just bounded complexity. Present methods (computation + transcendence bounds) only push the threshold; an infinite family needs a structural argument, plausibly a new Diophantine input controlling $2^\ell - 3^k$ uniformly.

A disproof would require exhibiting either a cycle or a provably divergent orbit — both ruled out below $2^{68}$, so any counterexample is astronomically large or structurally subtle.

## Plausible routes

- **Strengthening the entropy/additive-combinatorics method** behind Tao's theorem to reach full density and true boundedness.
- **A new conserved or monotone invariant** distinguishing integer orbits from measure-typical orbits — the missing structural object.
- **Sharper transcendence theory** on $\log_2 3$ to settle the cycle problem unconditionally.
- **Ergodic / $2$-adic rigidity** results that transfer measure-theoretic typicality to the (measure-zero) integers.

The sobering backdrop is the undecidability of *generalized* Collatz maps (Conway; Kurtz–Simon), which warns that any sufficiently general technique must fail — a proof must exploit the specific arithmetic of $3$ and $2$. Erdős's assessment, *"mathematics is not yet ready for such problems,"* remains the field's honest summary.

## Related problems

- [Goldbach Conjecture](../goldbach-conjecture/README.md) — another elementary-to-state, hard-to-prove additive question resistant to current methods.
- [Twin Prime Conjecture](../twin-prime-conjecture/README.md) — like Collatz, blocked by a "parity"-type barrier separating heuristic from proof.
- [Erdős–Straus Conjecture](../erdos-straus-conjecture/README.md) — a kindred simply-stated number-theoretic iteration/representation problem.
- [Lonely Runner Conjecture](../lonely-runner-conjecture/README.md) — another problem where dynamics and Diophantine approximation meet.
- [abc Conjecture](../abc-conjecture/README.md) — its strong Diophantine control over $a+b=c$ relations bears on cycle-exclusion-style bounds.
