# History — The Happy Ending Problem (Erdős–Szekeres Conjecture)

_Origin, formulation, and timeline._

In 1933 in Budapest, Esther Klein observed that any 5 points in the plane in general position (no three collinear) contain 4 points forming a convex quadrilateral, and asked whether for every $n \ge 3$ there exists a finite threshold $\mathrm{ES}(n)$ guaranteeing a convex $n$-gon. Paul Erdős and George Szekeres proved the existence of $\mathrm{ES}(n)$ in their classic 1935 paper — independently rediscovering Ramsey's theorem and proving the monotone-subsequence theorem along the way — and conjectured the exact formula $\mathrm{ES}(n) = 2^{n-2} + 1$.

Erdős nicknamed it the **Happy Ending Problem** because collaboration on it led to the marriage of Esther Klein and George Szekeres (who were married for 68 years). Erdős offered a **\$500** prize (**Erdős Problem #107**) for proving $\mathrm{ES}(n) = 2^{n-2} + 1$. In 1961, Erdős and Szekeres proved the matching lower bound $\mathrm{ES}(n) \ge 2^{n-2} + 1$. For 80 years, the best upper bounds hovered around $\binom{2n-5}{n-2} \approx 4^n / \sqrt{n}$ until Andrew Suk's 2016/2017 breakthrough slashed the upper bound to $2^{n + O(n^{2/3} \log n)}$, bringing it asymptotically close to $2^n$ — yet the exact value $\mathrm{ES}(7)$ itself remains open!

## Timeline

- **1933** — Esther Klein proves $\mathrm{ES}(4) = 5$ and poses the general $n$-gon problem.
- **1935** — Erdős and Szekeres prove $\mathrm{ES}(n) \le \binom{2n-4}{n-2} + 1$ via the cup-and-cap theorem and conjecture $\mathrm{ES}(n) = 2^{n-2} + 1$.
- **1961** — Erdős and Szekeres construct $2^{n-2}$ points in general position with no convex $n$-gon, proving $\mathrm{ES}(n) \ge 2^{n-2} + 1$.
- **1970** — Kalbfleisch, Kalbfleisch, and Stanton prove $\mathrm{ES}(5) = 9$.
- **1998** — Chung–Graham and Kleitman–Pachter improve the binomial upper bound slightly; Tóth and Valtr prove $\mathrm{ES}(n) \le \binom{2n-5}{n-2} + 2$.
- **2006** — George Szekeres and Lindsay Peters settle $n = 6$ via exhaustive computer search over realizable order types, proving $\mathrm{ES}(6) = 17$.
- **2016–2017** — Andrew Suk proves $\mathrm{ES}(n) \le 2^{n + 6n^{2/3} \log n}$ (`arXiv:1604.08657`, *JAMS* 2017), shattering the $4^n$ barrier.
- **2020** — Holmsen, Mojarrad, Pach, and Tardos refine Suk's bound to $\mathrm{ES}(n) \le 2^{n + O(\sqrt{n \log n})}$ (*JEMS* 2020).
