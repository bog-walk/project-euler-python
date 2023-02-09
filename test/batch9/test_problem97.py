import unittest
from util.tests.reusable import compare_speed
from solution.batch9.problem97 import *


class LargeNonMersennePrime(unittest.TestCase):
    def test_single_tail_lower_constraints(self):
        inputs = [[1, 2, 3, 4], [2, 3, 4, 5], [6, 7, 8, 9]]
        expected = ["000000000012", "000000000167", "000034588815"]

        for (a, b, c, d), e in zip(inputs, expected):
            self.assertEqual(e, tail_of_very_large_num(a, b, c, d))
            self.assertEqual(e, tail_of_very_large_num_opt(a, b, c, d))

    def test_single_tail_mid_constraints(self):
        inputs = [[12, 13, 14, 15], [21, 22, 23, 24], [41, 42, 43, 44],
                  [100, 101, 102, 103]]
        expected = ["516628391483", "250786295832", "663853662252", "925152020203"]

        for (a, b, c, d), e in zip(inputs, expected):
            self.assertEqual(e, tail_of_very_large_num(a, b, c, d))
            self.assertEqual(e, tail_of_very_large_num_opt(a, b, c, d))

    def test_single_tail_upper_constraints(self):
        inputs = [[500, 501, 502, 503], [1111, 2222, 3333, 4444],
                  [111111, 222222, 333333, 444444]]
        expected = ["719000501003", "154267476316", "045667596316"]

        for (a, b, c, d), e in zip(inputs, expected):
            self.assertEqual(e, tail_of_very_large_num(a, b, c, d))
            self.assertEqual(e, tail_of_very_large_num_opt(a, b, c, d))

    def test_HR_problem(self):
        input_lists = [
            ["1 2 3 4", "2 3 4 5", "3 4 5 6"],
            ["6 7 8 9", "12 13 14 15", "21 22 23 24", "41 42 43 44"]
             ]
        expected = ["000000003257", "431302938382"]

        for inputs, e in zip(input_lists, expected):
            args = list(map(lambda s: s.split(" "), inputs))
            self.assertEqual(e, tail_sum_of_very_large_nums(args))

    def test_speed(self):
        expected = "8739992577"
        solutions = {
            "Manual": [tail_of_non_mersenne_prime, True],
            "Built-In": [tail_of_non_mersenne_prime, False],
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
