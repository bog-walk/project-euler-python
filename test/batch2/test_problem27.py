import unittest
from solution.batch2.problem27 import quad_prime_coeff


class QuadraticPrimes(unittest.TestCase):
    def test_lower_constraints(self):
        nums = [42, 50]
        expected = [(-1, 41, 42), (-5, 47, 44)]
        for i, n in enumerate(nums):
            self.assertTupleEqual(expected[i], quad_prime_coeff(n))

    def test_upper_constraints(self):
        nums = [1000, 2000]
        expected = [(-61, 971, 72), (-79, 1601, 81)]
        for i, n in enumerate(nums):
            self.assertTupleEqual(expected[i], quad_prime_coeff(n))


if __name__ == '__main__':
    unittest.main()
