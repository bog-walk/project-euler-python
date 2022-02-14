import unittest
from util.tests.reusable import compare_speed
from solution.batch3.problem33 import *


class DigitCancellingFractions(unittest.TestCase):
    def test_is_reduced_equivalent_all_true(self):
        k = 1
        fractions = [(16, 64), (26, 65), (1249, 9992), (4999, 9998)]
        for num, denom in fractions:
            n = len(str(num))
            self.assertTrue(is_reduced_equivalent(n, num, denom, k))

    def test_is_reduced_equivalent_all_false(self):
        k = 1
        fractions = [(11, 19), (47, 71), (328, 859), (8777, 7743)]
        for num, denom in fractions:
            n = len(str(num))
            self.assertFalse(is_reduced_equivalent(n, num, denom, k))

    def test_is_reduced_equivalent_all_k(self):
        fractions = [(16, 64), (166, 664), (1666, 6664)]
        for num, denom in fractions:
            n = len(str(num))
            for k in range(1, 4):
                if k >= n:
                    break
                self.assertTrue(is_reduced_equivalent(n, num, denom, k))

    def test_find_non_trivials_k1(self):
        k = 1
        expected = [
            [(16, 64), (19, 95), (26, 65), (49, 98)],
            [(166, 664), (199, 995), (217, 775), (249, 996), (266, 665), (499, 998)],
            [(1249, 9992), (1666, 6664), (1999, 9995), (2177, 7775), (2499, 9996),
             (2666, 6665), (4999, 9998)]
        ]
        for n in range(2, 5):
            self.assertListEqual(expected[n - 2], find_non_trivials_brute(n, k))
            self.assertListEqual(expected[n - 2], find_non_trivials(n, k))

    def test_find_non_trivials_k2(self):
        n, k = 3, 2
        expected = [(166, 664), (199, 995), (266, 665), (484, 847), (499, 998)]
        self.assertListEqual(expected, find_non_trivials_brute(n, k))
        self.assertListEqual(expected, find_non_trivials(n, k))

    def test_PE_problem(self):
        expected = 100
        self.assertEqual(expected, product_of_non_trivials())

    def test_find_non_trivials_speed(self):
        n, k = 4, 1
        expected = [17255, 61085]  # sums of numerators & denominators
        solutions = {
            "Brute": [find_non_trivials_brute, n, k],
            "Improved": [find_non_trivials, n, k]
        }
        results = compare_speed(solutions, precision=2)
        for actual in results.values():
            actual_n, actual_d = map(list, zip(*actual))
            self.assertEqual(expected[0], sum(actual_n))
            self.assertEqual(expected[1], sum(actual_d))

    def test_get_cancelled_combos(self):
        to_cancel = [
            ("9919", ('9', '9')), ("1233", ('1', '2', '3')),
            ("1051", ('1', '5')), ("5959", ('9'))
        ]
        expected = [{19, 91}, {3}, {1, 10}, {559, 595}]
        for i, (num, combo) in enumerate(to_cancel):
            self.assertSetEqual(expected[i], get_cancelled_combos(num, combo))

    def test_HR_problem_k1(self):
        k = 1
        expected = [(110, 322), (77262, 163_829)]
        for n in range(2, 4):
            self.assertTupleEqual(expected[n - 2], sum_of_non_trivials_brute(n, k))
            self.assertTupleEqual(expected[n - 2], sum_of_non_trivials_gcd(n, k))

    def test_HR_problem_k2(self):
        k = 2
        expected = [(7429, 17305), (3_571_225, 7_153_900)]
        for n in range(3, 5):
            self.assertTupleEqual(expected[n - 3], sum_of_non_trivials_brute(n, k))
            self.assertTupleEqual(expected[n - 3], sum_of_non_trivials_gcd(n, k))

    def test_HR_problem_k3(self):
        n, k = 4, 3
        expected = (255_983, 467_405)
        self.assertTupleEqual(expected, sum_of_non_trivials_brute(n, k))
        self.assertTupleEqual(expected, sum_of_non_trivials_gcd(n, k))

    def test_find_sum_of_non_trivials_speed(self):
        n, k = 4, 1
        expected = (12_999_936, 28_131_911)
        solutions = {
            "Brute": [sum_of_non_trivials_brute, n, k],
            "GCD": [sum_of_non_trivials_gcd, n, k]
        }
        results = compare_speed(solutions, precision=2)
        for actual in results.values():
            self.assertTupleEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
