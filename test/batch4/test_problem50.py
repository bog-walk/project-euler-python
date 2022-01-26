import unittest
from util.tests.reusable import compare_speed_seconds
from solution.batch4.problem50 import *


class ConsecutivePrimeSum(unittest.TestCase):
    def test_lower_constraints(self):
        nums = [
            2, 5, 10, 20, 50, 100, 150, 200, 300, 500, 1000, 2000, 10_000, 22340
        ]
        expected = [
            (2, 1), (5, 2), (5, 2), (17, 4), (41, 6), (41, 6), (127, 9),
            (197, 12), (281, 14), (499, 17), (953, 21),
            (1583, 27), (9521, 65), (22039, 96)
        ]
        for i, n in enumerate(nums):
            self.assertTupleEqual(expected[i], consecutive_prime_sum(n))
            self.assertTupleEqual(expected[i], consecutive_prime_sum_improved(n))

    def test_mid_values(self):
        expected = [
            (92_951, 183), (997_651, 543),
            (9_951_191, 1587), (99_819_619, 4685), (999_715_711, 13935)
        ]
        for i in range(5, 10):
            n = pow(10, i)
            self.assertTupleEqual(expected[i - 5], consecutive_prime_sum(n))
            self.assertTupleEqual(expected[i - 5], consecutive_prime_sum_improved(n))

    def test_upper_constraints(self):
        expected = [(99_987_684_473, 125_479), (999_973_156_643, 379_317)]
        for i in range(11, 13):
            n = pow(10, i)
            self.assertTupleEqual(expected[i - 11], consecutive_prime_sum_improved(n))

    def test_consecutive_prime_sum_speed(self):
        n = pow(10, 10)
        expected = (9_999_419_621, 41708)
        solutions = {
            "Brute": [consecutive_prime_sum, n],
            "Improved": [consecutive_prime_sum_improved, n]
        }
        results = compare_speed_seconds(solutions, precision=2)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
