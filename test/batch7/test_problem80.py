import unittest
from util.tests.reusable import compare_speed
from solution.batch7.problem80 import *


class SquareRootDigitalExpansion(unittest.TestCase):
    def test_lower_constraints(self):
        inputs = [
            (1, 1), (2, 10), (2, 20), (2, 100), (2, 10_000), (16, 500), (100, 100)
        ]
        expected = [0, 29, 76, 475, 45349, 26795, 40886]
        for (n, p), e in zip(inputs, expected):
            self.assertEqual(e, irrational_square_digit_sum(n, p))
            self.assertEqual(e, irrational_square_digit_sum_improved(n, p))

    def test_mid_constraints(self):
        inputs = [(230, 100), (500, 100), (900, 1000)]
        expected = [96340, 214_519, 3_913_848]
        for (n, p), e in zip(inputs, expected):
            self.assertEqual(e, irrational_square_digit_sum(n, p))
            self.assertEqual(e, irrational_square_digit_sum_improved(n, p))

    def test_upper_constraints(self):
        n, p = 1000, 1000
        expected = 4_359_087
        self.assertEqual(expected, irrational_square_digit_sum(n, p))
        self.assertEqual(expected, irrational_square_digit_sum_improved(n, p))

    def test_upper_constraints_speed(self):
        n, p = 100, 10_000
        expected = 4_048_597
        solutions = {
            "Original": [irrational_square_digit_sum, n, p],
            "Improved": [irrational_square_digit_sum_improved, n, p],
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
