import unittest
from solution.batch5.problem46 import smallest_failing_num, goldbach_repr


class GoldbachsOtherConjecture(unittest.TestCase):
    def test_HR_problem_lower_constraints(self):
        composites = [9, 15, 21, 25, 27, 33]
        expected = [1, 2, 3, 3, 1, 1]
        for i, composite in enumerate(composites):
            self.assertEqual(expected[i], goldbach_repr(composite))

    def test_HR_problem_normal_values(self):
        composites = [403, 695, 1599, 3393]
        expected = [5, 2, 12, 10]
        for i, composite in enumerate(composites):
            self.assertEqual(expected[i], goldbach_repr(composite))

    def test_HR_problem_upper_constraints(self):
        composites = [23851, 499_999]
        expected = [53, 156]
        for i, composite in enumerate(composites):
            self.assertEqual(expected[i], goldbach_repr(composite))

    def test_smallest_failing_num(self):
        expected = 5777
        self.assertEqual(expected, smallest_failing_num())

    def test_HR_problem_no_rep(self):
        composite = 5777
        expected = 0
        self.assertEqual(expected, goldbach_repr(composite))


if __name__ == '__main__':
    unittest.main()
