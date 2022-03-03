import unittest
from solution.batch6.problem65 import nth_convergent_digit_sum


class ConvergentsOfE(unittest.TestCase):
    def test_lower_constraints(self):
        expected = [2, 3, 8, 2, 10, 15, 7, 13, 13, 17]
        for n in range(1, 11):
            self.assertEqual(expected[n-1], nth_convergent_digit_sum(n))

    def test_mid_constraints(self):
        nums = [100, 200, 300, 400, 500]
        expected = [272, 597, 980, 1397, 1849]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], nth_convergent_digit_sum(n))

    def test_upper_constraints(self):
        nums = [4999, 9999, 30_000]
        expected = [25652, 55534, 187_838]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], nth_convergent_digit_sum(n))


if __name__ == '__main__':
    unittest.main()
