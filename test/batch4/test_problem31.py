import unittest
from time import perf_counter
from solution.batch4.problem31 import *


class CoinSums(unittest.TestCase):
    def test_count_coin_combos_low_n(self):
        expected = [1, 2, 2, 3, 4, 5, 6, 7, 8, 11]
        for n in range(10):
            self.assertEqual(expected[n], count_coin_combos(n + 1))
            self.assertEqual(expected[n], count_coin_combos_recursive(n + 1))

    def test_count_coin_combos_mid_n(self):
        nums = [15, 20, 50, 200, 500]
        expected = [22, 41, 451, 73682, 6295434]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], count_coin_combos(n))
            self.assertEqual(expected[i], count_coin_combos_recursive(n))

    def test_count_coin_combos_high_n(self):
        n = 10000
        expected = 296710490
        self.assertEqual(expected, count_coin_combos(n))
        self.assertEqual(expected, count_coin_combos_recursive(n))

    def test_count_coin_combos_speed(self):
        n = 100000
        solutions = [count_coin_combos_recursive, count_coin_combos]
        starts = []
        stops = []
        answers = []
        for solution in solutions:
            starts.append(perf_counter())
            answers.append(solution(n))
            stops.append(perf_counter())
        print(f"Recursive solution took: {stops[0] - starts[0]:0.4f}s\n"
              f"Improved solution took: {stops[1] - starts[1]:0.4f}s\n")
        self.assertEqual(answers[0], answers[1])


if __name__ == '__main__':
    unittest.main()
