import unittest
from time import perf_counter

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
        start_brute = perf_counter()
        result_brute = None
        for _ in range(10):
            result_brute = max_triplet_brute(n)
        stop_brute = perf_counter()
        start_optimised = perf_counter()
        result_optimised = None
        for _ in range(10):
            result_optimised = max_triplet_optimised(n)
        stop_optimised = perf_counter()
        print(f"Brute took: {stop_brute - start_brute:.5f}s\n"
              f"Optimised took: {stop_optimised - start_optimised:.5f}s")
        self.assertEqual(result_brute, result_optimised)

    def test_max_triplet_product(self):
        nums = [1, 10, 1231, 12, 90, 1000, 3000]
        expected = [-1, -1, -1, 60, 21060, 31875000, 937500000]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], max_triplet_product(n))


if __name__ == '__main__':
    unittest.main()
