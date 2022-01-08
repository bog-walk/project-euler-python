import unittest
from util.tests.reusable import compare_speed_seconds
from solution.batch1.problem9 import max_triplet_brute, max_triplet_optimised, max_triplet_product


class SpecialPythagoreanTriplet(unittest.TestCase):
    def test_find_triplets_none_found(self):
        nums = [1, 4, 6, 31, 99, 100]
        for n in nums:
            self.assertIsNone(max_triplet_brute(n))
            self.assertIsNone(max_triplet_optimised(n))

    def test_find_triplets_found(self):
        nums = [12, 24, 30, 90, 650, 1000, 2214, 3000]
        expected = (
            (3, 4, 5), (6, 8, 10), (5, 12, 13), (15, 36, 39),
            (25, 312, 313), (200, 375, 425), (533, 756, 925),
            (750, 1000, 1250)
        )
        for index, n in enumerate(nums):
            self.assertTupleEqual(expected[index], max_triplet_brute(n))
            self.assertTupleEqual(expected[index], max_triplet_optimised(n))

    def test_compare_speed(self):
        n = 3000
        solutions = {
            "Brute": [max_triplet_brute, n],
            "Optimised": [max_triplet_optimised, n]
        }
        expected = (750, 1000, 1250)
        results = compare_speed_seconds(solutions, precision=5, repeat=10)
        self.assertTrue(all(expected == actual for actual in results.values()))

    def test_max_triplet_product(self):
        nums = [1, 10, 1231, 12, 90, 1000, 3000]
        expected = [-1, -1, -1, 60, 21060, 31875000, 937500000]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], max_triplet_product(n))


if __name__ == '__main__':
    unittest.main()
