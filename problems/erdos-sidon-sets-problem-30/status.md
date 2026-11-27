# Status & Frontier — The Erdős–Turán Sidon Set Conjecture (Erdős Problem 30)

_Where the problem stands and what a resolution would require._

**Overall status: `active-progress` (OPEN; \$1,000 Erdős Prize unclaimed).**

## What is known

- **Best upper bound:** $h(N) \le \sqrt{N} + 0.98183 N^{1/4} + O(1)$ (Carter–Hunter–O'Bryant, improving Balogh–Füredi–Roy 2021 `arXiv:2103.15850`, $0.998 N^{1/4}$).
- **Best lower bound:** $h(N) \ge \sqrt{N} - O(N^{0.2625})$ from Singer's construction combined with Baker–Harman–Pintz prime-gap bounds.
- **Open gap:** Proving $h(N) \le \sqrt{N} + o(N^{1/4})$ is already open, let alone $h(N) = \sqrt{N} + O_\varepsilon(N^\varepsilon)$ (Erdős's \$1,000 prize) or $O(1)$.
- **Formal tracking:** Formalized in Lean 4 in `google-deepmind/formal-conjectures` as `Erdos30.erdos_30` (`kind: open`, prize `\$1,000`).

## What a resolution requires

Breaking past the second-moment / autocorrelation linear-programming barrier at exponent $1/4$ — either via a structural stability theorem forcing near-maximal Sidon sets to embed cleanly in Singer/Bose–Chowla sets, or via higher-order additive-energy / incidence arguments.

## Related problems

- [The Erdős–Turán Conjecture on Additive Bases](../erdos-turan-additive-bases/README.md)
- [Erdős Problem 142 (Asymptotic Density of k-AP-Free Sets)](../erdos-szemeredi-asymptotic-bounds/README.md)
- [The Sunflower Conjecture](../sunflower-conjecture/README.md)
