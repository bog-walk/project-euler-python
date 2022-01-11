import unittest
from util.tests.reusable import compare_speed_nano
from solution.batch3.problem29 import *


class DistinctPowers(unittest.TestCase):
    def test_distinct_power(self):
        nums = [2, 3, 4, 5, 10, 100]
        expected = [1, 4, 8, 15, 69, 9183]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], distinct_powers_brute(n))
            self.assertEqual(expected[index], distinct_power(n))
            self.assertEqual(expected[index], distinct_power_improved(n))

    def test_distinct_powers_speed(self):
        n = 1000
        expected = 977358
        solutions = {
            "Brute": [distinct_powers_brute, n],
            "Original": [distinct_power, n],
            "Improved": [distinct_power_improved, n]
        }
        results = compare_speed_nano(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
