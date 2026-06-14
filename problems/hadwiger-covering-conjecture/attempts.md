# Attempts — The Hadwiger Covering Conjecture

_Notable attempts, near-misses, retracted proofs._

## Settled fragments (genuine partial results)

- **Plane case (Levi, 1950s).** $c(K)\le 4$ for every $K\subset\mathbb{R}^2$, with $4$ attained only by parallelograms. This is the one dimension in which the full conjecture — bound *and* equality characterization — is a theorem.
- **Smooth bodies (any $n$).** If $\partial K$ is $C^1$ (a unique supporting hyperplane at each boundary point), then $I(K)=n+1$. This is a clean, complete result, but smoothness is exactly the opposite of the cube, so it does not approach the hard case.
- **Centrally symmetric bodies in $\mathbb{R}^3$ (Lassak, 1980s).** $c(K)\le 8$ for symmetric $K\subset\mathbb{R}^3$, matching the conjectured value in that dimension and class.
- **Constant-width bodies in $\mathbb{R}^3$ (Dekster and others).** The conjecture holds; such bodies need at most $6 < 8$ homothets, comfortably below the bound.
- **Zonotopes, belt polytopes, belt bodies (Boltyanski, Martini).** The conjecture is established with the parallelepiped the unique extremizer.

## Asymptotic near-misses

The headline quantitative story is the long-standing gap between $2^n$ and the best general upper bound:

- **Rogers / Erdős–Rogers (1960s).** Economic covering gives $c(K)\le \binom{2n}{n}\, n\ln n\,(1+o(1))$ for symmetric bodies — roughly $4^n$, exponentially above the target $2^n$.
- **Huang–Slomka–Tkocz–Vritsiou (2021).** The first asymptotic improvement in decades, reducing the symmetric-case bound to $\binom{2n}{n}(n\ln n + n\ln\ln n + 5n)$ and improving the general bound. Important, but still $\approx 4^n$: the factor-$2^n$ gap persists.

No incremental method has come within a sub-exponential factor of $2^n$ for general bodies; this is the standing "near-miss" frustration of the field.

## Disputed and withdrawn claims

The Hadwiger covering / illumination conjecture has periodically attracted **claimed full proofs**, especially of the three-dimensional case ($c(K)\le 8$ for all $K\subset\mathbb{R}^3$). These appear sporadically on preprint servers.

- **Status, stated neutrally.** As of the present, **no claimed proof of the general conjecture, and no claimed proof of the full $\mathbb{R}^3$ case, has been accepted by the discrete-geometry community.** Survey literature (Bezdek–Khan; Boltyanski–Martini–Soltan) continues to list both the general statement and the $n=3$ case as **open**.
- **Common objections.** Announced arguments for the $3$-dimensional case typically founder on the boundary case of "spiky" or irregular vertices, where a proposed partition of the sphere of normal directions into $8$ illuminable regions fails; reviewers have repeatedly identified gaps in the handling of vertices whose normal cones are large or pathologically arranged. Because the obstruction is precisely at the extremal configurations, partial verifications (symmetric, smooth, constant-width) do not patch these gaps.

This dossier records no specific claimed proof as resolving the problem; per the source metadata the status is **open**. Readers should treat any individual preprint asserting a resolution as **unverified** until it appears in a refereed venue and is endorsed in the survey literature.

## Why it resists

The difficulty is structural. The conjecture is uniform in $n$ yet the extremizer (parallelepiped) is the least "generic" body; volumetric methods overshoot by an inherent $2^n$ factor; illumination is local but does not aggregate; and there is no monotonicity of $c(K)$ under the natural operations (sections, projections, polarity). Each near-miss illuminates the gap without closing it.
