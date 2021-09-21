import unittest
from solution.batch2.problem16 import *


class PowerDigitSum(unittest.TestCase):
    def test_power_digit_sum(self):
        nums = [1, 2, 3, 4, 7, 9, 15, 99, 1000, 10000]
        expected = [2, 4, 8, 7, 11, 8, 26, 107, 1366, 13561]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], exp_digit_sum_A(n))
            self.assertEqual(expected[index], exp_digit_sum_B(n))


if __name__ == '__main__':
    unittest.main()
