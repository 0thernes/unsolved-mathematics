# Status & Frontier — The Tate Conjecture

_Where the problem stands and what a resolution would require._

**Status: open.** The Tate conjecture is unproved in general. It is, however, one of the better-understood "algebraicity of cohomology" problems, with a substantial archipelago of resolved special cases and a precise conjectural web linking it to motives, the standard conjectures, and $L$-functions.

## What is known (unconditional)

- **Divisors on abelian varieties** ($T^1$) over finitely generated fields, with semisimplicity of the Galois representation — **Faltings (1983)**, extended to positive characteristic by **Zarhin**. This includes the **endomorphism case over finite fields**, Tate's own 1966 theorem.
- **$K3$ surfaces** over finitely generated fields of characteristic $\neq 2$ — **Charles, Maulik, Madapusi Pera (2012–2016)**, with **Kim–Madapusi Pera** addressing $p=2$ cases; via Kuga–Satake and Shimura-variety integral models.
- Many **specific varieties**: Fermat hypersurfaces, products of curves of low genus, certain abelian-type Shimura varieties, Hilbert and Picard modular surfaces, and varieties dominated by products of curves.
- Over **finite fields**, equivalences (Milne) making $T^i$ tractable as: numerical $=$ $\ell$-homological equivalence, plus the order-of-pole statement, plus semisimplicity.

## What is known conditionally

- Under **Grothendieck's standard conjectures**, semisimplicity and large portions of the Tate picture follow (and conversely Tate + semisimplicity over finite fields yields the Lefschetz standard conjecture).
- Under the **Mumford–Tate conjecture**, Hodge-theoretic information transfers to the $\ell$-adic side, aligning Hodge and Tate classes — but the Mumford–Tate conjecture is itself open in general.

## What a full resolution would require

A complete proof over number fields must (i) construct *actual algebraic cycles* realizing every Galois-invariant class — the genuinely hard, non-formal step, since no general cycle-construction machine exists; (ii) handle **higher codimension** beyond the $H^1$/divisor reach of the abelian-variety method; and (iii) most likely settle **semisimplicity of Frobenius** and integrate with the standard conjectures. The structural obstruction is that current tools (Kuga–Satake, Shimura varieties, Hecke correspondences) produce cycles only for cohomology of restricted "abelian/$K3$ type."

## Plausible routes

1. Extend Shimura-variety methods to broader **abelian-type** and orthogonal/unitary motives, capturing more weight-2 and special higher-weight classes.
2. Deeper **automorphic / Langlands** input: realize Tate classes as functorial transfers and produce the matching cycles (special-cycle / Kudla-program technology).
3. Advances on the **standard conjectures** in characteristic $p$, plus lifting techniques from $\bar{\mathbb F}_p$ to characteristic $0$.
4. Progress on the **Mumford–Tate conjecture** to bridge Hodge and Tate definitively.

The consensus is that the general case awaits a substantially new idea; no announced proof of the general conjecture has been accepted by the community.

## Related problems

- [Hodge Conjecture](../hodge-conjecture/README.md) — the complex-analytic analogue; the two form the central pair on algebraicity of cohomology classes.
- [Birch and Swinnerton-Dyer Conjecture](../birch-swinnerton-dyer/README.md) — shares the "$L$-function pole/zero order equals a cycle/rank" philosophy.
- [Riemann Hypothesis](../riemann-hypothesis/README.md) — its function-field analogue (Weil conjectures) underlies the Frobenius-weight input to Tate.
- [Novikov Conjecture](../novikov-conjecture/README.md) — a sibling among major rigidity/structure conjectures linking topology and arithmetic-flavored invariants.
