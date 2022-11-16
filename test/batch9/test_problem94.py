import unittest
from util.tests.reusable import compare_speed
from solution.batch9.problem94 import *


class AlmostEquilateralTriangles(unittest.TestCase):
    def test_lower_constraints(self):
        nums = [15, 16, 17, 51, 200, 1000, 2705]
        expected = [0, 16, 16, 66, 262, 984, 3688]
        for n, e in zip(nums, expected):
            self.assertEqual(e, perimeter_sum_of_almost_equilaterals(n))
            self.assertEqual(e, perimeter_sum_of_sequence(n))

    def test_mid_constraints(self):
        nums = [38000, 100_000, 500_000, 1_000_000]
        expected = [51406, 51406, 191_856, 716_032]
        for n, e in zip(nums, expected):
            self.assertEqual(e, perimeter_sum_of_almost_equilaterals(n))
            self.assertEqual(e, perimeter_sum_of_sequence(n))

    def test_speed(self):
        n = 10_000_000
        expected = 9_973_078
        solutions = {
            "Brute": [perimeter_sum_of_almost_equilaterals, n],
            "Sequence": [perimeter_sum_of_sequence, n],
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))

    def test_upper_constraints(self):
        expected = [
            518_408_346, 375_326_930_086, 1_014_133_226_193_376,
            734_231_055_024_833_850
        ]
        for exp, e in zip(range(9, 19, 3), expected):
            n = int(pow(10, exp))
            self.assertEqual(e, perimeter_sum_of_sequence(n))


if __name__ == '__main__':
    unittest.main()
