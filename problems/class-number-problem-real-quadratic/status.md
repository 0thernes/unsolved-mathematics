# Status & Frontier — Gauss's Class Number Problem for Real Quadratic Fields

_Where the problem stands and what a resolution would require._

**Overall status: `open`.**

## What is known

- **Imaginary quadratic case ($d < 0$):** Completely solved (Heegner–Baker–Stark for $h=1$; Goldfeld–Gross–Zagier effectively for all $h$).
- **Real quadratic case ($d > 0$):** Completely **OPEN** — it is not known whether infinitely many real quadratic fields have $h(d) = 1$, or even $h(d) \le B$ for any fixed constant $B$.
- **Partial arithmetic statistics:** Genus theory forces $h(p)$ odd for primes $p \equiv 1 \pmod 4$, and Davenport–Heilbronn (1971) proves a positive proportion have $3 \nmid h(d)$.
- **Formal tracking:** Formalized in Lean 4 in `google-deepmind/formal-conjectures` as `ClassNumberProblem.class_number_problem` (`kind: open`).

## What a resolution requires

A way to decouple $h(D)$ from the fundamental regulator $\log \varepsilon_D$ in the Dirichlet class number formula — or to control the entire odd part of $\mathrm{Cl}(\mathbb{Q}(\sqrt{D}))$ across all primes simultaneously (which even full Cohen–Lenstra proof for all moments would illuminate, though individual $h(D)=1$ requires ruling out *all* primes at once).

## Related problems

- [The Cohen–Lenstra Heuristics](../cohen-lenstra-heuristics/README.md)
- [The Grand Riemann Hypothesis](../grand-riemann-hypothesis/README.md)
- [Greenberg's Conjecture](../greenberg-conjecture/README.md)
