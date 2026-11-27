# Approaches — The Beck–Fiala Conjecture

_Major strategies, partial results, and barriers._

1. **Iterated Linear-Algebra Rounding (Beck–Fiala 1981; Bukh 2016).** Start with fractional colors $x_v = 0$. Whenever fewer than $n$ sets have $> t$ unfixed elements, the underdetermined system $\sum_{v \in S} x_v = 0$ on "large" sets ($|S| > t$) admits a non-zero kernel vector; move to a vertex of $[-1, 1]^n$ fixing at least one coordinate to $\pm 1$. Once a set drops to $\le t$ active elements, drop it — its remaining error is at most $t$ (giving $< 2t$). Bukh (2016) improved $2t-1$ to $2t - \log^* t$ by tracking tiny rounding slack across levels.
2. **Convex Geometry & Gaussian Measure (Banaszczyk 1998).** Using the $K$-convexity / Gaussian-measure separation theorem on $\mathbb{R}^m$, Banaszczyk proved that for any symmetric convex body $K$ with $\gamma_m(K) \ge 1/2$ and vectors $\|v_i\|_2 \le 1/5$, there exist signs with $\sum \varepsilon_i v_i \in K$. Taking $K$ to be the $\ell_\infty$ cube of radius $C\sqrt{\log m}$ yields $O(\sqrt{t \log n})$ immediately.
3. **Subgaussian Random Walks & Semidefinite Relaxations (Bansal–Garg 2017; Bansal–Dadush–Garg–Lovett 2018).** Randomizing the kernel walk using the Gram–Schmidt Walk gives a distribution over $\pm 1$-colorings whose signed sum is $O(1)$-subgaussian in every direction, matching Banaszczyk's bound algorithmically and linking Komlós/Beck–Fiala to Nikolov's $\gamma_2$ factorization norm.

## Core Barrier
Notice the astonishing gap: **not even $1.99\,t$ (or $o(t)$) independent of $n$ is known!** Purely linear-algebraic rounding loses the full remaining size $t$ whenever a constraint is dropped; conversely, Gaussian/subgaussian methods must union-bound over $m$ coordinates, incurring an apparently unavoidable $\sqrt{\log m}$ factor unless one controls joint correlation across sets (as Spencer did when $m = n$ via partial coloring, which fails when $m \gg n$ or $t \ll n$).
