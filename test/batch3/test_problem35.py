import unittest
from solution.batch3.problem35 import get_circular_primes, sum_circular_primes


class CircularPrimes(unittest.TestCase):
    def test_get_circular_primes_lower_constraints(self):
        n = 100
        expected = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
        self.assertListEqual(expected, sorted(get_circular_primes(n)))

    def test_get_circular_primes_upper_constraints(self):
        n = 1_000_000
        expected_length = 55
        self.assertEqual(expected_length, len(get_circular_primes(n)))

    def test_sum_circular_primes(self):
        nums = [10, 50, 100, 200, 1_000_000]
        expected = [17, 126, 446, 1086, 8_184_200]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], sum_circular_primes(n))


if __name__ == '__main__':
    unittest.main()
