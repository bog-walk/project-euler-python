import unittest

from util.tests.reusable import compare_speed
from solution.batch7.problem72 import *


class CountingFractions(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.all_farey_lengths = generate_all_farey_lengths(1_000_000)

    def test_lower_constraints(self):
        expected = [1, 3, 5, 9, 11, 17, 21]
        for n in range(2, 9):
            self.assertEqual(expected[n-2], farey_sequence_length_formula(n))
            self.assertEqual(expected[n-2], farey_sequence_length_sieve(n))
            self.assertEqual(expected[n-2], self.all_farey_lengths[n])

    def test_mid_constraints(self):
        nums = [100, 200, 678, 1999, 8888, 10_000]
        expected = [
            3043, 12231, 139_897, 1_215_787, 24_015_245, 30_397_485
        ]
        for n, e in zip(nums, expected):
            self.assertEqual(e, farey_sequence_length_formula(n))
            self.assertEqual(e, farey_sequence_length_sieve(n))
            self.assertEqual(e, self.all_farey_lengths[n])

    def test_upper_constraints(self):
        nums = [51999, 300_000]
        expected = [821_903_377, 27_356_748_483]
        for n, e in zip(nums, expected):
            self.assertEqual(e, farey_sequence_length_formula(n))
            self.assertEqual(e, farey_sequence_length_sieve(n))
            self.assertEqual(e, self.all_farey_lengths[n])

    def test_upper_constraints_speed(self):
        n = 1_000_000
        expected = 303_963_552_391
        solutions = {
            "Formula": [farey_sequence_length_formula, n],
            "Sieve": [farey_sequence_length_sieve, n],
            "Generator": [generate_all_farey_lengths, n]
        }    
        results = compare_speed(solutions)
        self.assertEqual(expected, results["Formula"])
        self.assertEqual(expected, results["Sieve"])
        self.assertEqual(expected, results["Generator"][n])


if __name__ == '__main__':
    unittest.main()
