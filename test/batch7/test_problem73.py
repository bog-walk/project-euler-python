import unittest
from util.tests.reusable import compare_speed
from solution.batch7.problem73 import farey_range_count_recursive, \
    farey_range_count_sieve, farey_range_count_iterative, farey_range_count_IE


class CountingFractionsInARange(unittest.TestCase):
    def test_lower_constraints(self):
        d_values = [3, 5, 8, 8, 8]
        a_values = [2, 2, 2, 3, 6]
        expected = [0, 1, 3, 1, 0]
        for d, a, e in zip(d_values, a_values, expected):
            self.assertEqual(e, farey_range_count_recursive(d, a))
            self.assertEqual(e, farey_range_count_iterative(d, a))
            self.assertEqual(e, farey_range_count_sieve(d, a))

    def test_lower_constraints_speed(self):
        d, a = 1000, 2
        expected = 50695
        solutions = {
            "Recursive count": [farey_range_count_recursive, d, a],
            "Iterative count": [farey_range_count_iterative, d, a],
            "Inclusion-Exclusion": [farey_range_count_IE, d, a],
            "Rank": [farey_range_count_sieve, d, a],
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))

    def test_mid_constraints(self):
        d_values = [100, 100]
        a_values = [2, 4]
        expected = [505, 150]
        for d, a, e in zip(d_values, a_values, expected):
            self.assertEqual(e, farey_range_count_recursive(d, a))
            self.assertEqual(e, farey_range_count_iterative(d, a))
            self.assertEqual(e, farey_range_count_sieve(d, a))

    def test_mid_constraints_speed(self):
        d, a = 10_000, 100
        expected = 3003
        solutions = {
            "Recursive count": [farey_range_count_recursive, d, a],
            "Iterative count": [farey_range_count_iterative, d, a]
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))

    def test_mid_upper_constraints_speed(self):
        d, a = 1_000_000, 100
        expected = 30_095_571
        solutions = {
            "Iterative count": [farey_range_count_iterative, d, a],
            "Rank": [farey_range_count_sieve, d, a],
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))

    def test_upper_constraints(self):
        d_values = [49999, 50_000, 200_000, 1_000_000, 2_000_000]
        a_values = [3, 2, 5, 2, 100]
        expected = [
            63_325_374, 126_654_024, 405_286_681, 50_660_592_050, 120_381_464
        ]
        for d, a, e in zip(d_values, a_values, expected):
            self.assertEqual(e, farey_range_count_sieve(d, a))

    def test_upper_constraints_speed(self):
        d, a = 2_000_000, 2
        expected = 202_642_449_955
        solutions = {
            "Inclusion-Exclusion": [farey_range_count_IE, d, a],
            "Rank": [farey_range_count_sieve, d, a],
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
