import unittest
from solution.batch1.problem14 import *


class LongestCollatzSequence(unittest.TestCase):
    def test_collatz_length(self):
        starts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 17, 19, 27]
        expected = [1, 2, 8, 3, 6, 9, 17, 4, 20, 7, 15, 10, 18, 13, 21, 112]
        for i, start in enumerate(starts):
            self.assertEqual(expected[i], collatz_length(start))

    def test_longest_collatz_under_N(self):
        starters = generate_longest_starters(1_000_000)
        nums = [
            1, 2, 3, 5, 10, 15, 19, 20, 26, 100,
            1000, 10_000, 100_000, 1_000_000
        ]
        expected = [
            1, 2, 3, 3, 9, 9, 19, 19, 25, 97,
            871, 6171, 77031, 837_799
        ]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], largest_collatz_starter(starters, n))


if __name__ == '__main__':
    unittest.main()
