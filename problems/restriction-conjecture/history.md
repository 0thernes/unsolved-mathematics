# History — The Restriction Conjecture

_Origin, formulation, and timeline._

## Origin

The restriction problem grew from a deceptively simple observation Elias M. Stein made in the mid-1960s: although the Fourier transform of an $L^p$ function is, a priori, only defined almost everywhere, for certain $p$ its values can be meaningfully *restricted* to a curved hypersurface of measure zero, such as the unit sphere $S^{n-1}\subset\mathbb{R}^n$ or the paraboloid. For flat surfaces this is hopeless, but curvature confers integrability. Stein circulated the question in lectures and seminars at Princeton around 1967; the first published traces appear in work of Charles Fefferman and Stein in the early 1970s.

Concretely, the **restriction estimate** $R(p\to q)$ asserts
$$\big\|\widehat{f}\,|_{S^{n-1}}\big\|_{L^q(S^{n-1},d\sigma)} \le C\,\|f\|_{L^p(\mathbb{R}^n)} .$$
By duality this is equivalent to the **extension estimate** for the adjoint operator $Eg(x)=\int_{S^{n-1}} g(\xi)\,e^{2\pi i x\cdot\xi}\,d\sigma(\xi)$:
$$\|Eg\|_{L^{p'}(\mathbb{R}^n)} \le C\,\|g\|_{L^{q'}(S^{n-1})}.$$
The **Restriction Conjecture** is the sharp endpoint statement: $E$ maps $L^\infty(S^{n-1})$ to $L^{q}(\mathbb{R}^n)$ for every $q>\tfrac{2n}{n-1}$ (equivalently $R(p\to q)$ holds for $p'<\tfrac{2n}{n-1}$). The threshold $\tfrac{2n}{n-1}$ is dictated by the decay of the surface measure's Fourier transform and is sharp via a **Knapp example** (a flat cap concentrating a wave packet).

## Timeline

**1967** — Stein poses the restriction problem; circulated in Princeton seminars.

**1970** — Charles Fefferman, with Stein, establishes the first nontrivial restriction theorems; the $L^2$-restriction phenomenon is identified.

**1975** — Peter Tomas proves the $L^2$-based restriction theorem $R(p\to 2)$ for $p'\ge\tfrac{2(n+1)}{n-1}$; Stein supplies the endpoint. The **Stein–Tomas theorem** becomes the canonical baseline.

**1971** — Fefferman disproves the disc (ball) multiplier conjecture, exposing the role of Besicovitch/Kakeya sets and the limits of naive square-function approaches.

**1991** — Jean Bourgain breaks the Stein–Tomas exponent in higher dimensions, linking restriction directly to the **Kakeya maximal conjecture** and introducing "bush" and arithmetic ideas.

**1995** — Bourgain pushes the Kakeya–restriction connection further; Thomas Wolff develops the bush/hairbrush method, obtaining a $\tfrac{n+2}{2}$ Kakeya bound.

**1995–1999** — Bilinear methods emerge; Wolff proves the sharp $L^2$ bilinear cone (local smoothing) estimate (1999).

**1998** — Moyua, Vargas, and Vega, and then Tao, Vargas, and Vega, systematize the bilinear restriction–Kakeya machinery.

**2003** — Terence Tao proves the sharp **bilinear restriction estimate** for the paraboloid, the strongest general restriction input for over a decade.

**2006** — Jonathan Bennett, Anthony Carbery, and Tao prove the near-sharp **multilinear (Kakeya) inequality**.

**2009** — Zeev Dvir resolves the finite-field Kakeya conjecture by the **polynomial method**; Bourgain and Larry Guth convert multilinear estimates into improved linear restriction bounds via the **broad–narrow** decomposition.

**2016** — Guth uses **polynomial partitioning** to obtain the best restriction range in $\mathbb{R}^3$ ($p>3.25$), refined in subsequent work.

**2017** — Bourgain–Demeter **decoupling** reshapes the surrounding theory and yields striking number-theoretic consequences (Vinogradov).

**2018–2020** — Guth, Hong Wang, and Ruixiang Zhang push three-dimensional restriction and the local smoothing conjecture for the wave equation (Guth–Wang–Zhang, 2020).

**2022–2025** — Hong Wang and Joshua Zahl announce, then post, a proof of the three-dimensional **Kakeya set conjecture** (2025), a major adjacent milestone. Restriction in $\mathbb{R}^3$ remains open at the conjectural endpoint.

## Status

The conjecture is fully proven only in dimension $n=2$ (Fefferman–Stein, in the Carleson–Sjölin circle of ideas). In all dimensions $n\ge 3$ it remains **open**, with the current frontier driven by the polynomial method, decoupling, and the deep coupling to Kakeya.
