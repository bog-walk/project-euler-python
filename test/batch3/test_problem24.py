import unittest
from time import perf_counter_ns
from solution.batch3.problem24 import *


class LexicographicPermutations(unittest.TestCase):
    def test_lexico_perms_short_string(self):
        string = "abc"
        expected = ["abc", "acb", "bac", "bca", "cab", "cba"]
        for n in range(6):
            self.assertEqual(expected[n], lexicographic_perms(n, string))
            self.assertEqual(expected[n], lexicographic_perms_improved(n, string))
            self.assertEqual(expected[n], lexicographic_perms_builtin(n, string))

    def test_lexico_perms_long_string(self):
        string = "0123456789"
        # 10! = 3628800 permutations, already 0-indexed
        perms = [0, 362880, 999999, 1088640, 3628799]
        expected = ["0123456789", "1023456789", "2783915460", "3012456789", "9876543210"]
        for index, p in enumerate(perms):
            self.assertEqual(expected[index], lexicographic_perms(p, string))
            self.assertEqual(expected[index], lexicographic_perms_improved(p, string))
            self.assertEqual(expected[index], lexicographic_perms_builtin(p, string))

    def test_speed_comparison(self):
        string = "0123456789"
        perm = 999999  # the millionth permutation
        expected = "2783915460"
        solutions = [
            lexicographic_perms_builtin,
            lexicographic_perms,
            lexicographic_perms_improved
        ]
        starts = []
        stops = []
        for i, solution in enumerate(solutions):
            starts.insert(i, perf_counter_ns())
            self.assertEqual(expected, solution(perm, string))
            stops.insert(i, perf_counter_ns())
        print(f"Builtin solution took: {stops[0] - starts[0]}ns\n" +
              f"Alt solution took: {stops[1] - starts[1]}ns\n" +
              f"Improved solution took: {stops[2] - starts[2]}ns\n")


if __name__ == '__main__':
    unittest.main()
