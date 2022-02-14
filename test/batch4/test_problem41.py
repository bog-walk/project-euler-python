import unittest
from util.tests.reusable import compare_speed
from solution.batch4.problem41 import *


class PandigitalPrime(unittest.TestCase):
    def test_largest_pandigital_prime_existing(self):
        expected = 7_652_413
        self.assertEqual(expected, largest_pandigital_prime_brute())

    def test_lower_constraints(self):
        nums = [10, 100, 2140]
        expected = [-1, -1, 1423]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], largest_pandigital_prime(n))

    def test_mid_values(self):
        nums = [10_000, 100_000, 1_000_000]
        expected = 4231
        for n in nums:
            self.assertEqual(expected, largest_pandigital_prime(n))

    def test_upper_constraints(self):
        nums = [7_652_412, 10_000_000]
        expected = [7_642_513, 7_652_413]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], largest_pandigital_prime(n))

    def test_all_pandigital_primes_speed(self):
        expected_len = 538
        solutions = {
            "Built-in": [all_pandigital_primes_builtin],
            "Helper function": [all_pandigital_primes]
        }
        results = list(compare_speed(solutions).values())
        self.assertListEqual(results[0], results[1])
        self.assertTrue(all(expected_len == len(actual) for actual in results))


if __name__ == '__main__':
    unittest.main()
