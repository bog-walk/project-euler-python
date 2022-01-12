import unittest
from util.tests.reusable import compare_speed_seconds
from solution.batch5.problem48 import *


class SelfPowers(unittest.TestCase):
    def test_self_powers_sum_low(self):
        nums = [1, 2, 3, 4, 6, 10]
        expected = [1, 5, 32, 288, 50069, 405_071_317]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], self_powers_sum(n))
            self.assertEqual(expected[i], self_powers_sum_modulo(n))

    def test_self_powers_sum_mid(self):
        nums = [99, 1000, 8431]
        expected = [9_027_641_920, 9_110_846_700, 2_756_754_292]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], self_powers_sum(n))
            self.assertEqual(expected[i], self_powers_sum_modulo(n))

    def test_self_powers_sum_speed(self):
        n = 10_000
        expected = 6_237_204_500
        solutions = {
            "Brute": [self_powers_sum, n],
            "Mod": [self_powers_sum_modulo, n]
        }
        results = compare_speed_seconds(solutions, precision=3)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
