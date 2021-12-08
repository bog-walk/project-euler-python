import unittest
from solution.batch4.problem37 import sum_of_trunc_primes


class TruncatablePrimes(unittest.TestCase):
    def test_sum_of_trunc_primes(self):
        nums = [100, 1000, 10000, 100000, 1_000_000]
        expected = [186, 1986, 8920, 8920, 748317]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], sum_of_trunc_primes(n))


if __name__ == '__main__':
    unittest.main()
