import unittest
from solution.batch9.problem95 import longest_amicable_chain


class AmicableChains(unittest.TestCase):
    def test_lower_constraints(self):
        limits = [6, 10, 30, 100, 300, 1000]
        expected = [6, 6, 6, 6, 220, 220]
        for limit, e in zip(limits, expected):
            chain = longest_amicable_chain(limit)
            self.assertEqual(e, min(chain))

    def test_mid_constraints(self):
        limits = [5000, 10_000, 50_000, 100_000]
        expected = [220, 220, 12496, 12496]
        for limit, e in zip(limits, expected):
            chain = longest_amicable_chain(limit)
            self.assertEqual(e, min(chain))

    def test_upper_constraints(self):
        limits = [500_000, 800_000, 1_000_000]
        expected = [12496, 14316, 14316]
        for limit, e in zip(limits, expected):
            chain = longest_amicable_chain(limit)
            self.assertEqual(e, min(chain))


if __name__ == '__main__':
    unittest.main()
