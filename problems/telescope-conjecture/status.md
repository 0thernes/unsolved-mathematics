# Status & Frontier — The Telescope Conjecture (Disproved 2023)

_Where the problem stands and what a resolution would require._

**Status: recently resolved — DISPROVED (2023).** The telescope conjecture is **false** for every height $n \ge 2$ and every prime $p$. The comparison map $L_n^f X \to L_{K(n)} X$ is *not* an equivalence in general; telescopic localization retains strictly more information than $K(n)$-localization. The conjecture remains *true* only at the low heights where it was always known: $n = 0$ (rationalization) and $n = 1$.

## The resolving result

The disproof is due to **Robert Burklund, Jeremy Hahn, Ishan Levy, and Tomer Schlank**, "*$K$-theoretic Counterexamples to Ravenel's Telescope Conjecture*" (2023, arXiv:2310.17459). The argument is a synthesis of recent trace-methods technology:

- **Redshift / Lichtenbaum–Quillen** for truncated Brown–Peterson spectra $\mathrm{BP}\langle n\rangle$ (Hahn–Wilson, Hahn–Raksit–Wilson): algebraic $K$-theory raises chromatic height by one, in a *bounded* and computable way.
- **The chromatic Nullstellensatz** (Burklund–Schlank–Yuan, 2022, arXiv:2207.09929): control of maps from height-$n$ ring spectra into Lubin–Tate theories.
- **Cyclotomic trace and even/motivic filtrations** on $\mathrm{TC}$, used to compute the $v_{n+1}$-periodic homotopy of $K$-theory spectra precisely enough to detect a gap.

Concretely, they exhibit ring spectra whose telescopic (i.e. $T(n+1)$-local) algebraic $K$-theory is provably *larger* than its $K(n+1)$-localization, producing an unbounded discrepancy. Because $K$-theory ascends one height, a counterexample at height $n+1$ is manufactured from controlled height-$n$ input — which is why the failure was invisible to four decades of within-height computation.

## What is known — unconditional vs. conditional

**Unconditional:** (i) $T(n)$ and $K(n)$ are *not* Bousfield-equivalent for $n \ge 2$; (ii) $L_n^f \ne L_{K(n)}$ in general; (iii) the failure is qualitative, not a borderline case — the telescopic part is infinitely larger in a precise sense; (iv) heights 0 and 1 are unaffected.

**Conditional / in progress:** the *exact* structure of the telescopic-but-not-$K(n)$-local homotopy, the asymptotic growth rate of $v_n$-periodic homotopy of finite complexes, and the implications for the **chromatic splitting conjecture** (whose original form interacts with telescope phenomena) are open and depend on further $\mathrm{TC}$ computations.

## What a full understanding now requires

The yes/no question is settled, so "resolution" has shifted to *quantification*:

1. **Measure the gap.** Determine the size and growth of $\pi_* L_n^f S / \pi_* L_{K(n)} S$ across heights and primes.
2. **Structural model.** Give an algebraic or trace-theoretic description of the extra telescopic classes — they are not algebraic in the Morava-stabilizer sense, so a new model is needed.
3. **Reassess dependent conjectures.** Re-examine chromatic splitting, the telescopic analogues of the algebraicity conjectures, and the systematics of infinite families in the stable stems in light of the failure.

## Plausible routes forward

Continued **trace-methods** computation ($\mathrm{TC}$ via even/motivic filtrations), the **chromatic Nullstellensatz** extended to higher heights, and **redshift** refinements are the most promising tools — the same apparatus that produced the disproof now drives the quantitative program.

## Related problems

- [Hodge Conjecture](../hodge-conjecture/) — another deep structural conjecture resolved/unresolved by comparison maps between geometric and algebraic invariants.
- [Tate Conjecture](../tate-conjecture/) — algebraic-cycle analogue of comparing geometric and cohomological data, kin in spirit to chromatic comparison maps.
- [Novikov Conjecture](../novikov-conjecture/) — assembly/comparison-map question whose resolution likewise hinges on $K$-theoretic technology.
- [Baum–Connes Conjecture](../baum-connes-conjecture/) — another $K$-theory assembly-map conjecture, parallel methodology to trace-methods attacks.
