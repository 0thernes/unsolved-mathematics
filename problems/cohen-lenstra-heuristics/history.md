# History — The Cohen–Lenstra Heuristics

_Origin, formulation, and timeline._

In 1984, Henri Cohen and Hendrik W. Lenstra Jr. proposed a breathtakingly simple probabilistic law governing the distribution of ideal class groups of quadratic number fields: in the absence of special algebraic structure (such as genus theory at the prime $p = 2$), a finite abelian $p$-group $G$ ($p$ odd) should appear as the $p$-Sylow subgroup of $\mathrm{Cl}(K)$ with probability proportional to $1/|\mathrm{Aut}(G)|$ for imaginary quadratic fields ($u = 0$), and proportional to $1/(|G|\cdot |\mathrm{Aut}(G)|)$ for real quadratic fields ($u = 1$, accounting for the rank-1 unit group).

This single heuristic immediately predicts dozens of striking numerical constants — e.g., that $h(p) = 1$ holds for $\prod_{k \ge 2} (1 - p^{-k}) \approx 75.446\%$ of prime-discriminant real quadratic fields, that the average size of $\mathrm{Cl}(K)[p]$ is $2$ (imaginary) or $1 + p^{-1}$ (real), and that non-cyclic $p$-parts are extraordinarily rare. Extended to higher-degree fields by Cohen–Martinet (1990) and Malle, the Cohen–Lenstra heuristics now anchor the entire field of **arithmetic statistics**. Yet over $\mathbb{Q}$, only the $p = 3$ first moment (Davenport–Heilbronn 1971) and the 2-part (Fouvry–Klüners 2007; Alexander Smith 2022/2025) have been proved!

## Timeline

- **1971** — Davenport and Heilbronn compute the average number of 3-torsion elements in quadratic class groups (`10.1098/rspa.1971.0075`), providing the sole odd-prime moment confirmed over $\mathbb{Q}$ to this day!
- **1984** — Henri Cohen and Hendrik Lenstra formulate the general $1/|\mathrm{Aut}(G)|$ and $1/(|G||\mathrm{Aut}(G)|)$ heuristics (`10.1007/bfb0099440`).
- **1990** — Henri Cohen and Jacques Martinet generalize the heuristics to arbitrary number field extensions (`10.1515/crll.1990.404.39`).
- **2005–2010** — Manjul Bhargava proves density theorems for quartic and quintic fields (`10.4007/annals.2005.162.1031`, `10.4007/annals.2010.172.1559`), proving the 2-torsion average for cubic fields (Bhargava–Varma).
- **2007** — Étienne Fouvry and Jürgen Klüners prove the Gerth-modified Cohen–Lenstra distribution for the 4-rank of quadratic class groups.
- **2016** — Jordan Ellenberg, Akshay Venkatesh, and Craig Westerland prove the **function-field analogue** of Cohen–Lenstra over $\mathbb{F}_q(t)$ in the large-$q$ limit via homological stability of Hurwitz spaces (`10.4007/annals.2016.183.3.1`).
- **2022–2025** — Alexander Smith proves the full $2^\infty$-part (Gerth–Cohen–Lenstra) distribution for imaginary quadratic class groups and $\ell^\infty$-Selmer groups in twist families (`10.1090/jams/1062`, *JAMS* 2025).
