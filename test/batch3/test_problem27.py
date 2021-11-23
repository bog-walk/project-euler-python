import unittest
from solution.batch3.problem27 import quad_prime_coeff


class QuadraticPrimes(unittest.TestCase):
    def test_quad_prime_coeff(self):
        nums = [50, 42, 1000]
        expected = [(-5, 47, 44), (-1, 41, 42), (-61, 971, 72)]
        for index, n in enumerate(nums):
            self.assertTupleEqual(expected[index], quad_prime_coeff(n))


if __name__ == '__main__':
    unittest.main()
