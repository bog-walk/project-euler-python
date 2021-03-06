import unittest
from util.tests.reusable import compare_speed
from solution.batch2.problem28 import *


class NumberSpiralDiagonals(unittest.TestCase):
    def test_lower_constraints(self):
        nums = [1, 3, 5, 7]
        expected = [1, 25, 101, 261]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], spiral_diag_sum_brute(n))
            self.assertEqual(expected[i], spiral_diag_sum_formula_brute(n))
            self.assertEqual(expected[i], spiral_diag_sum_formula_derived(n))

    def test_normal_values(self):
        nums = [1001, 7001]
        expected = [669_171_001, 789_195_405]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], spiral_diag_sum_brute(n))
            self.assertEqual(expected[i], spiral_diag_sum_formula_brute(n))
            self.assertEqual(expected[i], spiral_diag_sum_formula_derived(n))

    def test_spiral_diag_sum_speed(self):
        n = 1_000_001
        expected = 4_315_867
        solutions = {
            "Brute": [spiral_diag_sum_brute, n],
            "Iterative": [spiral_diag_sum_formula_brute, n],
            "Derivative": [spiral_diag_sum_formula_derived, n]
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
