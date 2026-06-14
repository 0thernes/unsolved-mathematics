# Status & Frontier — The Zariski Cancellation Problem

_Where the problem stands and what a resolution would require._

The problem is **partially resolved**, and the resolution is split sharply by characteristic. Metadata status: *active-progress*.

## What is known (unconditional)

- **$n=1$, any field.** Cancellation holds: $C\times\mathbb{A}^1\cong\mathbb{A}^2 \Rightarrow C\cong\mathbb{A}^1$ (Abhyankar–Eakin–Heinzer, 1972).
- **$n=2$, characteristic $0$.** Cancellation holds: $X\times\mathbb{A}^1\cong\mathbb{A}^3 \Rightarrow X\cong\mathbb{A}^2$ (Fujita 1979; Miyanishi–Sugie 1980), via the structure theory of affine surfaces and $\mathbb{A}^1$-fibrations. The $n=2$ positive-characteristic case is also resolved positively (Russell; Miyanishi–Sugie methods).
- **$n\ge 3$, characteristic $p>0$: FALSE.** This is the decisive modern result. **Neena Gupta** proved that Zariski cancellation *fails* for affine $n$-space in positive characteristic for all $n\ge 3$: there exist finitely generated $k$-algebras $A$ with $A^{[1]}\cong k^{[n+1]}$ but $A\not\cong k^{[n]}$. Key paper: N. Gupta, *On the cancellation problem for the affine space $\mathbb{A}^3$ in characteristic $p$*, **Inventiones Mathematicae** (2014), DOI `10.1007/s00222-013-0455-2`, arXiv:`1306.3043` (identifiers best-known, flagged for verification). The proof builds on Asanuma's deformation threefolds and a characteristic-$p$ Makar-Limanov-type invariant. Gupta received the 2014 Ramanujan Prize for this work.

## What is open (conditional / unresolved)

- **$n\ge 3$, characteristic $0$.** **Open.** The flagship live case is the threefold question: does $X\times\mathbb{A}^1\cong\mathbb{A}^4$ over a field of characteristic $0$ force $X\cong\mathbb{A}^3$? No proof and no counterexample is accepted. The Russell cubic and Koras–Russell threefolds show that contractible exotic threefolds exist, but none is known to be a cylinder base, so they do not (yet) refute cancellation.

## What a full resolution requires

A *positive* char-$0$ resolution would need an invariant that (a) is preserved under adding a polynomial variable, (b) is computable on candidate threefolds, and (c) distinguishes any non-$\mathbb{A}^3$ base from $\mathbb{A}^3$. The Makar-Limanov invariant satisfies (a)–(b) but is trivial on all known char-$0$ cylinder bases, so it cannot by itself close the problem. A *negative* char-$0$ resolution would require an explicit $X\not\cong\mathbb{A}^3$ with $X\times\mathbb{A}^1\cong\mathbb{A}^4$ — the obstruction is that Gupta's char-$p$ construction relies essentially on Frobenius/inseparability, which has no char-$0$ analogue.

## Plausible routes

1. **Refined $\mathbb{G}_a$-action invariants** beyond Makar-Limanov (e.g. Derksen invariant, or families of LNDs with controlled kernels) tailored to char-$0$ threefolds.
2. **$\mathbb{A}^1$-homotopy / motivic methods** (Dubouloz–Fasel and collaborators) probing whether $\mathbb{A}^1$-contractibility plus extra structure forces $\mathbb{A}^3$.
3. **New char-$0$ deformation families** analogous to Asanuma's, searched for genuine cancellation failures — so far none has materialized.

## Related problems

- [Jacobian Conjecture](../jacobian-conjecture/README.md)
- [Hodge Conjecture](../hodge-conjecture/README.md)
- [Tate Conjecture](../tate-conjecture/README.md)
- [Inverse Galois Problem](../inverse-galois-problem/README.md)
