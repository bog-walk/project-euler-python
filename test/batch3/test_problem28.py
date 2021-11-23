import unittest
from time import perf_counter_ns
from solution.batch3.problem28 import *


class NumberSpiralDiagonals(unittest.TestCase):
    def test_spiral_diag_sum(self):
        nums = [1, 3, 5, 7, 1001, 7001]
        expected = [1, 25, 101, 261, 669171001, 789195405]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], spiral_diag_sum_brute(n))
            self.assertEqual(expected[index], spiral_diag_sum_formula_brute(n))
            self.assertEqual(expected[index], spiral_diag_sum_formula_derived(n))

    def test_speed_comparison(self):
        n = 1_000_001
        expected = 4315867
        solutions = [
            spiral_diag_sum_brute, spiral_diag_sum_formula_brute, spiral_diag_sum_formula_derived
        ]
        starts = []
        stops = []
        for solution in solutions:
            starts.append(perf_counter_ns())
            result = solution(n)
            stops.append(perf_counter_ns())
            self.assertEqual(expected, result)
        print(f"Brute took: {stops[0] - starts[0]}ns\n"
              f"Formula iterative took: {stops[1] - starts[1]}ns\n"
              f"Formula derivative took: {stops[2] - starts[2]}ns\n")


if __name__ == '__main__':
    unittest.main()
