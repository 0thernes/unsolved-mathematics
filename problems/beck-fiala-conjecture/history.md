# History — The Beck–Fiala Conjecture

_Origin, formulation, and timeline._

In 1981, József Beck and Tibor Fiala proved a remarkably clean theorem in combinatorial discrepancy theory: if a set system $\mathcal{F}$ on a finite ground set $V$ has maximum element degree $t$ (each $v \in V$ belongs to at most $t$ sets in $\mathcal{F}$), then there exists a $\pm 1$-coloring $\chi: V \to \{-1, +1\}$ with discrepancy $\mathrm{disc}(\mathcal{F}) \le 2t - 1$ — completely independent of $|V| = n$ and $|\mathcal{F}| = m$! Their proof uses a sleek iterated linear-algebra rounding argument.

In the same paper, Beck and Fiala conjectured that the true dependence on $t$ is **square-root**: $\mathrm{disc}(\mathcal{F}) = O(\sqrt{t})$ (and Komlós formulated the even stronger vector-balancing generalization: for any unit Euclidean vectors $v_1, \dots, v_n \in \mathbb{R}^m$ with $\|v_i\|_2 \le 1$, there exist signs $\varepsilon_i \in \{-1, +1\}$ with $\|\sum \varepsilon_i v_i\|_\infty = O(1)$). Over 45 years later, **no bound of $o(t)$ independent of $n$ has ever been proved**! The best $n$-independent bound is still Boris Bukh's $2t - \log^* t$ (2016), while Wojciech Banaszczyk's famous convex-geometry theorem (1998) achieves $O(\sqrt{t \log n})$ — leaving a frustrating $\sqrt{\log n}$ factor separating us from the conjecture.

## Timeline

- **1981** — József Beck and Tibor Fiala prove $\mathrm{disc}(\mathcal{F}) \le 2t - 1$ and conjecture $O(\sqrt{t})$ (`10.1016/0166-218x(81)90022-6`).
- **1985** — Joel Spencer proves "six standard deviations suffice" ($\mathrm{disc}(\mathcal{F}) \le 6\sqrt{n}$ when $m = n$) via the entropy / partial-coloring method (`10.1090/s0002-9947-1985-0784009-0`).
- **1997** — Bednarchak–Helm and Helm improve the additive constant from $2t - 1$ to $2t - 3$ (for $t \ge 3$).
- **1998** — Wojciech Banaszczyk proves his landmark Gaussian-measure balancing theorem (`10.1002/(sici)1098-2418(199807)12:4<351::aid-rsa3>3.0.co;2-s`), implying $\mathrm{disc}(\mathcal{F}) \le O(\sqrt{t \log n})$ (and $O(\sqrt{\log n})$ for Komlós).
- **2013–2016** — Boris Bukh breaks the $2t - O(1)$ barrier with the first $n$-independent super-constant improvement: $\mathrm{disc}(\mathcal{F}) \le 2t - \log^* t$ (`arXiv:1306.6081`, `10.1017/s0963548315000140`).
- **2017–2018** — Nikhil Bansal, Daniel Dadush, Shashwat Garg, and Shachar Lovett invent the algorithmic **Gram–Schmidt Walk** (`10.1145/3055399.3055490`, `arXiv:1708.01079`), matching Banaszczyk's $O(\sqrt{t \log n})$ bound constructively via subgaussian random walks.
- **2019–2025** — Sharp progress on random/smoothed instances and $\ell_p$-norm Komlós variants (Bansal–Jiang–Meka; Dadush–Nikolov–Talwar–Tomczak-Jaegermann), while the worst-case $O(\sqrt{t})$ Beck–Fiala conjecture and even $1.99\,t$ remain open!
