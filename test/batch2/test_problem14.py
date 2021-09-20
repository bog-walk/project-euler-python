import unittest
from solution.batch2.problem14 import *


class LongestCollatzSequence(unittest.TestCase):
    def test_collatz_length(self):
        starts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 17, 19, 27]
        expected = [1, 2, 8, 3, 6, 9, 17, 4, 20, 7, 15, 10, 18, 13, 21, 112]
        for index, start in enumerate(starts):
            self.assertEqual(expected[index], collatz_length(start))

    def test_longest_collatz_under_N(self):
        all_lengths = generate_collatz_lengths(1000000)
        nums = [1, 2, 3, 5, 10, 15, 19, 20, 26, 100, 1000, 10000, 100000, 1000000]
        expected = [1, 2, 3, 3, 9, 9, 19, 19, 25, 97, 871, 6171, 77031, 837799]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], longest_collatz_under_N(n, all_lengths))


if __name__ == '__main__':
    unittest.main()
