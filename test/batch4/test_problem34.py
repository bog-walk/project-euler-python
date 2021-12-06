import unittest
from solution.batch4.problem34 import *


class DigitFactorials(unittest.TestCase):
    def test_sum_of_digit_factorials_HR(self):
        nums = [10, 20, 30, 40, 50, 100, 200, 500]
        expected = [0, 19, 19, 19, 19, 239, 384, 603]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], sum_of_digit_factorials_HR(n))

    def test_sum_of_digit_factorials_PE(self):
        self.assertEqual(40730, sum_of_digit_factorials_PE())


if __name__ == '__main__':
    unittest.main()
