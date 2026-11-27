# Status & Frontier — The Erdős–Turán Conjecture on Additive Bases

_Where the problem stands and what a resolution would require._

**Overall status: `open` (\$500 Erdős Prize unclaimed).**

## What is known

- **Best unconditional lower bound:** For every asymptotic basis $A \subseteq \mathbb{N}$ of order 2, $\limsup_{n \to \infty} r_A(n) \ge 8$ (ordered representations; Borwein–Choi–Chu 2006, refining Grekos–Haddad–Helou–Pihko 2003). No proof even reaches $\limsup r_A(n) \ge 100$, let alone $\infty$.
- **Sharpness of slow growth:** Erdős (1956) proved bases exist with $r_A(n) = \Theta(\log n)$, so any proof cannot hope for polynomial growth in $\limsup r_A(n)$.
- **Essential role of $\mathbb{N}$:** False over $\mathbb{Z}$ (Nathanson 2003) and true for multiplicative bases of $\mathbb{N}$ (Erdős 1964).
- **Formal tracking:** Formalized in Lean 4 in `google-deepmind/formal-conjectures` as `Erdos28.erdos_28` (`kind: open`, prize `\$500`).

## What a resolution requires

A genuinely new analytic or additive-combinatorial principle sensitive to the **non-negativity** of elements in $\mathbb{N}$ (i.e., Hardy-space / Toeplitz positivity of $f(z) = \sum_{a \in A} z^a$ on $|z| < 1$) that goes strictly beyond second-moment / Parseval bounds on $f(z)^2$.

## Related problems

- [The Erdős–Turán Sidon Set Conjecture (Erdős Problem 30)](../erdos-sidon-sets-problem-30/README.md)
- [Erdős Problem 142 (Asymptotic Density of k-AP-Free Sets)](../erdos-szemeredi-asymptotic-bounds/README.md)
- [Goldbach's Conjecture](../goldbach-conjecture/README.md)
