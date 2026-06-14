# Status & Frontier — The Slice–Ribbon Conjecture

_Where the problem stands and what a resolution would require._

**Status: OPEN** (since 1962). No general proof and no counterexample. The conjecture is understood in the **smooth** category: *every smoothly slice knot is ribbon*. The topological analogue is effectively false in spirit (Freedman's theorem yields topologically slice, non-ribbon knots), so all serious work is smooth.

## What is known (unconditional)

- **Implication one way is trivial:** ribbon $\Rightarrow$ slice always.
- **Confirmed for large infinite families:**
  - **2-bridge (rational) knots** — Lisca (2007), *Lens spaces, rational balls and the ribbon conjecture* (arXiv:math/0701610, *needs-verification* on exact id), via Donaldson diagonalization plus Heegaard Floer $d$-invariants.
  - **Odd 3-stranded pretzel knots $P(p,q,r)$** — Greene–Jabuka (2011).
  - **Many Montesinos knots** — Lecuona (2012 onward), with explicit residual lists.
  - Additional families via lattice embeddings and correction terms (Aceto et al.; Owens; Manolescu–Owens $\delta$).
- **No counterexample survives:** every candidate built to break it (Whitehead doubles, cables, fibered constructions) has been shown either non-slice (by $\tau$, $s$, $\nu^+$, $d$-invariants) or in fact ribbon. Empirically, every knot anyone has *certified* smoothly slice is ribbon.

## What is known (conditional / structural)

- "Ribbon" $\equiv$ "the slice disk admits a Morse function with **no local maxima**." So the conjecture is equivalent to: *every slice disk can be isotoped to remove all maxima.*
- Sliceness obstructions live in gauge theory and Floer homology; **algebraic** (Levine) invariants are insufficient (Casson–Gordon, 1975, exhibit algebraically slice non-slice knots).

## What a full resolution requires

- **For a proof:** a method that, given *any* slice knot, produces a ribbon presentation (a no-maxima handle simplification) independent of the structure of the double branched cover. The current toolkit only works when $\Sigma_2(K)$ is a lens or small Seifert space bounding a definite plumbing — a genuinely restrictive hypothesis.
- **For a disproof:** a knot proved *smoothly slice* yet *provably non-ribbon*. The obstacle is a **double bind** — our only general sliceness certificates are essentially ribbon moves, and **no smooth invariant is known that distinguishes slice-but-non-ribbon from ribbon** (all concordance invariants vanish on slice knots).

## Plausible routes

1. **Extend lattice/$d$-invariant confirmations** to all Montesinos and arborescent knots, then to satellites — incremental but proven productive.
2. **Find a ribbon obstruction:** a new invariant of slice disks sensitive to the no-maxima property (perhaps from bordered/involutive Floer theory, or from the fundamental group / Casson–Gordon refinements of the disk complement). This is the conceptual breakthrough the problem awaits.
3. **Targeted counterexample search** among KnotInfo's slice knots and exotic constructions, using the trace-embedding circle of ideas (cf. Piccirillo, 2020, for sliceness detection — adjacent, not directly applicable).

The consensus is cautious: the conjecture is *probably true* given the weight of confirmed families and the absence of counterexamples, but a decisive idea — most likely a genuine smooth ribbon obstruction — is missing.

## Related problems

- [Smooth 4-Dimensional Poincaré Conjecture](../smooth-4d-poincare-conjecture/README.md)
- [The Volume Conjecture](../volume-conjecture/README.md)
- [The Andrews–Curtis Conjecture](../andrews-curtis-conjecture/README.md)
- [The Zeeman Conjecture](../zeeman-conjecture/README.md)
