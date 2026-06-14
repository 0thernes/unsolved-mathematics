# Status & Frontier — The Baum–Connes Conjecture

_Where the problem stands and what a resolution would require._

**Status: active progress; open in general.** The plain (coefficient-free) Baum–Connes conjecture — that the assembly map $\mu\colon K^G_*(\underline{E}G)\to K_*(C^*_r(G))$ is an isomorphism — is **proven for a vast class of groups** and has **no known counterexample**, but it remains **unproven in full generality**. Its strong form **with coefficients is false** (Higson–Lafforgue–Skandalis, 2003), which is the key structural fact shaping all current work.

## What is known (unconditional)

- **a-T-menable / Haagerup groups** (Higson–Kasparov, 2001): the conjecture **with coefficients** holds for all groups acting properly isometrically on Hilbert space — amenable, free, one-relator, Coxeter, and many more.
- **Property (T) groups via Banach $KK$** (Lafforgue, 2002 onward): including cocompact lattices in $Sp(n,1)$ and rank-one groups.
- **All (Gromov-)hyperbolic groups and their lattices**, with coefficients (Lafforgue, 2012, via strong Property (T)).
- **Almost-connected groups** and reductive **$p$-adic** groups (Chabert–Echterhoff–Nest, 2003) — the Connes–Kasparov isomorphism.
- **Injectivity / strong Novikov** for every group that **coarsely embeds into Hilbert space** or has **finite asymptotic dimension / Property A** (Yu and successors) — an enormous class.
- Groups acting properly on **bolic spaces, CAT(0) spaces, trees, and buildings** (Kasparov–Skandalis, Tu).

## What is known (conditional / negative)

- The **conjecture with coefficients is false**: Gromov monster groups with embedded **expanders** break exactness of the reduced crossed product (HLS 2003; Skandalis–Tu–Yu). Thus any general proof must avoid the coefficient reduction.
- For groups **without** coarse Hilbert-space embedding (the monster groups), even injectivity of the *reduced* coarse assembly map is subtle — though a *maximal* version is often recoverable.

## What a full resolution requires

A proof of the general conjecture must produce, for an **arbitrary** second-countable locally compact group, either a surjectivity argument or an obstruction-killing element that works **without** the Haagerup property and **past strong Property (T)** — the regime of higher-rank lattices such as $SL_3(\mathbb{Z})$, $SL_n(\mathbb{Z})\,(n\ge3)$, and lattices in higher-rank simple $p$-adic groups. No current technique reaches surjectivity there. Equivalently, in the Meyer–Nest categorical picture, one must show the derived obstruction term vanishes for these groups.

## Plausible routes

1. **Extending strong Property (T) / Banach-$KK$ technology** (Lafforgue's program) to higher-rank lattices — the most direct attack, but the relevant Banach-space representation theory is hard.
2. **Higher-rank Mackey analogy / deformation** methods relating $SL_n(\mathbb{Z})$ to its motion-group degenerations.
3. **Categorical / homological** vanishing results (Meyer–Nest) isolating and killing the obstruction class.
4. **Coarse-geometric** advances handling expander-containing groups for the reduced theory.

A complete resolution would settle the **Novikov** and **Kadison–Kaplansky idempotent** conjectures for the groups in question and is regarded as one of the deepest open problems linking analysis, topology, and geometric group theory.

## Related problems

- [Novikov Conjecture](../novikov-conjecture/README.md)
- [Connes Embedding (aftermath)](../connes-embedding-aftermath/README.md)
- [Yang–Mills Mass Gap](../yang-mills-mass-gap/README.md)
- [Invariant Subspace Problem](../invariant-subspace-problem/README.md)
