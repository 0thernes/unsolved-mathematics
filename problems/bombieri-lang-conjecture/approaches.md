# Approaches — The Bombieri–Lang Conjecture

_Major strategies, partial results, and barriers._

## Diophantine approximation and the Vojta inequality

**Core idea.** The most influential framework recasts the conjecture as a statement about heights. Vojta's conjecture predicts, for a smooth projective $X/K$ with canonical divisor $K_X$ and an effective ample $A$, an inequality of the shape $h_{K_X}(P) \le \epsilon\, h_A(P) + d(P) + O(1)$ outside a proper closed subset, where $d(P)$ is a discriminant term. For $X$ of general type this forces the height to be bounded away from the ample height, confining all but finitely many points to the exceptional set — exactly Bombieri–Lang.

**Best result reached.** Vojta (1989, 1991) and, in a celebrated elementary reworking, Bombieri (1990) and Faltings used precisely this circle of ideas to *reprove* Mordell and then to prove the **Mordell–Lang conjecture** for subvarieties of abelian and semiabelian varieties (Faltings 1991, 1994; Vojta 1996, McQuillan 1995). This is the deepest unconditional evidence: the conjecture holds whenever $X$ embeds in (a subvariety of) a semiabelian variety.

**Barrier.** The method controls points using a global section of a carefully chosen line bundle on $X \times X$ (or higher products) and the Faltings–Vojta product theorem. It crucially exploits the *group structure*. For a general variety of general type there is no ambient group, no Néron–Tate height machinery, and no known substitute for the index estimates. Extracting an inequality for arbitrary general-type $X$ is open and is essentially equivalent to the conjecture itself.

## Kobayashi hyperbolicity and the function-field / Nevanlinna analogy

**Core idea.** Lang's program asserts that arithmetic non-density should mirror complex hyperbolicity: a general-type $X$ should contain no entire curves outside its special set. By the dictionary between Nevanlinna theory and Diophantine approximation, theorems about holomorphic maps $\mathbb{C} \to X$ guide and predict the arithmetic.

**Best result reached.** Substantial progress exists on the *complex-analytic* side. McQuillan (1998) proved the Green–Griffiths–Lang conjecture for surfaces of general type with positive Segre class $c_1^2 - c_2 > 0$ (and second Segre number condition), establishing degeneracy of entire curves. Demailly, Diverio–Merker–Rousseau, and Brotbek (2017, proving the Kobayashi hyperbolicity of generic high-degree hypersurfaces) pushed hyperbolicity far. The function-field analogue of Bombieri–Lang is known in significant generality (e.g. via Manin, Grauert, and later work).

**Barrier.** Complex hyperbolicity and non-density are theorems about $\mathbb{C}$, not number fields; the analogy is heuristic, not a proof. There is no implication "hyperbolic $\Rightarrow$ Mordellic" available — that implication is itself part of Lang's conjecture. Translating analytic degeneracy into arithmetic finiteness remains the missing bridge.

## $p$-adic period maps (Lawrence–Venkatesh)

**Core idea.** Lawrence and Venkatesh (2020) reproved Mordell by studying the variation of $p$-adic Galois representations (or Hodge structures) in a family over $X$: if the period map has large image, rational points must be sparse because $p$-adic points with the same monodromy cluster on subvarieties. The method is geometric and avoids the equidistribution input of Faltings's original proof.

**Best result reached.** Beyond curves, the technique gives non-density of integral/rational points for several higher-dimensional families — e.g. for the moduli of hypersurfaces and certain ramified covers, and (Lawrence–Sawin) the Shafarevich conjecture for hypersurfaces in abelian varieties. It produces genuinely new unconditional finiteness statements in dimension $> 1$.

**Barrier.** The method needs a family with a sufficiently non-degenerate period map (large monodromy / variation of Hodge structure) sitting over $X$. A general variety of general type carries no such family, so the approach proves special cases rather than the conjecture. Constructing the requisite geometry is itself a hard open problem.

## Positivity, the canonical bundle, and the special set

**Core idea.** Attack the *geometric* heart: prove that the special set $\mathrm{Sp}(X)$ is a proper closed subset and understand its structure, so that arithmetic statements need only be proved on the complement. This draws on the minimal model program, Iitaka fibrations, and the structure theory of varieties of general type.

**Best result reached.** Much is known about the special set in examples and for fibered varieties; Abramovich, and Campana's "orbifold" / "special variety" theory, refine the dichotomy between general-type and "special" behaviour. For abelian varieties the special set is fully understood (it is everything when there is positive-dimensional abelian subvariety structure), matching Faltings.

**Barrier.** No general unconditional control of $\mathrm{Sp}(X)$ for arbitrary $X$ exists, and even granting the geometry, no mechanism converts "outside the special set" into a finiteness theorem without Vojta-type input.

## Counting and density heuristics (Batyrev–Manin / negative evidence)

**Core idea.** Asymptotic-counting philosophy (Batyrev–Manin) predicts how many points of bounded height a variety carries; for general type the predicted exponent is so small as to be consistent with non-density.

**Status / cautionary results.** This is *evidence*, not proof, and it cuts both ways: there exist general-type surfaces with provably dense rational points after passing to a finite extension if and only if certain subvarieties exist — making clear that the conjecture cannot be strengthened to finiteness and that any approach must respect the role of the exceptional locus. Caporaso–Harris–Mazur (1997) further showed the conjecture has *surprising* uniform consequences, a warning that any proof technique must be powerful enough to yield uniformity.
