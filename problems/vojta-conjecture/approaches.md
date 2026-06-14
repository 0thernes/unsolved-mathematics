# Approaches — Vojta's Conjecture

_Major strategies, partial results, and barriers._

## The Subspace Theorem method (Schmidt–Schlickewei, Ru–Wong, Evertse–Ferretti)

The most productive unconditional route replaces Roth's theorem with **Schmidt's Subspace Theorem** and its quantitative and many-divisor extensions. The idea: for points approximating a divisor $D$ that is a sum of hyperplanes (or, more generally, components in general position) on $\mathbb{P}^n$, build auxiliary linear forms whose vanishing forces the approximating points into a finite union of proper subspaces — exactly the exceptional $Z$ predicted by Vojta. **Ru–Wong (1991)** proved the conjecture for hyperplanes in general position on $\mathbb{P}^n$; **Evertse–Ferretti** and **Ru** extended this to arbitrary effective divisors in general position via Mumford's degree/Chow-form arguments and to the "general position" Vojta inequality.
- **Best result:** the conjecture holds for $D=\sum D_i$ with the $D_i$ in general position on $\mathbb{P}^n$ (and on suitable varieties), with explicit dependence on the number of components.
- **Barrier:** the method intrinsically needs the divisor components to be in *general position* and supplies no information about the canonical term $h_{K_X}$ for varieties of general type. It does not reach Mordell-type curves or surfaces of general type. The exceptional set produced is a union of linear subspaces, not the genuine Zariski-closed $Z$ allowed by the conjecture.

## Ru–Vojta and the $\beta$-constant / Seshadri-positivity method

A 2020 synthesis by **Min Ru and Paul Vojta** packages the Subspace-Theorem method into a single "**General Theorem**" governed by a positivity invariant $\beta(L,D)$ (built from Seshadri constants and filtrations of sections), recovering and unifying earlier cases.
- **Best result:** the Vojta inequality for points/curves with respect to divisors satisfying an explicit $\beta$-condition, on varieties of arbitrary dimension, including many previously inaccessible configurations and the corresponding Nevanlinna Second Main Theorems.
- **Barrier:** the $\beta$-condition still encodes a general-position/positivity hypothesis on $D$; the canonical-class case of general-type varieties with no large boundary divisor lies outside its reach.

## Arakelov / arithmetic-geometry method (Vojta, Faltings, Bombieri)

Vojta's **1991 reproof of Mordell** used an explicit arithmetic intersection (Gillet–Soulé / Arakelov geometry) and an index/Roth-type argument on a product $C\times C$; **Faltings (1991, 1994)** simplified and vastly extended it to subvarieties of abelian and semiabelian varieties (the Mordell–Lang conjecture); **Bombieri (1990)** gave an elementary version for curves.
- **Best result:** the Mordell case and the Mordell–Lang / Faltings "Big Theorem" — finiteness of rational points on subvarieties of abelian varieties not containing a translated abelian subvariety. Vojta's **1996** integral-points theorem on semiabelian varieties is the strongest general evidence.
- **Barrier:** the arguments exploit the rich endomorphism/group structure of abelian and semiabelian varieties (Mumford gap, the $[n]$-multiplication trick). They do **not** generalize to arbitrary general-type varieties, where no such self-maps exist. This is the central obstruction: the full conjecture asks for an inequality with no group structure to lean on.

## Nevanlinna-theoretic transfer (the analytic mirror)

Because Vojta's conjecture is the exact arithmetic image of the Second Main Theorem, progress on the analytic side (holomorphic curves omitting divisors — work of **Bloch–Cartan, Ru, Yamanoi, Noguchi–Winkelmann, McQuillan**) is read as a heuristic and a target. **Yamanoi (2004)** proved the SMT-with-ramification (the "Griffiths conjecture" / defect relation) for curves, and **McQuillan's** tautological-inequality method proved the Green–Griffiths conjecture for surfaces of general type with positive Segre class.
- **Best result (analytic):** Second Main Theorems and degeneracy of entire curves into general-type surfaces under positivity hypotheses.
- **Barrier:** the dictionary is not a theorem — there is **no mechanism** transferring an analytic SMT to its arithmetic counterpart. The analytic side has the Ahlfors–Schwarz lemma / negative curvature and integration over $\mathbb{C}$; the arithmetic side has nothing analogous. McQuillan's "tautological inequality" has an arithmetic shadow (Vojta's tautological inequality on the arithmetic discriminant) but it is far weaker than the full conjecture.

## $abc$-driven and uniformity approaches

Since the conjecture implies $abc$ and the uniform Mordell/Bombieri–Lang statements, partial results on $abc$ (Stewart–Yu's exponential bounds via linear forms in logarithms) and uniform-bound theorems (Dimitrov–Gao–Habegger 2021, Kühne) on rational points illuminate what a proof must deliver.
- **Best result:** unconditional uniform bounds on $\#C(k)$ for genus $\ge 2$ curves (height-machine + Vojta-type inequalities on the geometry of the Faltings–Vojta divisor), and explicit but far-from-sharp $abc$ bounds.
- **Barrier:** every known partial result toward the height inequality is either restricted to special geometry (general position, group varieties) or is ineffective. No approach has produced an effective $abc$ with the correct shape, which the full conjecture would. A claimed proof of $abc$ by **Mochizuki (Inter-universal Teichmüller theory, 2012)** would imply the relevant case, but its central Corollary 3.12 is **disputed** by Scholze and Stix (2018) and the proof is not accepted by the broader community.
