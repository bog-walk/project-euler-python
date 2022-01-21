import unittest
from util.tests.reusable import compare_speed_seconds
from solution.batch6.problem58 import spiral_prime_ratio, spiral_prime_ratio_mr


class SpiralPrimes(unittest.TestCase):
    def test_lower_constraints(self):
        percents = [8, 10, 15]
        expected = [238_733, 26241, 981]
        for i, n in enumerate(percents):
            self.assertEqual(expected[i], spiral_prime_ratio(n))

    def test_mid_values(self):
        percents = [20, 30, 40]
        expected = [309, 49, 31]
        for i, n in enumerate(percents):
            self.assertEqual(expected[i], spiral_prime_ratio(n))

    def test_upper_constraints(self):
        percents = [50, 55, 60]
        expected = [11, 9, 5]
        for i, n in enumerate(percents):
            self.assertEqual(expected[i], spiral_prime_ratio(n))

    def test_speed(self):
        percent = 10
        expected = 26241
        solutions = {
            "OG": [spiral_prime_ratio, percent],
            "MR": [spiral_prime_ratio_mr, percent]
        }
        results = compare_speed_seconds(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
