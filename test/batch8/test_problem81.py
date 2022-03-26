import unittest
from util.tests.reusable import compare_speed, get_test_resource
from solution.batch8.problem81 import *


class PathSum2Ways(unittest.TestCase):
    def test_HR_problem_with_tiny_grid(self):
        n = 3
        grid: list[list[int]] = get_test_resource(
            "../resources/path_sum_2to4_ways_with_3_rows.txt",
            transformation=int, line_split=","
        )
        expected = 20
        self.assertEqual(expected, min_path_sum(n, grid))
        self.assertEqual(expected, min_path_sum_dijkstra(n, grid))

    def test_HR_problem_with_small_grid_with_smaller_values(self):
        n = 5
        grid: list[list[int]] = get_test_resource(
            "../resources/path_sum_2to4_ways_with_5_small_rows.txt",
            transformation=int, line_split=","
        )
        expected = 25
        self.assertEqual(expected, min_path_sum(n, grid))
        self.assertEqual(expected, min_path_sum_dijkstra(n, grid))

    def test_HR_problem_with_small_grid_with_larger_values(self):
        n = 5
        grid: list[list[int]] = get_test_resource(
            "../resources/path_sum_2to4_ways_with_5_large_rows.txt",
            transformation=int, line_split=","
        )
        expected = 2427
        self.assertEqual(expected, min_path_sum(n, grid))
        self.assertEqual(expected, min_path_sum_dijkstra(n, grid))

    def test_PE_problem_with_speed(self):
        n = 80
        grid: list[list[int]] = get_test_resource(
            "../resources/path_sum_2to4_ways_with_80_rows.txt",
            transformation=int, line_split=","
        )
        expected = 427_337
        solutions = {
            "Dynamic": [min_path_sum, n, grid],
            "Dijkstra": [min_path_sum_dijkstra, n, grid],
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
