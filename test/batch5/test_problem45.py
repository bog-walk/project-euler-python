import unittest
from util.tests.reusable import compare_speed_nano
from solution.batch5.problem45 import common_numbers, common_numbers_formula,\
    next_triple_type


class TriPentHex(unittest.TestCase):
    def test_HR_problem_TriPent(self):
        a, b = 3, 5
        nums = [2, 10, 10_000, 1_000_000]
        expected = [[1], [1], [1, 210], [1, 210, 40755]]
        for i, n in enumerate(nums):
            self.assertListEqual(expected[i], common_numbers(n, a, b))
            self.assertListEqual(expected[i], common_numbers_formula(n, a, b))

    def test_HR_problem_PentHex(self):
        a, b = 5, 6
        nums = [2, 100_000, 10_000_000]
        expected = [[1], [1, 40755], [1, 40755]]
        for i, n in enumerate(nums):
            self.assertListEqual(expected[i], common_numbers(n, a, b))
            self.assertListEqual(expected[i], common_numbers_formula(n, a, b))

    def test_common_number_speed(self):
        n, a, b = 200_000_000_000_000, 5, 6
        expected = [1, 40755, 1_533_776_805, 57_722_156_241_751]
        solutions = {
            "Original formula": [common_numbers, n, a, b],
            "Diophantine formula": [common_numbers_formula, n, a, b]
        }
        results = compare_speed_nano(solutions)
        for actual in results.values():
            self.assertListEqual(expected, actual)

    def test_next_triple_type(self):
        expected = 1_533_776_805
        self.assertEqual(expected, next_triple_type())


if __name__ == '__main__':
    unittest.main()
