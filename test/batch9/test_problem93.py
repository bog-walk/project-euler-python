import unittest
from solution.batch9.problem93 import *


class ArithmeticExpressions(unittest.TestCase):
    def test_HR_problem_single_digit_sets(self):
        for d in range(10):
            value = [d]
            expected = 1 if d == 1 else 0
            self.assertEqual(expected, highest_streak(value))

    def test_HR_problem_no_streaks(self):
        values = [[2, 8], [1, 3], [1, 4]]
        for value in values:
            self.assertEqual(0, highest_streak(value))

    def test_HR_problem_M_equal_2(self):
        value = [1, 2]
        expected = 3
        self.assertEqual(expected, highest_streak(value))

    def test_HR_problem_M_equal_3(self):
        values = [[1, 2, 3], [1, 2, 4], [2, 5, 9]]
        expected = [9, 10, 3]
        for value, e in zip(values, expected):
            self.assertEqual(e, highest_streak(value))

    def test_HR_problem_M_equal_4(self):
        value = [1, 2, 3, 4]
        expected = 28
        self.assertEqual(expected, highest_streak(value))

    def test_HR_problem_handles_floating_point(self):
        values = [[1, 5, 6, 7], [1, 3, 4, 5], [1, 3, 4, 7]]
        expected = [15, 24, 10]
        for value, e in zip(values, expected):
            self.assertEqual(e, highest_streak(value))

    def test_HR_problem_M_equal_5(self):
        values = [[1, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]
        expected = [75, 192, 102]
        for value, e in zip(values, expected):
            self.assertEqual(e, highest_streak(value))

    def test_PE_problem(self):
        expected_set = [1, 2, 5, 8]
        expected_highest = 51
        actual = list(map(int, longest_streak_set()))
        self.assertListEqual(expected_set, actual)
        self.assertEqual(expected_highest, highest_streak(actual))


if __name__ == '__main__':
    unittest.main()
