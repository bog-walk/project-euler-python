import unittest
from solution.batch1.problem6 import sum_square_diff


class SumSquareDifference(unittest.TestCase):
    def test_sum_square_diff_lower_constraints(self):
        test_n = [1, 2, 3]
        expected = [0, 4, 22]
        for index, n in enumerate(test_n):
            self.assertEqual(expected[index], sum_square_diff(n))

    def test_sum_square_diff_normal_values(self):
        test_n = [10, 51, 100]
        expected = [2640, 1712750, 25164150]
        for index, n in enumerate(test_n):
            self.assertEqual(expected[index], sum_square_diff(n))

    def test_sum_square_diff_large_values(self):
        test_n = [2256, 7000]
        expected = [6477756566600, 600307154415500]
        for index, n in enumerate(test_n):
            self.assertEqual(expected[index], sum_square_diff(n))

    def test_sum_square_diff_upper_constraint(self):
        self.assertEqual(2500166641665000, sum_square_diff(10000))


if __name__ == '__main__':
    unittest.main()
