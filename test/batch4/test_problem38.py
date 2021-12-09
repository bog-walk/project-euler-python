import unittest
from solution.batch4.problem38 import *


class PandigitalMultiples(unittest.TestCase):
    def test_find_pandigital_multipliers_small_N(self):
        n = 100
        expected = [[18, 78], [9]]
        for k in range(8, 10):
            self.assertEqual(expected[k - 8], find_pandigital_multipliers(n, k))

    def test_find_pandigital_multipliers_mid_N(self):
        n = 1000
        expected = [[18, 78], [9, 192, 219, 273, 327]]
        for k in range(8, 10):
            self.assertEqual(expected[k - 8], find_pandigital_multipliers(n, k))

    def test_find_pandigital_multipliers_high_N(self):
        n = 10000
        expected = [
            [18, 78, 1728, 1764, 1782, 1827, 2178, 2358, 2718, 2817, 3564, 3582, 4176, 4356],
            [9, 192, 219, 273, 327, 6729, 6792, 6927, 7269, 7293, 7329, 7692, 7923, 7932, 9267, 9273, 9327]
        ]
        for k in range(8, 10):
            self.assertEqual(expected[k - 8], find_pandigital_multipliers(n, k))

    def test_largest_9_pandigital(self):
        expected = "932718654"
        self.assertEqual(expected, largest_9_pandigital())


if __name__ == '__main__':
    unittest.main()
