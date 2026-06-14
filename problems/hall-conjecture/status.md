# Status & Frontier — Hall's Conjecture

_Where the problem stands and what a resolution would require._

**Overall status: open** (both forms). The metadata records the problem as unresolved, and that is accurate for both the strong and weak versions.

## What is known

**Unconditional.**
- *Trivial lower bound only.* For $x^3 \neq y^2$ one has $|x^3 - y^2| \geq 1$; beyond this, **no power-saving unconditional bound** $|x^3 - y^2| \gg x^{\delta}$ with a fixed $\delta > 0$ is known. This is the stark gap: the conjecture wants $\delta = 1/2-\varepsilon$, and we cannot prove *any* positive $\delta$ unconditionally.
- *Per-fixed-$k$ effectivity.* For each individual $k$, Baker's linear-forms-in-logarithms bounds make $y^2 = x^3 + k$ effectively solvable, and integral points have been tabulated for large ranges of $|k|$ (Gebel–Pethő–Zimmer; Stroeker–Tzanakis). This gives effective but non-uniform, exponential-in-$k$ control — the wrong shape for Hall.
- *Function-field analogue is a theorem.* Davenport (1965) proved the exact strong inequality, with sharp constant, for coprime polynomials $f, g$ with $f^3 \neq g^2$ (equivalently via Mason–Stothers). The exponent $1/2$ is therefore confirmed in the polynomial world.
- *Sharpness.* Davenport–Lewis–Schinzel (1965) and Danilov (1982) give infinitely many integers with $|x^3-y^2| \asymp \sqrt{x}$, so no exponent larger than $1/2$ can hold; the strong form's constant is genuinely small and in doubt.

**Conditional.**
- *Weak Hall follows from the $abc$ conjecture* (Masser–Oesterlé): for every $\varepsilon>0$, $|x^3-y^2| \gg_\varepsilon x^{1/2-\varepsilon}$.
- *Weak Hall follows from Vojta's conjecture*, as a special case of its height inequality for integral points on genus-1 affine curves.
- These conditional results are robust and standard, but $abc$ and Vojta are themselves open. Shinichi Mochizuki's claimed proof of $abc$ via **inter-universal Teichmüller theory** (published in *PRIMS*, 2021) is **not accepted by the broad community**; **Scholze and Stix (2018)** identified what they argue is an unjustified inequality at the heart of the proof (the "Corollary 3.12" step), and the dispute is unresolved. Weak Hall therefore cannot be treated as proven through this channel.

## What a full resolution requires

- **Weak form:** any accepted proof of the $abc$ conjecture (or of the relevant case of Vojta) immediately yields it. Alternatively, a direct uniform power-saving lower bound on $|x^3-y^2|$ by some method not currently available — no such technique is on the horizon, since Baker's method is structurally exponential and Diophantine-approximation tools give ineffective, non-uniform constants.
- **Strong form:** beyond proving the exponent, one must pin down the correct absolute constant. The record examples (Elkies's $r\approx 0.0211$ and the Danilov family) show the constant is small; whether the infimum of the Hall ratio $r = |x^3-y^2|/\sqrt{x}$ is strictly positive is itself unsettled, so even the *truth* of the strong form (as literally stated with a positive constant) is not assured.

## Plausible routes

1. **Through $abc$/Vojta** — the only route that currently reaches the weak form, but entirely contingent on a major unsolved conjecture.
2. **Transfer from the function-field proof** — blocked by the absence of an arithmetic analogue of the derivative/Wronskian; would require a genuinely new idea bridging the function-field/number-field divide.
3. **Refined effective Diophantine methods** — improvements to Baker-type bounds toward uniformity in $k$; no path is known that converts these into a power law.
4. **Computation** — can only refute over-strong constants or guide the conjectural constant; cannot prove a lower bound.

## Related problems

- [abc Conjecture](../abc-conjecture/README.md)
- [Vojta's Conjecture](../vojta-conjecture/README.md)
- [Bombieri–Lang Conjecture](../bombieri-lang-conjecture/README.md)
- [Birch and Swinnerton-Dyer Conjecture](../birch-swinnerton-dyer/README.md)
- [Schinzel's Hypothesis H](../schinzel-hypothesis-h/README.md)
