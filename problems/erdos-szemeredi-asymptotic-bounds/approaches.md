# Approaches — Erdős Problem 142 (Asymptotic Density of $k$-AP-Free Sets)

_Major strategies, partial results, and barriers._

1. **Fourier-Analytic Density Increment (Roth–Bourgain–Sanders–Bloom–Sisask).** For $k=3$, linear Fourier analysis detects a large Fourier coefficient whenever a set lacks 3-APs, incrementing density on a Bohr set. For decades this yielded bounds of shape $N / (\log N)^{1-o(1)}$ until Bloom–Sisask (2020) pushed past $(\log N)^{-1}$ via almost-periodicity in $L^p$.
2. **Physical-Space Sifting & Spectral Positivity (Kelley–Meka 2023).** Abandoning direct Fourier-coefficient extraction, Kelley and Meka combined Croot–Sisask almost-periodicity with a physical-space Hölder/positivity argument on $r$-fold convolutions, achieving $r_3(N) \le N \exp(-c (\log N)^{1/12})$ — the first bound matching Behrend's $\exp(-(\log N)^\alpha)$ shape.
3. **Higher-Order Fourier Analysis & Nilsequences (Gowers 2001; Green–Tao–Ziegler; Leng–Sah–Sawhney 2024).** For $k \ge 4$, linear characters do not control $k$-AP counts; one requires Gowers $U^{k-1}$ norms and quantitative inverse theorems relating large $U^{k-1}$ norms to correlation with $(k-2)$-step nilsequences. Leng, Sah, and Sawhney (2024) proved quasipolynomial inverse $U^{k-1}$ bounds, upgrading Gowers's $N/(\log\log N)^{c_k}$ bound to $N \exp(-(\log\log N)^{c_k})$ for every $k \ge 5$.
4. **Geometric Sphere-Packing & Modular Constructions (Behrend–Rankin–Elkin).** Lower bounds construct $k$-AP-free subsets by mapping high-dimensional integer lattice points lying on a thin spherical shell (where no three points are collinear) into $\mathbb{Z}$ via base-$B$ expansion, yielding $r_k(N) \ge N \exp(-c_k (\log N)^{1/\lceil \log_2 k \rceil})$.

## Core Barrier
For $k=3$, closing the gap between $\exp(-c(\log N)^{1/2})$ (Behrend) and $\exp(-c(\log N)^{1/9})$ (Kelley–Meka / Bloom–Sisask) — let alone finding an asymptotic formula — requires controlling how Bohr-set dimension grows across density-increment iterations. For $k \ge 4$, even reaching $\exp(-(\log N)^{c_k})$ (removing the iterated logarithm altogether) remains out of reach of current nilsequence inverse technology.
