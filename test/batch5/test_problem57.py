import unittest
from util.tests.reusable import compare_speed_seconds
from solution.batch5.problem57 import square_root_fractions_manual, \
    square_root_fractions_optimised


class SquareRootConvergents(unittest.TestCase):
    def test_lower_constraints(self):
        nums = [8, 10, 14, 20]
        expected = [[8], [8], [8, 13], [8, 13]]
        for i, n in enumerate(nums):
            self.assertListEqual(expected[i], square_root_fractions_manual(n))
            self.assertListEqual(expected[i], square_root_fractions_optimised(n))

    def test_mid_values(self):
        nums = [50, 60, 100]
        expected = [
            [8, 13, 21, 26, 34, 39, 47],
            [8, 13, 21, 26, 34, 39, 47, 55, 60],
            [8, 13, 21, 26, 34, 39, 47, 55, 60, 68, 73, 81, 86, 89, 94]
        ]
        for i, n in enumerate(nums):
            self.assertListEqual(expected[i], square_root_fractions_manual(n))
            self.assertListEqual(expected[i], square_root_fractions_optimised(n))

    def test_upper_constraints(self):
        n = 1000
        expected_len = 153
        self.assertEqual(expected_len, len(square_root_fractions_manual(n)))
        self.assertEqual(expected_len, len(square_root_fractions_optimised(n)))

    def test_speed(self):
        n = 2000
        solutions = {
            "Manual": [square_root_fractions_manual, n],
            "Optimised": [square_root_fractions_optimised, n]
        }
        results = list(compare_speed_seconds(solutions).values())
        self.assertListEqual(results[0], results[1])


if __name__ == '__main__':
    unittest.main()
