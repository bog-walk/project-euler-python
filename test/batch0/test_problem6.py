import unittest
from solution.batch0.problem6 import sum_square_diff, sum_square_diff_brute
from util.tests.reusable import compare_speed


class SumSquareDifference(unittest.TestCase):
    def test_lower_constraints(self):
        nums = [1, 2, 3]
        expected = [0, 4, 22]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], sum_square_diff_brute(n))
            self.assertEqual(expected[i], sum_square_diff(n))

    def test_normal_n(self):
        nums = [10, 51, 100]
        expected = [2640, 1_712_750, 25_164_150]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], sum_square_diff_brute(n))
            self.assertEqual(expected[i], sum_square_diff(n))

    def test_large_n(self):
        nums = [2256, 7000]
        expected = [6_477_756_566_600, 600_307_154_415_500]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], sum_square_diff_brute(n))
            self.assertEqual(expected[i], sum_square_diff(n))

    def test_upper_constraints_speed(self):
        n = 10_000
        expected = 2_500_166_641_665_000
        solutions = {
            "Brute": [sum_square_diff_brute, n],
            "Improved": [sum_square_diff, n],
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
