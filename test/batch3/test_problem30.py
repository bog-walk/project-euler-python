import unittest
from util.tests.reusable import compare_speed_seconds
from solution.batch3.problem30 import *


class DigitFifthPowers(unittest.TestCase):
    def test_all_but_upper(self):
        expected = [
            [153, 370, 371, 407],
            [1634, 8208, 9474],
            [4150, 4151, 54748, 92727, 93084, 194_979]
        ]
        for n in range(3, 6):
            self.assertListEqual(expected[n - 3], digit_nth_powers_brute(n))
            self.assertListEqual(expected[n - 3], digit_nth_powers_builtin(n))

    def test_digit_nth_powers_speed(self):
        n = 6
        expected = [548_834]
        solutions = {
            "Brute": [digit_nth_powers_brute, n],
            "Built-in": [digit_nth_powers_builtin, n]
        }
        results = compare_speed_seconds(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
