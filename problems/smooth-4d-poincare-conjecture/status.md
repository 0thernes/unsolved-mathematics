# Status & Frontier — The Smooth 4-Dimensional Poincaré Conjecture

_Where the problem stands and what a resolution would require._

**Status: open.** SPC4 is the only unresolved case of the generalized Poincaré conjecture in any category and any dimension. There is no accepted proof in either direction, and — unusually — the expected truth value is itself contested among experts.

## What is known (unconditional)

- **Topological case settled.** Every topological 4-manifold homeomorphic to $S^4$ *is* $S^4$ (Freedman, 1982). So any exotic $S^4$ would be homeomorphic but not diffeomorphic to the standard one.
- **All other dimensions settled (smooth).** $n = 1,2$ classical; $n = 3$ Perelman; $n \geq 5$ Smale. Dimension four is the sole gap.
- **Gauge invariants vanish.** Donaldson and Seiberg–Witten invariants cannot distinguish a homotopy 4-sphere from $S^4$ (no $b_2$ to carry basic classes). The most powerful detection tools are structurally blind here — an unconditional negative result about method, not about the answer.
- **Leading candidates eliminated.** The prominent infinite families of Cappell–Shaneson spheres are diffeomorphic to $S^4$ (Akbulut 2009; Gompf 2010). Many Gluck twists are known standard. No specific homotopy 4-sphere is currently known to be exotic.

## What is known (conditional)

- **$s$-invariant reduction (Manolescu–Piccirillo, 2020/2021).** *If* there exists a knot $K$ that is topologically slice in a homotopy 4-ball with Rasmussen $s(K) \neq 0$, *then* an exotic 4-sphere (or exotic 4-ball) exists. This converts SPC4's falsity into a concrete, checkable knot-theoretic condition. Every candidate tested so far has $s = 0$; whether a qualifying knot exists is open, and there is partial evidence that $s$ alone may be insufficient.
- **Trisection / Powell reformulation.** A homotopy 4-sphere admits a genus-$g$ trisection; deciding standardness reduces to questions about the mapping class group of $\#^g(S^1\times S^2)$ and the Powell conjecture — themselves open and conjecturally as hard.

## What a full resolution requires

- **To prove SPC4 (no exotic $S^4$):** either a smooth 4-dimensional $h$-cobordism theorem (currently impossible — the smooth Whitney trick fails) or a new global argument showing every homotopy 4-sphere standardizes, e.g. via a controlled handle-cancellation theory or a 4-dimensional flow with adequate singularity control (no current Ricci-flow analogue exists).
- **To disprove SPC4 (build an exotic $S^4$):** an invariant nonvanishing at $b_2 = 0$ that separates a specific candidate from $S^4$ — the role hoped for the $s$-invariant or skein-lasagna modules — together with a candidate that the invariant actually detects.

## Plausible routes

1. **Khovanov-flavored invariants** ($s$-invariant, skein-lasagna modules of Morrison–Walker–Wedrich) detecting an exotic candidate — the most active current program.
2. **The Gluck-twist sub-problem**: proving all Gluck twists standard would remove a major candidate source; finding an exotic one would resolve SPC4 negatively.
3. **Trisection combinatorics** maturing into a decision procedure for standardness.
4. A genuinely new smooth invariant or PDE method bypassing the gauge-theory vanishing.

No route is close to completion; the consensus is that SPC4 will require a fundamentally new idea. Because the status is **open** (not resolved/disputed/independent), no resolution paper is cited as definitive; the key strategic reference is Manolescu–Piccirillo (2021, arXiv:2102.04391, *needs-verification on identifier*) and the program-defining Freedman–Gompf–Morrison–Walker (2010, arXiv:0906.5177).

## Related problems

- [Andrews–Curtis Conjecture](../andrews-curtis-conjecture/README.md) — directly entangled via balanced presentations arising from homotopy 4-spheres.
- [Slice–Ribbon Conjecture](../slice-ribbon-conjecture/README.md) — knot sliceness underlies the $s$-invariant route to exotic 4-spheres.
- [Borel Conjecture](../borel-conjecture/README.md) — sibling rigidity question in manifold topology where smooth vs. topological subtleties recur.
- [Zeeman Conjecture](../zeeman-conjecture/README.md) — low-dimensional collapsibility problem linked to Andrews–Curtis and 4-dimensional handle theory.
- [Volume Conjecture](../volume-conjecture/README.md) — adjacent quantum-topological program (Khovanov/skein invariants) feeding the same toolkit.
