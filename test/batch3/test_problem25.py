import unittest
from time import perf_counter_ns
from solution.batch3.problem25 import *


class NDigitFibonacciNumber(unittest.TestCase):

    def test_n_digit_fib_terms(self):
        all_terms = n_digit_fib_terms(5000)
        digits = [2, 3, 4, 9, 1000, 5000]
        expected = [7, 12, 17, 40, 4782, 23922]
        for index, digit in enumerate(digits):
            self.assertEqual(expected[index], all_terms[digit - 2])
            self.assertEqual(expected[index], n_digit_fib_term_by_digits_golden(digit))

    def test_nth_fib_golden(self):
        expected = [
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
        ]
        for n in range(18):
            self.assertEqual(expected[n], nth_fib_golden(n))

    def test_n_digit_fib_term_using_golden(self):
        expected = [7, 12, 17, 21, 26, 31, 36, 40]
        for n in range(2, 10):
            self.assertEqual(expected[n - 2], n_digit_fib_term_using_golden(n))

    def test_n_digit_fib_term_speed_low_n(self):
        n = 10
        expected = 45
        solutions = [
            n_digit_fib_terms,
            n_digit_fib_term_using_golden,
            n_digit_fib_term_by_digits_golden
        ]
        starts = []
        stops = []
        for i in range(3):
            starts.append(perf_counter_ns())
            ans = solutions[i](n)
            if i == 0:
                self.assertEqual(expected, ans[n - 2])
            else:
                self.assertEqual(expected, ans)
            stops.append(perf_counter_ns())
        print(f"Brute solution took: {stops[0] - starts[0]}ns\n"
              f"Golden iteration took: {stops[1] - starts[1]}ns\n"
              f"Golden by digits took: {stops[2] - starts[2]}ns\n")

    def test_n_digit_fib_term_speed_high_n(self):
        n = 5000
        expected = 23922
        solutions = [
            n_digit_fib_terms,
            n_digit_fib_term_by_digits_golden
        ]
        starts = []
        stops = []
        for i in range(2):
            starts.append(perf_counter_ns())
            ans = solutions[i](n)
            if i == 0:
                self.assertEqual(expected, ans[n - 2])
            else:
                self.assertEqual(expected, ans)
            stops.append(perf_counter_ns())
        print(f"Brute solution took: {(stops[0] - starts[0]) // 1_000_000}ms\n"
              f"Golden by digits took: {stops[1] - starts[1]}ns\n")


if __name__ == '__main__':
    unittest.main()
