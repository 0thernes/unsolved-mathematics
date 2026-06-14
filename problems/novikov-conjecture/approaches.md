# Approaches — The Novikov Conjecture

_Major strategies, partial results, and barriers._

The Novikov Conjecture is equivalent to the **rational injectivity of the assembly map** in $L$-theory, and (by the Mishchenko–Kasparov dictionary) is implied by rational injectivity of the Baum–Connes assembly map in $C^*$-algebra $K$-theory. Almost every line of attack proves injectivity of an assembly or index map for some class of groups. There is no known counterexample; the difficulty is uniformity across *all* discrete groups.

## Dirac–dual-Dirac method ($KK$-theory)

The dominant analytic strategy, due to Mishchenko and especially **Kasparov**, builds a "$\gamma$-element" in equivariant $KK$-theory. One constructs a Dirac operator along a $\pi$-equivariant proper metric space (e.g. a complete non-positively curved manifold on which $\pi$ acts) and a dual-Dirac element; their product $\gamma \in KK^\pi(\mathbb{C},\mathbb{C})$, when it equals $1$, forces the assembly map to be an isomorphism (Baum–Connes), and weaker statements give Novikov. **Best result:** Kasparov proved Novikov for all closed subgroups of connected Lie groups and for fundamental groups of complete non-positively curved manifolds; Connes–Gromov–Moscovici and Kasparov–Skandalis extended this to hyperbolic groups and groups acting on bolic spaces / buildings. **Barrier:** the construction needs a contractible space with controlled curvature ("bolicity") on which the group acts amenably at infinity; groups with **property (T)** can have $\gamma \neq 1$, obstructing the strong (Baum–Connes) form — though Novikov itself often survives.

## Coarse geometry and embeddings into Hilbert space

Reframing the problem via the coarse Baum–Connes conjecture, **Guoliang Yu** showed that the large-scale geometry of $|\pi|$ (as a metric space) controls injectivity. **Best result:** Yu proved the Novikov Conjecture for every group that **coarsely embeds into Hilbert space**, and earlier for groups of **finite asymptotic dimension**. This is the single most general unconditional theorem, covering linear groups (Guentner–Higson–Weinberger), amenable groups, hyperbolic groups, and many more. **Barrier:** **Gromov's random/monster groups** contain expanders and therefore do *not* coarsely embed into Hilbert space, so this method cannot reach all groups. Whether monster groups satisfy Novikov is open; they are the canonical test case where the Hilbert-space toolkit fails.

## Surgery theory and controlled/bounded topology

The original topological route works directly with the $L$-theory assembly map and Wall surgery groups. **Carlsson–Pedersen**, **Ferry–Weinberger**, and **Quinn** used controlled and bounded topology to prove integral injectivity (split injectivity) of the assembly map for groups with finite $B\pi$ admitting suitable compactifications. **Best result:** split injectivity of the $L$- and $K$-theory assembly maps for groups $\pi$ whose classifying space has a "nice" (e.g. $\mathcal{Z}$-set, or finite asymptotic dimension) compactification of $E\pi$. **Barrier:** requires geometric control on $B\pi$ at infinity that is unavailable for general groups; does not by itself handle groups with bad-large-scale geometry.

## The Farrell–Jones Conjecture

The Farrell–Jones Conjecture (FJC) computes the full $K$- and $L$-theory of $\mathbb{Z}\pi$ via assembly over the family of virtually cyclic subgroups; it **implies** the Novikov Conjecture (and the Borel rigidity conjecture). The **Bartels–Lück–Reich** program proved FJC using controlled topology plus flow-space dynamics. **Best result:** FJC (hence Novikov) for hyperbolic groups, CAT(0) groups, virtually solvable groups, mapping class groups, $\mathrm{GL}_n(\mathbb{Z})$ and lattices in Lie groups, and groups acting on suitable spaces — proved through "transfer reducibility" and finitely-$\mathcal F$-amenable actions. **Barrier:** the method requires a geometric action on a finite-dimensional space with good flow dynamics; it is not known to be closed under all the operations needed to reach arbitrary groups, and property-(T) lattices required substantial extra work.

## Cyclic cohomology and the Connes–Moscovici higher index theorem

For a group cocycle of polynomial/bounded growth, **Connes–Moscovici** pair the higher signature against a cyclic cocycle on a smooth dense subalgebra of $C^*_r\pi$, proving homotopy invariance of the corresponding higher signature. **Best result:** Novikov for all cohomology classes of $B\pi$ coming from **bounded** (e.g. Gromov-norm-finite) cocycles, hence for hyperbolic groups and groups of polynomial growth. **Barrier:** unbounded cohomology classes resist the analytic smoothing; controlling the relevant Banach-algebra completions for general groups is the obstruction.

## Descent and split injectivity via assembly

A unifying meta-strategy (Carlsson, Weiss–Williams, the isomorphism-conjecture framework) is to prove **split injectivity** of assembly with respect to a sufficiently large family, using descent from a known equivariant homology theory. **Best result:** general "going-down/induction" theorems that combine the above special cases. **Barrier:** the same fundamental obstacle — there is no known construction producing the required equivariant compactification or coarse embedding for *every* group, and expander-based monster groups remain outside reach. No barrier theorem rules out Novikov, but several rule out specific methods (e.g. Higson–Lafforgue–Skandalis counterexamples to Baum–Connes *with coefficients*).
