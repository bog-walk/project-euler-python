import unittest
from solution.batch5.problem41 import largest_pandigital_prime_brute, \
    largest_pandigital_prime_improved


class PandigitalPrime(unittest.TestCase):
    def test_largest_pandigital_prime(self):
        nums = [10, 100, 2140, 10_000, 100_000, 1_000_000, 7_652_412, 10_000_000]
        expected = [-1, -1, 1423, 4231, 4231, 4231, 7642513, 7652413]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], largest_pandigital_prime_improved(n))

    def test_largest_pandigital_prime_existing(self):
        expected = 7652413
        self.assertEqual(expected, largest_pandigital_prime_brute())


if __name__ == '__main__':
    unittest.main()
