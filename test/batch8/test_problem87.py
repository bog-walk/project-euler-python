import unittest
from solution.batch8.problem87 import all_prime_power_triple_counts


class PrimePowerTriples(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        limit = 50_000_000
        cls.all_counts = all_prime_power_triple_counts(limit)

    def test_lower_constraints(self):
        inputs = [1, 2, 10, 50, 100, 212, 499]
        expected = [0, 0, 0, 4, 10, 24, 53]
        for n, e in zip(inputs, expected):
            self.assertEqual(e, self.all_counts[n])

    def test_mid_constraints(self):
        inputs = [1000, 8888, 10_000, 40_000]
        expected = [98, 634, 683, 2229]
        for n, e in zip(inputs, expected):
            self.assertEqual(e, self.all_counts[n])

    def test_upper_constraints(self):
        inputs = [1_000_000, 10_000_000, 50_000_000]
        expected = [33616, 256_629, 1_097_343]
        for n, e in zip(inputs, expected):
            self.assertEqual(e, self.all_counts[n])


if __name__ == '__main__':
    unittest.main()
