import unittest
from reusable import *


class MathsReusable(unittest.TestCase):
    def test_gauss_sum(self):
        nums = [1, 2, 3, 50, 100, 2234]
        expected = [1, 3, 6, 1275, 5050, 2_496_495]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], gauss_sum(n))

    def test_is_coprime_all_true(self):
        inputs = [
            (1, 2), (2, 3), (3, 5), (4, 7), (4, 9), (5, 7), (5, 9), (11, 13),
            (14, 15), (17, 19), (29, 31), (3, 67), (99, 100), (34, 79), (54, 67)
        ]
        for x, y in inputs:
            self.assertTrue(is_coprime(x, y))

    def test_is_coprime_all_false(self):
        inputs = [(3, 12), (4, 18), (5, 5), (6, 10), (24, 57), (13, 117), (99, 102)]
        for x, y in inputs:
            self.assertFalse(is_coprime(x, y))

    def test_is_hexagonal_all_true(self):
        h_n_s = [1, 6, 15, 28, 45, 325, 703, 1326]
        expected = [1, 2, 3, 4, 5, 13, 19, 26]
        for i, h_n in enumerate(h_n_s):
            self.assertEqual(expected[i], is_hexagonal_number(h_n))

    def test_is_hexagonal_all_false(self):
        h_n_s = [2, 23, 100, 313, 691, 1111]
        for h_n in h_n_s:
            self.assertIsNone(is_hexagonal_number(h_n))

    def test_is_pentagonal_all_true(self):
        p_n_s = [1, 5, 12, 22, 35, 247, 532, 1001]
        expected = [1, 2, 3, 4, 5, 13, 19, 26]
        for i, p_n in enumerate(p_n_s):
            self.assertEqual(expected[i], is_pentagonal_number(p_n))

    def test_is_pentagonal_all_false(self):
        p_n_s = [2, 23, 100, 313, 691, 1111]
        for p_n in p_n_s:
            self.assertIsNone(is_pentagonal_number(p_n))

    def test_is_prime_all_true(self):
        primes = [
            2, 5, 11, 17, 29, 7919, 514_229, 9_369_319, 2_147_483_647,
            99_987_684_473, 999_973_156_643, 888_888_877_777_777,
            999_998_727_899_999
        ]
        for p in primes:
            self.assertTrue(is_prime(p))
            self.assertTrue(is_prime_mr(p))

    def test_is_prime_all_false(self):
        not_primes = [
            1, 4, 9, 14, 221, 9523, 22041, 997_653, 999_715_709, 99_987_684_471,
            3_889_108_085_625, 809_709_509_409_105
        ]
        for p in not_primes:
            self.assertFalse(is_prime(p))
            self.assertFalse(is_prime_mr(p))

    def test_is_triangular_all_true(self):
        t_n_s = [1, 3, 6, 10, 190, 325, 496, 595]
        expected = [1, 2, 3, 4, 19, 25, 31, 34]
        for i, t_n in enumerate(t_n_s):
            self.assertEqual(expected[i], is_triangular_number(t_n))

    def test_is_triangular_all_false(self):
        t_n_s = [2, 8, 46, 121, 173, 299, 403]
        for t_n in t_n_s:
            self.assertIsNone(is_triangular_number(t_n))

    def test_power_digit_sum(self):
        arguments = [
            (0, 0), (0, 1), (1, 0), (1, 10), (2, 0), (2, 2), (2, 9), (2, 31),
            (4, 5), (7, 10), (10, 100), (20, 10)
        ]
        expected = [1, 0, 1, 1, 1, 4, 8, 47, 7, 43, 1, 7]
        for i, (base, exp) in enumerate(arguments):
            self.assertEqual(expected[i], power_digit_sum(base, exp))

    def test_prime_factors_valid(self):
        nums = [2, 3, 4, 12, 100, 999]
        expected = [[2], [3], [2, 2], [2, 2, 3], [2, 2, 5, 5], [3, 3, 3, 37]]
        solutions = [
            prime_factors, prime_factors_og
        ]
        for solution in solutions:
            for i, n in enumerate(nums):
                factors = [[k] * v for k, v in solution(n).items()]
                flattened = sum(factors, [])
                self.assertListEqual(expected[i], flattened)

    def test_prime_factors_invalid(self):
        self.assertRaises(ValueError, prime_factors, 1)
        self.assertRaises(ValueError, prime_factors, 0)
        self.assertRaises(ValueError, prime_factors_og, 1)
        self.assertRaises(ValueError, prime_factors_og, 0)

    def test_prime_numbers_small(self):
        n = 30
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(expected, prime_numbers_og(n))
        self.assertEqual(expected, prime_numbers(n))

    def test_prime_numbers_large(self):
        n = 10_000
        expected_size = 1229
        expected_tail = [9887, 9901, 9907, 9923, 9929, 9931, 9941, 9949, 9967, 9973]
        actual_og = prime_numbers_og(n)
        actual = prime_numbers(n)
        self.assertEqual(expected_size, len(actual_og))
        self.assertEqual(expected_size, len(actual))
        self.assertEqual(expected_tail, actual_og[-10:])
        self.assertEqual(expected_tail, actual[-10:])

    def test_pythagorean_triplet_valid(self):
        arguments = [(2, 1, 1), (3, 2, 1), (4, 1, 1), (4, 3, 1)]
        expected = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)]
        for i, (m, n, d) in enumerate(arguments):
            self.assertTupleEqual(expected[i], pythagorean_triplet(m, n, d))

    def test_pythagorean_triplet_invalid(self):
        self.assertRaises(ValueError, pythagorean_triplet, 1, 0, 1)
        self.assertRaises(ValueError, pythagorean_triplet, 1, 10, 1)
        self.assertRaises(ValueError, pythagorean_triplet, 2, 2, 1)
        self.assertRaises(ValueError, pythagorean_triplet, 5, 3, 1)
        self.assertRaises(ValueError, pythagorean_triplet, 9, 3, 1)

    def test_sum_proper_divisors(self):
        nums = [1, 2, 3, 12, 20, 36, 49, 220, 284, 999, 5500, 100_000]
        expected = [0, 1, 1, 16, 22, 55, 8, 284, 220, 521, 7604, 146_078]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], sum_proper_divisors_og(n))
            self.assertEqual(expected[i], sum_proper_divisors(n))


if __name__ == '__main__':
    unittest.main()
