# History — Gauss's Class Number Problem for Real Quadratic Fields

_Origin, formulation, and timeline._

In Article 304 of his *Disquisitiones Arithmeticae* (1801), Carl Friedrich Gauss formulated the two foundational class number problems for binary quadratic forms (in modern terms, quadratic number fields $\mathbb{Q}(\sqrt{d})$):
1. **Imaginary quadratic fields ($d < 0$):** Gauss conjectured that $h(d) \to \infty$ as $d \to -\infty$, and in particular only finitely many have $h(d) = 1$. This imaginary case was completely resolved over the twentieth century: Heilbronn (1934) proved $h(d) \to \infty$; Heegner (1952), Baker (1966), and Stark (1967) proved that **exactly nine** imaginary quadratic fields have $h(d) = 1$ ($d \in \{-1,-2,-3,-7,-11,-19,-43,-67,-163\}$); and Goldfeld (1976) + Gross–Zagier (1986) gave an effective lower bound solving the general imaginary class-number-$k$ problem.
2. **Real quadratic fields ($d > 0$):** Gauss observed empirically that class number $1$ appears to occur **infinitely often** for positive discriminants — roughly 75.4% of prime discriminants $p \equiv 1 \pmod 4$ appear to have $h(p) = 1$ (later quantitatively explained by the Cohen–Lenstra heuristics, 1984). Yet after **225 years**, it is not even known whether there are infinitely many number fields *of any degree* with class number 1, let alone infinitely many real quadratic fields!

## Timeline

- **1801** — Gauss poses the class number problems for both negative and positive discriminants in *Disquisitiones Arithmeticae* (Articles 303–304).
- **1839** — Dirichlet proves the analytic class number formula $h(D) \log \varepsilon_D = \sqrt{D} L(1, \chi_D)$ for real quadratic fields, exposing the fundamental coupling between $h(D)$ and the regulator $\log \varepsilon_D$.
- **1935** — Carl Ludwig Siegel proves $h(D) \log \varepsilon_D = D^{1/2 + o(1)}$ (ineffectively), pinning down the product $h(D) R_D$ without separating $h(D)$ from the regulator $R_D = \log \varepsilon_D$.
- **1952–1967** — Heegner (1952), Baker (1966), and Stark (1967) completely settle the *imaginary* class number 1 problem (exactly 9 fields).
- **1976–1986** — Goldfeld (1976, 1985) and Gross–Zagier (1986) resolve the effective imaginary class number problem for arbitrary $h$.
- **1984** — Henri Cohen and Hendrik Lenstra formulate quantitative heuristics predicting that $\approx 75.446\%$ of real quadratic fields of prime discriminant have $h(p) = 1$ (and infinitely many for every $h$).
- **2004–2025** — Extensive computations verify the Cohen–Lenstra frequencies up to $D \sim 10^{11}$+, while the infinitude of real quadratic fields with $h(D) = 1$ remains completely open.
