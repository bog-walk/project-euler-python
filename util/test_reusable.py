import unittest
from time import perf_counter
from util.reusable import *


class Reusable(unittest.TestCase):
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
            self.assertEqual(expected[index], least_common_multiple(x, y))

    def test_lcm_invalid(self):
        with self.assertRaises(ValueError):
            least_common_multiple(0, 2)

    def test_prime_numbers_small(self):
        n = 30
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(expected, prime_numbers(n))

    def test_prime_numbers_large(self):
        n = 10000
        expected_size = 1229
        expected_tail = [9887, 9901, 9907, 9923, 9929, 9931, 9941, 9949, 9967, 9973]
        actual = prime_numbers(n)
        self.assertEqual(expected_size, len(actual))
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

    def test_is_palindrome_all_true(self):
        test_n = [5, 22, 303, 9119]
        for n in test_n:
            self.assertTrue(is_palindrome(n))
            self.assertTrue(is_palindrome_recursive(str(n)))
            self.assertTrue(is_palindrome_no_cast(n))

    def test_is_palindrome_all_false(self):
        test_n = [10, 523, 8018, 124521]
        for n in test_n:
            self.assertFalse(is_palindrome(n))
            self.assertFalse(is_palindrome_recursive(str(n)))
            self.assertFalse(is_palindrome_no_cast(n))

    def test_is_palindrome_speed_comparison(self):
        n = 987654321123456789
        solutions = [
            is_palindrome, is_palindrome_no_cast, is_palindrome_recursive
        ]
        starts = []
        stops = []
        for s in range(3):
            if s == 2:
                n = str(n)
            ans = False
            starts.append(perf_counter())
            for _ in range(1000):
                ans = solutions[s](n)
            stops.append(perf_counter())
            self.assertTrue(ans)
        print(f"String in-built solution took: {stops[0] - starts[0]:0.4f}s\n"
              f"String recursive solution took: {stops[2] - starts[2]:0.4f}s\n"
              f"Maths only solution took: {stops[1] - starts[1]:0.4f}s\n")


if __name__ == '__main__':
    unittest.main()
