import unittest
from util.tests.reusable import compare_speed_seconds
from solution.batch6.problem60 import sum_of_prime_pair_sets


class PrimePairSets(unittest.TestCase):
    def test_lower_constraints(self):
        n, k = 100, 3
        expected = [107, 123]
        self.assertListEqual(expected, sum_of_prime_pair_sets(n, k))

    def test_lower_mid_values(self):
        n, k = 1000, 4
        expected = [792, 1838]
        self.assertListEqual(expected, sum_of_prime_pair_sets(n, k))

    def test_upper_constraints(self):
        n, k = 20000, 5
        expected = [26033, 34427]
        self.assertListEqual(expected, sum_of_prime_pair_sets(n, k))


if __name__ == '__main__':
    unittest.main()
