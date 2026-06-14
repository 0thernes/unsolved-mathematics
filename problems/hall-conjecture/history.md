# History — Hall's Conjecture

_Origin, formulation, and timeline._

The conjecture grew out of the study of the **Mordell equation** $y^2 = x^3 + k$ and the older question of how small the difference between a perfect square and a perfect cube can be. Bounding $|x^3 - y^2|$ from below is classical: if $x^3 \neq y^2$ the difference is a nonzero integer, hence $\geq 1$, but the real question is how the gap grows as $x, y \to \infty$. Numerically, near-collisions are rare and seem to require $x$ to be very large relative to the gap.

**Original (strong) form (1971).** Marshall Hall Jr., in "The Diophantine equation $x^3 - y^2 = k$," conjectured an absolute constant $C > 0$ such that for all integers $x, y$ with $x^3 \neq y^2$,
$$|x^3 - y^2| > C\,\sqrt{x}.$$
Equivalently, if $0 < |x^3 - y^2| = k$ then $x \ll k^2$. This *strong* form asserts the exponent $1/2$ is best possible: a 1965 parametric construction of Davenport, Lewis and Schinzel — later sharpened by L. V. Danilov (1982) — yields infinitely many pairs with $|x^3 - y^2| \asymp \sqrt{x}$, so no larger exponent can hold.

**Weak form.** Because the sharp constant proved elusive (and the strongest reading is now doubted), the community adopted the **weak Hall conjecture**: for every $\varepsilon > 0$ there is $C_\varepsilon > 0$ with
$$|x^3 - y^2| > C_\varepsilon\, x^{1/2 - \varepsilon}.$$
This is the version that follows from the $abc$ conjecture and from Vojta's conjecture, and the one most often meant by "Hall's conjecture" today.

**Reformulations.** Hall's bound governs the height of integral points on Mordell curves: writing $H = |x^3 - y^2|$, the claim is $x \ll H^{2+\varepsilon}$, controlling integral solutions of $y^2 = x^3 - H$ by $H$. It is a model case of the principle — made precise by $abc$ (Masser–Oesterlé, 1985) and Vojta's height inequalities — that integral points cannot greatly exceed the arithmetic complexity forcing them.

## Timeline

- **1965** — Davenport, Lewis and Schinzel exhibit polynomial identities producing infinitely many small values of $x^3 - y^2$, foreshadowing sharpness of the exponent $1/2$.
- **1971** — Marshall Hall Jr. states the conjecture in "The Diophantine equation $x^3 - y^2 = k$" (in *Computers in Number Theory*, eds. Atkin & Birch), proposing $|x^3-y^2| \gg \sqrt{x}$.
- **1965** — Davenport proves the *function-field* analogue: for polynomials $f, g$ with $f^3 \neq g^2$, $\deg(f^3 - g^2) \geq \tfrac12\deg f + 1$, confirming the exponent in the polynomial setting.
- **1982** — L. V. Danilov constructs an explicit infinite family with $|x^3 - y^2| < C\sqrt{x}$, with constant near $0.97$, casting doubt on the strongest constant in the strong form.
- **1985** — Masser and Oesterlé formulate the $abc$ conjecture; weak Hall is recognized as a consequence.
- **1995–1998** — Elkies develops lattice-reduction searches and finds the celebrated example with $|x^3-y^2| \approx 0.0211\sqrt{x}$ near $x = 5853886516781223$, the record "good" point for many years.
- **1998** — Vojta's conjecture is seen to imply weak Hall as a special case of its height inequality for curves.
- **2000s** — Large-scale computations (Jiménez Calvo, Herzog; Gebel–Pethő–Zimmer Mordell-curve tables) extend the list of record Hall ratios and test the strong constant.
- **2015–2020** — Continued searches lower the record Hall ratio; both forms remain open, with smallest known ratios serving as benchmarks for the conjectural constant.
- **Present** — Weak Hall is a theorem conditional on $abc$ / Vojta; both forms are unconditionally open. No unconditional power-saving lower bound $|x^3-y^2| \gg x^\delta$ with fixed $\delta > 0$ is known.
