import unittest
from util.tests.reusable import compare_speed, get_test_resource
from solution.batch6.problem67 import *


class MaximumPathSum2(unittest.TestCase):
    def test_tree_with_20_rows(self):
        n = 20
        expected = 1407
        pyramid: list[list[int]] = get_test_resource(
            "../resources/maximum_path_sum_2_with_20_rows",
            transformation=int
        )
        elements = [n for row in pyramid for n in row]
        solutions = {
            "Custom class": [max_path_sum, n, elements],
            "Dynamic": [max_path_sum_dynamic, n, pyramid]
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))

    def test_tree_with_25_rows(self):
        n = 25
        expected = 1810
        pyramid: list[list[int]] = get_test_resource(
            "../resources/maximum_path_sum_2_with_25_rows",
            transformation=int
        )
        elements = [n for row in pyramid for n in row]
        solutions = {
            "Custom class": [max_path_sum, n, elements],
            "Dynamic": [max_path_sum_dynamic, n, pyramid]
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))

    def test_tree_with_100_rows(self):
        n = 100
        expected = 7273
        pyramid: list[list[int]] = get_test_resource(
            "../resources/maximum_path_sum_2_with_100_rows",
            transformation=int
        )
        result = compare_speed({"Dynamic": [max_path_sum_dynamic, n, pyramid]})
        self.assertEqual(expected, result["Dynamic"])


if __name__ == '__main__':
    unittest.main()
