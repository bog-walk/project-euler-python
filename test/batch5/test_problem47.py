import unittest
from solution.batch5.problem47 import consecutive_distinct_primes, \
    first_4_distinct_primes


class DistinctPrimesFactors(unittest.TestCase):
    def test_consecutive_distinct_primes_k2(self):
        k = 2
        nums = [20, 100]
        expected = [
            [14, 20],
            [14, 20, 21, 33, 34, 35, 38, 39, 44, 45, 50, 51, 54, 55,
             56, 57, 62, 68, 74, 75, 76, 85, 86, 87, 91, 92, 93, 94, 95, 98, 99]
                    ]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], consecutive_distinct_primes(n, k))

    def test_consecutive_distinct_primes_k3(self):
        k = 3
        nums = [644, 1000]
        expected = [[644], [644, 740, 804, 986]]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], consecutive_distinct_primes(n, k))

    def test_consecutive_distinct_primes_k4(self):
        k = 4
        nums = [10_000, 100_000, 300_000]
        expected = [[], [], [134043, 238203, 253894, 259368]]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], consecutive_distinct_primes(n, k))

    def test_first_4_distinct_primes(self):
        expected = 134043
        self.assertEqual(expected, first_4_distinct_primes())


if __name__ == '__main__':
    unittest.main()
