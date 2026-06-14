# Approaches — The Fontaine–Mazur Conjecture

_Major strategies, partial results, and barriers._

## Modularity lifting (Taylor–Wiles–Kisin patching)

**Core idea.** Fix a residual representation $\bar\rho: G_{\mathbb{Q}} \to \mathrm{GL}_n(\overline{\mathbb{F}_p})$. Mazur's deformation theory packages all geometric lifts of $\bar\rho$ of a fixed type into a universal deformation ring $R$; modular forms of the corresponding type are governed by a Hecke algebra $\mathbb{T}$. A natural surjection $R \twoheadrightarrow \mathbb{T}$ exists, and the strategy is to prove it is an isomorphism ("$R = \mathbb{T}$"), so that **every** geometric lift is automorphic. Wiles and Taylor–Wiles invented the patching argument; the Taylor–Wiles primes and a numerical criterion force $R$ to be as small as $\mathbb{T}$.

**Best result.** Combined with Kisin's local deformation-ring computations, this yields the full modularity of elliptic curves over $\mathbb{Q}$ (BCDT, 2001) and Kisin's near-complete proof of the $\mathrm{GL}_2/\mathbb{Q}$ Fontaine–Mazur conjecture (2009): an odd, irreducible, de-Rham-at-$p$, Hodge–Tate regular $\rho:G_{\mathbb{Q}}\to\mathrm{GL}_2(\overline{\mathbb{Q}_p})$ is modular, away from a few residual exceptions.

**Barrier.** The method requires a starting point of **residual modularity** (a known automorphic $\bar\rho$) — Serre's conjecture provides this for $\mathrm{GL}_2/\mathbb{Q}$ (Khare–Wintenberger) but has no analogue in higher rank. It also needs Hodge–Tate **regularity** (distinct weights) and self-duality or oddness; the Calegari–Geraghty obstruction (nonzero defect $\ell_0 > 0$) breaks naive patching for general fields and ranks.

## $p$-adic local Langlands

**Core idea.** Kisin and Emerton exploit the $p$-adic local Langlands correspondence for $\mathrm{GL}_2(\mathbb{Q}_p)$ (Breuil, Colmez) to convert the local de Rham condition at $p$ into automorphic data inside completed cohomology. The de Rham condition forces the matching Banach-space representation to contain locally algebraic vectors, which detect classical automorphic forms.

**Best result.** Emerton's local–global compatibility proves large parts of the two-dimensional conjecture over $\mathbb{Q}$ independently of patching, and clarifies the edge cases.

**Barrier.** A full $p$-adic local Langlands correspondence is known essentially only for $\mathrm{GL}_2(\mathbb{Q}_p)$. For $\mathrm{GL}_2(F)$ with $F\neq\mathbb{Q}_p$, or for $\mathrm{GL}_n$ with $n\ge 3$, no usable correspondence exists, blocking direct generalization.

## Potential automorphy and the "$p,q$ switch"

**Core idea.** When one cannot prove modularity directly, prove it after restricting to some (unknown) totally real or CM extension, using automorphy-lifting plus the existence of automorphic forms with prescribed residual representation (Moret-Bailly / Calabi–Yau families). Taylor's potential-automorphy theorems realize this.

**Best result.** The Sato–Tate conjecture (Clozel–Harris–Shepherd-Barron–Taylor; Barnet-Lamb–Geraghty–Harris–Taylor) and broad potential automorphy for regular self-dual representations of $G_F$, $F$ CM.

**Barrier.** "Potential" automorphy is weaker than the conjecture's assertion over the base field, and the technique is confined to **essentially self-dual** (polarizable) representations, where Galois representations are attached to cohomology of unitary/symplectic Shimura varieties. Non-self-dual cases (e.g. generic $\mathrm{GL}_3$) lie outside its reach.

## Derived/Galois deformations and completed cohomology

**Core idea.** Calegari–Geraghty extend patching to situations with cohomology in several degrees (defect $\ell_0>0$) by working with derived Hecke algebras and complexes; Scholze's perfectoid construction attaches Galois representations to torsion classes in the cohomology of locally symmetric spaces, opening non-self-dual cases in principle.

**Best result.** Conditional modularity-lifting theorems over imaginary quadratic fields and for $\mathrm{GL}_n$ assuming expected properties of Galois representations and local–global compatibility; unconditional results in low-defect cases.

**Barrier.** These results are largely **conditional** on conjectures about the existence and local properties of Galois representations in torsion cohomology, and on vanishing/Cohen–Macaulay hypotheses for the patched modules. The integral $p$-adic local Langlands input needed at $p$ is not available beyond $\mathrm{GL}_2(\mathbb{Q}_p)$.

## Negative / structural constraints

The conjecture also predicts **non-existence** results, which serve as consistency checks rather than attacks. A continuous irreducible $\rho:G_{\mathbb{Q}}\to\mathrm{GL}_2(\overline{\mathbb{Q}_p})$ with **finite image at $p$** of suitable type, or one that is **not** de Rham at $p$, must not arise from geometry. Examples include the prediction that representations unramified everywhere and with infinite image cannot be geometric — closely tied to the (open) statement that $G_{\mathbb{Q}}$ has no such representations, and to expected finiteness theorems. No counterexample is known, and partial results (e.g. ruling out everywhere-unramified two-dimensional representations under hypotheses) support the conjecture. There is no known obstruction suggesting the conjecture is false; the difficulty is uniformly one of construction, not of a barrier theorem against it.
