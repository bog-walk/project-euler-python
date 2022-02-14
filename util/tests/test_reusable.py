import unittest
from fake_func import *
from reusable import compare_speed, get_test_resource


class TestsReusable(unittest.TestCase):
    def test_compare_speed_zero_arg(self):
        solutions = {
            "Sleep A": [sleep_A], "Sleep B": [sleep_B],
            "Sleep C": [sleep_C], "Sleep D": [sleep_D]
        }
        results = compare_speed(solutions)
        self.assertListEqual(
            ["Sleep A", "Sleep B", "Sleep C", "Sleep D"], list(results.keys())
        )
        self.assertTrue(all(actual is None for actual in results.values()))

    def test_compare_speed_single_arg(self):
        n = 3
        expected = 900
        solutions = {
            "Fast": [fast_fake, n],
            "Medium": [medium_fake, n],
            "Slow": [slow_fake, n]
        }
        results = compare_speed(solutions)
        self.assertListEqual(
            ["Fast", "Medium", "Slow"], list(results.keys())
        )
        self.assertTrue(all(actual == expected for actual in results.values()))

    def test_compare_speed_varargs(self):
        n = 3
        m = "100"
        expected = 2700
        solutions = {
            "Fake A": [fake_A, n],
            "Fake B": [fake_B, n, m],
            "Fake C": [fake_C, n, n]
        }
        results = compare_speed(solutions)
        self.assertListEqual(
            ["Fake A", "Fake B", "Fake C"], list(results.keys())
        )
        self.assertTrue(all(actual == expected for actual in results.values()))

    def test_compare_speed_with_repetitions(self):
        n = 3
        expected = 900
        solutions = {
            "Fast": [fast_fake, n],
            "Medium": [medium_fake, n],
            "Slow": [slow_fake, n]
        }
        results = compare_speed(solutions, precision=4, repeat=10)
        self.assertListEqual(
            ["Fast", "Medium", "Slow"], list(results.keys())
        )
        self.assertTrue(all(actual == expected for actual in results.values()))

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
