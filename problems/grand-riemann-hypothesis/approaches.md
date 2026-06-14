# Approaches — The Grand Riemann Hypothesis

GRH inherits every line of attack on RH, and adds challenges specific to higher degree: the absence of an unconditional Euler product bound (Ramanujan), poorly understood functional-equation data, and the difficulty of mollifying $L$-functions whose Dirichlet coefficients are not multiplicative in a tractable way. No approach has resolved RH even for $\zeta$, so all entries below are partial.

## Critical-line / mollifier method (Hardy–Selberg–Levinson–Conrey)

**Core idea.** Show a positive *proportion* of zeros lie on $\mathrm{Re}(s)=\tfrac12$ by computing mollified second (and higher) moments of $L$ on the critical line and applying Levinson's method to the logarithmic derivative. Hardy (1914) proved infinitely many on-line zeros for $\zeta$; Selberg got a positive proportion; Levinson (1974) reached $34\%$; Conrey (1989) $40\%$; Bui–Conrey–Young, Pratt–Robles, and Feng pushed past $41\%$ (current records hover near $41.7\%$).

**Best reached for GRH.** The machinery has been extended to Dirichlet, Dedekind, and some $\mathrm{GL}_2$ $L$-functions, giving positive proportions of on-line zeros there too.

**Barrier.** The method cannot in principle reach $100\%$: mollifier length is limited by available moment estimates, and even an optimal mollifier leaves a positive proportion uncontrolled. It also says nothing about a *single* high zero being off the line.

## Pair correlation and random matrix theory (Montgomery–Odlyzko–Katz–Sarnak)

**Core idea.** Montgomery's 1973 pair-correlation conjecture matches the statistics of $\zeta$-zeros to eigenvalues of large random unitary (GUE) matrices; Katz–Sarnak (1999) extended this to families of $L$-functions with symmetry type (unitary, orthogonal, symplectic). This makes GRH statistically *expected* and predicts fine zero statistics.

**Best reached.** Strong numerical confirmation (Odlyzko) and theorems on low-lying zeros of families under GRH, plus unconditional results for function-field families (where RH is Deligne's theorem).

**Barrier.** RMT is a heuristic for *where zeros are on average*; it provides no mechanism forbidding an individual off-line zero, and pair correlation is itself only partially proven (Montgomery's theorem holds in a restricted range).

## Function-field analogue (Weil–Deligne)

**Core idea.** For curves and varieties over finite fields $\mathbb{F}_q$, the analogue of RH is a *theorem*: Weil (1948) for curves, Deligne (1974) for general varieties, via $\ell$-adic cohomology and the Frobenius eigenvalue bound $|\alpha|=q^{w/2}$.

**Best reached.** A complete proof in the geometric setting, and a working template (spectral interpretation of zeros as eigenvalues).

**Barrier.** $\mathrm{Spec}\,\mathbb{Z}$ is not a variety over a field; there is no known cohomology theory ("the field with one element", $\mathbb{F}_1$) that makes $\zeta$ a geometric zeta function. Transporting Deligne's proof to number fields is the central open obstruction.

## Hilbert–Pólya / spectral approach

**Core idea.** Find a self-adjoint operator $H$ whose eigenvalues are the imaginary parts $\gamma$ of the non-trivial zeros; self-adjointness forces $\gamma\in\mathbb{R}$, i.e. zeros on the line. Berry–Keating and Connes propose explicit (semiclassical / adèlic) candidates.

**Best reached.** Connes (1999) gave a trace formula on the adèle class space $\mathbb{A}_{\mathbb{Q}}^\times/\mathbb{Q}^\times$ whose *spectral side* is equivalent to GRH for all $L$-functions with Größencharakter — a genuine reformulation covering many GRH cases at once.

**Barrier.** In Connes' framework GRH becomes a *positivity* statement (a Weil-type explicit formula must be a positive distribution); proving that positivity is exactly as hard as the original problem. No operator with the required spectrum has been constructed.

## Selberg class structure theory (Kaczorowski–Perelli)

**Core idea.** Rather than prove RH, classify $\mathcal{S}$. The degree $d_F$ (from the functional-equation gamma factors) is conjectured to be a non-negative integer; primitive elements should factor uniquely.

**Best reached.** Kaczorowski–Perelli proved there are **no** elements of degree $0<d<1$, classified degree $0$ (constants) and degree $1$ (Dirichlet $L$-functions and shifts of $\zeta$), and showed no elements exist with $1<d<2$. Each confirms the automorphic picture.

**Barrier.** Structural classification constrains *which* $L$-functions exist but never locates their zeros; the degree-$2$ case (which would include $\mathrm{GL}_2$ cusp forms) is already out of reach, and RH is untouched by these methods.

## Positivity / explicit-formula criteria (Weil, Li, Bombieri)

**Core idea.** Reformulate RH as a positivity condition: Weil's explicit formula is a positive quadratic form iff RH holds; Li's criterion (1997) states RH $\iff \lambda_n\ge 0$ for all $n$, where $\lambda_n=\sum_\rho[1-(1-1/\rho)^n]$. These extend verbatim to the Selberg class (Li–Sekatskii, Lagarias).

**Best reached.** Clean equivalent reformulations and partial positivity verifications; the de Bruijn–Newman constant work (Rodgers–Tao 2020 proved $\Lambda\ge 0$, with RH $\iff \Lambda\le 0$) shows the truth is "barely" true if true.

**Barrier.** Each criterion is logically equivalent to GRH, so it relocates rather than removes the difficulty; verifying the positivity unconditionally remains open.
