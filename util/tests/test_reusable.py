import unittest
from time import sleep
from util.tests.reusable import *


def pow_a(n: int) -> int:
    return n ** n


def pow_b(n: int) -> int:
    sleep(0.05)
    return pow(n, n)


def pow_c(n: str) -> int:
    num = int(n)
    sleep(0.1)
    return num ** num


def pow_d(base: int, exp: int) -> int:
    return base ** exp


class TestsReusable(unittest.TestCase):
    def test_compare_speed_single_arg(self):
        n = 3
        solutions = {
            pow_a: ["Pow A", n], pow_b: ["Pow B", n]
        }
        expected = 27
        results = compare_speed_seconds(
            solutions, precision=2, repeat=10
        )
        self.assertListEqual(
            [pow_a, pow_b], list(results.keys())
        )
        for actual in results.values():
            self.assertEqual(expected, actual)

    def test_compare_speed_arg_cast(self):
        n = 3
        solutions = {
            pow_a: ["Pow A", n], pow_b: ["Pow B", n],
            pow_c: ["Pow C", str(n)]
        }
        expected = 27
        results = compare_speed_seconds(solutions)
        for actual in results.values():
            self.assertEqual(expected, actual)

    def test_compare_speed_varargs(self):
        n = 3
        solutions = {
            pow_a: ["Pow A", n], pow_b: ["Pow B", n],
            pow_c: ["Pow C", str(n)], pow_d: ["Pow D", n, n]
        }
        expected = 27
        results = compare_speed_seconds(
            solutions, precision=3, repeat=10
        )
        self.assertListEqual(
            [pow_a, pow_b, pow_c, pow_d], list(results.keys())
        )
        for actual in results.values():
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
