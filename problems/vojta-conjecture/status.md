# Status & Frontier — Vojta's Conjecture

_Where the problem stands and what a resolution would require._

**Status: open.** No general form of the conjecture is proved, and there is no claimed proof of the full statement. What exists is a substantial body of theorems covering geometrically special cases, plus a disputed proof of a logical consequence ($abc$).

## What is known (unconditional)

- **Group-variety cases.** Faltings' theorem (Mordell, 1983) and Faltings' Mordell–Lang "Big Theorem" (1991/1994) prove the finiteness content of the conjecture for subvarieties of abelian varieties; Vojta (1994, 1996) extends this to semiabelian varieties and to integral points. These are the deepest unconditional facts in the conjecture's range.
- **General-position divisors.** Via Schmidt's Subspace Theorem, the height inequality is known for divisors in general position on $\mathbb{P}^n$ and on suitable varieties: Ru–Wong (1991), Evertse–Ferretti, Corvaja–Zannier, Levin, Autissier, and the unifying **Ru–Vojta General Theorem (2020)** with its $\beta$/Seshadri positivity invariant.
- **Function-field and analytic analogues.** The $abc$ inequality over function fields (Mason–Stothers) and many cases of the Nevanlinna Second Main Theorem (Yamanoi, McQuillan, Ru) hold — the analogues that motivate the conjecture but do not imply it.

## What is known (conditional)

- Vojta's conjecture **implies**: the $abc$ conjecture, the Mordell conjecture (reproved), the Bombieri–Lang conjecture (general-type varieties are not potentially dense), Siegel's theorem, and a qualitative Subspace Theorem. It is therefore a single statement subsuming much of Diophantine geometry. Conversely, uniform-bound results (Dimitrov–Gao–Habegger 2021) realize some quantitative consequences unconditionally for curves, narrowing the gap on the Mordell side.

## What a full resolution requires

A proof must control the **canonical-class term $h_{K_X}$** for an arbitrary variety of general type with **no boundary divisor and no group structure** — precisely the regime where every existing method fails. Equivalently, it must transfer the analytic Second Main Theorem (which uses the Ahlfors–Schwarz lemma and negative curvature, integrating over $\mathbb{C}$) to an arithmetic setting that has no analogue of curvature or integration. Producing the genuine Zariski-closed exceptional set $Z$ (not merely a union of linear subspaces) is part of the difficulty.

## Plausible routes

1. **Extend Ru–Vojta** by weakening the $\beta$/general-position hypothesis toward the pure canonical case — the most active near-term line.
2. **An arithmetic tautological inequality** strong enough to mirror McQuillan's surface result, sharpening Vojta's arithmetic-discriminant inequality.
3. **A new positivity principle** for $K_X$ on integral points without group structure — the genuinely missing idea; widely regarded as a generational problem. Tractability is rated very low.

Because the conjecture is open and there is no accepted resolution, no resolving citation is asserted here. The adjacent $abc$ proof by Mochizuki (IUT, *PRIMS* 2021) is **disputed**: Scholze–Stix ("Why abc is still a conjecture," 2018) identify a gap in Corollary 3.12; consensus has not formed, and $abc$ is treated as open.

## Related problems

- [abc Conjecture](../abc-conjecture/README.md)
- [Bombieri–Lang Conjecture](../bombieri-lang-conjecture/README.md)
- [Birch–Swinnerton-Dyer Conjecture](../birch-swinnerton-dyer/README.md)
- [Hall's Conjecture](../hall-conjecture/README.md)
- [Schinzel's Hypothesis H](../schinzel-hypothesis-h/README.md)
