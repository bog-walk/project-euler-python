import unittest
from solution.batch2.problem20 import *


class FactorialDigitSum(unittest.TestCase):
    def test_factorial_digit_sum(self):
        nums = [0, 1, 2, 3, 4, 5, 6, 10, 100, 333, 750, 946, 1000]
        expected = [1, 1, 2, 6, 6, 3, 9, 27, 648, 2862, 7416, 9675, 10539]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], factorial_digit_sum_A(n))
            self.assertEqual(expected[index], factorial_digit_sum_B(n))


if __name__ == '__main__':
    unittest.main()
