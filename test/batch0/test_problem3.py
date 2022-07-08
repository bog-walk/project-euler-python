import unittest
from util.tests.reusable import compare_speed
from solution.batch0.problem3 import *


class LargestPrimeFactor(unittest.TestCase):
    def test_lower_constraints(self):
        n = 10
        expected = 5
        self.assertEqual(expected, largest_prime_factor(n))
        self.assertEqual(expected, largest_prime_factor_simple(n))
        self.assertEqual(expected, largest_prime_factor_recursive(n))

    def test_n_is_small_prime(self):
        n = 17
        expected = 17
        self.assertEqual(expected, largest_prime_factor(n))
        self.assertEqual(expected, largest_prime_factor_simple(n))
        self.assertEqual(expected, largest_prime_factor_recursive(n))

    def test_normal_n(self):
        nums = [48, 147, 330]
        expected = [3, 7, 11]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], largest_prime_factor(n))
            self.assertEqual(expected[i], largest_prime_factor_simple(n))
            self.assertEqual(expected[i], largest_prime_factor_recursive(n))

    def test_large_n(self):
        nums = [13195, 200_000]
        expected = [29, 5]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], largest_prime_factor(n))
            self.assertEqual(expected[i], largest_prime_factor_simple(n))
            self.assertEqual(expected[i], largest_prime_factor_recursive(n))

    def test_n_is_large_prime(self):
        nums = [7919, 2_147_483_647]
        expected = [7919, 2_147_483_647]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], largest_prime_factor(n))
            self.assertEqual(expected[i], largest_prime_factor_simple(n))
            self.assertEqual(expected[i], largest_prime_factor_recursive(n))

    def test_largest_prime_factor_speed_large_factors(self):
        n = 600_851_475_143
        expected = 6857
        solutions = {
            "Decomposition": [largest_prime_factor, n],
            "Simplified": [largest_prime_factor_simple, n],
            "Recursive": [largest_prime_factor_recursive, n]
        }
        results = compare_speed(solutions, repeat=1000)
        self.assertTrue(all(expected == actual for actual in results.values()))

    def test_largest_prime_factor_speed_small_factors(self):
        n = pow(10, 12)
        expected = 5
        solutions = {
            "Decomposition": [largest_prime_factor, n],
            "Simplified": [largest_prime_factor_simple, n],
            "Recursive": [largest_prime_factor_recursive, n]
        }
        results = compare_speed(solutions, repeat=1000)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
