# History — Köthe's Conjecture

Köthe's conjecture sits at the heart of the radical theory of associative (generally noncommutative) rings. It concerns the behavior of *nil* one-sided ideals — ideals every element of which is nilpotent — and asks whether nilness, a fundamentally element-wise (and one-sided) notion, can be tracked by a well-behaved two-sided radical.

## Origin and formulation

In 1930 Gottfried Köthe, in *"Die Struktur der Ringe, deren Restklassenring nach dem Radikal vollständige Matrizenringe ist"* (Math. Z. **32** (1930), 161–186), conjectured that a ring with no nonzero nil two-sided ideal also has no nonzero nil one-sided ideal. Equivalently, the *upper nil radical* $\mathrm{Nil}^*(R)$ (the sum of all nil two-sided ideals, also called the Köthe radical or the sum of nilpotent ideals' nil analogue) should contain every nil one-sided ideal.

Over the following decades several equivalent reformulations were isolated, which is part of what makes the problem so resilient:

- **(Sum form.)** The sum of two nil left ideals of any ring is nil.
- **(Matrix form, Krempa 1972.)** For every nil ring $R$, the matrix ring $M_n(R)$ is nil (it suffices to take $n=2$); equivalently the polynomial ring $R[x]$ over a nil ring is Jacobson radical.
- **(Radical form.)** The upper nil radical $\mathrm{Nil}^*$ contains every nil right ideal, i.e. $\mathrm{Nil}^*(R)$ equals the *Levitzki-type* sum of all nil one-sided ideals.
- **(Amitsur form.)** Connections to whether $R[x]$ nil implies $R$ nil (Amitsur's problem), resolved separately, and to the question of whether nilness passes to polynomial extensions.

Because the lower nil radical (the prime radical, $\mathrm{Nil}_*$) and the upper nil radical generally differ, and because the Jacobson radical contains $\mathrm{Nil}^*$ but can be strictly larger, the conjecture is precisely a statement that one-sidedness does not generate "extra" nilness beyond the two-sided radical.

## Timeline

**1930** — Gottfried Köthe poses the conjecture in *Mathematische Zeitschrift*, asking whether a nil one-sided ideal must lie in a nil two-sided ideal.

**1945** — Jacob Levitzki introduces the locally nilpotent radical (Levitzki radical), clarifying the hierarchy of nil-type radicals around the conjecture.

**1951–1956** — S. A. Amitsur develops radical theory of polynomial rings; his work on $R[x]$ ties Köthe's question to nilness of polynomial extensions.

**1964** — Amitsur proves that the Jacobson radical of $R[x]$ is $N[x]$ for a nil ideal $N$, sharpening the link between Köthe's conjecture and Jacobson-radical questions over $R[x]$.

**1972** — Jan Krempa gives the influential equivalent reformulations: Köthe's conjecture holds iff $M_2(R)$ is nil for every nil ring $R$, iff $R[x]$ is Jacobson radical for every nil $R$.

**1973** — Efim Zelmanov and others examine PI and special classes; the conjecture is confirmed for rings satisfying a polynomial identity (PI-rings), via Levitzki/Amitsur–Levitzki type results.

**1989** — Confirmed for rings over uncountable fields and various countability/cardinality-restricted settings; algebras over uncountable fields are tractable through Amitsur's "nil implies nilpotent of bounded index" heuristics in special cases.

**2000** — A. Smoktunowicz constructs a simple nil ring (a nil algebra that is also simple — though not unital), reshaping intuitions about how wild nil rings can be and bearing on the matrix reformulation.

**2007–2008** — Smoktunowicz and others study nil polynomial rings; results on $R[x]$ and nil rings keep the matrix/polynomial reformulations central to the frontier.

**2012** — Smoktunowicz's survey-level work and constructions of nil rings with unexpected properties (e.g. nil rings $R$ with $R[x]$ not nil) clarify exactly which naïve strengthenings of the conjecture are false.

**Present** — The conjecture remains **open** in full generality. It is established for PI-rings, rings with right Krull dimension, algebras over uncountable fields, and several other classes, but the general associative case is unresolved, with the $M_2$/polynomial reformulations the most actively probed routes.
