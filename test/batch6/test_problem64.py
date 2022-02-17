import unittest
from solution.batch6.problem64 import odd_square_roots


class OddPeriodSquareRoots(unittest.TestCase):
    def test_lower_constraints(self):
        nums = [10, 13, 20, 30, 45]
        expected = [3, 4, 5, 7, 9]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], odd_square_roots(n))

    def test_mid_constraints(self):
        nums = [100, 500, 2000]
        expected = [20, 83, 296]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], odd_square_roots(n))

    def test_upper_constraints(self):
        nums = [10_000, 20_000, 30_000]
        expected = [1322, 2524, 3687]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], odd_square_roots(n))


if __name__ == '__main__':
    unittest.main()
