# Status & Frontier — The Beck–Fiala Conjecture

_Where the problem stands and what a resolution would require._

**Overall status: `active-progress` (OPEN; even $o(t)$ independent of $n$ is open).**

## What is known

- **Best $n$-independent bound:** $\mathrm{disc}(\mathcal{F}) \le 2t - \log^* t$ (Bukh 2016, `10.1017/s0963548315000140`). Even $(2 - \varepsilon)t$ for fixed $\varepsilon > 0$ is open!
- **Best $n$-dependent bound:** $\mathrm{disc}(\mathcal{F}) = O(\sqrt{t \log n})$ (Banaszczyk 1998; constructively via Bansal–Dadush–Garg–Lovett 2018 `arXiv:1708.01079`).
- **Conjectured truth:** $\mathrm{disc}(\mathcal{F}) = O(\sqrt{t})$ (sharp up to constants via Hadamard / projective hypergraphs).
- **Formal tracking:** Formalized in Lean 4 in `google-deepmind/formal-conjectures` as `BeckFiala.beck_fiala_conjecture` (`kind: open`).

## What a resolution requires

Combining the dimension-independence of linear-algebraic rounding with the square-root cancellation of Gaussian/subgaussian balancing — either eliminating the $\sqrt{\log n}$ factor from Banaszczyk's theorem or breaking the $2t$ rounding barrier down to $O(\sqrt{t})$.

## Related problems

- [The Hadamard Matrix Conjecture](../hadamard-matrix-conjecture/README.md)
- [The Sunflower Conjecture](../sunflower-conjecture/README.md)
- [The Union-Closed Sets Conjecture (Frankl)](../union-closed-sets-conjecture/README.md)
