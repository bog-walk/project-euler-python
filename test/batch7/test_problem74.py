import unittest
from util.tests.reusable import compare_speed
from solution.batch7.problem74 import *


class DigitFactorialChains(unittest.TestCase):
    def test_HR_problem_lower_constraints(self):
        inputs = [
            (10, 1), (24, 3), (29, 2), (147, 1), (175, 7), (210, 2), (221, 7),
            (258, 4), (261, 4), (265, 8), (273, 4)
        ]
        expected = [
            [1, 2], [], [0, 10, 11], [1, 2, 145], [24, 42, 104, 114, 140, 141],
            [0, 10, 11, 154], [24, 42, 104, 114, 140, 141], [78, 87, 196, 236],
            [78, 87, 196, 236], [4, 27, 39, 72, 93, 107, 117, 170, 171],
            [78, 87, 196, 236, 263]
        ]
        for i, e in enumerate(expected):
            limit, length = inputs[i]
            self.assertListEqual(e, digit_factorial_chain_starters(limit, length))
            self.assertListEqual(
                e, digit_factorial_chain_starters_improved(limit, length)
                 )
            self.assertListEqual(
                e, digit_factorial_chain_starters_optimised(limit, length)
            )

    def test_HR_problem_mid_constraints(self):
        inputs = [
            (1999, 50), (4000, 60), (10_000, 30)
        ]
        expected_sizes = [24, 6, 146]
        expected_heads = [
            [289, 298, 366, 466, 636, 646],
            [1479, 1497, 1749, 1794, 1947, 1974],
            [44, 126, 146, 162, 164, 206]
        ]
        solutions = [
            digit_factorial_chain_starters,
            digit_factorial_chain_starters_improved,
            digit_factorial_chain_starters_optimised
        ]
        for i, e_s in enumerate(expected_sizes):
            limit, length = inputs[i]
            actual = solutions[i](limit, length)
            self.assertEqual(e_s, len(actual))
            self.assertListEqual(expected_heads[i], actual[:6])

    def test_HR_problem_with_factorions(self):
        limit = 1_000_000
        length = 1
        expected = [1, 2, 145, 40585]
        self.assertListEqual(expected, digit_factorial_chain_starters(limit, length))
        self.assertListEqual(
            expected, digit_factorial_chain_starters_improved(limit, length)
        )
        self.assertListEqual(
            expected, digit_factorial_chain_starters_optimised(limit, length)
        )

    def test_HR_problem_upper_constraints_speed(self):
        limit = 1_000_000
        length = 10
        expected_size = 26837
        solutions = {
            "Original": [digit_factorial_chain_starters, limit, length],
            "Improved": [digit_factorial_chain_starters_improved, limit, length],
            "Optimised": [digit_factorial_chain_starters_optimised, limit, length]
        }
        results = compare_speed(solutions)
        self.assertTrue(
            all(expected_size == len(actual) for actual in results.values())
        )

    def test_PE_problem_correct(self):
        limit = 1_000_000
        length = 60
        expected_size = 402
        actual = digit_factorial_chain_starters(limit, length)
        self.assertEqual(expected_size, len(actual))


if __name__ == '__main__':
    unittest.main()
