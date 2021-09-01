import unittest
from solution.batch1.problem5 import *


class SmallestMultiple(unittest.TestCase):
    def test_lcm_of_range_lower_constraints(self):
        test_n = [1, 2, 3]
        expected = [1, 2, 6]
        for index, n in enumerate(test_n):
            self.assertEqual(expected[index], lcm_of_range(n))
            self.assertEqual(expected[index], lcm_of_range_reduce(n))

    def test_lcm_of_range_normals(self):
        test_n = [6, 10, 20]
        expected = [60, 2520, 232792560]
        for index, n in enumerate(test_n):
            self.assertEqual(expected[index], lcm_of_range(n))
            self.assertEqual(expected[index], lcm_of_range_reduce(n))

    def test_lcm_of_range_upper_constraints(self):
        test_n = [30, 40]
        expected = [2329089562800, 5342931457063200]
        for index, n in enumerate(test_n):
            self.assertEqual(expected[index], lcm_of_range(n))
            self.assertEqual(expected[index], lcm_of_range_reduce(n))


if __name__ == '__main__':
    unittest.main()
