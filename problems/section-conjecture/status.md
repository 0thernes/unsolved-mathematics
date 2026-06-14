# Status & Frontier — Grothendieck's Section Conjecture

_Where the problem stands and what a resolution would require._

**Status: open.** The Section Conjecture for smooth projective hyperbolic curves over number fields is unproven and unrefuted. There is no known counterexample and no accepted proof. It remains one of the central organizing problems of anabelian geometry.

**What is known (unconditional).**
- **Injectivity** of the map $X(k) \to \{\text{conjugacy classes of sections}\}$ holds for hyperbolic curves over number fields (and sub-$p$-adic fields), via the anabelian rigidity of Nakamura–Tamagawa–Mochizuki.
- The **isomorphism (anabelian) conjecture** — that $\pi_1^{\mathrm{ét}}$ with its Galois action determines the curve — is a theorem over sub-$p$-adic fields (Mochizuki, 1996). This is the "$\pi_1$ knows $X$" half; it does *not* yield the section conjecture.
- The **real section conjecture** (over $\mathbb{R}$) is fully proved (Mochizuki; Pál, 2011).
- The **birational $p$-adic section conjecture** is proved (Koenigsmann, 2005), with strong extensions over large/$p$-adically closed fields (Pop; Pop–Saïdi).
- Various **minimalist negative facts**: abelian and metabelian quotients are too coarse; $n$-nilpotent (Massey-product) obstructions can detect non-geometric sections in examples (Wickelgren).

**What is known (conditional).**
- Surjectivity (every section is geometric) over number fields is linked by Esnault–Wittenberg to **finiteness of $\Sha$** of the Jacobian and to cycle-theoretic/Tate-type conjectures; granting these yields partial geometricity in cases.
- There is **no Hasse principle for sections**: local geometricity at all places does not force a global point, and the gap is controlled by Tate–Shafarevich and Brauer–Manin/descent obstructions (Harari–Stix, Stix).

**What a full resolution requires.** One must prove **surjectivity** over number fields: produce, from an arbitrary conjugacy class of group-theoretic sections of $\pi_1^{\mathrm{ét}}(X)\twoheadrightarrow \mathrm{Gal}(\bar k/k)$, an actual rational point $x\in X(k)$ with $s\sim s_x$, and rule out exotic non-geometric sections. This demands a mechanism converting purely profinite-group-theoretic data into Diophantine information — exactly what no current method supplies at the global level.

**Plausible routes.**
1. **Local-to-global gluing** of the (still open) $p$-adic local section conjecture with control of the descent/Brauer–Manin obstruction.
2. **Birational descent**: leverage Koenigsmann–Pop birational results and push them from function fields down to curves over number fields — currently blocked by the lack of global rigidity.
3. **Obstruction-theoretic finiteness**: prove the relevant $\Sha$/cycle-class inputs in the Esnault–Wittenberg reduction.
4. **Homotopy-theoretic refinement**: use the étale homotopy type and $n$-nilpotent obstructions (Wickelgren) to characterize geometric sections, possibly in tandem with Lawrence–Venkatesh-style transcendence input.

No route is close to completion; tractability is correspondingly low. The honest expert consensus is that the conjecture is true but far beyond present techniques over number fields.

## Related problems

- [The abc Conjecture](../abc-conjecture/) — adjacent Diophantine target of the anabelian program; the IUT controversy bears on both.
- [The Tate Conjecture](../tate-conjecture/) — cycle-class finiteness of the type that enters Esnault–Wittenberg's conditional reductions.
- [The Birch and Swinnerton-Dyer Conjecture](../birch-swinnerton-dyer/) — finiteness of $\Sha$, a hypothesis linked to surjectivity of the section map.
- [The Inverse Galois Problem](../inverse-galois-problem/) — sibling question on realizing and splitting Galois groups, sharing profinite-group-theoretic technique.
- [The Fontaine–Mazur Conjecture](../fontaine-mazur-conjecture/) — Galois-representation-theoretic constraints in the same arithmetic-geometry orbit.
