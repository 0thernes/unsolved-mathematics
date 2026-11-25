module

-- SPDX-License-Identifier: MIT
import Solution
import NonVacuity
import Adversarial

/-!
# VerifyAxioms — Explicit `#print axioms` Audit for Every Audited Declaration

Running `lake env lean VerifyAxioms.lean` prints the exact axiom dependency set
of all 22 headline theorems, 6 non-vacuity witnesses, and 8 adversarial false-variant
refutations (36 total declarations). Every declaration must depend ONLY on a subset
of the three standard Lean 4 axioms `[propext, Classical.choice, Quot.sound]`.
-/

#print axioms FormalAtlas.Challenge.thm_collatz_cylinder_affine_law
#print axioms FormalAtlas.Challenge.thm_collatz_exact_intercept_law
#print axioms FormalAtlas.Challenge.thm_terras_parity_word_bijection
#print axioms FormalAtlas.Challenge.thm_collatz_descent_certificate_sound
#print axioms FormalAtlas.Challenge.thm_collatz_no_finite_subcritical_cover
#print axioms FormalAtlas.Challenge.thm_collatz_spine_ladder_identity
#print axioms FormalAtlas.Challenge.thm_collatz_positivity_localization
#print axioms FormalAtlas.Challenge.thm_collatz_epsilon_invariance_barrier
#print axioms FormalAtlas.Challenge.thm_collatz_cycle_equation
#print axioms FormalAtlas.Challenge.thm_collatz_parity_word_append
#print axioms FormalAtlas.Challenge.thm_collatz_negative_cycles
#print axioms FormalAtlas.Challenge.thm_erdos_straus_mordell_840
#print axioms FormalAtlas.Challenge.thm_erdos_straus_multiplicative_closure
#print axioms FormalAtlas.Challenge.thm_erdos_straus_mordell_exceptions_small
#print axioms FormalAtlas.Challenge.thm_lonely_runner_sharpness_all_n
#print axioms FormalAtlas.Challenge.thm_lonely_runner_n1
#print axioms FormalAtlas.Challenge.thm_lonely_runner_n2
#print axioms FormalAtlas.Challenge.thm_lonely_runner_speed_scaling
#print axioms FormalAtlas.Challenge.thm_brocard_brown_solutions
#print axioms FormalAtlas.Challenge.thm_brocard_exhaustive_le_12
#print axioms FormalAtlas.Challenge.thm_brocard_mod4_ge_4
#print axioms FormalAtlas.Challenge.thm_brocard_exhaustive_le_15
#print axioms FormalAtlas.NonVacuity.witness_descent_certificate
#print axioms FormalAtlas.NonVacuity.witness_positivity_localization
#print axioms FormalAtlas.NonVacuity.witness_subcritical_positive_cycle
#print axioms FormalAtlas.NonVacuity.witness_erdos_straus_hypotheses
#print axioms FormalAtlas.NonVacuity.witness_lonely_runner_concrete
#print axioms FormalAtlas.NonVacuity.witness_brocard_non_solution
#print axioms FormalAtlas.Adversarial.adv_erdos_straus_zero_denom_blocked
#print axioms FormalAtlas.Adversarial.adv_erdos_straus_wrong_witness_refuted
#print axioms FormalAtlas.Adversarial.adv_collatz_no_universal_descent_d1
#print axioms FormalAtlas.Adversarial.adv_collatz_positivity_required_for_no_nontrivial_cycles
#print axioms FormalAtlas.Adversarial.adv_collatz_positivity_converse_false
#print axioms FormalAtlas.Adversarial.adv_lonely_runner_strict_threshold_fails
#print axioms FormalAtlas.Adversarial.adv_lonely_runner_bad_time_refuted
#print axioms FormalAtlas.Adversarial.adv_brocard_false_candidates_refuted
