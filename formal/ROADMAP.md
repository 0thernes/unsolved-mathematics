# Formalization Roadmap

Scope: trust infrastructure for the Collatz repository. This roadmap does not claim novelty and does not claim any progress on the Collatz conjecture itself.

## Formalize First

1. Shortcut map definitions.
2. Parity words and prefix cylinders.
3. Cylinder affine law.
4. Terras parity-word bijection.
5. Descent certificate criterion.
6. No finite 2-adic cover via the all-ones path and the fixed point `-1`.
7. Spine ladder identity.
8. Positivity localization for supercritical spines.
9. Exact cycle product identity.
10. Crude continued-fraction lower-bound derivation for nontrivial cycles.

## Proof Assistant Targets

The first pass should be boring and small:

- integer parity lemmas;
- affine iteration under a fixed parity word;
- residue uniqueness modulo `2^d`;
- exact inequalities for descent certificates;
- rational fixed points with odd denominators.

Only after those are stable should the repo attempt larger certificate-generation or proof-by-reflection work.

## Non-Goals

- No formal proof of Collatz is implied.
- No infinite regeneration theorem is currently formalized.
- No stochastic or fitted-model result counts as proof.

## Artifact Requirements

Every formal artifact should include:

- source theorem statement;
- corresponding informal repo statement;
- checker command;
- generated proof/certificate files if any;
- known assumptions and remaining gaps.

