import unittest
from solution.batch6.problem52 import permuted_multiples, smallest_permuted_multiple


class PermutedMultiples(unittest.TestCase):
    def test_HR_problem_lower_constraints(self):
        n, k = 125_875, 2
        expected = [[125_874, 251_748]]
        self.assertListEqual(expected, permuted_multiples(n, k))

    def test_HR_problem_mid_values(self):
        n, k = 1_000_000, 4
        expected = [[142_857, 285_714, 428_571, 571_428]]
        self.assertListEqual(expected, permuted_multiples(n, k))

    def test_HR_problem_upper_constraints(self):
        n, k = 2_000_000, 6
        expected = [
            [142_857, 285_714, 428_571, 571_428, 714_285, 857_142],
            [1_428_570, 2_857_140, 4_285_710, 5_714_280, 7_142_850, 8_571_420],
            [1_429_857, 2_8597_14, 4_289_571, 5_7194_28, 7_149_285, 8_579_142]
        ]
        self.assertListEqual(expected, permuted_multiples(n, k))

    def test_PE_problem(self):
        expected = 142_857
        self.assertEqual(expected, smallest_permuted_multiple())


if __name__ == '__main__':
    unittest.main()
