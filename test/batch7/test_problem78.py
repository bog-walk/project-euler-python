import unittest
from util.tests.reusable import compare_speed
from solution.batch7.problem78 import *


class CoinPartitions(unittest.TestCase):
    def test_HR_problem_lower_constraints(self):
        limit = 100
        nums = [2, 3, 4, 5, 6, 7, 10, 100]
        expected = [2, 3, 5, 7, 11, 15, 42, 190_569_292]
        dynamic_actual = coin_pile_combos(limit)
        theorem_actual = coin_pile_combos_theorem(limit)
        for n, e in zip(nums, expected):
            self.assertEqual(e, dynamic_actual[n])
            self.assertEqual(e, theorem_actual[n])

    def test_HR_problem_lower_constraints_speed(self):
        n = 1000
        expected = 709_496_666
        solutions = {
            "Dynamic": [coin_pile_combos, n],
            "Theorem": [coin_pile_combos_theorem, n],
        }    
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual[n] for actual in results.values()))

    def test_HR_problem_mid_constraints_speed(self):
        n = 10_000
        expected = 17_783_467
        solutions = {
            "Dynamic": [coin_pile_combos, n],
            "Theorem": [coin_pile_combos_theorem, n]
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual[n] for actual in results.values()))

    def test_HR_problem_mid_to_upper_constraints(self):
        limit = 60_000
        nums = [500, 8432, 30_000, 60_000]
        expected = [168_879_716, 720_964_692, 977_046_096, 168_497_963]
        theorem_actual = coin_pile_combos_theorem(limit)
        for n, e in zip(nums, expected):
            self.assertEqual(e, theorem_actual[n])

    def test_PE_problem(self):
        expected = 55374
        self.assertEqual(expected, first_coin_combo())


if __name__ == '__main__':
    unittest.main()
