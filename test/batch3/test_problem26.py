import unittest
from util.tests.reusable import compare_speed_seconds
from solution.batch3.problem26 import *


class ReciprocalCycles(unittest.TestCase):
    def test_longest_repetend_denominator(self):
        nums = [5, 10, 14, 19, 25, 46, 50, 70, 1000, 10000]
        expected = [3, 7, 7, 17, 23, 29, 47, 61, 983, 9967]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], longest_repetend_denominator_primes(n))
            self.assertEqual(expected[index], longest_repetend_denominator(n))

    def test_longest_repetend_speed(self):
        n = 10000
        expected = 9967
        solutions = {
            "Prime": [longest_repetend_denominator_primes, n],
            "Improved": [longest_repetend_denominator, n]
        }
        results = compare_speed_seconds(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
