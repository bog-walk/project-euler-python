import unittest
from util.tests.reusable import compare_speed
from solution.batch6.problem63 import *


class PowerfulDigitCounts(unittest.TestCase):
    def test_HR_problem_lower_constraints(self):
        expected = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9], [16, 25, 36, 49, 64, 81],
            [125, 216, 343, 512, 729], [1296, 2401, 4096, 6561]
        ]
        for n in range(1, 5):
            self.assertListEqual(expected[n - 1], n_digit_nth_powers(n))

    def test_HR_problem_mid_constraints(self):
        expected = [
            [1_073_741_824, 3_486_784_401], [31_381_059_609],
            [282_429_536_481]
        ]
        for n in range(10, 13):
            self.assertListEqual(expected[n - 10], n_digit_nth_powers(n))

    def test_HR_problem_upper_constraints(self):
        n = 19
        expected = [1_350_851_717_672_992_089]
        self.assertListEqual(expected, n_digit_nth_powers(n))

    def test_PE_problem_and_speed(self):
        expected = 49
        solutions = {
            "Brute": [all_n_digit_nth_powers_brute],
            "Formula": [all_n_digit_nth_powers_formula]
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
