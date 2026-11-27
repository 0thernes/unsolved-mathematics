# Status & Frontier — Cramér's Conjecture on Prime Gaps

_Where the problem stands and what a resolution would require._

**Overall status: `open`.**

## What is known

- **Best unconditional upper bound:** $p_{n+1} - p_n \ll p_n^{0.525}$ (Baker–Harman–Pintz 2001).
- **Best conditional upper bound (under RH):** $p_{n+1} - p_n \ll \sqrt{p_n} \log p_n$ (Cramér 1936) — still exponentially far from $(\log p_n)^2$!
- **Best lower bound for infinitely many gaps:** $g_n \gg \frac{\log p_n \log\log p_n \log\log\log\log p_n}{\log\log\log p_n}$ (Ford–Green–Konyagin–Maynard–Tao 2016/2018, `10.1090/jams/876`).
- **Constant controversy:** Numerical searches up to $4 \times 10^{18}$ stay below $0.921 (\log p_n)^2$, yet Granville (1995) provides strong analytic evidence that the true $\limsup$ exceeds $2 e^{-\gamma} \approx 1.1229$.
- **Formal tracking:** Formalized in Lean 4 in `google-deepmind/formal-conjectures` as `CramerConjecture.cramer_conjecture` (`kind: open`).

## What a resolution requires

Even proving $p_{n+1} - p_n \ll p_n^{1/2 - \varepsilon}$ unconditionally would surpass the power of the Riemann Hypothesis; reaching $O((\log p_n)^2)$ requires completely new machinery controlling local zero-spacing conspiracies or direct sieve lower bounds in logarithmic-scale intervals.

## Related problems

- [Legendre's Conjecture](../legendre-conjecture/README.md)
- [The Riemann Hypothesis](../riemann-hypothesis/README.md)
- [Montgomery's Pair Correlation Conjecture](../montgomery-pair-correlation/README.md)
- [The Twin Prime Conjecture](../twin-prime-conjecture/README.md)
