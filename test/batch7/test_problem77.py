import unittest
from solution.batch7.problem77 import *


class PrimeSummations(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.all_counts = all_prime_sum_combos(1000)

    def test_HR_problem_lower_constraints(self):
        nums = [2, 3, 4, 5, 6, 7, 10, 35, 71]
        expected = [1, 1, 1, 2, 2, 3, 5, 175, 5007]
        for n, e in zip(nums, expected):
            self.assertEqual(e, self.all_counts[n])

    def test_HR_problem_mid_constraints(self):
        nums = [80, 100, 350]
        expected = [10003, 40899, 3_791_614_657]
        for n, e in zip(nums, expected):
            self.assertEqual(e, self.all_counts[n])

    def test_HR_problem_upper_constraints(self):
        nums = [880, 1000]
        expected = [4_205_301_095_670_916, 48_278_613_741_845_757]
        for n, e in zip(nums, expected):
            self.assertEqual(e, self.all_counts[n])

    def test_PE_problem(self):
        expected = 71
        self.assertEqual(expected, first_prime_sum_combo())


if __name__ == '__main__':
    unittest.main()
