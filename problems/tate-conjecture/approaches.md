# Approaches — The Tate Conjecture

_Major strategies, partial results, and barriers._

## Tate modules and finiteness (the abelian-variety method)

The original and still most powerful line. Tate (1966) showed that for abelian varieties over a finite field, the isogeny class is recovered from the Galois action on the Tate module, deducing surjectivity of $\mathrm{Hom}(A,B)\otimes\mathbb{Z}_\ell \to \mathrm{Hom}_{G_k}(T_\ell A, T_\ell B)$ from a finiteness statement on $p$-divisible groups. **Faltings (1983)** transplanted the strategy to number fields and finitely generated fields, proving both the **semisimplicity** of the Galois representation and the **Tate conjecture for divisors on abelian varieties** — the deepest unconditional result in the area. **Best result:** the conjecture is fully known for divisors ($T^1$) on abelian varieties over all finitely generated fields, and for endomorphisms over finite fields (with Zarhin handling characteristic $p$). **Barrier:** the method controls $H^1$ and its tensor constructions but does not directly reach cycles of higher codimension on varieties that are not built from abelian varieties; "exotic" Hodge/Tate classes (e.g. Mumford's families) lie outside its reach.

## Kuga–Satake and Shimura-variety methods ($K3$ surfaces)

For $K3$ surfaces the transcendental lattice in $H^2$ can be embedded, via the **Kuga–Satake construction**, into the cohomology of an associated abelian variety, reducing $T^1$ for $K3$s to the abelian-variety case. Combined with the theory of integral canonical models of orthogonal Shimura varieties, this yielded a near-complete resolution: **Nygaard–Ogus (1985)** for ordinary $K3$s in $p\geq 5$; **Maulik**, **Charles**, and **Madapusi Pera (2012–2016)** for $K3$ surfaces over finitely generated fields of characteristic $\neq 2$; **Kim–Madapusi Pera** extending to $p=2$ in cases. **Best result:** Tate conjecture for $K3$ surfaces (and certain holomorphic-symplectic and abelian-type cases) over finitely generated fields, char $\neq 2$. **Barrier:** the construction is special to weight-2 Hodge structures of $K3$ type; it does not generalize to arbitrary surfaces of general type or higher-weight motives.

## Automorphic methods and the Langlands program

When a variety's cohomology is automorphic (Shimura varieties, certain modular varieties), Galois-invariant classes can sometimes be matched to automorphic forms whose $L$-functions have prescribed poles, and the cycles produced by Hecke correspondences or special subvarieties. This underlies results on products of curves, Hilbert and Picard modular surfaces, and the appearance of Tate classes as $\mathrm{GL}_n$-functorial transfers. **Best result:** the conjecture for many specific Shimura varieties and for self-products in low dimension; conditional results assuming standard conjectures. **Barrier:** functoriality and the construction of the relevant cycles are themselves open; one typically *assumes* Langlands-type inputs.

## Reduction to finite fields and lifting

A natural strategy is to prove the conjecture over $\bar{\mathbb{F}}_p$ (where the Frobenius eigenvalue picture is cleanest) and lift. Over finite fields the Tate conjecture is equivalent, by results of Tate and **Milne**, to the order of the pole of the zeta function equaling the rank of the cycle group, and is implied by the (also open) conjecture that **numerical and $\ell$-homological equivalence agree** plus semisimplicity. **Best result:** equivalences among Tate, the "strong" pole-order form, and Beilinson-type statements; verification for many specific varieties. **Barrier:** even over $\bar{\mathbb{F}}_p$ the general conjecture is open; lifting from char $p$ to char $0$ confronts the failure of de Rham/crystalline comparison to detect algebraicity.

## Motives and standard conjectures

Grothendieck's **standard conjectures** (Lefschetz type $B$, Hodge type) would imply semisimplicity of Frobenius and tie the Tate conjecture into a clean Tannakian theory of motives. Conversely, the Tate conjecture (plus semisimplicity) over finite fields implies Lefschetz-type standard conjectures there. **Best result:** rich web of equivalences (Tate $\Leftrightarrow$ standard conjectures + semisimplicity in many settings, due to Milne, André, others). **Barrier:** the standard conjectures are themselves unproved in characteristic $p$; only the Lefschetz standard conjecture in some cases (e.g. via hard Lefschetz from Deligne's Weil II) is unconditional.

## Negative and cautionary results

There is no known counterexample, and the conjecture is widely believed. The principal cautionary phenomenon is the existence of **non-algebraic absolute Hodge / "exotic" classes** in the analogous Hodge setting (Mumford–Tate groups smaller than expected), showing that naive "all invariant classes are obviously algebraic" reasoning fails; the **Mumford–Tate conjecture** (that the $\ell$-adic monodromy equals the Mumford–Tate group, conjecturally aligning the Hodge and Tate pictures) remains open and is a genuine obstruction to transferring Hodge-theoretic intuition. Deligne's theorem that **Hodge classes on abelian varieties are absolutely Hodge** is the closest positive transfer, but it does not establish algebraicity, only the compatibility needed to *relate* Hodge and Tate.
