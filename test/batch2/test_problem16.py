import unittest
from util.tests.reusable import compare_speed_nano
from solution.batch2.problem16 import *


class PowerDigitSum(unittest.TestCase):
    def test_exp_digit_sum(self):
        nums = [1, 2, 3, 4, 7, 9, 15, 99, 1000]
        expected = [2, 4, 8, 7, 11, 8, 26, 107, 1366]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], exp_digit_sum_builtin(n))
            self.assertEqual(expected[i], exp_digit_sum_iterative(n))

    def test_exp_digit_sum_speed_2(self):
        n = 10_000
        expected = 13561
        solutions = {
            "Built-in": [exp_digit_sum_builtin, n],
            "Iterative": [exp_digit_sum_iterative, n]
        }
        results = compare_speed_nano(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
