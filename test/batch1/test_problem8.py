import unittest
from time import perf_counter
from solution.batch1.problem8 import *


class LargestProductInSeries(unittest.TestCase):
    def test_product(self):
        series = ["8", "1234", "63972201", "1111111111111", "3675356291"]
        expected = [8, 24, 0, 1, 1020600]
        for index, s in enumerate(series):
            self.assertEqual(expected[index], string_product(s))
            self.assertEqual(expected[index], digits_product(int(s)))

    def test_compare_product_speed(self):
        series = "1234567898765433123456774675683342647"
        sp_start = perf_counter()
        result_sp = 0
        for _ in range(1000):
            result_sp = string_product(series)
        sp_stop = perf_counter()
        dp_start = perf_counter()
        result_dp = 0
        for _ in range(1000):
            result_dp = digits_product(int(series))
        dp_stop = perf_counter()
        print(f"String_Product took {sp_stop - sp_start:0.5f}s\n"
              f"Digits_Product took {dp_stop - dp_start:0.5f}s")
        self.assertEqual(result_sp, result_dp)

    def test_largest_series_product_N_is_1(self):
        series = "8"
        self.assertEqual(8, largest_series_product_recursive(series, len(series), 1))
        self.assertEqual(8, largest_series_product(series, len(series), 1))

    def test_largest_series_product_K_is_1(self):
        series = "63972201"
        self.assertEqual(9, largest_series_product_recursive(series, len(series), 1))
        self.assertEqual(9, largest_series_product(series, len(series), 1))

    def test_largest_series_product_N_equals_K(self):
        series = "1111111111111"
        self.assertEqual(1, largest_series_product_recursive(series, len(series), len(series)))
        self.assertEqual(1, largest_series_product(series, len(series), len(series)))

    def test_largest_series_product_N_has_0_in_all_series(self):
        series = "2709360626"
        self.assertEqual(0, largest_series_product_recursive(series, len(series), 5))
        self.assertEqual(0, largest_series_product(series, len(series), 5))

    def test_largest_series_product_N_has_0_in_some_series(self):
        series = "12034"
        self.assertEqual(12, largest_series_product_recursive(series, len(series), 2))
        self.assertEqual(12, largest_series_product(series, len(series), 2))

    def test_largest_series_product_N_is_normal(self):
        series = "3675356291"
        self.assertEqual(3150, largest_series_product_recursive(series, len(series), 5))
        self.assertEqual(3150, largest_series_product(series, len(series), 5))

    def test_largest_series_product_100_digits(self):
        series = "".join('6' if 60 <= i <= 65 else '1' for i in range(100))
        expected = 46656  # 6 ** 6
        self.assertEqual(expected, largest_series_product_recursive(series, len(series), 6))
        self.assertEqual(expected, largest_series_product(series, len(series), 6))

    def test_largest_series_product_1000_digits(self):
        series = "73167176531330624919225119674426574742355349194934" \
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
        self.assertEqual(5832, largest_series_product(series, len(series), 4))
        self.assertEqual(23514624000, largest_series_product(series, len(series), 13))


if __name__ == '__main__':
    unittest.main()
