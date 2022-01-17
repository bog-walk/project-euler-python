import unittest
from util.tests.reusable import compare_speed_seconds
from solution.batch4.problem31 import *


class CoinSums(unittest.TestCase):
    def test_lower_constraints(self):
        expected = [1, 2, 2, 3, 4, 5, 6, 7, 8, 11]
        for n in range(10):
            self.assertEqual(expected[n], count_coin_combos(n + 1))
            self.assertEqual(expected[n], count_coin_combos_recursive(n + 1))

    def test_mid_values(self):
        nums = [15, 20, 50, 200, 500]
        expected = [22, 41, 451, 73682, 6_295_434]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], count_coin_combos(n))
            self.assertEqual(expected[i], count_coin_combos_recursive(n))

    def test_upper_constraints(self):
        n = 10000
        expected = 296_710_490
        self.assertEqual(expected, count_coin_combos(n))
        self.assertEqual(expected, count_coin_combos_recursive(n))

    def test_count_coin_combos_speed(self):
        n = 100_000
        solutions = {
            "Recursive": [count_coin_combos_recursive, n],
            "Improved": [count_coin_combos, n]
        }
        results = list(compare_speed_seconds(solutions, precision=2).values())
        self.assertEqual(results[0], results[1])


if __name__ == '__main__':
    unittest.main()
