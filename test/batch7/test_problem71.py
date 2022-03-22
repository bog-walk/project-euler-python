import unittest
from util.tests.reusable import compare_speed
from solution.batch7.problem71 import left_farey_neighbour, \
    left_farey_neighbour_improved, left_farey_neighbour_optimised


class OrderedFractions(unittest.TestCase):
    def test_lower_constraints(self):
        limit = 8
        numerators = [1, 1, 2, 3, 1, 5, 5, 7]
        denominators = [7, 6, 7, 7, 2, 8, 6, 8]
        expected = [
            (1, 8), (1, 7), (1, 4), (2, 5), (3, 7), (3, 5), (4, 5), (6, 7)
        ]
        for n, d, e in zip(numerators, denominators, expected):
            self.assertTupleEqual(e, left_farey_neighbour(limit, n, d))
            self.assertTupleEqual(e, left_farey_neighbour_improved(limit, n, d))
            self.assertTupleEqual(e, left_farey_neighbour_optimised(limit, n, d))

    def test_lower_mid_constraints(self):
        limit = 10_000
        numerators = [1, 3, 1, 3]
        denominators = [5, 7, 2, 4]
        expected = [
            (1999, 9996), (4283, 9994), (4999, 9999), (7499, 9999)
        ]
        for n, d, e in zip(numerators, denominators, expected):
            self.assertTupleEqual(e, left_farey_neighbour(limit, n, d))
            self.assertTupleEqual(e, left_farey_neighbour_improved(limit, n, d))
            self.assertTupleEqual(e, left_farey_neighbour_optimised(limit, n, d))

    def test_mid_constraints_speed(self):
        limit = 10_000_000
        n, d = 3, 7
        expected = 4_285_712, 9_999_995
        solutions = {
            "Original": [left_farey_neighbour, limit, n, d],
            "Improved": [left_farey_neighbour_improved, limit, n, d],
            "Optimised": [left_farey_neighbour_optimised, limit, n, d]
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))

    def test_upper_mid_constraints(self):
        limit = 1_000_000_000
        numerators = [1, 3, 7]
        denominators = [7, 7, 8]
        expected = [
            (142_857_142, 999_999_995), (428_571_428, 999_999_999),
            (874_999_999, 999_999_999)
        ]
        for n, d, e in zip(numerators, denominators, expected):
            self.assertTupleEqual(e, left_farey_neighbour_improved(limit, n, d))
            self.assertTupleEqual(e, left_farey_neighbour_optimised(limit, n, d))

    def test_upper_constraints(self):
        limit = 1_000_000_000_000
        numerators = [1, 1, 4]
        denominators = [6, 2, 5]
        expected = [
            (166_666_666_666, 999_999_999_997),
            (499_999_999_999, 999_999_999_999),
            (799_999_999_999, 999_999_999_999)
        ]
        for n, d, e in zip(numerators, denominators, expected):
            self.assertTupleEqual(e, left_farey_neighbour_improved(limit, n, d))
            self.assertTupleEqual(e, left_farey_neighbour_optimised(limit, n, d))

    def test_upper_constraints_speed(self):
        limit = 1_000_000_000_000_000
        n, d = 100_010_627, 100_010_633
        expected = 999_999_842_024_434, 999_999_902_018_049
        solutions = {
            "Improved": [left_farey_neighbour_improved, limit, n, d],
            "Optimised": [left_farey_neighbour_optimised, limit, n, d]
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))

    def test_PE_problem_correct(self):
        limit = 1_000_000
        n, d = 3, 7
        expected = 428_570, 999_997  # only numerator required
        self.assertTupleEqual(expected, left_farey_neighbour(limit, n, d))


if __name__ == '__main__':
    unittest.main()
