import unittest
from util.tests.reusable import compare_speed_seconds
from solution.batch4.problem39 import *


class IntegerRightTriangles(unittest.TestCase):
    def test_lower_constraints(self):
        nums = [12, 15, 40, 50, 80, 100, 1000]
        expected = [12, 12, 12, 12, 60, 60, 840]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], most_triplet_solutions_brute(n))
            self.assertEqual(expected[i], most_triplet_solutions(n))
            self.assertEqual(expected[i], most_triplet_solutions_improved(n))

    def test_most_triplet_solutions_speed(self):
        n = 100_000
        expected = 55440
        solutions = {
            "Brute": [most_triplet_solutions_brute, n],
            "Original": [most_triplet_solutions, n],
            "Improved": [most_triplet_solutions_improved, n]
        }
        results = compare_speed_seconds(solutions, precision=3)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
