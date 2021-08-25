import unittest
from solution.batch1.problem3 import *


class LargestPrimeFactor(unittest.TestCase):
    def test_lower_constraints(self):
        self.assertEqual(5, largest_prime_factor(10))
        self.assertEqual(5, largest_prime_factor_recursive(10))

    def test_n_is_small_prime(self):
        self.assertEqual(17, largest_prime_factor(17))
        self.assertEqual(17, largest_prime_factor_recursive(17))

    def test_normal_n(self):
        test_n = [48, 330]
        expected = [3, 11]
        for i, n in enumerate(test_n):
            self.assertEqual(expected[i], largest_prime_factor(n))
            self.assertEqual(expected[i], largest_prime_factor_recursive(n))

    def test_large_n(self):
        test_n = [13195, 200000, 600851475143]
        expected = [29, 5, 6857]
        for i, n in enumerate(test_n):
            self.assertEqual(expected[i], largest_prime_factor(n))
            self.assertEqual(expected[i], largest_prime_factor_recursive(n))

    def test_n_is_large_prime(self):
        test_n = [7919, 2147483647, 67280421310721]
        expected = [7919, 2147483647, 67280421310721]
        for i, n in enumerate(test_n):
            self.assertEqual(expected[i], largest_prime_factor(n))
            self.assertEqual(expected[i], largest_prime_factor_recursive(n))

    def test_upper_constraints(self):
        test_n = [9007199254740991, 10000000000000000]
        expected = [20394401, 5]
        for i, n in enumerate(test_n):
            self.assertEqual(expected[i], largest_prime_factor(n))
            self.assertEqual(expected[i], largest_prime_factor_recursive(n))


if __name__ == '__main__':
    unittest.main()
