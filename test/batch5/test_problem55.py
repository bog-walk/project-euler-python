import unittest
from util.tests.reusable import compare_speed
from solution.batch5.problem55 import *


class LychrelNumbers(unittest.TestCase):
    def test_lower_constraints(self):
        nums = [100, 130, 500]
        expected = [(121, 16), (121, 18), (121, 18)]
        for i, n in enumerate(nums):
            self.assertTupleEqual(expected[i], max_palindrome_convergence(n))
            self.assertTupleEqual(expected[i], max_palindrome_convergence_cached(n))

    def test_mid_values(self):
        nums = [1000, 5000]
        expected = [(1111, 25), (12221, 88)]
        for i, n in enumerate(nums):
            self.assertTupleEqual(expected[i], max_palindrome_convergence(n))
            self.assertTupleEqual(expected[i], max_palindrome_convergence_cached(n))

    def test_upper_constraints(self):
        nums = [10_000, 50_000]
        expected = [(79497, 215), (79497, 295)]
        for i, n in enumerate(nums):
            self.assertTupleEqual(expected[i], max_palindrome_convergence(n))
            self.assertTupleEqual(expected[i], max_palindrome_convergence_cached(n))

    def test_speed(self):
        n = 100_000
        expected = (4964444694, 583)
        solutions = {
            "Cache": [max_palindrome_convergence_cached, n],
            "No cache": [max_palindrome_convergence, n]
        }
        results = compare_speed(solutions, precision=2)
        self.assertTrue(all(expected == actual for actual in results.values()))

    def test_PE_problem(self):
        expected = 249
        self.assertEqual(expected, count_lychrel_numbers())


if __name__ == '__main__':
    unittest.main()
