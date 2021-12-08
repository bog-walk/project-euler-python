import unittest
from solution.batch4.problem38 import find_pandigital_multipliers


class PandigitalMultiples(unittest.TestCase):
    def test_find_pandigital_multipliers_small_N(self):
        n = 100
        expected = [[18, 78], [9]]
        for k in range(8, 10):
            self.assertEqual(expected[k - 8], find_pandigital_multipliers(n, k))


if __name__ == '__main__':
    unittest.main()
