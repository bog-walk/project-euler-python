import unittest
from util.tests.reusable import compare_speed_nano
from solution.batch2.problem18 import *


def nested_pyramid(rows: int, elements: list[int]) -> list[list[int]]:
    """
    Convert a flat list to a nested list that mimics the rows of a pyramid as
    seen in this solution.
    e.g. [1, 2, 3, 4, 5, 6] -> [[1], [2, 3], [4, 5, 6]]
    """

    nested = []
    first = 0
    for row in range(1, rows + 1):
        end = first + row
        nested.append(elements[first:end])
        first = end
    return nested


class MaximumPathSum1(unittest.TestCase):
    def test_small_tree(self):
        n = 4
        elements = [3, 7, 4, 2, 4, 6, 8, 5, 9, 3]
        nested = nested_pyramid(n, elements)
        expected = 23
        self.assertEqual(expected, max_path_sum(n, elements))
        self.assertEqual(expected, max_path_sum_dynamic(n, nested))

    def test_large_tree_and_speed(self):
        n = 15
        elements = [
            75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 4, 82, 47, 65, 19, 1, 23,
            75, 3, 34, 88, 2, 77, 73, 7, 63, 67, 99, 65, 4, 28, 6, 16, 70, 92, 41,
            41, 26, 56, 83, 40, 80, 70, 33, 41, 48, 72, 33, 47, 32, 37, 16, 94,
            29, 53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 70, 11, 33, 28, 77,
            73, 17, 78, 39, 68, 17, 57, 91, 71, 52, 38, 17, 14, 91, 43, 58, 50,
            27, 29, 48, 63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 4,
            62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23
        ]
        nested = nested_pyramid(n, elements)
        expected = 1074
        solutions = {
            "Custom class": [max_path_sum, n, elements],
            "Dynamic": [max_path_sum_dynamic, n, nested]
        }
        results = compare_speed_nano(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
