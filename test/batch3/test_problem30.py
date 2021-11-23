import unittest
from time import perf_counter
from solution.batch3.problem30 import *


class DigitFifthPowers(unittest.TestCase):
    def test_digit_nth_powers(self):
        expected = [
            [153, 370, 371, 407],
            [1634, 8208, 9474],
            [4150, 4151, 54748, 92727, 93084, 194979],
            [548834]
        ]
        for n in range(3, 7):
            self.assertListEqual(expected[n - 3], digit_nth_powers_brute(n))
            self.assertListEqual(expected[n - 3], digit_nth_powers_builtin(n))

    def test_sum_speed_comparison(self):
        n = 6
        expected = 548834
        solutions = [digit_nth_powers_brute, digit_nth_powers_builtin]
        starts = []
        stops = []
        for solution in solutions:
            starts.append(perf_counter())
            self.assertEqual(expected, sum(solution(n)))
            stops.append(perf_counter())
        print(f"Brute solution took: {stops[0] - starts[0]:0.4f}s\n"
              f"Builtin solution took: {stops[1] - starts[1]:0.4f}s\n")


if __name__ == '__main__':
    unittest.main()
