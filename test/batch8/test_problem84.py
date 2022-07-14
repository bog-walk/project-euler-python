import unittest
from solution.batch8.problem84 import markov_chain_odds


class MonopolyOdds(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lower_constraints = [[4, 3, "101524"], [6, 3, "102400"]]
        cls.mid_constraints = [[5, 4, "10242515"], [6, 5, "1024001925"],
                               [7, 6, "102400051925"]]
        cls.upper_constraints = [
            [10, 5, "1000240525"], [16, 8, "1000052425391128"],
            [24, 9, "100005392411251215"], [39, 3, "100005"]
        ]

    def test_markov_chain_odds_lower(self):
        for n, k, expected in self.lower_constraints:
            self.assertEqual(
                expected, markov_chain_odds(n, k), f"Error with {n} {k}"
            )

    def test_markov_chain_odds_mid(self):
        for n, k, expected in self.mid_constraints:
            self.assertEqual(
                expected, markov_chain_odds(n, k), f"Error with {n} {k}"
            )

    def test_markov_chain_odds_upper(self):
        for n, k, expected in self.upper_constraints:
            self.assertEqual(
                expected, markov_chain_odds(n, k), f"Error with {n} {k}"
            )


if __name__ == '__main__':
    unittest.main()
