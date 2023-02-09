import unittest
from solution.batch9.problem100 import *


class ArrangedProbability(unittest.TestCase):
    def test_lower_constraints(self):
        inputs = [(2, 1, 2), (5, 1, 2), (100, 1, 2), (450, 1, 2), (500, 3, 8),
                  (100, 5, 9)]
        expected = [("3", "4"), ("15", "21"), ("85", "120"), ("493", "697"),
                    ("931", "1520"), ("141", "189")]

        for (d, p, q), e in zip(inputs, expected):
            self.assertTupleEqual(e, get_next_arrangement(d, p, q))
            if p == 1 and q == 2:
                self.assertTupleEqual(e, get_next_half_arrangement(d))

    def test_mid_constraints(self):
        inputs = [(1000, 3, 8), (5000, 3, 8), (5000, 5, 9)]
        expected = [("931", "1520"), ("3871", "6321"), ("6601", "8856")]

        for (d, p, q), e in zip(inputs, expected):
            self.assertTupleEqual(e, get_next_arrangement(d, p, q))
            if p == 1 and q == 2:
                self.assertTupleEqual(e, get_next_half_arrangement(d))

    def test_when_no_solution_possible(self):
        inputs = [(100, 1, 4)]

        for d, p, q in inputs:
            self.assertIsNone(get_next_arrangement(d, p, q))


if __name__ == '__main__':
    unittest.main()
