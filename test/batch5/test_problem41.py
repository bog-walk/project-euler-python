import unittest
from solution.batch5.problem41 import largest_pandigital_prime


class PandigitalPrime(unittest.TestCase):
    def test_largest_pandigital_prime(self):
        nums = [10, 100, 10000, 100000]
        expected = [-1, -1, 4231, ]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], largest_pandigital_prime(n))


if __name__ == '__main__':
    unittest.main()
