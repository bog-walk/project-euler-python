import unittest
from util.tests.reusable import compare_speed_seconds
from solution.batch2.problem16 import *


class PowerDigitSum(unittest.TestCase):
    def test_power_digit_sum(self):
        nums = [1, 2, 3, 4, 7, 9, 15, 99, 1000, 10000]
        expected = [2, 4, 8, 7, 11, 8, 26, 107, 1366, 13561]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], exp_digit_sum_A(n))
            self.assertEqual(expected[index], exp_digit_sum_B(n))

    def test_speed(self):
        n = 10_000
        expected = 13561
        solutions = {
            "A": [exp_digit_sum_A, n], "B": [exp_digit_sum_B, n]
        }
        results = compare_speed_seconds(solutions, precision=3, repeat=1000)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
