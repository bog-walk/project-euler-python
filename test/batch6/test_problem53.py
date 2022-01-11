import unittest
from util.tests.reusable import compare_speed_seconds
from solution.batch6.problem53 import count_large_combinatorics, \
    count_large_combinatorics_improved


class CombinatoricSelections(unittest.TestCase):
    def test_count_large_combinatorics_lower_constraints(self):
        k = 5
        expected = [0, 0, 1, 3, 8, 14]
        for n in range(2, 8):
            self.assertEqual(expected[n - 2], count_large_combinatorics(n, k))
            self.assertEqual(expected[n - 2], count_large_combinatorics_improved(n, k))

    def test_count_large_combinatorics(self):
        nums = [2, 23, 100, 1000]
        k = 1_000_000
        expected = [0, 4, 4075, 494_861]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], count_large_combinatorics(n, k))
            self.assertEqual(expected[i], count_large_combinatorics_improved(n, k))

    def test_count_large_combinatorics_upper_constraint(self):
        n, k = 1000, 10_000_000_000
        expected = 490_806
        self.assertEqual(expected, count_large_combinatorics(n, k))
        self.assertEqual(expected, count_large_combinatorics_improved(n, k))

    def test_speed_compare(self):
        n, k = 1000, 1000
        expected = 497_376
        solutions = {
            "OG": [count_large_combinatorics, n, k],
            "Improved": [count_large_combinatorics_improved, n, k]
        }
        results = compare_speed_seconds(solutions, repeat=10)
        self.assertTrue(all([expected == actual for actual in results.values()]))


if __name__ == '__main__':
    unittest.main()
