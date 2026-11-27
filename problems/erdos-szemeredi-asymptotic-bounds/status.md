# Status & Frontier — Erdős Problem 142 (Asymptotic Density of $k$-AP-Free Sets)

_Where the problem stands and what a resolution would require._

**Overall status: `active-progress` (OPEN; \$10,000 Erdős Prize unclaimed).**

## What is known (through November 2026)

- **Case $k = 3$:** Behrend (1946; refined by Elkin 2010 / Green–Wolf 2010) gives $r_3(N) \ge N \exp(-c_1 \sqrt{\log N})$, while Kelley–Meka (2023, `arXiv:2302.05537`) and Bloom–Sisask (2023, `arXiv:2302.07211`) give $r_3(N) \le N \exp(-c_2 (\log N)^{1/9})$. Thus the shape $\exp(-(\log N)^{\alpha})$ is pinned down to $\alpha \in [1/9, 1/2]$, yet even the exact exponent $\alpha$ — let alone an asymptotic formula for $r_3(N)$ — remains wide open.
- **Case $k = 4$:** Green and Tao proved $r_4(N) \ll N / (\log N)^{c}$ (breaking Gowers's doubly logarithmic barrier for $k=4$), still exponentially far from Rankin's lower bound $N \exp(-c \sqrt{\log N})$.
- **General $k \ge 5$:** Leng, Sah, and Sawhney (2024, `arXiv:2402.17995`) proved $r_k(N) \le N \exp(-(\log\log N)^{c_k})$, the first major quantitative jump since Gowers (2001), yet still strictly weaker than $N / \log N$ (hence the $k \ge 4$ Erdős–Turán reciprocal-sum conjecture remains open).
- **Formal tracking:** Formalized in Lean 4 in `google-deepmind/formal-conjectures` as `Erdos142.erdos_142` (`kind: open`, prize `$10,000`).

## What a resolution requires

1. Determining the true exponent $\alpha_k$ in $r_k(N) = N \exp(-(\log N)^{\alpha_k + o(1)})$ (if that is indeed the asymptotic regime), or discovering substantially denser $k$-AP-free constructions beating Behrend–Rankin.
2. Lifting Kelley–Meka-style physical-space sifting to higher-order $U^{k-1}$ norms / nilmanifolds without losing an exponential in the inverse theorem.

## Related problems

- [The Sunflower Conjecture](../sunflower-conjecture/README.md)
- [The Erdős–Turán Conjecture on Additive Bases](../erdos-turan-additive-bases/README.md)
- [The Erdős–Turán Sidon Set Conjecture (Erdős Problem 30)](../erdos-sidon-sets-problem-30/README.md)
- [The Furstenberg ×2 ×3 Conjecture](../furstenberg-conjecture/README.md)
