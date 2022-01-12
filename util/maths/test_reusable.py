import unittest
from reusable import *


class MathsReusable(unittest.TestCase):
    def test_prime_factors(self):
        nums = [2, 12, 100, 999]
        expected = [[2], [2, 2, 3], [2, 2, 5, 5], [3, 3, 3, 37]]
        for index, n in enumerate(nums):
            factors = [[k] * v for k, v in prime_factors(n).items()]
            flattened = sum(factors, [])
            self.assertListEqual(expected[index], flattened)

    def test_lcm_valid(self):
        test_pairs = [(-2, -6), (-15, 30), (12, 18)]
        expected = [6, 30, 36]
        for index, (x, y) in enumerate(test_pairs):
            self.assertEqual(expected[index], lcm(x, y))

    def test_lcm_invalid(self):
        with self.assertRaises(ValueError):
            lcm(0, 2)

    def test_prime_numbers_small(self):
        n = 30
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(expected, prime_numbers_og(n))
        self.assertEqual(expected, prime_numbers(n))

    def test_prime_numbers_large(self):
        n = 10000
        expected_size = 1229
        expected_tail = [9887, 9901, 9907, 9923, 9929, 9931, 9941, 9949, 9967, 9973]
        actual_og = prime_numbers_og(n)
        actual = prime_numbers(n)
        self.assertEqual(expected_size, len(actual_og))
        self.assertEqual(expected_size, len(actual))
        self.assertEqual(expected_tail, actual_og[-10:])
        self.assertEqual(expected_tail, actual[-10:])

    def test_gaussian_sum(self):
        nums = [1, 2, 3, 50, 100, 2234]
        expected = [1, 3, 6, 1275, 5050, 2496495]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], gaussian_sum(n))

    def test_sum_proper_divisors(self):
        nums = [1, 2, 3, 12, 20, 36, 49, 220, 284, 999, 5500, 100000]
        expected = [0, 1, 1, 16, 22, 55, 8, 284, 220, 521, 7604, 146078]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], sum_proper_divisors_og(n))
            self.assertEqual(expected[index], sum_proper_divisors_pf(n))

    def test_is_prime_all_true(self):
        primes = [2, 5, 11, 17, 29]
        for p in primes:
            self.assertTrue(is_prime(p))

    def test_is_prime_all_false(self):
        not_primes = [1, 4, 9, 14]
        for p in not_primes:
            self.assertFalse(is_prime(p))

    def test_pythagorean_triple(self):
        expected = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (12, 16, 20), (7, 24, 25)]
        actual = []
        for m in range(2, 5):
            for n in range(1, m):
                actual.append(pythagorean_triplet(m, n, d=1))
        self.assertListEqual(expected, actual)

    def test_is_triangular_all_true(self):
        t_n_s = [1, 3, 6, 10, 190, 325, 496, 595]
        expected = [1, 2, 3, 4, 19, 25, 31, 34]
        for i, t_n in enumerate(t_n_s):
            self.assertEqual(expected[i], is_triangular_number(t_n))

    def test_is_triangular_all_false(self):
        t_n_s = [2, 8, 46, 121, 173, 299, 403]
        for t_n in t_n_s:
            self.assertIsNone(is_triangular_number(t_n))

    def test_is_pentagonal_all_true(self):
        p_n_s = [1, 5, 12, 22, 35, 247, 532, 1001]
        expected = [1, 2, 3, 4, 5, 13, 19, 26]
        for i, p_n in enumerate(p_n_s):
            self.assertEqual(expected[i], is_pentagonal_number(p_n))

    def test_is_pentagonal_all_false(self):
        p_n_s = [2, 23, 100, 313, 691, 1111]
        for p_n in p_n_s:
            self.assertIsNone(is_pentagonal_number(p_n))


if __name__ == '__main__':
    unittest.main()
