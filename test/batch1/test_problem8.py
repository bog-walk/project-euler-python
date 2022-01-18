import unittest
from util.tests.reusable import compare_speed_seconds, get_test_resource
from solution.batch1.problem8 import *


class LargestProductInSeries(unittest.TestCase):
    def test_product(self):
        strings = ["8", "1234", "63972201", "1111111111111", "3675356291"]
        expected = [8, 24, 0, 1, 1020600]
        for i, s in enumerate(strings):
            self.assertEqual(expected[i], string_product(s))
            self.assertEqual(expected[i], digits_product(int(s)))

    def test_product_speed(self):
        string = "12345678987654331234567746756833426477362957402167"
        string_int = int(string)
        solutions = {
            "String Product": [string_product, string],
            "Digits Product": [digits_product, string_int]
        }
        results = list(
            compare_speed_seconds(solutions, precision=5, repeat=1000).values()
        )
        self.assertEqual(results[0], results[1])

    def test_largest_series_product_N_is_1(self):
        string = "8"
        n, k = 1, 1
        expected = 8
        self.assertEqual(expected, largest_series_product_recursive(string, n, k))
        self.assertEqual(expected, largest_series_product(string, n, k))

    def test_largest_series_product_K_is_1(self):
        string = "63972201"
        n, k = len(string), 1
        expected = 9
        self.assertEqual(expected, largest_series_product_recursive(string, n, k))
        self.assertEqual(expected, largest_series_product(string, n, k))

    def test_largest_series_product_N_equals_K(self):
        string = "1111111111111"
        n, k = len(string), 1
        expected = 1
        self.assertEqual(expected, largest_series_product_recursive(string, n, k))
        self.assertEqual(expected, largest_series_product(string, n, k))

    def test_largest_series_product_N_has_0_in_all_k(self):
        string = "2709360626"
        n, k = len(string), 5
        expected = 0
        self.assertEqual(expected, largest_series_product_recursive(string, n, k))
        self.assertEqual(expected, largest_series_product(string, n, k))

    def test_largest_series_product_N_has_0_in_some_series(self):
        string = "12034"
        n, k = len(string), 2
        expected = 12
        self.assertEqual(expected, largest_series_product_recursive(string, n, k))
        self.assertEqual(expected, largest_series_product(string, n, k))

    def test_largest_series_product_N_is_normal(self):
        string = "3675356291"
        n, k = len(string), 5
        expected = 3150
        self.assertEqual(expected, largest_series_product_recursive(string, n, k))
        self.assertEqual(expected, largest_series_product(string, n, k))

    def test_largest_series_product_speed(self):
        string = "".join('6' if 60 <= i <= 65 else '1' for i in range(100))
        n, k = 100, 6
        expected = 46656  # 6 ** 6
        solutions = {
            "Recursive": [largest_series_product_recursive, string, n, k],
            "Iterative": [largest_series_product, string, n, k]
        }
        results = compare_speed_seconds(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))

    def test_largest_series_product_1000_digits(self):
        string = "".join(
            get_test_resource("../resources/largest_product_in_series_1000")
        )
        n = 1000
        k = [4, 13]
        expected = [5832, 23_514_624_000]
        for i, e in enumerate(expected):
            self.assertEqual(e, largest_series_product(string, n, k[i]))


if __name__ == '__main__':
    unittest.main()
