import unittest
from solution.batch6.problem56 import max_digit_sum


class PowerfulDigitSum(unittest.TestCase):
    def test_lower_constraints(self):
        nums = [5, 6, 7, 8, 9, 10]
        expected = [13, 13, 27, 36, 37, 45]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], max_digit_sum(n))

    def test_mid_values(self):
        nums = [20, 30, 50, 100]
        expected = [127, 224, 406, 972]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], max_digit_sum(n))

    def test_upper_constraints(self):
        n = 200
        expected = 2205
        self.assertEqual(expected, max_digit_sum(n))


if __name__ == '__main__':
    unittest.main()
