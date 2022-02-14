import unittest
from util.tests.reusable import compare_speed
from solution.batch0.problem5 import *


class SmallestMultiple(unittest.TestCase):
    def test_lower_constraints(self):
        nums = [1, 2, 3]
        expected = [1, 2, 6]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], lcm_of_range(n))
            self.assertEqual(expected[i], lcm_of_range_builtin(n))

    def test_normal_n(self):
        nums = [6, 10, 20]
        expected = [60, 2520, 232_792_560]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], lcm_of_range(n))
            self.assertEqual(expected[i], lcm_of_range_builtin(n))

    def test_upper_constraints(self):
        n = 30
        expected = 2_329_089_562_800
        self.assertEqual(expected, lcm_of_range(n))
        self.assertEqual(expected, lcm_of_range_builtin(n))

    def test_lcm_of_range_speed(self):
        n = 40
        expected = 5_342_931_457_063_200
        solutions = {
            "Iterative": [lcm_of_range, n],
            "Built-in": [lcm_of_range_builtin, n]
        }
        results = compare_speed(solutions, repeat=1000)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
