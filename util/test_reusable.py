import unittest
from util.reusable import *


class Reusable(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
