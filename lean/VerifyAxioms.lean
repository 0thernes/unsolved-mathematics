module

-- SPDX-License-Identifier: MIT
import Solution
import NonVacuity
import Adversarial

/-!
# VerifyAxioms — Explicit `#print axioms` Audit for All 69 Audited Declarations (`v0.5.0`)

45 headline theorems (`Solution.lean`) + 10 non-vacuity witnesses (`NonVacuity.lean`) +
14 adversarial false-variant refutations (`Adversarial.lean`) = 69 declarations.
Every declaration must depend strictly on a subset of `{propext, Classical.choice, Quot.sound}`.
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
#print axioms FormalAtlas.Challenge.thm_collatz_zero_fixed_point
#print axioms FormalAtlas.Challenge.thm_collatz_intercept_nonneg
#print axioms FormalAtlas.Challenge.thm_collatz_parity_word_length
#print axioms FormalAtlas.Challenge.thm_erdos_straus_mordell_840
#print axioms FormalAtlas.Challenge.thm_erdos_straus_multiplicative_closure
#print axioms FormalAtlas.Challenge.thm_erdos_straus_mordell_exceptions_small
#print axioms FormalAtlas.Challenge.thm_erdos_straus_symmetry
#print axioms FormalAtlas.Challenge.thm_erdos_straus_all_le_30
#print axioms FormalAtlas.Challenge.thm_lonely_runner_sharpness_all_n
#print axioms FormalAtlas.Challenge.thm_lonely_runner_n1
#print axioms FormalAtlas.Challenge.thm_lonely_runner_n2
#print axioms FormalAtlas.Challenge.thm_lonely_runner_speed_scaling
#print axioms FormalAtlas.Challenge.thm_lonely_runner_period_shift
#print axioms FormalAtlas.Challenge.thm_lonely_runner_neg_time
#print axioms FormalAtlas.Challenge.thm_lonely_runner_n3_nondiv4
#print axioms FormalAtlas.Challenge.thm_brocard_brown_solutions
#print axioms FormalAtlas.Challenge.thm_brocard_exhaustive_le_12
#print axioms FormalAtlas.Challenge.thm_brocard_mod4_ge_4
#print axioms FormalAtlas.Challenge.thm_brocard_exhaustive_le_15
#print axioms FormalAtlas.Challenge.thm_brocard_not_div3_ge_3
#print axioms FormalAtlas.Challenge.thm_brocard_mod10_ge_5
#print axioms FormalAtlas.Challenge.thm_brocard_exhaustive_le_20
#print axioms FormalAtlas.Challenge.thm_euclid_infinitely_many_primes
#print axioms FormalAtlas.Challenge.thm_arbitrary_prime_gaps
#print axioms FormalAtlas.Challenge.thm_prime_odd_ge_3
#print axioms FormalAtlas.Challenge.thm_twin_prime_mod6
#print axioms FormalAtlas.Challenge.thm_goldbach_even_le_100
#print axioms FormalAtlas.Challenge.thm_goldbach_odd_binary_obstruction
#print axioms FormalAtlas.Challenge.thm_goldbach_binary_fails_at_11
#print axioms FormalAtlas.Challenge.thm_mersenne_exponent_prime
#print axioms FormalAtlas.Challenge.thm_perfect_numbers_first_four
#print axioms FormalAtlas.Challenge.thm_no_odd_perfect_le_100
#print axioms FormalAtlas.Challenge.thm_ramsey_R33_upper
#print axioms FormalAtlas.Challenge.thm_ramsey_R33_lower
#print axioms FormalAtlas.NonVacuity.witness_descent_certificate
#print axioms FormalAtlas.NonVacuity.witness_positivity_localization
#print axioms FormalAtlas.NonVacuity.witness_subcritical_positive_cycle
#print axioms FormalAtlas.NonVacuity.witness_erdos_straus_hypotheses
#print axioms FormalAtlas.NonVacuity.witness_lonely_runner_concrete
#print axioms FormalAtlas.NonVacuity.witness_brocard_non_solution
#print axioms FormalAtlas.NonVacuity.witness_twin_primes_concrete
#print axioms FormalAtlas.NonVacuity.witness_goldbach_100
#print axioms FormalAtlas.NonVacuity.witness_mersenne_31
#print axioms FormalAtlas.NonVacuity.witness_lonely_runner_n3_concrete
#print axioms FormalAtlas.Adversarial.adv_erdos_straus_zero_denom_blocked
#print axioms FormalAtlas.Adversarial.adv_erdos_straus_wrong_witness_refuted
#print axioms FormalAtlas.Adversarial.adv_collatz_no_universal_descent_d1
#print axioms FormalAtlas.Adversarial.adv_collatz_positivity_required_for_no_nontrivial_cycles
#print axioms FormalAtlas.Adversarial.adv_collatz_positivity_converse_false
#print axioms FormalAtlas.Adversarial.adv_lonely_runner_strict_threshold_fails
#print axioms FormalAtlas.Adversarial.adv_lonely_runner_bad_time_refuted
#print axioms FormalAtlas.Adversarial.adv_brocard_false_candidates_refuted
#print axioms FormalAtlas.Adversarial.adv_non_primes_refuted
#print axioms FormalAtlas.Adversarial.adv_mersenne_converse_false
#print axioms FormalAtlas.Adversarial.adv_non_perfect_refuted
#print axioms FormalAtlas.Adversarial.adv_twin_prime_mod6_needs_ge_4
#print axioms FormalAtlas.Adversarial.adv_ramsey_R33_not_le_5
#print axioms FormalAtlas.Adversarial.adv_goldbach_requires_even
