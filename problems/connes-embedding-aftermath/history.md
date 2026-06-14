# History — The Connes Embedding Problem (Resolved 2020)

_Origin, formulation, and timeline._

## How the problem arose

The problem traces to a single, almost offhand remark in Alain Connes's 1976 *Annals of Mathematics* paper "Classification of injective factors." Studying the hyperfinite type II$_1$ factor $R$ — the unique amenable factor with separable predual, and the most tractable infinite-dimensional von Neumann algebra — Connes wrote that "it seems that every type II$_1$ factor" embeds into an ultrapower $R^{\omega}$ of $R$ relative to a free ultrafilter $\omega$ on $\mathbb{N}$. The Connes Embedding Problem (CEP) asks whether this is true: does every separable II$_1$ factor $M$, with trace $\tau$, admit a trace-preserving embedding $M \hookrightarrow R^{\omega}$?

Equivalently — and this is what made the problem so consequential — CEP asks whether every II$_1$ factor can be *approximated by matrices*. An embedding into $R^{\omega}$ means the algebra's moments are matched, to arbitrary precision in the normalized-trace norm, by finite matrices. The question thus reads as: is every tracial von Neumann algebra "matricially approximable" (hyperlinear)?

## Reformulations

CEP's depth comes from a web of equivalences proved over four decades:

- **Kirchberg (1993):** CEP is equivalent to the statement that $C^*(\mathbb{F}_\infty) \otimes_{\min} C^*(\mathbb{F}_\infty) = C^*(\mathbb{F}_\infty) \otimes_{\max} C^*(\mathbb{F}_\infty)$, tying it to the QWEP conjecture and the structure of tensor norms on $C^*$-algebras.
- **Tsirelson / Quantum correlations:** CEP is equivalent to the statement that the set of *quantum commuting* correlations equals the closure of *quantum tensor* (finite-dimensional) correlations, i.e. $C_{qc} = C_{qa}$ — the resolution of Tsirelson's problem.
- **Ozawa, Junge–Navascués–Palazuelos–Pérez-García–Scholz–Werner (2011):** assembled these into a precise dictionary linking CEP, Tsirelson's problem, and the QWEP conjecture.

The negative resolution came from theoretical computer science: the 2020 result $\mathrm{MIP}^* = \mathrm{RE}$ shows the entangled-prover complexity class equals the recursively enumerable sets, which forces $C_{qa} \neq C_{qc}$, refuting Tsirelson's problem and hence CEP.

## Timeline

- **1976** — Connes poses the embedding remark in "Classification of injective factors" (*Ann. Math.*).
- **1985** — Voiculescu inaugurates free probability; later the *free entropy* program supplies tools relevant to embeddability.
- **1993** — Kirchberg proves the equivalence of CEP with QWEP and the $C^*(\mathbb{F}_\infty)$ tensor-norm question.
- **2004** — Voiculescu shows free-entropy obstructions (no II$_1$ factor with two Cartan subalgebras embeds "with negative free entropy" pathologies), sharpening structure theory.
- **2006** — Răăburu/Brown and others develop the convex-structure ("hom space") viewpoint on embeddings.
- **2008** — Tsirelson's problem on quantum correlation sets formulated precisely (Scholz–Werner).
- **2010** — Ozawa's influential survey "About the QWEP conjecture" maps the equivalences.
- **2011** — Junge–Navascués–Palazuelos–Pérez-García–Scholz–Werner and Fritz independently prove CEP $\Leftrightarrow$ Tsirelson's problem.
- **2012–2018** — Slofstra shows the quantum correlation set $C_q$ is non-closed and that group-embeddability problems are undecidable, signaling that complexity-theoretic methods could attack CEP.
- **2016** — Ozawa–Slofstra and others connect non-local games to operator-algebra approximation.
- **2020 (Jan)** — Ji, Natarajan, Vidick, Wright, Yuen post "MIP* = RE" (arXiv:2001.04383), proving $\mathrm{MIP}^* = \mathrm{RE}$ and thereby refuting Connes's embedding conjecture.
- **2020–2022** — Community verification; Vidick and others write expositions; Goldbring–Hart, Gao, and Coladangelo–Stark probe consequences and alternative routes.
- **2023–2025** — Frontier shifts to quantitative/effective non-embeddability, the structure of $\mathrm{Th}(R^\omega)$, the QWEP conjecture's residual status, and explicit non-hyperlinear witnesses.
