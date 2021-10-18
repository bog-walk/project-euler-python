import unittest
from solution.batch3.problem29 import *


class DistinctPowers(unittest.TestCase):
    def test_distinct_power(self):
        nums = [2, 3, 4, 5, 10, 100]
        expected = [1, 4, 8, 15, 69, 9183]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], distinct_powers_brute(n))
            self.assertEqual(expected[index], distinct_power(n))


if __name__ == '__main__':
    unittest.main()
