# History — The Littlewood Conjecture

_Origin, formulation, and timeline._

## How the problem arose

The Littlewood conjecture grew out of the theory of *simultaneous Diophantine approximation*, the study of how well a tuple of real numbers can be approximated by rationals with a common denominator. For a single irrational $\alpha$, classical theory is complete: by the theory of continued fractions, the one-dimensional analogue $\liminf_{n\to\infty} n\,\lVert n\alpha\rVert$ is positive precisely for badly approximable $\alpha$ (those of bounded partial quotients), and the supremum of these values is governed by the Markov spectrum. The Littlewood problem asks what happens when *two* numbers must be approximated at once and the two errors are allowed to compensate one another multiplicatively.

The precise statement is: for **all** real $\alpha,\beta$,
$$\liminf_{n\to\infty} \; n \,\lVert n\alpha\rVert\,\lVert n\beta\rVert = 0,$$
where $\lVert x\rVert$ denotes the distance from $x$ to the nearest integer. The conjecture is trivial unless both $\alpha$ and $\beta$ are *badly approximable*, since if either has unbounded partial quotients the corresponding factor can be driven to $0$ faster than $n$ grows. So the genuine content concerns pairs of badly approximable numbers — a set of measure zero but uncountable. J. E. Littlewood is reported to have posed it around 1930 in Cambridge; it circulated informally for years before appearing in print.

A productive reformulation comes from **homogeneous dynamics**. Cassels and Swinnerton-Dyer recast the question in terms of products of linear forms and orbits in the space of unimodular lattices $\mathrm{SL}_3(\mathbb{R})/\mathrm{SL}_3(\mathbb{Z})$. A counterexample pair $(\alpha,\beta)$ corresponds to a lattice whose orbit under the full diagonal subgroup $A$ is **bounded** (stays in a compact set) and stays away from where the product of coordinates vanishes. Thus Littlewood becomes a statement that certain diagonal orbits cannot be bounded — a question about *measure rigidity* and *topological rigidity* of higher-rank torus actions.

## Timeline

- **c. 1930** — J. E. Littlewood poses the conjecture in Cambridge; it spreads by word of mouth.
- **1955** — J. W. S. Cassels and H. P. F. Swinnerton-Dyer connect the conjecture to products of three linear forms and the geometry of lattices, proving results conditional on a lattice-rigidity hypothesis and reframing the problem dynamically.
- **1962** — B. F. Davenport and others develop the metric and structural theory of badly approximable pairs; the difficulty of the badly-approximable case becomes the recognized obstacle.
- **1970s–1980s** — G. A. Margulis's work on rigidity of higher-rank lattices and unipotent flows builds the dynamical machinery (later Ratner's theorems) that will be brought to bear; Margulis explicitly proposes that conjectures of Littlewood type follow from rigidity of diagonal actions.
- **1986** — M. Pollicott, and separately the broader ergodic-theory community, sharpen the dynamical dictionary between bounded $A$-orbits and Diophantine exceptionality.
- **2000** — D. Y. Kleinbock and G. A. Margulis prove flows-to-infinity and logarithm-law results clarifying the dynamics of the diagonal action relevant to Littlewood.
- **2003** — Pollington and Velani give explicit constructions and metric refinements; the set of potential counterexamples is shown to be very thin.
- **2006** — **Breakthrough.** M. Einsiedler, A. Katok, and E. Lindenstrauss prove that the set of exceptions to the Littlewood conjecture has *Hausdorff dimension zero* (in fact is a countable union of compact sets of dimension zero). Almost every pair satisfies it, and the exceptional set is provably tiny — but possibly nonempty.
- **2007–2011** — Refinements (Einsiedler–Lindenstrauss, Venkatesh, and others) extend the measure-classification techniques; the *$p$-adic* and function-field analogues are attacked.
- **2010s** — Adiceam, Bugeaud, Badziahin, Velani and collaborators pursue the *mixed Littlewood conjecture* (de Mathan–Teulié) and inhomogeneous variants; counterexamples are found for some mixed/$p$-adic versions, sharpening intuition about why the original resists.
- **Present** — The conjecture remains **open**. The EKL theorem is the strongest unconditional result; full resolution is believed to require either a complete classification of bounded diagonal orbits or a genuinely new analytic input.

The two threads — continued fractions / explicit number theory on one side, ergodic theory of group actions on the other — define the modern landscape and explain why the problem sits at the boundary of number theory and homogeneous dynamics.
