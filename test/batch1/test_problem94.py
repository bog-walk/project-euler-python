import unittest
from solution.batch1.problem9 import *


class MyTestCase(unittest.TestCase):
    def test_find_triplets_none_found(self):
        nums = [1, 4, 6, 31, 99, 100]
        for n in nums:
            self.assertIsNone(pythagorean_triplets(n))

    def test_find_triplets_found(self):
        nums = [12, 24, 30, 90, 650, 1000, 2214, 3000]
        expected = (
            (3, 4, 5), (6, 8, 10), (5, 12, 13), (15, 36, 39),
            (25, 312, 313), (200, 375, 425), (533, 756, 925),
            (750, 1000, 1250)
        )
        for index, n in enumerate(nums):
            self.assertTupleEqual(expected[index], pythagorean_triplets(n))

    def test_max_triplets_product(self):
        nums = [1, 10, 1231, 12, 90, 1000, 3000]
        expected = [-1, -1, -1, 60, 21060, 31875000, 937500000]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], max_triplets_product(n))


if __name__ == '__main__':
    unittest.main()
