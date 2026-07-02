# Unverified / Refuted Proof Claims — Quarantine

Files in this directory claim or imply a resolution of the Collatz Conjecture.
**None has survived verification. The conjecture is OPEN.** They are preserved
(not deleted) for the record; do not cite them, chunk them into the RAG
corpus, or move them back without a written verification trail.

Refutation summaries live in `../AUDIT-REGISTER.md` ("Proof-claim artifacts").
Current inventory and one-line diagnoses:

- `P13-REAL-CF-K-BOUND-FORCING.md` — Kolmogorov/Berry-paradox misuse: asserts a
  counterexample would need description cost exceeding the repo's own byte
  size, "contradiction." No such theorem exists; integers are not bounded by
  the complexity of documents about them. (Its opening frontier facts are
  correct — they are copied from the verified dossier.)
- `defect_algebra_contraction_proof.md` — declares "closes the conjecture for
  positives" from ‖A‖∞ = 0.92 < 1 for a 4×4 matrix *empirically fitted* by
  `defect_algebra.py`. A fitted linear model's contraction is not a theorem
  about the true dynamics; the injection-boundedness step is circular; the
  claimed bound τ(n) ≤ 11.2·bitlen(n) is an empirical maximum relabeled as
  proved.

Added later on 2026-07-01 (same fitted-matrix / Kolmogorov-misuse families,
all sharing the refuted defect-algebra load-bearing step or the P13 schema):
`P14-CODEX-INCOMPLETENESS-K-BOUND.md`, `collatz_full_algebraic_proof.md`
("Core claim: No positive integer is a counterexample" — chains honest repo
reductions onto the unproved fitted-matrix stopping-time bound, so the chain
fails at that link), `collatz_defect_theorem.md`,
`defect_algebra_contraction_lemma.md`, `defect_algebra_lemma.md`,
`defect_ultrametric.md`, `11.8_MASTER_THEOREM.md`,
`defect_algebra_formal_proof.md`. Note: the fitted matrix A with
‖A‖∞ = 0.92 < 1 describes a linear *regression on sampled orbits*; no theorem
connects its contraction to the true nonlinear dynamics, and the
injection-boundedness step assumes the escape it purports to prove.

An earlier ~25-file family of prompt-as-axiom documents
(`THE-PROMPT-IS-THE-PROOF.md` and the `P-*` series, deposited and removed
2026-07-01) is diagnosed in the audit register; its mechanistic core was
refuted by `kick_repulsion_claim_audit.py` (199 counterexamples).
