import unittest
from time import perf_counter_ns
from solution.batch3.problem29 import *


class DistinctPowers(unittest.TestCase):
    def test_distinct_power(self):
        nums = [2, 3, 4, 5, 10, 100]
        expected = [1, 4, 8, 15, 69, 9183]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], distinct_powers_brute(n))
            self.assertEqual(expected[index], distinct_power(n))
            self.assertEqual(expected[index], distinct_power_improved(n))

    def test_speed_comparison(self):
        n = 1000
        expected = 977358
        solutions = [
            distinct_powers_brute, distinct_power, distinct_power_improved
        ]
        starts = []
        stops = []
        for solution in solutions:
            starts.append(perf_counter_ns())
            result = solution(n)
            stops.append(perf_counter_ns())
            self.assertEqual(expected, result)
        print(f"Brute took: {(stops[0] - starts[0]) / 1_000_000}ms\n"
              f"Draft solution took: {(stops[1] - starts[1]) / 1_000_000}ms\n"
              f"New solution took: {(stops[2] - starts[2]) / 1_000_000}ms\n")


if __name__ == '__main__':
    unittest.main()
