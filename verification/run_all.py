"""Finite checks for the parity-block search law."""

import itertools
import math
import unittest
from collections import Counter
from fractions import Fraction

import numpy as np


SIGNS = (-1, 1)


def sign_words(length):
    return itertools.product(SIGNS, repeat=length)


def block_probability(signs, kappa):
    return (1 + kappa * math.prod(signs)) / (2 ** len(signs))


def favored_words(length, preferred_parity):
    return tuple(word for word in sign_words(length) if math.prod(word) == preferred_parity)


def mean_mark_probability(theta, words, diffusion):
    """Enumerate oracle words using actual two-dimensional orthogonal matrices."""
    uniform = np.array([math.sin(theta), math.cos(theta)])
    reflector = 2 * np.outer(uniform, uniform) - np.eye(2)
    results = []
    for signs in words:
        state = uniform.copy()
        for active_sign, diffuse in zip(signs, diffusion, strict=True):
            if active_sign == 1:
                state[0] *= -1
            if diffuse:
                state = reflector @ state
        results.append(state[0] ** 2)
    return math.fsum(results) / len(results)


def lengths_at_offset(length, full_trial_length, first_slot):
    """Sizes of the proper prefix and suffix and the count of complete blocks."""
    prefix_length = (-first_slot) % length
    complete_blocks, suffix_length = divmod(full_trial_length - prefix_length, length)
    return prefix_length, complete_blocks, suffix_length


def hidden_offset_probability(theta, length, trial_length, first_slot, diffuse):
    """Closed form conditional on the full blocks having preferred parity."""
    prefix, complete_blocks, suffix = lengths_at_offset(length, trial_length, first_slot)
    prefix_last = int(diffuse[prefix - 1]) if prefix else 0
    suffix_last = int(diffuse[-1]) if suffix else 0
    prefix_parities = SIGNS if prefix else (1,)
    suffix_parities = SIGNS if suffix else (1,)
    complete_drift = complete_blocks * diffuse[prefix + length - 1]
    random_drift_count = sum(diffuse) - prefix_last - suffix_last - complete_drift
    attenuation = math.cos(4 * theta) ** random_drift_count
    conditional_probabilities = []
    for prefix_parity, suffix_parity in itertools.product(prefix_parities, suffix_parities):
        mean_multiple = (
            2 * suffix_last
            + suffix_parity * prefix_parity
            + 2 * suffix_parity * (prefix_last + complete_drift)
        )
        conditional_probabilities.append((1 - math.cos(2 * theta * mean_multiple) * attenuation) / 2)
    return math.fsum(conditional_probabilities) / len(conditional_probabilities)


def operator_product(factors):
    size = factors[0].shape[0]
    result = np.eye(size, dtype=complex)
    for factor in factors:
        result = factor @ result
    return result


def pure_block_component(projectors, kappa):
    """The two product terms in the mean unitary of a block."""
    identity = np.eye(projectors[0].shape[0])
    project_complement = operator_product([identity - projector for projector in projectors])
    project_mark = operator_product(projectors)
    return project_complement + (-1) ** len(projectors) * kappa * project_mark


def enumerate_block_unitaries(projectors, kappa):
    identity = np.eye(projectors[0].shape[0])
    reflections = [identity - 2 * projector for projector in projectors]
    for signs in sign_words(len(projectors)):
        probability = block_probability(signs, kappa)
        factors = [
            reflection if sign == 1 else identity
            for reflection, sign in zip(reflections, signs, strict=True)
        ]
        yield probability, operator_product(factors)


def unit_vector(rng, dimension):
    raw = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
    return raw / np.linalg.norm(raw)


def mark_projectors(rng, dimension, marks, length):
    """Make jointly orthogonal rank-one mark projectors in independent slot frames."""
    frames = []
    for _ in range(length):
        raw = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(size=(dimension, dimension))
        columns, _ = np.linalg.qr(raw)
        frames.append([np.outer(column, column.conj()) for column in columns.T[:marks]])
    return tuple(zip(*frames, strict=True))


class BlockLawChecks(unittest.TestCase):
    def test_proper_marginals_and_full_parity(self):
        for length in range(3, 8):
            for kappa in map(Fraction, (-1, "-3/5", 0, "2/7", 1)):
                with self.subTest(length=length, kappa=kappa):
                    probabilities = {word: block_probability(word, kappa) for word in sign_words(length)}
                    self.assertEqual(sum(probabilities.values()), 1)
                    self.assertGreaterEqual(min(probabilities.values()), 0)
                    full_parity = sum(math.prod(word) * weight for word, weight in probabilities.items())
                    self.assertEqual(full_parity, kappa)
                    for width in range(1, length):
                        for subset in itertools.combinations(range(length), width):
                            marginal = Counter()
                            for word, weight in probabilities.items():
                                marginal[tuple(word[index] for index in subset)] += weight
                            self.assertEqual(len(marginal), 2**width)
                            self.assertEqual(set(marginal.values()), {Fraction(1, 2**width)})


class ConstructionChecks(unittest.TestCase):
    def test_aligned_grover_probability(self):
        cases = itertools.product((3, 4, 5), SIGNS, (1, 2), (3, 8, 1024, 65536))
        for length, preferred_parity, blocks, size in cases:
            with self.subTest(length=length, parity=preferred_parity, blocks=blocks, size=size):
                theta = math.asin(1 / math.sqrt(size))
                diffuse_one_block = (preferred_parity == 1,) + (True,) * (length - 1)
                words = itertools.product(favored_words(length, preferred_parity), repeat=blocks)
                concatenated = (sum(word, ()) for word in words)
                actual = mean_mark_probability(theta, concatenated, diffuse_one_block * blocks)
                random_steps = blocks * (sum(diffuse_one_block) - 1)
                attenuation = math.cos(4 * theta) ** random_steps
                expected = (1 - math.cos((4 * blocks + 2) * theta) * attenuation) / 2
                self.assertAlmostEqual(actual, expected, places=12)

    def test_offset_residue_and_fragment_probability(self):
        theta = math.asin(1 / math.sqrt(4096))
        blocks = 3
        for length, preferred_parity in itertools.product((3, 4, 5), SIGNS):
            trial_length = blocks * length
            for offset in range(length):
                prefix, complete_blocks, suffix = lengths_at_offset(length, trial_length, offset)
                residues = (None,) if preferred_parity == 1 else (0, 1)
                good_residues = [residue for residue in residues if residue != (prefix - 1) % length]
                self.assertTrue(good_residues)
                for residue in residues:
                    with self.subTest(length=length, parity=preferred_parity, offset=offset, residue=residue):
                        diffuse = tuple(slot % length != residue for slot in range(trial_length))
                        middle_words = favored_words(length, preferred_parity)
                        words = itertools.product(
                            sign_words(prefix),
                            *([middle_words] * complete_blocks),
                            sign_words(suffix),
                        )
                        actual = mean_mark_probability(theta, (sum(word, ()) for word in words), diffuse)
                        expected = hidden_offset_probability(theta, length, trial_length, offset, diffuse)
                        self.assertAlmostEqual(actual, expected, places=12)
                        if residue in good_residues:
                            guaranteed_probability = math.sin((2 * complete_blocks - 3) * theta) ** 2
                            self.assertGreaterEqual(actual, guaranteed_probability - 1e-13)

    def test_guard_does_not_share_hidden_blocks(self):
        for length, blocks in itertools.product(range(3, 12), range(3, 7)):
            calls = blocks * length
            for offset in range(length):
                last_probe_block = (offset + calls - 1) // length
                first_verification_block = (offset + calls + length) // length
                last_verification_block = (offset + calls + length + 1) // length
                first_next_probe_block = (offset + calls + 2 * length + 2) // length
                self.assertLess(last_probe_block, first_verification_block)
                self.assertLess(last_verification_block, first_next_probe_block)

    def test_two_reference_certificate_and_scan(self):
        def probability_minus(mark, pair, active):
            ideal_signs = np.array([-1 if active and mark == address else 1 for address in pair])
            return abs(ideal_signs[0] - ideal_signs[1]) ** 2 / 4

        for addresses in (3, 4, 7):
            for candidate in range(addresses):
                reference_a, reference_b = [index for index in range(addresses) if index != candidate][:2]
                for mark in [None, *range(addresses)]:
                    probabilities = []
                    for first_active, second_active in itertools.product((False, True), repeat=2):
                        probabilities.append(
                            probability_minus(mark, (candidate, reference_a), first_active)
                            * probability_minus(mark, (candidate, reference_b), second_active)
                        )
                    self.assertEqual(sum(probabilities) / 4, 1 / 4 if mark == candidate else 0)

                scan_slots = [index for index in range(addresses) for _ in range(2)] * 9
                candidate_slots = [slot for slot, index in enumerate(scan_slots) if index == candidate]
                for length in (3, 4, 5, 8, 25, 200):
                    for offset in range(length):
                        visits = Counter((slot + offset) // length for slot in candidate_slots)
                        self.assertLess(max(visits.values()), length)


class ConverseChecks(unittest.TestCase):
    def test_mean_operator_loss_and_adaptive_progress(self):
        rng = np.random.default_rng(20261126)
        marks, dimension = 5, 8
        for length, kappa in itertools.product(range(3, 7), (-1, -0.95, -0.4, 0, 0.6, 0.98, 1)):
            for repeat in range(3):
                with self.subTest(length=length, kappa=kappa, repeat=repeat):
                    reference = unit_vector(rng, dimension)
                    progress = 0
                    for projectors in mark_projectors(rng, dimension, marks, length):
                        component = unit_vector(rng, dimension) * rng.uniform(0.3, 1)
                        rho = np.outer(component, component.conj())
                        mean = np.zeros((dimension, dimension), dtype=complex)
                        output = np.zeros_like(mean)
                        for probability, unitary in enumerate_block_unitaries(projectors, kappa):
                            mean += probability * unitary
                            output += probability * (unitary @ rho @ unitary.conj().T)
                        expected = pure_block_component(projectors, kappa)
                        np.testing.assert_allclose(mean, expected, atol=1e-12, rtol=0)

                        transformed = mean @ component
                        positive_residual = output - np.outer(transformed, transformed.conj())
                        self.assertGreaterEqual(np.linalg.eigvalsh(positive_residual).min(), -1e-12)

                        first_mark_component = projectors[0] @ component
                        next_input = component - first_mark_component
                        predicted_loss = (1 - kappa**2) * np.linalg.norm(first_mark_component) ** 2
                        for projector in projectors[1:]:
                            removed = projector @ next_input
                            predicted_loss += np.linalg.norm(removed) ** 2
                            next_input -= removed
                        actual_loss = np.linalg.norm(component) ** 2 - np.linalg.norm(transformed) ** 2
                        self.assertGreaterEqual(actual_loss + 1e-12, predicted_loss)

                        old_distance = np.linalg.norm(reference - component) ** 2
                        new_distance = np.linalg.norm(reference - transformed) ** 2
                        increase = new_distance - old_distance
                        progress += increase
                        jump = 2 * np.real(np.vdot(reference, component - transformed)) - actual_loss
                        self.assertAlmostEqual(increase, jump, places=12)

                    shell_bound = 2 * (1 + abs(kappa)) * math.sqrt(marks)
                    if abs(kappa) < 1:
                        shell_bound = min(shell_bound, (1 + abs(kappa)) ** 2 / (1 - kappa**2))
                    self.assertLessEqual(progress, length - 1 + shell_bound + 1e-12)

    def test_incomplete_block_is_iid(self):
        rng = np.random.default_rng(190827)
        physical_length = 6
        dimension = 5
        identity = np.eye(dimension)
        for length, kappa in itertools.product(range(1, physical_length), (-1, -0.4, 0, 0.98, 1)):
            projectors = mark_projectors(rng, dimension, 1, length)[0]
            reflections = [identity - 2 * projector for projector in projectors]
            mean = np.zeros((dimension, dimension), dtype=complex)
            for full_word in sign_words(physical_length):
                factors = [
                    reflection if sign == 1 else identity
                    for reflection, sign in zip(reflections, full_word[:length], strict=True)
                ]
                mean += block_probability(full_word, kappa) * operator_product(factors)
            expected = operator_product([identity - projector for projector in projectors])
            np.testing.assert_allclose(mean, expected, atol=1e-12, rtol=0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
