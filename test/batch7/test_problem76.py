import unittest
from solution.batch7.problem76 import count_sum_combos


class CountingSummations(unittest.TestCase):
    def test_lower_constraints(self):
        nums = [2, 3, 4, 5, 6, 7, 10]
        expected = [1, 2, 4, 6, 10, 14, 41]
        for n, e in zip(nums, expected):
            self.assertEqual(e, count_sum_combos(n))

    def test_mid_constraints(self):
        nums = [80, 100, 350]
        expected = [15_796_475, 190_569_291, 528_158_869]
        for n, e in zip(nums, expected):
            self.assertEqual(e, count_sum_combos(n))

    def test_upper_constraints(self):
        nums = [880, 1000]
        expected = [200_208_910, 709_496_665]
        for n, e in zip(nums, expected):
            self.assertEqual(e, count_sum_combos(n))


if __name__ == '__main__':
    unittest.main()
