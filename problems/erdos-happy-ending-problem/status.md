# Status & Frontier — The Happy Ending Problem (Erdős–Szekeres Conjecture)

_Where the problem stands and what a resolution would require._

**Overall status: `active-progress` (OPEN; \$500 Erdős Prize unclaimed).**

## What is known

- **Exact values:** $\mathrm{ES}(3)=3$, $\mathrm{ES}(4)=5$, $\mathrm{ES}(5)=9$, $\mathrm{ES}(6)=17$ (Szekeres–Peters 2006). Even $\mathrm{ES}(7)$ (conjecturally $33$) is open.
- **Asymptotic bounds:** $2^{n-2} + 1 \le \mathrm{ES}(n) \le 2^{n + O(\sqrt{n \log n})}$ (Erdős–Szekeres 1961; Suk 2017 `10.1090/jams/869`; Holmsen–Mojarrad–Pach–Tardos 2020 `10.4171/jems/1000`).
- **Formal tracking:** Formalized in Lean 4 in `google-deepmind/formal-conjectures` as `Erdos107.erdos_107` (`kind: open`, prize `\$500`).

## What a resolution requires

Replacing the positive-fraction clustering step (which loses a sub-exponential $2^{O(\sqrt{n \log n})}$ factor) with a tight inductive or algebraic-topological invariant directly achieving $2^{n-2} + 1$ — or finding an unexpected counterexample at $n \ge 7$.

## Related problems

- [The Erdős Unit Distance Problem (Disproved 2026)](../unit-distance-problem/README.md)
- [The Hadwiger–Nelson Problem](../hadwiger-nelson-problem/README.md)
- [The Erdős–Hajnal Conjecture](../erdos-hajnal-conjecture/README.md)
