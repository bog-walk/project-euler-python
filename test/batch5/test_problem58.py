import unittest
from util.tests.reusable import compare_speed
from solution.batch5.problem58 import spiral_prime_ratio


class SpiralPrimes(unittest.TestCase):
    def test_lower_constraints(self):
        percents = [8, 9, 10, 11, 12, 15]
        expected = [238_733, 74373, 26241, 12201, 6523, 981]
        for i, n in enumerate(percents):
            self.assertEqual(expected[i], spiral_prime_ratio(n, speed_toggle=True))

    def test_mid_constraints(self):
        percents = [20, 25, 30, 40]
        expected = [309, 99, 49, 31]
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
            "Original prime": [spiral_prime_ratio, percent],
            "Miller-Rabin": [spiral_prime_ratio, percent, True]
        }
        results = compare_speed(solutions, precision=3)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
