# Status & Frontier — The Bombieri–Lang Conjecture

_Where the problem stands and what a resolution would require._

**Status: open** in every dimension $\ge 2$. No variety of general type is known unconditionally to have non-Zariski-dense rational points *solely* by virtue of being of general type. The dimension-1 case (Mordell) is a theorem (Faltings, 1983), and a substantial sub-case in all dimensions — subvarieties of semiabelian varieties — is also a theorem (Faltings 1991, 1994; with Vojta and McQuillan giving independent proofs). Beyond these regimes the conjecture is unproven.

## What is known

**Unconditional.**
- **Curves:** Mordell's conjecture holds — finiteness of $X(K)$ for $g \ge 2$ (Faltings 1983; reproved by Vojta 1989, Bombieri 1990, and Lawrence–Venkatesh 2020).
- **Subvarieties of (semi)abelian varieties:** the Mordell–Lang conjecture is proved; rational points are confined to translates of subgroups (Faltings, Vojta, McQuillan). This is the largest fully settled higher-dimensional family.
- **Large-monodromy families:** the Lawrence–Venkatesh period method yields non-density / Shafarevich-type finiteness for certain higher-dimensional varieties carrying a sufficiently non-degenerate variation of Hodge structure (e.g. Lawrence–Sawin, 2020).
- **Complex-analytic analogue:** strong hyperbolicity and degeneracy results (McQuillan's Green–Griffiths–Lang for general-type surfaces with $c_1^2 > c_2$; Brotbek's hyperbolicity of generic high-degree hypersurfaces) confirm the *geometric* side of Lang's web, though these do not transfer to number fields.

**Conditional.**
- Assuming a **uniform** Bombieri–Lang, Caporaso–Harris–Mazur (1997) deduce a genus-only bound on the number of rational points on curves over a fixed number field — and various further uniformity statements follow.
- The full conjecture follows from **Vojta's conjecture**, which is therefore the principal target of choice.

## What a full resolution requires

A proof of the general case must produce, for an arbitrary smooth projective $X/K$ of general type, a mechanism forcing $X(K)$ into a proper closed subset *without* an ambient group structure. Concretely it would need either: (i) a Vojta-type height inequality valid on general $X$ (currently out of reach, and essentially equivalent to the conjecture); (ii) a transfer principle converting complex hyperbolicity into arithmetic non-density (the "$\text{hyperbolic} \Rightarrow \text{Mordellic}$" implication, itself conjectural); or (iii) a vast generalization of the period-map method covering varieties with no natural family of motives. Each route currently terminates at a hard, well-identified obstruction.

## Plausible routes

1. **Vojta's inequality** for general-type varieties — the consensus "right" approach, but no partial inequality for arbitrary $X$ is known.
2. **Period maps / $p$-adic Hodge theory** (Lawrence–Venkatesh and successors) — the most active unconditional front, steadily enlarging the list of settled families.
3. **Hyperbolicity transfer** via the Green–Griffiths–Lang conjecture and Campana's orbifold theory — strong on the analytic side, awaiting an arithmetic bridge.

The community's working belief is that Bombieri–Lang is true and that it will fall, if at all, as a corollary of Vojta's conjecture or of a dramatic extension of period-theoretic methods — not by an isolated elementary argument.

## Related problems

- [Vojta's Conjecture](../vojta-conjecture/README.md) — the master height inequality implying Bombieri–Lang.
- [Mordell Conjecture / abc Conjecture](../abc-conjecture/README.md) — closely linked Diophantine finiteness, with effective ramifications.
- [Tate Conjecture](../tate-conjecture/README.md) — sibling arithmetic-geometry conjecture on algebraic cycles and Galois representations.
- [Hodge Conjecture](../hodge-conjecture/README.md) — period-map and Hodge-theoretic methods overlap with the period approach here.
- [Birch–Swinnerton-Dyer Conjecture](../birch-swinnerton-dyer/README.md) — companion conjecture on rational points, in the abelian-variety setting.
