import unittest
from util.tests.reusable import compare_speed
from solution.batch1.problem20 import *


class FactorialDigitSum(unittest.TestCase):
    def test_factorial_digit_sum(self):
        nums = [0, 1, 2, 3, 4, 5, 6, 10, 100, 333, 750, 946]
        expected = [1, 1, 2, 6, 6, 3, 9, 27, 648, 2862, 7416, 9675]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], factorial_digit_sum_builtin(n))
            self.assertEqual(expected[i], factorial_digit_sum_iterative(n))

    def test_speed(self):
        n = 1000
        expected = 10539
        solutions = {
            "Built-in": [factorial_digit_sum_builtin, n],
            "Iterative": [factorial_digit_sum_iterative, n]
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
