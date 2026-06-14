# Originator(s) — The Eilenberg–Ganea Conjecture

_Biography, background, and the ideas that led here._

## Samuel Eilenberg (1913–1998)

Samuel Eilenberg was born in Warsaw and trained in the Polish mathematical school, completing his doctorate at the University of Warsaw in 1936 under Kazimierz Kuratowski and Karol Borsuk, with early work in set-theoretic topology and the topology of the plane. Emigrating to the United States in 1939 as the situation in Europe darkened, he held positions at the University of Michigan and then, for most of his career, at Columbia University.

Eilenberg is one of the principal architects of twentieth-century algebraic topology and the co-founder, with Saunders Mac Lane, of **category theory** (their 1945 paper "General theory of natural equivalences" introduced functors and natural transformations). With Mac Lane he also introduced **Eilenberg–MacLane spaces** $K(\pi,n)$ and laid the foundations of the **cohomology of groups**, the exact setting in which cohomological and geometric dimension live. With Norman Steenrod he wrote *Foundations of Algebraic Topology* (1952), axiomatizing homology theory. Later, under the collective pseudonym (and partly as himself), he helped shape homological algebra; his book with Henri Cartan, *Homological Algebra* (1956), is the canonical reference for the projective dimensions that define $\operatorname{cd}(G)$. He was also a celebrated collector of Asian art. Eilenberg received the Wolf Prize in 1986.

The Eilenberg–Ganea question is a natural outgrowth of his program: having built the machinery to measure groups by the cohomological dimension of $\mathbb{Z}G$-resolutions, one asks whether that purely algebraic measure is always realized geometrically by a complex of the same dimension. Eilenberg's instinct throughout his career was that good algebraic invariants should have clean geometric meaning — the conjecture is the one place in the dimension dictionary where that principle remains unverified.

## Tudor Ganea (1922–1971)

Tudor Ganea was a Romanian-born topologist, educated in Bucharest, who worked at the Institute of Mathematics of the Romanian Academy before emigrating; he spent his later years in the United States, ultimately at the University of Washington in Seattle. He is best known for foundational contributions to **homotopy theory and Lusternik–Schnirelmann (LS) category**: the *Ganea conjecture* on the LS-category of products, the *Ganea fibration* and *Ganea construction*, and a body of work on the homotopy of suspensions and joins.

The 1957 collaboration sits precisely at the meeting point of the two men's interests. The LS-category of a group (equivalently of its $K(G,1)$) and the geometric dimension are companion invariants, and the Eilenberg–Ganea theorem is often stated in the joint language of category and dimension. Ganea's facility with cell structures, joins, and the manipulation of CW models supplied the constructive side; Eilenberg's homological framework supplied the invariants. Ganea died young, in 1971, but his name remains attached to several live problems in homotopy theory in addition to this one.

## The idea behind the conjecture

The motivating principle is **dimensional rigidity**: for an aspherical space, homotopy type is determined by $\pi_1$, so $\operatorname{gd}(G)$ asks for the most economical model and $\operatorname{cd}(G)$ gives an algebraic lower bound. Eilenberg and Ganea proved these agree above dimension $2$ by an explicit cell-attachment argument: given a resolution of length $n\ge 3$, one builds a $K(G,1)$ of dimension $n$ by killing higher homotopy with cells of the right dimension, using the freedom that exists when $n\ge 3$. The argument breaks at $n=2$ because attaching $3$-cells to kill $\pi_2$ may be unavoidable even when $\operatorname{cd}=2$, since a projective (but possibly non-free) module of relations can obstruct a $2$-dimensional geometric realization. Closing that gap — proving the obstruction never bites, or constructing a group where it does — is the whole conjecture, and remains open more than six decades later.
