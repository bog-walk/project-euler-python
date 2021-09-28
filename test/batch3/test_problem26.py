import unittest
from solution.batch3.problem26 import *


class ReciprocalCycles(unittest.TestCase):
    def test_longest_repetend_denominator(self):
        nums = [5, 10, 14, 19, 25, 46, 50, 70, 1000, 10000]
        expected = [3, 7, 7, 17, 23, 29, 47, 61, 983, 9967]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], longest_repetend_denominator_primes(n))
            self.assertEqual(expected[index], longest_repetend_denominator(n))


if __name__ == '__main__':
    unittest.main()
