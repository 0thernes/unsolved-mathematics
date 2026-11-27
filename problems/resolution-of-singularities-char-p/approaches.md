# Approaches — Resolution of Singularities in Positive Characteristic

_Major strategies, partial results, and barriers._

1. **Maximal Contact & Inductive Dimension Reduction (Hironaka; Villamayor; Bierstone–Milman; Włodarczyk).** In char 0, a smooth hypersurface of maximal contact (obtained via partial derivatives $\partial / \partial x_i$) contains all singular centers and permits clean induction on dimension. In char $p > 0$, taking $p$-th derivatives annihilates $x^p$, destroying smooth hypersurfaces of maximal contact (explicit counterexamples by Narasimhan 1983 and Hauser).
2. **Valuation-Theoretic Local Uniformization (Zariski; Cossart–Piltant; Knaf–Kuhlmann; Temkin).** Resolving singularities locally along every valuation ring and patching finite local resolutions globally succeeded for threefolds ($d = 3$) via Cossart–Piltant's detailed analysis of Artin–Schreier hypersurfaces and Newton polyhedra, yet the complexity of wild ramification explodes in dimension $4$.
3. **Alterations & Quotient Singularities (de Jong 1996; Gabber).** De Jong proved smooth alterations exist in all dimensions, and Gabber improved the degree to be prime to any chosen prime $\ell \ne p$. Turning a degree-$p^m$ inseparable/wildly ramified alteration into a degree-1 birational morphism remains the central obstacle.
4. **Weighted Blowings Up & Stack-Theoretic Resolution (Abramovich–Temkin–Włodarczyk 2024).** Replacing classical smooth centers by weighted blowings up yields single-step invariant drops in characteristic zero without memory/history data; extending these stacky invariants past wild $p$-ramification is an active frontier.

## Core Barrier
In positive characteristic $p > 0$, differential operators vanish on $p$-th powers, causing **failure of maximal contact**, **wildly ramified finite projections** (Artin–Schreier towers where invariants can *increase* after blow-up, the "kangaroo" phenomenon of Hauser), and breakdown of Hironaka's characteristic-zero induction.
