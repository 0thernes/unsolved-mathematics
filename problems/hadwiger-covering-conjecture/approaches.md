# Approaches — The Hadwiger Covering Conjecture

_Major strategies, partial results, and barriers._

Throughout, $c(K)$ denotes the covering number (= illumination number $I(K)$ = minimum translates of $\operatorname{int}K$ covering $K$). The conjecture is $c(K) \le 2^n$, with equality only for parallelepipeds.

## Illumination reformulation (Boltyanski)

**Core idea.** A direction $d$ *illuminates* a boundary point $x \in \partial K$ if the ray $x + td$ ($t>0$) enters the interior of $K$ immediately. $I(K)$ is the least number of directions illuminating every boundary point. Boltyanski proved $I(K)=c(K)$, so the problem becomes local: control the "shadow boundary" and the normal cones at extreme points.

**Best result.** This is the working language of essentially all progress: smooth bodies satisfy $I(K)=n+1$, while the cube needs $2^n$. The reformulation reduces the equality case to understanding how many directions a single vertex's normal cone forces.

**Barrier.** Illumination is genuinely combinatorial at vertices: a polytope with many "spiky" vertices can demand many directions, and there is no clean monotonicity under taking sections or projections, so local control does not assemble into a global $2^n$ bound.

## Probabilistic / volumetric covering (Rogers, Erdős–Rogers, modern)

**Core idea.** Random covering arguments and the Rogers–Zong economic-covering lemma bound the number of translates of one convex body needed to cover another by a product of a volume ratio and a covering density. For symmetric $K$ this yields
$$
c(K) \le \binom{2n}{n}\big(n \ln n + n \ln\ln n + 5n\big),
$$
the Huang–Slomka–Tkocz–Vritsiou (2021) refinement of the classical $\binom{2n}{n}\, n\ln n$ bound.

**Best result.** General bodies are covered by roughly $4^n$ homothets up to polynomial factors (since $\binom{2n}{n}\approx 4^n/\sqrt{n}$). This is the best *unconditional* bound for all $K$ and all large $n$.

**Barrier.** The volume-ratio method is lossy by an exponential factor: $4^n$ versus the conjectured $2^n$. The extra $\binom{2n}{n}/2^n \approx 2^n$ slack is intrinsic to covering-by-volume and cannot be removed by sharpening the density constant alone. Closing it appears to need a fundamentally non-volumetric idea.

## Belt bodies, zonotopes, and bodies with symmetry

**Core idea.** Boltyanski's *belt bodies* (limits of belt polytopes / zonotopes) admit a structure theory in which illumination is controlled by the body's "belts" of parallel edges. Bodies invariant under large symmetry groups (e.g. $1$-symmetric, or bodies of revolution) inherit covering bounds from their symmetry.

**Best result.** The conjecture is **proved** for zonotopes and zonoids, for belt polytopes, for direct sums and certain Cartesian products, and for bodies with sufficiently rich symmetry; for these classes $c(K) \le 2^n$ holds (often strictly, since the parallelepiped is the unique extremizer). Dekster and others settled bodies of constant width in $\mathbb{R}^3$.

**Barrier.** The methods are class-specific. A general convex body has no belts, no symmetry, and no product structure, so these results, while extensive, do not approach the general case.

## Low-dimensional / topological attacks ($n=3$)

**Core idea.** In $\mathbb{R}^3$ the conjecture predicts $c(K)\le 8$. One attacks it via the structure of the boundary $\partial K$ (a topological $2$-sphere), partitioning it into regions illuminable by a common direction, often using the Gauss map / spherical image of the normal cones.

**Best result.** Verified for many subclasses in $\mathbb{R}^3$: centrally symmetric bodies ($c\le 8$, Lassak), bodies of constant width, bodies of revolution, and polytopes with few vertices or special symmetry. Papadoperakis and others gave bounds for symmetric bodies in $\mathbb{R}^4$.

**Barrier.** The general $\mathbb{R}^3$ case is **still open**. The sphere admits no canonical partition into $8$ illuminable caps for arbitrary normal-cone configurations; constructions with irregular vertices defeat naive partitions, and no topological invariant has been found that forces $8$.

## Fractional and LP-relaxation methods

**Core idea.** Replace exact covering by a *fractional* covering number (an LP relaxation) which is more amenable to duality and concentration-of-measure estimates; then round. Naszódi, Artstein-Avidan, and others developed fractional illumination and used it to recover and improve the $\binom{2n}{n}$-type bounds and to prove sharper results for symmetric bodies.

**Best result.** Fractional methods give the cleanest proofs of the current asymptotic bounds and, for symmetric bodies, can shave logarithmic factors; they also yield stability/quantitative versions for bodies close to the cube.

**Barrier.** The integrality gap between fractional and integer covering numbers can itself be exponential, so even an optimal fractional bound need not deliver $2^n$.

## Equality / stability program

**Core idea.** Even granting an eventual $c(K)\le 2^n$, the conjecture demands *uniqueness*: equality only for parallelepipeds. Stability results aim to show that bodies with $c(K)$ near $2^n$ must be close (in Banach–Mazur distance) to a cube.

**Best result.** For the plane the equality case is classical ($c=4$ only for parallelograms). In higher dimensions, partial rigidity is known for bodies already verified to satisfy the bound (e.g. symmetric bodies), but a general stability theorem is absent. This program is, in a sense, ahead of the existence question and waits on it.
