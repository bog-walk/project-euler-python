import unittest
from util.tests.reusable import compare_speed_seconds
from solution.batch5.problem43 import sum_of_pandigital_substrings, \
    sum_of_9_pandigital_substrings


class SubstringDivisibility(unittest.TestCase):
    def test_sum_of_pandigital_subs(self):
        expected = [
            22212, 711104, 12444480, 189838560, 1099210170, 1113342912, 16695334890
        ]
        for n in range(3, 10):
            self.assertEqual(expected[n-3], sum_of_pandigital_substrings(n))

    def test_sum_of_9_pandigital_subs_speed(self):
        expected = 16695334890
        solutions = {
            "Brute": [sum_of_pandigital_substrings, 9],
            "Filtered": [sum_of_9_pandigital_substrings]
        }
        results = compare_speed_seconds(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
