# Attempts — Ryser's Conjecture (Hypergraph Covering)

_Notable attempts, near-misses, retracted proofs._

Unlike some celebrated conjectures, Ryser's Conjecture has **not** been the subject of widely publicized false proofs or retracted claims of full resolution. Its difficulty is so well understood that the literature consists of honest partial results, sharp characterizations of where naive strategies break, and constructions that refute the *strongest* auxiliary conjectures while leaving the main inequality intact. The notable episodes are below.

## The case $r = 3$: from Henderson to Aharoni

The first genuine result was **Henderson's 1971 thesis proof for $r = 3$**, established by direct combinatorial argument. It stood essentially alone for three decades. **Ron Aharoni's 2001 proof** re-derived $r = 3$ via topological connectivity of independence complexes (the Aharoni–Haxell machinery), turning an isolated result into the seed of a general method. Aharoni's argument is the canonical "near-miss" in the positive direction: it works perfectly at $r = 3$ and makes transparent *why* the same idea cannot reach $r = 4$ — the connectivity hypotheses it relies on genuinely fail there.

## The intersecting case and the collapse of uniqueness conjectures

For the intersecting case ($\nu = 1$, asserting $\tau \le r-1$), a tempting refinement was that **equality $\tau = r-1$ forces a truncated projective plane** of order $r-1$, making projective planes the *unique* extremal objects. **Abu-Khazneh, Barát, Pokrovskiy and Szabó (around 2014–2018)** disproved this: they constructed intersecting $r$-partite $r$-uniform hypergraphs with $\tau = r-1$ that are **not** derived from projective planes, including infinite families. This is a clean example of a plausible strengthening being refuted by explicit construction — a cautionary near-miss showing the extremal landscape is richer than the "projective planes only" intuition.

## Sub-$(r-1)$ bounds when projective planes are absent

A productive line attacks ranks where **no projective plane of order $r-1$ exists** (e.g. order $6$, ruled out by Bruck–Ryser–Chowla / Tarry's verification of Euler's $36$-officers problem). **Haxell and Scott**, and later **Bishnoi, Das, Morris and Pokrovskiy**, and **Francetić, Herke, McKay and Wanless**, proved strict improvements $\tau \le r-2$ (or stronger) for intersecting hypergraphs in such ranks. These are partial results, not full proofs: they confirm the conjecture comfortably in those ranks but rely essentially on the *nonexistence* of a design, so they say nothing about ranks where planes exist.

## Equality and stability for $r = 3$

**Haxell, Narins and Szabó (2009 onward)** gave a complete characterization of the extremal $3$-partite hypergraphs achieving $\tau = 2\nu$, a stability-type result. While not progress on $r \ge 4$, it represents the deepest structural understanding available for any rank and is the model for what a future general resolution might have to produce.

## Status of full attacks on $r = 4$

No correct proof of $r = 4$ (general $\nu$) exists, and no widely circulated incorrect one has gained traction either. **Haxell and Scott (2017)** obtained the strongest partial results, proving the conjecture for $r = 4$ and $r = 5$ in restricted forms (e.g. with improved constants, or under structural assumptions). The honest summary is that the conjecture is **wide open for all $r \ge 4$**, the intersecting case included, and that the field's caution about announcing proofs reflects how cleanly the known barriers are mapped.
