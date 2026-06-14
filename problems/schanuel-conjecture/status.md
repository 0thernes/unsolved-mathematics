# Status & Frontier — Schanuel's Conjecture

**Status: open** (for every $n\ge 1$ beyond the cases covered by classical theorems). No credible general proof exists, and the first genuinely new instance — for example the algebraic independence of $e$ and $\pi$ over $\mathbb{Q}$ — is itself wide open.

## What is known (unconditional)

- **Algebraic case.** When $z_1,\dots,z_n$ are algebraic and $\mathbb{Q}$-linearly independent, the conjecture is exactly the **Lindemann–Weierstrass theorem** and is fully proved. This is the largest established fragment.
- **Gelfond–Schneider** gives the relevant $n=2$ arithmetic instance underlying $a^b$ transcendence.
- **Nesterenko (1996)** proved $\operatorname{trdeg}_\mathbb{Q}\mathbb{Q}(\pi,e^\pi,\Gamma(1/4))=3$, certifying a Schanuel-strength trdeg lower bound for one specific modular configuration — the deepest algebraic-independence result in the area.
- **Wüstholz's analytic subgroup theorem (1989)** yields the strongest unconditional results on *linear* relations among logarithms / on algebraic groups, but not the full nonlinear trdeg bound.
- **Ax–Schanuel (1971)** proves the conjecture's exact analogue in the differential/formal setting; Pila–Tsimerman (2016) and Mok–Pila–Tsimerman (2019) extend the functional version to the $j$-function and Shimura varieties.

## What is known (conditional)

- **Macintyre–Wilkie:** a real form of Schanuel implies the **decidability** of the first-order theory of $(\mathbb{R},\exp)$.
- **Zilber's program:** a *strong* Schanuel statement, together with **Exponential-Algebraic Closedness** (now largely a theorem via Bays–Kirby and Aslanyan–Kirby–Mantova), implies Zilber's conjecture that the pseudo-exponential field $\mathbb{B}$ is isomorphic to $(\mathbb{C},\exp)$. The closedness half being settled has sharpened Schanuel into the *sole* remaining arithmetic obstruction of that program.

## What a full resolution would require

A proof would need to certify, for arbitrary $\mathbb{Q}$-linearly independent complex $z_1,\dots,z_n$, a trdeg lower bound that grows **linearly in $n$**. Every current arithmetic technique (auxiliary functions, zero/multiplicity estimates, linear forms in logarithms) controls only a *bounded* number of algebraically independent quantities, and the only result giving the full linear bound — Ax–Schanuel — lives in a differential category that provably does not specialize to $\mathbb{C}$ (there is no derivation on $\mathbb{C}$ realizing $\exp$). Crossing this **functional-to-arithmetic gap** is the crux; it is widely believed to demand a genuinely new idea rather than a refinement of existing methods.

## Plausible routes

1. **A new specialization principle** transporting Ax–Schanuel-type functional independence to complex points — the most direct conceptual target.
2. **Algebraic-independence breakthroughs** in the Gelfond–Nesterenko tradition extending modular/period methods to certify $\operatorname{trdeg}\ge n$ for growing families.
3. **Model-theoretic input** from the o-minimal and exponential-field side that might extract an arithmetic predimension bound, now that closedness is understood.

Given difficulty (88/100) and very low tractability (17/100) in this dossier's metadata, the realistic near-term expectation is continued progress on analogues, conditional theorems, and isolated trdeg results — not a general proof.

## Related problems

- [abc Conjecture](../abc-conjecture/README.md)
- [Riemann Hypothesis](../riemann-hypothesis/README.md)
- [Birch and Swinnerton-Dyer Conjecture](../birch-swinnerton-dyer/README.md)
- [Littlewood Conjecture](../littlewood-conjecture/README.md)
- [Montgomery's Pair Correlation Conjecture](../montgomery-pair-correlation/README.md)
