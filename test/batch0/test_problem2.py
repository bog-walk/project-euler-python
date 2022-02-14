import unittest
from util.tests.reusable import compare_speed
from solution.batch0.problem2 import *


class EvenFibonacciNumbers(unittest.TestCase):
    def test_lower_constraints(self):
        n = 10
        expected = 10
        self.assertEqual(expected, sum_even_fibs_brute(n))
        self.assertEqual(expected, sum_even_fibs_formula(n))

    def test_max_is_even_fibonacci(self):
        n = 10946
        expected = 3382
        self.assertEqual(expected, sum_even_fibs_brute(n))
        self.assertEqual(expected, sum_even_fibs_formula(n))

    def test_max_is_odd(self):
        n = 2583
        expected = 798
        self.assertEqual(expected, sum_even_fibs_brute(n))
        self.assertEqual(expected, sum_even_fibs_formula(n))

    def test_normal_n(self):
        n = 200
        expected = 188
        self.assertEqual(expected, sum_even_fibs_brute(n))
        self.assertEqual(expected, sum_even_fibs_formula(n))

    def test_large_n(self):
        n = 4_000_000
        expected = 4_613_732
        self.assertEqual(expected, sum_even_fibs_brute(n))
        self.assertEqual(expected, sum_even_fibs_formula(n))

    def test_sum_even_fibs_speed(self):
        n = 4 * pow(10, 16)
        expected = 49_597_426_547_377_748
        solutions = {
            "Brute": [sum_even_fibs_brute, n],
            "Formula": [sum_even_fibs_formula, n]
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
