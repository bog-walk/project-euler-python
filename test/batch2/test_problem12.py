import unittest

from solution.batch2.problem12 import *


class HighlyDivisibleTriangularNumber(unittest.TestCase):
    def test_count_divisors(self):
        nums = [2, 3, 6, 28, 100, 144, 3455, 10000]
        expected = [2, 2, 4, 6, 9, 15, 4, 25]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], count_divisors(n))

    def test_first_triangle_over_N(self):
        nums = [1, 2, 4, 12, 500, 1000]
        expected = [3, 6, 28, 120, 76576500, 842161320]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], first_triangle_over_N(n))
            self.assertEqual(expected[index], first_triangle_over_N_Alt(n))


if __name__ == '__main__':
    unittest.main()
