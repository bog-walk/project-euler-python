import unittest
from solutions.batch1.problem1 import sum_of_multiples_brute, sum_of_multiples


class MultiplesOf3Or5(unittest.TestCase):
    def test_same_factors(self):
        self.assertEqual(18, sum_of_multiples(10, 3, 3))
        self.assertEqual(18, sum_of_multiples_brute(10, 3, 3))

    def test_different_factors_1(self):
        self.assertEqual(23, sum_of_multiples(10, 3, 5))
        self.assertEqual(23, sum_of_multiples_brute(10, 3, 5))

    def test_different_factors_2(self):
        self.assertEqual(233168, sum_of_multiples(1000, 3, 5))
        self.assertEqual(233168, sum_of_multiples_brute(1000, 3, 5))

    def test_different_factors_3(self):
        self.assertEqual(44087172, sum_of_multiples(23000, 8, 21))
        self.assertEqual(44087172, sum_of_multiples_brute(23000, 8, 21))

    def test_lower_limits(self):
        self.assertEqual(0, sum_of_multiples(1, 1, 1))
        self.assertEqual(0, sum_of_multiples_brute(1, 1, 1))
        self.assertEqual(1, sum_of_multiples(2, 1, 2))
        self.assertEqual(1, sum_of_multiples_brute(2, 1, 2))

    def test_upper_limits(self):
        self.assertEqual(3749995000000, sum_of_multiples(10_000_000, 20, 32))
        self.assertEqual(3749995000000, sum_of_multiples_brute(10_000_000, 20, 32))
        self.assertEqual(233333333166666668, sum_of_multiples(1_000_000_000, 3, 5))


if __name__ == '__main__':
    unittest.main()
