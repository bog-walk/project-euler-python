import unittest
from time import sleep
from reusable import *


def pow_a(n: int) -> int:
    return n ** n


def pow_b(n: int) -> int:
    sleep(0.5)
    return pow(n, n)


def pow_c(n: str) -> int:
    num = int(n)
    return num ** num


def pow_d(base: int, exp: int) -> int:
    sleep(0.1)
    return base ** exp


class TestsReusable(unittest.TestCase):
    def test_compare_speed_single_arg(self):
        n = 3
        solutions = {
            "Pow A": [pow_a, n], "Pow B": [pow_b, n],
        }
        expected = 27
        results_s = compare_speed_seconds(
            solutions, precision=2, repeat=10
        )
        results_ns = compare_speed_nano(
            solutions, repeat=10
        )
        self.assertListEqual(
            ["Pow A", "Pow B"], list(results_s.keys())
        )
        self.assertListEqual(
            ["Pow A", "Pow B"], list(results_ns.keys())
        )
        self.assertTrue(all(actual == expected for actual in results_s.values()))
        self.assertTrue(all(actual == expected for actual in results_ns.values()))

    def test_compare_speed_arg_cast(self):
        n = 3
        solutions = {
            "Pow A": [pow_a, n], "Pow B": [pow_b, n],
            "Pow C": [pow_c, str(n)]
        }
        expected = 27
        results_s = compare_speed_seconds(solutions)
        results_ns = compare_speed_nano(solutions)
        self.assertTrue(all(actual == expected for actual in results_s.values()))
        self.assertTrue(all(actual == expected for actual in results_ns.values()))

    def test_compare_speed_varargs(self):
        n = 3
        solutions = {
            "Pow A": [pow_a, n], "Pow B": [pow_b, n],
            "Pow C": [pow_c, str(n)], "Pow D": [pow_d, n, n]
        }
        expected = 27
        results_s = compare_speed_seconds(
            solutions, precision=2, repeat=10
        )
        results_ns = compare_speed_nano(
            solutions, repeat=10
        )
        self.assertListEqual(
            ["Pow A", "Pow B", "Pow C", "Pow D"], list(results_s.keys())
        )
        self.assertListEqual(
            ["Pow A", "Pow B", "Pow C", "Pow D"], list(results_ns.keys())
        )
        self.assertTrue(all(actual == expected for actual in results_s.values()))
        self.assertTrue(all(actual == expected for actual in results_ns.values()))

    def test_get_test_resource_default(self):
        path = "fake_resource"
        resource = get_test_resource(path)
        expected_lines = 5
        expected_first = "A, B, C, D, E, F"
        self.assertEqual(expected_lines, len(resource))
        self.assertIsInstance(resource[0], str)
        self.assertEqual(expected_first, resource[0])

    def test_get_test_resource_transformed(self):
        path = "fake_resource"
        resource = get_test_resource(
            path, transformation=lambda s: s.lower(), line_split=", ")
        expected_lines = 5
        expected_first = ["a", "b", "c", "d", "e", "f"]
        self.assertEqual(expected_lines, len(resource))
        self.assertIsInstance(resource[0], list)
        self.assertEqual(expected_first, resource[0])


if __name__ == '__main__':
    unittest.main()
