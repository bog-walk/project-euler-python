import unittest
from util.tests.reusable import compare_speed_nano
from solution.batch3.problem28 import *


class NumberSpiralDiagonals(unittest.TestCase):
    def test_spiral_diag_sum(self):
        nums = [1, 3, 5, 7, 1001, 7001]
        expected = [1, 25, 101, 261, 669171001, 789195405]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], spiral_diag_sum_brute(n))
            self.assertEqual(expected[index], spiral_diag_sum_formula_brute(n))
            self.assertEqual(expected[index], spiral_diag_sum_formula_derived(n))

    def test_spiral_diag_sum_speed(self):
        n = 1_000_001
        expected = 4315867
        solutions = {
            "Brute": [spiral_diag_sum_brute, n],
            "Iterative": [spiral_diag_sum_formula_brute, n],
            "Derivative": [spiral_diag_sum_formula_derived, n]
        }
        results = compare_speed_nano(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
