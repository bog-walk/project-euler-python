import unittest
from util.tests.reusable import compare_speed_nano
from solution.batch2.problem12 import *


class HighlyDivisibleTriangularNumber(unittest.TestCase):
    def test_count_divisors(self):
        nums = [2, 3, 6, 28, 100, 144, 3455, 10000]
        expected = [2, 2, 4, 6, 9, 15, 4, 25]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], count_divisors(n))

    def test_first_triangle_over_N(self):
        nums = [1, 2, 4, 12, 500, 900]
        expected = [3, 6, 28, 120, 76_576_500, 842_161_320]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], first_triangle_over_N(n))
            self.assertEqual(expected[i], first_triangle_over_N_improved(n))
            self.assertEqual(expected[i], first_triangle_over_N_optimised(n))

    def test_first_triangle_speed(self):
        n = 1000
        expected = 842_161_320
        solutions = {
            "Original": [first_triangle_over_N, n],
            "Improved": [first_triangle_over_N_improved, n],
            "Optimised": [first_triangle_over_N_optimised, n]
        }
        results = compare_speed_nano(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
