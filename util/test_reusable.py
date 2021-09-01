import unittest
from util.reusable import *


class Reusable(unittest.TestCase):
    def test_lcm_valid(self):
        test_pairs = [(-2, -6), (-15, 30), (12, 18)]
        expected = [6, 30, 36]
        for index, (x, y) in enumerate(test_pairs):
            self.assertEqual(expected[index], least_common_multiple(x, y))

    def test_lcm_invalid(self):
        with self.assertRaises(ValueError):
            least_common_multiple(0, 2)


if __name__ == '__main__':
    unittest.main()
