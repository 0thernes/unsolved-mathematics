# Status & Frontier — The Inverse Galois Problem

_Where the problem stands and what a resolution would require._

**Status: open (active progress).** The Inverse Galois Problem over $\mathbb{Q}$—is every finite group $G$ a Galois group $\mathrm{Gal}(L/\mathbb{Q})$?—remains unsolved. There is no claimed proof of the full statement under serious consideration; the field advances by realizing ever-larger families of groups, not by contesting a putative resolution.

## What is known (unconditional)

- **Abelian groups:** all are realizable—classical, via the Kronecker–Weber theorem and cyclotomic fields.
- **Solvable groups:** *all* finite solvable groups occur over $\mathbb{Q}$. This is **Shafarevich's theorem (1954)**, with the $2$-adic gap in the original argument now repaired (see Neukirch–Schmidt–Wingberg, *Cohomology of Number Fields*).
- **Symmetric and alternating groups:** $S_n$ and $A_n$ for all $n$—Hilbert (1892).
- **Most simple groups:** the bulk of finite simple groups, including many groups of Lie type and $25$ of the $26$ sporadic groups, are realized via the **rigidity method**. Thompson's realization of the **Monster** (1984) is the showpiece.
- **The salient gap:** the Mathieu group $M_{23}$ is the standard cited example of a finite simple group **not yet known** to be a Galois group over $\mathbb{Q}$; numerous other non-solvable groups also remain open.

## Strongest current results (conditional / over other fields)

- Over any **ample (large) field**—e.g., $\mathbb{Q}_p$, $\mathbb{C}((t))$, PAC fields—and over function fields such as $k(t)$, *every* finite group is regularly realizable, by the **patching** methods of Harbater, Pop, Haran–Völklein. The obstruction to importing this to $\mathbb{Q}$ is precisely that $\mathbb{Q}$ is not ample.
- A positive answer to the **regular IGP** over $\mathbb{Q}$ would imply the arithmetic IGP via Hilbert irreducibility; RIGP is itself open and is the form most experts target.
- Counting refinements: the **Malle conjecture** predicts the asymptotic number of $G$-extensions of $\mathbb{Q}$ by discriminant, a conditional sharpening that, if proven, would entail realizability for the groups it covers.

## What a full resolution would require

A complete solution must realize *every* finite group, including those with no rigid rational tuple. By the classification of finite simple groups and standard extension/embedding arguments, it would essentially suffice to (i) realize all finite simple groups over $\mathbb{Q}$ and (ii) solve the resulting non-abelian embedding problems to assemble general $G$ from its composition factors. Step (ii) is well-developed in the solvable case; step (i) is where rigidity runs out. A genuinely new mechanism—beyond rigidity, Hurwitz-space rational points, and patching—appears necessary to handle the remaining simple groups uniformly.

## Plausible routes

- **Beyond-rigidity Hurwitz-space arithmetic:** prove existence of $\mathbb{Q}$-rational points on positive-genus Hurwitz components, controlling the $\mathrm{Gal}(\bar{\mathbb{Q}}/\mathbb{Q})$-action on braid orbits.
- **Descending patching to $\mathbb{Q}$:** find an arithmetic substitute for ampleness, transferring function-field realizations to the rationals.
- **Embedding-problem theory for non-solvable kernels:** general solvability criteria that would let known simple-group realizations be amplified to all finite groups.

## Related problems

- [Schinzel's Hypothesis H](../schinzel-hypothesis-h/README.md)
- [Riemann Hypothesis](../riemann-hypothesis/README.md)
- [The abc Conjecture](../abc-conjecture/README.md)
- [Tate Conjecture](../tate-conjecture/README.md)
- [Hodge Conjecture](../hodge-conjecture/README.md)
