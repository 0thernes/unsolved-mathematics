module

import Solution
import NonVacuity

/-!
# VerifyAxioms — Explicit `#print axioms` Audit for Every Headline Theorem

Running `lake env lean VerifyAxioms.lean` prints the exact axiom dependency set
of every exported theorem. Every theorem must depend ONLY on a subset of the
three standard Lean 4 axioms `[propext, Classical.choice, Quot.sound]`.
-/

#print axioms FormalAtlas.Challenge.thm_collatz_cylinder_affine_law
#print axioms FormalAtlas.Challenge.thm_collatz_exact_intercept_law
#print axioms FormalAtlas.Challenge.thm_terras_parity_word_bijection
#print axioms FormalAtlas.Challenge.thm_collatz_descent_certificate_sound
#print axioms FormalAtlas.Challenge.thm_collatz_no_finite_subcritical_cover
#print axioms FormalAtlas.Challenge.thm_collatz_spine_ladder_identity
#print axioms FormalAtlas.Challenge.thm_collatz_positivity_localization
#print axioms FormalAtlas.Challenge.thm_collatz_epsilon_invariance_barrier
#print axioms FormalAtlas.Challenge.thm_erdos_straus_mordell_840
#print axioms FormalAtlas.Challenge.thm_lonely_runner_sharpness_all_n
#print axioms FormalAtlas.Challenge.thm_lonely_runner_n1
#print axioms FormalAtlas.Challenge.thm_lonely_runner_n2
#print axioms FormalAtlas.Challenge.thm_brocard_brown_solutions
#print axioms FormalAtlas.Challenge.thm_brocard_exhaustive_le_12
#print axioms FormalAtlas.NonVacuity.witness_descent_certificate
#print axioms FormalAtlas.NonVacuity.witness_positivity_localization
#print axioms FormalAtlas.NonVacuity.witness_erdos_straus_hypotheses
#print axioms FormalAtlas.NonVacuity.witness_lonely_runner_concrete
