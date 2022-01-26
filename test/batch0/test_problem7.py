import unittest
from solution.batch0.problem7 import nth_prime


class The10001stPrime(unittest.TestCase):
    def test_lower_constraints(self):
        nums = [1, 2, 3]
        expected = [2, 3, 5]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], nth_prime(n))

    def test_normal_n(self):
        nums = [6, 20, 62]
        expected = [13, 71, 293]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], nth_prime(n))

    def test_large_n(self):
        nums = [289, 919, 1000]
        expected = [1879, 7193, 7919]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], nth_prime(n))

    def test_upper_constraints(self):
        nums = [5000, 10_000, 10_001]
        expected = [48611, 104_729, 104_743]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], nth_prime(n))


if __name__ == '__main__':
    unittest.main()
