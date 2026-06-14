# Attempts — The Connes Embedding Problem (Resolved 2020)

_Notable attempts, near-misses, retracted proofs._

## The reformulation cascade (the productive "near-misses")

For decades the most consequential work did not attack CEP head-on but *translated* it, each translation a near-miss that brought the answer closer.

- **Kirchberg (1993)** reduced CEP to the QWEP conjecture and a tensor-norm identity. This was widely (and, in retrospect, wrongly) read as evidence that CEP was *true*, because QWEP held in every case anyone could check.
- **Junge–Navascués–Palazuelos–Pérez-García–Scholz–Werner (2011)** and, independently, **Fritz (2011)** proved CEP equivalent to **Tsirelson's problem** ($C_{qa} = C_{qc}$). Many physicists expected the two correlation models to coincide, so this too was often taken as soft evidence *for* embeddability.
- **Ozawa's 2013 survey** "About the QWEP conjecture" consolidated the dictionary and made explicit that a *single* counterexample in any one of these formulations would topple all of them. It framed the eventual mechanism of resolution.

The lesson of the aftermath is that the accumulated intuition pointing toward "true" was a collective near-miss in the opposite direction.

## Slofstra's undecidability results — the decisive crack

William Slofstra (2017–2019) proved that the set of quantum correlations $C_q$ is **not closed** and that natural decision problems about whether systems of equations have finite/infinite-dimensional solutions (via the "embedding theorem" for solution groups of linear-system non-local games) are **undecidable**. These results did not by themselves refute CEP, but they demonstrated that *complexity-theoretic undecidability lives inside the quantum-correlation picture* — the exact ingredient the final proof would exploit. This is the most important true near-miss.

## The resolution (not a disputed claim)

**Ji, Natarajan, Vidick, Wright, Yuen (2020), "MIP* = RE" (arXiv:2001.04383).** The ~165-page proof establishes $\mathrm{MIP}^* = \mathrm{RE}$ and deduces the negative answer to Tsirelson's problem, the QWEP conjecture, and CEP. After intensive scrutiny the result is **accepted by the community**; it received the 2021 ACM Doctoral Dissertation / and broad recognition, and a refereed version appeared (Communications of the ACM exposition, 2021; journal versions subsequently). There is, to current knowledge, **no surviving credible dispute of the main theorem.** The principal caveats raised are about *what kind* of object the proof produces, not whether CEP fails:

- The argument is **non-constructive in the witness**: it proves a separating game/correlation exists without exhibiting an explicit non-hyperlinear group or non-embeddable II$_1$ factor.
- The proof is long and assembles many components (compression, introspection, gap amplification, quantum soundness of low-degree tests); early drafts had gaps that were repaired in revision, and the final argument has been checked by multiple expert groups (Vidick's lecture notes; Coladangelo–Stark and others reworked pieces).

No retracted proof of CEP in either direction is part of the accepted record; the field's posture before 2020 was open-question, not contested-claim.

## Post-resolution attempts at effectiveness

Since 2020 the genuine open *attempt* has been to make the failure explicit: produce a concrete, finitely presented group that is **not hyperlinear**, or a quantitative non-embeddability statement. As of the current frontier no such explicit witness has been published — the existence is known, the construction is not. This is the central unfinished business of the "aftermath."
