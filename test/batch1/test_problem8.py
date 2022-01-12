import unittest
from util.tests.reusable import compare_speed_seconds
from solution.batch1.problem8 import *


class LargestProductInSeries(unittest.TestCase):
    def test_product(self):
        strings = ["8", "1234", "63972201", "1111111111111", "3675356291"]
        expected = [8, 24, 0, 1, 1020600]
        for i, s in enumerate(strings):
            self.assertEqual(expected[i], string_product(s))
            self.assertEqual(expected[i], digits_product(int(s)))

    def test_product_speed(self):
        series = "12345678987654331234567746756833426477362957402167"
        series_int = int(series)
        solutions = {
            "String Product": [string_product, series],
            "Digits Product": [digits_product, series_int]
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

    def test_largest_series_product_100_digits(self):
        string = "".join('6' if 60 <= i <= 65 else '1' for i in range(100))
        n, k = 100, 6
        expected = 46656  # 6 ** 6
        self.assertEqual(expected, largest_series_product_recursive(string, n, k))
        self.assertEqual(expected, largest_series_product(string, n, k))

    def test_largest_series_product_1000_digits(self):
        string = "73167176531330624919225119674426574742355349194934" \
                 "96983520312774506326239578318016984801869478851843" \
                 "85861560789112949495459501737958331952853208805511" \
                 "12540698747158523863050715693290963295227443043557" \
                 "66896648950445244523161731856403098711121722383113" \
                 "62229893423380308135336276614282806444486645238749" \
                 "30358907296290491560440772390713810515859307960866" \
                 "70172427121883998797908792274921901699720888093776" \
                 "65727333001053367881220235421809751254540594752243" \
                 "52584907711670556013604839586446706324415722155397" \
                 "53697817977846174064955149290862569321978468622482" \
                 "83972241375657056057490261407972968652414535100474" \
                 "82166370484403199890008895243450658541227588666881" \
                 "16427171479924442928230863465674813919123162824586" \
                 "17866458359124566529476545682848912883142607690042" \
                 "24219022671055626321111109370544217506941658960408" \
                 "07198403850962455444362981230987879927244284909188" \
                 "84580156166097919133875499200524063689912560717606" \
                 "05886116467109405077541002256983155200055935729725" \
                 "71636269561882670428252483600823257530420752963450"
        n = 1000
        k = [4, 13]
        expected = [5832, 23_514_624_000]
        for i, e in enumerate(expected):
            self.assertEqual(e, largest_series_product(string, n, k[i]))


if __name__ == '__main__':
    unittest.main()
