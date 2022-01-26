import unittest
from util.tests.reusable import compare_speed_seconds
from solution.batch2.problem26 import *


class ReciprocalCycles(unittest.TestCase):
    def test_lower_constraints(self):
        nums = [5, 10, 14, 19, 25]
        expected = [3, 7, 7, 17, 23]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], longest_repetend_denominator_primes(n))
            self.assertEqual(
                expected[i], longest_repetend_denominator_primes_improved(n)
            )
            self.assertEqual(expected[i], longest_repetend_denominator(n))

    def test_normal_values(self):
        nums = [46, 50, 70]
        expected = [29, 47, 61]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], longest_repetend_denominator_primes(n))
            self.assertEqual(
                expected[i], longest_repetend_denominator_primes_improved(n)
            )
            self.assertEqual(expected[i], longest_repetend_denominator(n))

    def test_upper_constraints(self):
        nums = [1000, 5000]
        expected = [983, 4967]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], longest_repetend_denominator_primes(n))
            self.assertEqual(
                expected[i], longest_repetend_denominator_primes_improved(n)
                             )
            self.assertEqual(expected[i], longest_repetend_denominator(n))

    def test_longest_repetend_denominator_speed(self):
        n = 10000
        expected = 9967
        solutions = {
            "Prime": [longest_repetend_denominator_primes, n],
            "Prime optimised": [longest_repetend_denominator_primes_improved, n],
            "Improved": [longest_repetend_denominator, n]
        }
        results = compare_speed_seconds(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
