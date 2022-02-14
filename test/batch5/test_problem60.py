import unittest
from util.tests.reusable import compare_speed
from solution.batch5.problem60 import multiprocessing_prime_pair_set_sum, \
    prime_pair_set_sum_concise


class PrimePairSets(unittest.TestCase):
    def test_lower_constraints(self):
        n, k = 100, 3
        expected = [107, 123]
        self.assertListEqual(expected, multiprocessing_prime_pair_set_sum(n, k))
        self.assertListEqual(expected, prime_pair_set_sum_concise(n, k))

    def test_lower_mid_values(self):
        n, k = 1000, 4
        expected = [792, 1838]
        self.assertListEqual(expected, multiprocessing_prime_pair_set_sum(n, k))
        self.assertListEqual(expected, prime_pair_set_sum_concise(n, k))

    def test_upper_constraints(self):
        n, k = 20000, 5
        expected = [26033, 34427]
        solutions = {
            "Multiprocessing": [multiprocessing_prime_pair_set_sum, n, k],
            "Concise": [prime_pair_set_sum_concise, n, k]
        }
        results = compare_speed(solutions, precision=2)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
