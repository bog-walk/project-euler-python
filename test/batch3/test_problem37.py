import unittest
from solution.batch3.problem37 import sum_of_trunc_primes


class TruncatablePrimes(unittest.TestCase):
    def test_sum_of_trunc_primes(self):
        expected = [186, 1986, 8920, 8920, 748_317]
        for e in range(2, 7):
            n = pow(10, e)
            self.assertEqual(expected[e - 2], sum_of_trunc_primes(n))


if __name__ == '__main__':
    unittest.main()
