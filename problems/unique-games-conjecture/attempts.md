# Attempts — The Unique Games Conjecture

The UGC has not been the subject of widely-publicized *retracted* proofs in the manner of, say, the $P\neq NP$ literature — its difficulty is well-respected and the community is small and expert. The notable events are instead a sequence of deep partial results, surprising algorithmic discoveries that reshaped expectations, and a still-unsettled debate over whether the conjecture is even true.

## The 2-to-2 Games Theorem (the great near-miss)

The most important partial result is the proof of the **2-to-2 Games Theorem** by Subhash Khot, Dor Minzer, and Muli Safra, completed in 2018 after a multi-paper effort begun in 2016. It establishes the NP-hardness of unique games *with imperfect completeness*: distinguishing instances that are $(1/2-\varepsilon)$-satisfiable from those at most $\varepsilon$-satisfiable. This is genuinely "halfway" to UGC, which demands completeness $(1-\varepsilon)$. The proof's engine — the resolution of a conjecture about expansion of non-expanding sets in the **Grassmann graph** — was the missing combinatorial lemma; its proof (Khot–Minzer–Safra, with contributions building on Dinur–Khot–Kindler–Minzer–Safra) was hailed as a major breakthrough. The result immediately improved unconditional Vertex Cover hardness from $1.36$ (Dinur–Safra) toward $\sqrt 2 \approx 1.41$. **Open gap:** lifting completeness from $1/2$ to $1-\varepsilon$ remains unsolved and is not a routine extension.

## The subexponential algorithm (the expectation-shifter)

Arora, Barak, and Steurer's 2010 subexponential ($2^{n^{\varepsilon}}$) algorithm for Unique Games was a near-miss in the *opposite* direction: it was widely read as evidence that the problem might be substantially easier than NP-hard, and for a period it cooled confidence that UGC is true. It did not refute the conjecture — UGC concerns NP-hardness of a gap problem, which subexponential algorithms do not contradict — but it demonstrated that no proof of UGC can produce instances requiring exponential time, sharply constraining the proof space.

## Sum-of-Squares and integrality-gap instances

A recurring research thread has been attempts to *refute* UGC using the Sum-of-Squares (Lasserre) SDP hierarchy. Khot and Vishnoi (2005) constructed integrality-gap instances for Unique Games (and used them to derive an unconditional MAX-CUT integrality gap), instances later studied as candidate hard cases for SoS. Work by Barak, Brandão, Harrow, Kelner, Steurer, and Zhou (2012) showed that the basic SoS algorithm solves several instance families previously believed hard, including subexponential-time guarantees, again nudging expert opinion toward skepticism. No polynomial-round SoS refutation has been found, and no SoS lower bound ruling one out has been proven — the matter is genuinely open.

## The standing of the conjecture

Unusually for a famous conjecture, the community is *divided* on whether UGC is true. Some researchers regard the 2-to-2 theorem as strong evidence for eventual proof; others, citing the subexponential algorithm and SoS progress, suspect it may be false. There is no disputed *claimed proof* to adjudicate; the honest status is an open problem with substantial, carefully-vetted partial progress in both directions and no consensus on the answer.
