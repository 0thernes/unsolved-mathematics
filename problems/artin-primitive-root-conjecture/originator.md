# Originator(s) — Artin's Primitive Root Conjecture

_Biography, background, and the ideas that led here._

## Emil Artin (1898–1962)

Emil Artin was one of the principal architects of twentieth-century algebra and algebraic number theory. Born on **3 March 1898 in Vienna**, he studied at the University of Vienna and then at Leipzig, where he completed his doctorate in **1921** under **Gustav Herglotz** with a thesis on the quadratic function fields over finite fields — already a context where primitive roots, $L$-functions, and an analogue of the Riemann Hypothesis were intertwined. This early work is significant: in his thesis Artin introduced zeta functions for function fields and conjectured the Riemann Hypothesis in that setting (later proved by Hasse and Weil), establishing his lifelong fluency with the interplay between density statements about primes and the analytic behaviour of zeta and $L$-functions. That fluency is precisely the instinct behind the primitive-root conjecture.

Artin spent his most productive years (1923–1937) at the **University of Hamburg**, where, with Hasse, Hecke, and others, he built a research school of extraordinary depth. Forced out of Germany under the Nazi racial laws (his wife Natascha was of partly Jewish descent), he emigrated to the United States in **1937**, holding posts at Notre Dame, Indiana, and from **1946 Princeton University**, before returning to Hamburg in **1958**, where he remained until his death on **20 December 1962**.

## Mathematical background and motivations

Artin's monumental achievements frame the conjecture. He proved the **Artin reciprocity law** (1927) — the central theorem of class field theory, generalizing all earlier reciprocity laws — in the very same year he posed the primitive-root conjecture. He introduced **Artin $L$-functions** and the still-open **Artin conjecture on their holomorphy**, solved **Hilbert's 17th problem** (1927) on positive-definite rational functions as sums of squares, and co-founded the theory of **braids** and the **Artin–Schreier theory** of real fields. With Emmy Noether he reshaped abstract algebra; the modern axiomatic treatment of fields, rings, and Galois theory owes much to his lectures.

The primitive-root conjecture grows directly from this milieu. By 1927 Artin understood that the condition "$a$ is a primitive root mod $p$" is governed by the splitting behaviour of $p$ in the tower of **Kummer extensions** $\mathbb{Q}(\zeta_q, a^{1/q})$: $a$ fails to be a $q$-th power mod $p$ precisely when $p$ does not split completely in $\mathbb{Q}(\zeta_q, a^{1/q})$. The **Chebotarev density theorem** (1922–1926, then very fresh) supplies the density of primes with a given splitting type in each field. Artin's leap was to combine these conditions over all primes $q$ via an inclusion–exclusion / independence heuristic, producing the convergent Euler product now called Artin's constant. The conjecture is thus a quintessential Artin object: a statement about prime densities translated into the language of Galois theory and field extensions, exactly the dictionary he had spent his career building.

## The historical root versus the modern formulation

The *qualitative* statement (infinitely many primes) is the historical root; the *quantitative* density was Artin's own enhancement, communicated to Hasse in 1927. The modern formulation differs in one crucial respect: Artin's initial density product assumed full independence of the local conditions. The **Lehmer computations of 1957** showed this fails for non-generic $a$, and the conjecture was amended to include an explicit **correction factor** (worked out conceptually by Lenstra, Stevenhagen, and Moree decades later). So the conjecture as stated today — density $= c_a \cdot A(a)$ with a rational $c_a$ encoding "entanglement" of the Kummer extensions — is a refinement of Artin's 1927 vision, faithful to his Galois-theoretic strategy but corrected for the arithmetic dependencies he had overlooked.

## Legacy

Artin's broader legacy is the algebraization of number theory; the primitive-root conjecture is a small but emblematic facet of it, illustrating how a sharp analytic prediction can be derived from pure Galois theory. It continues to drive research in analytic number theory nearly a century after he stated it.
