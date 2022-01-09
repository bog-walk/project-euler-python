import unittest
from solution.batch6.problem52 import *


class PermutedMultiples(unittest.TestCase):
    def test_permuted_multiples_lower_constraint(self):
        n, k = 125875, 2
        expected = [[125874, 251748]]
        self.assertListEqual(expected, permuted_multiples(n, k))

    def test_permuted_multiples_mid_constraint(self):
        n, k = 1_000_000, 4
        expected = [[142857, 285714, 428571, 571428]]
        self.assertListEqual(expected, permuted_multiples(n, k))

    def test_permuted_multiples_upper_constraint(self):
        n, k = 2_000_000, 6
        expected = [
            [142857, 285714, 428571, 571428, 714285, 857142],
            [1428570, 2857140, 4285710, 5714280, 7142850, 8571420],
            [1429857, 2859714, 4289571, 5719428, 7149285, 8579142]
        ]
        self.assertListEqual(expected, permuted_multiples(n, k))

    def test_smallest_permuted_multiple(self):
        expected = 142857
        self.assertEqual(expected, smallest_permuted_multiple())


if __name__ == '__main__':
    unittest.main()
