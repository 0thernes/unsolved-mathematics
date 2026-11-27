# Status & Frontier — The Cohen–Lenstra Heuristics

_Where the problem stands and what a resolution would require._

**Overall status: `active-progress` (OPEN for every odd prime $p \ge 3$ over $\mathbb{Q}$).**

## What is known

- **Over $\mathbb{Q}$, $p = 2$ (Gerth modification):** Proved in full by Alexander Smith (`10.1090/jams/1062`, building on Fouvry–Klüners 2007).
- **Over $\mathbb{Q}$, $p = 3$:** First moment proved (Davenport–Heilbronn 1971); all higher moments and the full 3-Sylow distribution remain **OPEN**.
- **Over $\mathbb{Q}$, odd $p \ge 5$:** Not even the first moment (average $|\mathrm{Cl}(K)[p]|$) is known!
- **Over $\mathbb{F}_q(t)$:** Large-$q$ limit proved for all odd $p$ (Ellenberg–Venkatesh–Westerland 2016 `10.4007/annals.2016.183.3.1`); fixed-$q$ remains active.
- **Formal tracking:** Formalized in Lean 4 in `google-deepmind/formal-conjectures` as `CohenLenstraHeuristics.cohen_lenstra_imaginary_quadratic_p_sylow_conjecture` and `cohen_lenstra_real_quadratic_p_sylow_conjecture` (`kind: open`).

## What a resolution requires

Computing all moments $\mathbb{E}[|\mathrm{Sur}(\mathrm{Cl}(K), G)|]$ for arbitrary odd finite abelian $p$-groups $G$ over $\mathbb{Q}$ (equivalently, counting unramified $G$-extensions of quadratic fields ordered by discriminant) — requiring entirely new tools beyond prehomogeneous vector spaces.

## Related problems

- [Gauss's Class Number Problem for Real Quadratic Fields](../class-number-problem-real-quadratic/README.md)
- [The Birch and Swinnerton-Dyer Conjecture](../birch-swinnerton-dyer/README.md)
- [Greenberg's Conjecture](../greenberg-conjecture/README.md)
