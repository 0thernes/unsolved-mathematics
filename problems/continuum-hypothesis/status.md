# Status & Frontier — The Continuum Hypothesis

_Where the problem stands and what a resolution would require._

**Status: independent of ZFC, and that independence is itself a theorem.** The Continuum Hypothesis can neither be proved nor refuted from the Zermelo–Fraenkel axioms with Choice. This is established by two complementary results that must be cited precisely:

- **Gödel (1938–40).** The constructible universe $L$ is an inner model of ZFC in which the Generalized Continuum Hypothesis holds. Hence $\mathrm{Con}(\mathrm{ZFC}) \Rightarrow \mathrm{Con}(\mathrm{ZFC}+\mathrm{CH})$ — CH cannot be refuted in ZFC. (Gödel, *The Consistency of the Continuum Hypothesis*, Annals of Mathematics Studies 3, 1940; announced PNAS 1938, DOI 10.1073/pnas.24.12.556.)
- **Cohen (1963).** Forcing adjoins generic reals to a ground model, producing a model of ZFC with $2^{\aleph_0}\ge\aleph_2$. Hence $\mathrm{Con}(\mathrm{ZFC}) \Rightarrow \mathrm{Con}(\mathrm{ZFC}+\neg\mathrm{CH})$ — CH cannot be proved in ZFC. (Cohen, "The Independence of the Continuum Hypothesis," PNAS 1963/64, DOIs 10.1073/pnas.50.6.1143 and 10.1073/pnas.51.1.105.)

Together: CH is **formally undecided** by ZFC. This is not a gap in our knowledge of a ZFC-provable fact; it is a proven limitation of the axiom system.

**What is known unconditionally.** The only ZFC constraint on the size of the continuum is König's theorem: $\mathrm{cf}(2^{\aleph_0})>\aleph_0$, so $2^{\aleph_0}$ has uncountable cofinality (ruling out, e.g., $\mathfrak{c}=\aleph_\omega$). By Easton's theorem, the function $\kappa\mapsto 2^\kappa$ on regular cardinals is otherwise almost unconstrained. For **definable** sets CH holds: analytic sets have the perfect-set property (Suslin), so an uncountable analytic set has size $\mathfrak{c}$; under projective determinacy (which follows from infinitely many Woodin cardinals) this extends to all projective sets. Crucially, **no large-cardinal axiom decides CH**, since large cardinals are preserved by the small forcings that flip CH — this is the central barrier.

**Strongest conditional results.** Two principled programs reach opposite verdicts.
- *Toward $\neg$CH ($\mathfrak{c}=\aleph_2$):* Strong forcing axioms — PFA and Martin's Maximum (Foreman–Magidor–Shelah, 1988) — imply $2^{\aleph_0}=\aleph_2$. The Asperó–Schindler theorem, $\mathrm{MM}^{++}\Rightarrow(*)$ (Annals of Mathematics, 2021, DOI 10.4007/annals.2021.193.3.3), unifies Martin's Maximum with Woodin's axiom $(*)$, both giving $\mathfrak{c}=\aleph_2$, and is the strongest recent evidence on this side.
- *Toward CH:* Woodin's **Ultimate-$L$** program seeks a canonical inner model absorbing all large cardinals; the axiom $V=\text{Ultimate-}L$ would imply GCH (hence CH) while remaining compatible with supercompact cardinals.

**What a full resolution would require.** Since ZFC is settled (undecided), resolution means adopting a new axiom that is both (i) mathematically decisive on CH and (ii) justified as *true* of the intended universe of sets — by intrinsic plausibility, by structural fruitfulness, or by generic absoluteness. The $\neg$CH route needs the forcing-axiom/$(*)$ framework accepted as canonical; the CH route needs Ultimate-$L$ actually constructed, which in turn requires solving the inner-model problem at the level of supercompact cardinals — currently open. A third position, Hamkins's set-theoretic multiverse, holds that CH is already "answered" by the plurality of universes and has no single truth value; this remains contested.

**Plausible routes.** (1) Complete the inner-model program to build Ultimate-$L$, vindicating CH. (2) Establish the $\Omega$-conjecture and the canonicity of strong forcing axioms, vindicating $\mathfrak{c}=\aleph_2$. (3) A decisive philosophical case for the multiverse view, dissolving the question. No route is near completion; the problem is open in the modern sense of "which axioms, if any, are true," not in the classical sense of "provable in ZFC."

## Related problems

- [Riemann Hypothesis](../riemann-hypothesis/README.md)
- [P versus NP](../p-versus-np/README.md)
- [Invariant Subspace Problem](../invariant-subspace-problem/README.md)
- [Hadwiger–Nelson Problem](../hadwiger-nelson-problem/README.md)
