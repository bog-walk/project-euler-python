import unittest
from util.tests.reusable import compare_speed
from solution.batch6.problem70 import *


class TotientPermutation(unittest.TestCase):
    def test_lower_constraints(self):
        nums = [100, 200, 300, 400, 500, 1000]
        expected = [21, 21, 291, 291, 291, 291]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], totient_permutation(n))
            self.assertEqual(expected[i], totient_permutation_robust(n))

    def test_mid_constraints(self):
        nums = [2900, 3000, 5000, 10_000, 50_000]
        expected = [2817, 2991, 4435, 4435, 45421]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], totient_permutation(n))
            self.assertEqual(expected[i], totient_permutation_robust(n))

    def test_upper_constraints(self):
        nums = [100_000, 1_000_000]
        expected = [75841, 783_169]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], totient_permutation(n))
            self.assertEqual(expected[i], totient_permutation_robust(n))

    def test_totient_permutation_speed(self):
        n = 10_000_000
        expected = 8_319_823
        solutions = {
            "Original": [totient_permutation, n],
            "Robust": [totient_permutation_robust, n]
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
