import unittest
from solution.batch1.problem7 import *


class The10001stPrime(unittest.TestCase):
    def test_is_prime_all_true(self):
        primes = [2, 5, 11, 17, 29]
        for prime in primes:
            self.assertTrue(is_prime(prime))

    def test_is_prime_all_false(self):
        non_primes = [1, 4, 9, 14]
        for prime in non_primes:
            self.assertFalse(is_prime(prime))

    def test_nth_prime_lower_constraints(self):
        test_n = [1, 2, 3]
        expected = [2, 3, 5]
        for index, n in enumerate(test_n):
            self.assertEqual(expected[index], nth_prime(n))

    def test_nth_prime_normal_values(self):
        test_n = [6, 20, 62]
        expected = [13, 71, 293]
        for index, n in enumerate(test_n):
            self.assertEqual(expected[index], nth_prime(n))

    def test_nth_prime_large_values(self):
        test_n = [289, 919, 1000]
        expected = [1879, 7193, 7919]
        for index, n in enumerate(test_n):
            self.assertEqual(expected[index], nth_prime(n))

    def test_nth_prime_upper_constraints(self):
        test_n = [5000, 10000, 10001]
        expected = [48611, 104729, 104743]
        for index, n in enumerate(test_n):
            self.assertEqual(expected[index], nth_prime(n))


if __name__ == '__main__':
    unittest.main()
