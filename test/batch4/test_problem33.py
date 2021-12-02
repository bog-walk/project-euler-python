import unittest
from time import perf_counter
from solution.batch4.problem33 import *


class DigitCancellingFractions(unittest.TestCase):
    def test_is_reduced_equivalent_all_true(self):
        fractions = [[16, 64], [26, 65], [1249, 9992], [4999, 9998]]
        for (num, denom) in fractions:
            n = len(str(num))
            self.assertTrue(is_reduced_equivalent(n, num, denom, 1))

    def test_is_reduced_equivalent_all_false(self):
        fractions = [[11, 19], [47, 71], [328, 859], [8777, 7743]]
        for (num, denom) in fractions:
            n = len(str(num))
            self.assertFalse(is_reduced_equivalent(n, num, denom, 1))

    def test_is_reduced_equivalent_all_k(self):
        fractions = [[16, 64], [166, 664], [1666, 6664]]
        for (num, denom) in fractions:
            n = len(str(num))
            for k in range(1, 4):
                if k >= n:
                    break
                self.assertTrue(is_reduced_equivalent(n, num, denom, k))

    def test_find_non_trivials_k1(self):
        expected = [
            [[16, 64], [19, 95], [26, 65], [49, 98]],
            [[166, 664], [199, 995], [217, 775], [249, 996], [266, 665], [499, 998]],
            [[1249, 9992], [1666, 6664], [1999, 9995], [2177, 7775], [2499, 9996],
             [2666, 6665], [4999, 9998]]
        ]
        for n in range(2, 5):
            self.assertListEqual(expected[n - 2], find_non_trivials_brute(n, 1))
            improved_actual = find_non_trivials(n, 1)
            self.assertEqual(len(expected[n - 2]), len(improved_actual))
            for fraction in improved_actual:
                self.assertIn(fraction, expected[n - 2])

    def test_find_non_trivials_k2(self):
        expected = [[166, 664], [199, 995], [266, 665], [484, 847], [499, 998]]
        self.assertListEqual(expected, find_non_trivials_brute(3, 2))
        improved_actual = find_non_trivials(3, 2)
        self.assertEqual(len(expected), len(improved_actual))
        for fraction in improved_actual:
            self.assertIn(fraction, expected)

    def test_product_of_non_trivials(self):
        self.assertEqual(100, product_of_non_trivials())

    def test_find_non_trivials_speed_comparison(self):
        n, k = 4, 1
        expected = [17255, 61085]  # sums of numerators & denominators
        solutions = [find_non_trivials_brute, find_non_trivials]
        starts = []
        stops = []
        for solution in solutions:
            starts.append(perf_counter())
            actual_n, actual_d = map(list, zip(*solution(n, k)))
            self.assertEqual(expected[0], sum(actual_n))
            self.assertEqual(expected[1], sum(actual_d))
            stops.append(perf_counter())
        print(f"Brute solution took: {stops[0] - starts[0]:0.4f}s\n"
              f"Improved solution took: {stops[1] - starts[1]:0.4f}s\n")

    def test_find_sum_of_non_trivials_k1(self):
        expected = [(110, 322), (77262, 163829)]
        for n in range(2, 4):
            self.assertTupleEqual(expected[n - 2], sum_of_non_trivials_brute(n, 1))
            self.assertTupleEqual(expected[n - 2], sum_of_non_trivials_gcd(n, 1))

    def test_find_sum_of_non_trivials_k2(self):
        expected = [(7429, 17305), (3571225, 7153900)]
        for n in range(3, 5):
            self.assertTupleEqual(expected[n - 3], sum_of_non_trivials_brute(n, 2))
            self.assertTupleEqual(expected[n - 3], sum_of_non_trivials_gcd(n, 2))

    def test_find_sum_of_non_trivials_k3(self):
        expected = (255983, 467405)
        self.assertTupleEqual(expected, sum_of_non_trivials_brute(4, 3))
        self.assertTupleEqual(expected, sum_of_non_trivials_gcd(4, 3))

    def test_find_sum_of_non_trivials_speed_comparison(self):
        n, k = 4, 1
        expected = (12999936, 28131911)
        solutions = [sum_of_non_trivials_brute, sum_of_non_trivials_gcd]
        starts = []
        stops = []
        for solution in solutions:
            starts.append(perf_counter())
            self.assertTupleEqual(expected, solution(n, k))
            stops.append(perf_counter())
        print(f"Brute solution took: {stops[0] - starts[0]:0.4f}s\n"
              f"GCD solution took: {stops[1] - starts[1]:0.4f}s\n")


if __name__ == '__main__':
    unittest.main()
