import unittest
from util.tests.reusable import compare_speed_seconds
from solution.batch4.problem43 import sum_of_pandigital_substrings, \
    sum_of_9_pandigital_substrings


class SubstringDivisibility(unittest.TestCase):
    def test_sum_of_pandigital_subs(self):
        expected = [
            22212, 711_104, 12_444_480, 189_838_560,
            1_099_210_170, 1_113_342_912
        ]
        for n in range(3, 9):
            self.assertEqual(expected[n-3], sum_of_pandigital_substrings(n))

    def test_sum_of_9_pandigital_subs_speed(self):
        n = 9
        expected = 16_695_334_890
        solutions = {
            "Brute": [sum_of_pandigital_substrings, n],
            "Filtered": [sum_of_9_pandigital_substrings]
        }
        results = compare_speed_seconds(solutions, precision=3)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
