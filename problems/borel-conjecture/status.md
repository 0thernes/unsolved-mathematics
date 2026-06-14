# Status & Frontier — The Borel Conjecture

_Where the problem stands and what a resolution would require._

**Status: active-progress — open in general.** The Borel Conjecture is proven for a vast and steadily growing class of fundamental groups, but **not for all** closed aspherical manifolds. It is one of the central open problems of geometric topology.

## What is known (unconditional)

For closed aspherical $M^n$ with $n\geq 5$ and $\pi_1(M)=\Gamma$, the conjecture **holds** whenever $\Gamma$ satisfies the **Farrell–Jones Conjecture** in $L$-theory (with $\mathrm{Wh}(\Gamma)=0$). This class now includes:

- **Word-hyperbolic groups** (Bartels–Lück–Reich) and **CAT(0) groups** (Bartels–Lück, with Wegner).
- **Lattices** in virtually connected Lie groups; $\mathrm{GL}_n(\mathbb Z)$, $\mathrm{SL}_n(\mathbb Z)$, arithmetic groups (Bartels–Lück–Reich–Rüping, Kammeyer–Lück–Rüping).
- **Crystallographic, flat, infranil, and nonpositively curved** manifolds (classical Farrell–Hsiang, Farrell–Jones).
- **Virtually solvable / poly-(cyclic-or-finite)** groups; groups acting suitably on CAT(0) or finite-dimensional spaces; and classes closed under the **inheritance properties** of FJC (subgroups, extensions, finite products, directed colimits, free and amalgamated products).

In **dimension 3** the conjecture is a theorem via Perelman's geometrization (with the Haken case due classically to Waldhausen). In **dimension 4** it holds for aspherical 4-manifolds with **good** (amenable/subexponential) $\pi_1$, by Freedman–Quinn topological surgery.

## What is known (conditional / structural)

The modern reduction is: **$L$-theoretic FJC for $\Gamma$ $\Rightarrow$ Borel for $M$** (dim $\geq 5$). So progress is now equivalent to *verifying FJC for more groups*. The smooth and PL analogues are **false** (Farrell–Jones counterexamples), so the target is strictly the homeomorphism category. The key reference establishing the modern hyperbolic/CAT(0) cases is Bartels–Lück, *The Borel Conjecture for hyperbolic and CAT(0)-groups*, **Annals of Mathematics 175 (2012)**, with the $K$/$L$ machinery from Bartels–Lück–Reich, *The K-theoretic Farrell–Jones conjecture for hyperbolic groups*, **Inventiones Mathematicae 172 (2008)**.

## What a full resolution requires

A complete proof must establish (the $L$-theoretic) **Farrell–Jones Conjecture for every group**, or otherwise prove structure-set triviality without a geometric model — together with resolving the **dimension-4** case, which is entangled with the open **disk-embedding / surgery** problem for general (non-good) 4-manifold groups. Equivalently: show the assembly map
$$ H_n^{\Gamma}\!\big(E_{\mathcal{VCyc}}\Gamma;\mathbf{L}^{\langle-\infty\rangle}\big)\to L_n^{\langle-\infty\rangle}(\mathbb Z\Gamma) $$
is an isomorphism for all $\Gamma=\pi_1$ of a closed aspherical manifold.

## Plausible routes

1. **Extend FJC** to the remaining hard classes — general **mapping class groups**, $\mathrm{Out}(F_n)$, and groups without nonpositive-curvature geometry — via new flow-space / transfer-reducibility methods (Bartels–Bestvina and successors).
2. **Geometrize the input**: find weaker-than-CAT(0) structures (e.g. injective/Helly metrics, hierarchically hyperbolic spaces) sufficient to run controlled-topology arguments.
3. **Resolve 4-dimensional surgery** (disk embedding for free/hyperbolic groups), unlocking Borel rigidity in dimension 4.

The frontier is conceptual: FJC may *fail* for some pathological group, in which case the conjecture itself could be false — though no counterexample is known, and the evidence overwhelmingly favors rigidity for "geometric" groups.

## Related problems

- [Novikov Conjecture](../novikov-conjecture/README.md) — the higher-signature / assembly-map cousin implied by, and strategically intertwined with, Borel.
- [Baum–Connes Conjecture](../baum-connes-conjecture/README.md) — the $C^*$-algebraic analogue of the assembly-map philosophy.
- [Smooth 4-Dimensional Poincaré Conjecture](../smooth-4d-poincare-conjecture/README.md) — the simply connected, smooth-category neighbor where 4D surgery also obstructs.
- [Whitehead Asphericity Conjecture](../whitehead-asphericity-conjecture/README.md) — another deep asphericity question for 2-complexes.
- [Eilenberg–Ganea Conjecture](../eilenberg-ganea-conjecture/README.md) — dimension theory of aspherical $K(\pi,1)$ complexes.
