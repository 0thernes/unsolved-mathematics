# Attempts — The Zariski Cancellation Problem

_Notable attempts, near-misses, retracted proofs._

## The dimension ladder: confirmed positive cases

The earliest decisive progress was the **$n=1$ case** of Abhyankar, Eakin, and Heinzer (1972): any affine algebra $A$ over a field with $A^{[1]}$ a polynomial ring in two variables, and $A$ of dimension one, must itself be a polynomial ring — equivalently, a curve cannot be "cancelled" wrongly. This established the line as rigid.

The major near-classical triumph is the **surface case** in characteristic zero. Fujita (1979), and Miyanishi–Sugie (1980), proved that $X\times\mathbb{A}^1\cong\mathbb{A}^3$ implies $X\cong\mathbb{A}^2$ over a field of characteristic $0$. Russell and others extended the surface result toward positive characteristic. These results were not retracted and remain the firm lower rungs of the ladder; the obstruction to climbing higher is the absence of a threefold classification analogous to Miyanishi's surface theory.

## The Russell cubic: a famous near-miss that taught the right invariant

For years the **Russell cubic threefold** $V=\{x+x^2y+z^2+t^3=0\}\subset\mathbb{A}^4$ was a leading candidate to either be a new copy of $\mathbb{A}^3$ or a counterexample-adjacent object. It is smooth, contractible, factorial, with trivial Picard group — homologically indistinguishable from $\mathbb{A}^3$. Several heuristic arguments that it *was* $\mathbb{A}^3$ circulated informally. **Makar-Limanov (1996)** resolved this decisively in the negative: by computing $\mathrm{ML}(V)\ne k$ (the variable $x$ lies in the kernel of every locally nilpotent derivation) he proved $V\not\cong\mathbb{A}^3$. The Russell cubic is therefore an *exotic* contractible threefold, not a counterexample to cancellation — but the episode produced the Makar-Limanov invariant, the very tool that later cracked the positive-characteristic problem. Kaliman–Makar-Limanov (1997) and Crachiola (2005, char-$p$ refinement) consolidated these computations.

## The positive-characteristic resolution (not a dispute, a theorem)

**Neena Gupta's 2014 theorem** is the headline result: ZCP is *false* in characteristic $p>0$ for $n\ge 3$. Building on Asanuma's 1987 deformation threefolds, she exhibited an explicit $A$ with $A^{[1]}\cong k^{[n+1]}$ but $A\not\cong k^{[n]}$, computing a characteristic-$p$ Makar-Limanov-type invariant to separate $A$ from affine space. The work was published in *Inventiones Mathematicae* and *Compositio* and is broadly accepted; it won the 2014 Ramanujan Prize and the 2021 INSA Young Scientist recognition. No serious objection has been raised — this is settled mathematics for char $p$, $\dim\ge 3$.

## Status of claimed characteristic-zero resolutions

As of the present writing the **characteristic-zero problem for $n\ge 3$ remains open**, and no widely accepted proof — positive or negative — exists. Periodic preprints announcing either a char-$0$ counterexample (typically a Koras–Russell- or Asanuma-type construction) or a proof of char-$0$ cancellation have appeared; in each case the community's consensus has been that the argument either reduces to the already-handled cases, or that the proposed invariant fails to distinguish the candidate from $\mathbb{A}^3$ (mirroring the lesson of the Russell cubic, whose ML invariant in char $0$ is non-trivial only because it is *not* a cylinder base). Readers should treat any announced char-$0$ resolution as **unverified** until vetted; the foundational obstruction — that all known char-$0$ candidates with the cylinder property have trivial ML invariant — has not been overcome. The honest summary: the threefold cancellation question in characteristic zero is genuinely unsolved.
