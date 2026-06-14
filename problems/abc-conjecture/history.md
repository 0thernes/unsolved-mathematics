# History — The abc Conjecture

_Origin, formulation, and timeline._

The abc conjecture grew out of the rich soil of late-twentieth-century Diophantine geometry, where a single recurring theme — that solutions of polynomial equations cannot be simultaneously "small" and "highly divisible by large prime powers" — was crystallizing into precise statements. Its proximate stimulus was the **Mason–Stothers theorem** (W. W. Stothers, 1981; rediscovered by R. C. Mason, 1984), the polynomial analogue: for coprime polynomials $a(t)+b(t)=c(t)$ over a field, not all constant, one has $\max(\deg a,\deg b,\deg c) \le N_0(abc)-1$, where $N_0$ counts distinct roots. This is an *exact*, *unconditional*, *easily proved* statement. The abc conjecture is the bold proposal that an analogue holds for integers, where the role of "number of distinct roots" is played by the **radical** $\mathrm{rad}(n)=\prod_{p\mid n}p$.

**Precise formulation.** For coprime positive integers with $a+b=c$, define the radical $\mathrm{rad}(abc)$. The conjecture (Masser–Oesterlé form) asserts: for every $\varepsilon>0$ there exists a constant $K_\varepsilon$ such that
$$ c \;<\; K_\varepsilon \cdot \mathrm{rad}(abc)^{\,1+\varepsilon} $$
for all such triples. Equivalently, defining the *quality* $q(a,b,c)=\dfrac{\log c}{\log \mathrm{rad}(abc)}$, only finitely many triples have $q>1+\varepsilon$. The $\varepsilon$ is genuinely necessary: triples with $q>1$ exist infinitely often (e.g. the family built from $9^n \mid 3^{2^n}-1$ generated from $1+(2^{6n}-1)=2^{6n}$), so the naive statement with $\varepsilon=0$ is false. The conjecture is striking because it implies, often effortlessly, Fermat's Last Theorem for large exponents, the Mordell conjecture (with effective bounds, via Elkies), Roth's theorem, Wieferich-prime infinitude, Erdős–Woods, and much more.

**Reformulations.** Oesterlé phrased a version while examining the Szpiro conjecture relating the conductor and minimal discriminant of elliptic curves; indeed abc is essentially equivalent to a uniform Szpiro inequality. Vojta later embedded abc into his sweeping conjectures on heights in Diophantine geometry, recasting the radical as a truncated counting function and the inequality as a height bound mirroring the Second Main Theorem of Nevanlinna theory — making abc the arithmetic shadow of value-distribution theory.

## Timeline

- **1981** — W. W. Stothers proves the polynomial degree inequality later called Mason–Stothers.
- **1983** — L. Szpiro formulates the Szpiro conjecture on elliptic-curve conductors and discriminants, a close cousin.
- **1984** — R. C. Mason independently publishes the function-field theorem, popularizing the analogy.
- **1985** — Joseph Oesterlé (in a Séminaire Bourbaki context on Szpiro) and David Masser (at a Cambridge meeting) formulate the integer conjecture; Masser states the clean $\mathrm{rad}(abc)^{1+\varepsilon}$ form.
- **1988** — Noam Elkies shows abc implies an *effective* Mordell/Faltings, with explicit height bounds.
- **1991** — Paul Vojta connects abc to his height conjectures and the Nevanlinna dictionary.
- **1994** — C. L. Stewart and Kunrui Yu prove the first unconditional lower-bound progress: $\log c \ll \mathrm{rad}(abc)^{1/3+\varepsilon}$ via linear forms in logarithms (Baker's method).
- **2001** — Stewart–Yu sharpen the exponent to $1/3$ with refined constants.
- **2006** — A. Granville and T. Tucker survey and popularize abc ("It's As Easy As abc").
- **2007** — ABC@home distributed-computing project begins exhaustively cataloguing high-quality triples.
- **August 2012** — Shinichi Mochizuki releases four papers on Inter-universal Teichmüller theory (IUT) claiming a proof.
- **2015–2016** — Oxford and Kyoto workshops convene; the proof's Corollary 3.12 becomes the contested crux.
- **2018** — Peter Scholze and Jakob Stix circulate a report asserting a gap in the inequality of Corollary 3.12; Mochizuki rebuts.
- **2020** — Mochizuki's papers are accepted by *Publications of the RIMS* (of which he is chief editor), intensifying controversy.
- **2021** — Kirti Joshi and others announce alternative arithmetic-Teichmüller frameworks aiming to clarify or reconstruct the claims.
- **Present** — The conjecture is regarded as **open** by the mainstream community; the IUT proof remains disputed and not independently validated.
