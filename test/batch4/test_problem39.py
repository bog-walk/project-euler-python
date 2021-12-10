import unittest
from time import perf_counter
from solution.batch4.problem39 import *


class IntegerRightTriangles(unittest.TestCase):
    def test_most_triplet_solutions(self):
        nums = [12, 15, 40, 50, 80, 100, 1000]
        expected = [12, 12, 12, 12, 60, 60, 840]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], most_triplet_solutions_brute(n))
            self.assertEqual(expected[i], most_triplet_solutions(n))
            self.assertEqual(expected[i], most_triplet_solutions_improved(n))

    def test_most_triplet_solutions_speed_comparison(self):
        n = 100_000
        solutions = [
            most_triplet_solutions_brute, most_triplet_solutions, most_triplet_solutions_improved
        ]
        expected = 55440
        starts = []
        stops = []
        for solution in solutions:
            starts.append(perf_counter())
            self.assertEqual(expected, solution(n))
            stops.append(perf_counter())
        print(f"Brute solution took: {stops[0] - starts[0]:0.4f}s\n"
              f"Better solution took: {stops[1] - starts[1]:0.4f}s\n"
              f"Improved solution took: {stops[2] - starts[2]:0.4f}s\n")


if __name__ == '__main__':
    unittest.main()
