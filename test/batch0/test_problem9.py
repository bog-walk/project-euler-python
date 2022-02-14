import unittest
from util.tests.reusable import compare_speed
from solution.batch0.problem9 import max_triplet_product_loop_c_b, \
    max_triplet_product_optimised, max_triplet_product_loop_a


class SpecialPythagoreanTriplet(unittest.TestCase):
    def test_max_triplet_none_found(self):
        nums = [1, 4, 6, 10, 31, 99, 100, 1231]
        expected = -1,
        for n in nums:
            self.assertTupleEqual(expected, max_triplet_product_loop_c_b(n))
            self.assertTupleEqual(expected, max_triplet_product_optimised(n))
            self.assertTupleEqual(expected, max_triplet_product_loop_a(n))

    def test_max_triplet_found(self):
        nums = [12, 24, 30, 90, 650, 1000, 2214]
        expected = (
            (60, 3, 4, 5), (480, 6, 8, 10), (780, 5, 12, 13), (21060, 15, 36, 39),
            (2_441_400, 25, 312, 313), (31_875_000, 200, 375, 425),
            (372_726_900, 533, 756, 925)
        )
        for i, n in enumerate(nums):
            self.assertTupleEqual(expected[i], max_triplet_product_loop_c_b(n))
            self.assertTupleEqual(expected[i], max_triplet_product_optimised(n))
            self.assertTupleEqual(expected[i], max_triplet_product_loop_a(n))

    def test_max_triplet_product_speed(self):
        n = 3000
        solutions = {
            "Brute": [max_triplet_product_loop_c_b, n],
            "Optimised": [max_triplet_product_optimised, n],
            "Formula": [max_triplet_product_loop_a, n]
        }
        expected = (937_500_000, 750, 1000, 1250)
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
