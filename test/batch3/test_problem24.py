import unittest
from time import perf_counter
from solution.batch3.problem24 import *


class LexicographicPermutations(unittest.TestCase):
    def test_lexico_perms_short_string(self):
        string = "abc"
        expected = ["abc", "acb", "bac", "bca", "cab", "cba"]
        for n in range(6):
            self.assertEqual(expected[n], lexicographic_perms(n, string))
            self.assertEqual(expected[n], lexicographic_perms_builtin(n, string))

    def test_lexico_perms_long_string(self):
        string = "0123456789"
        # 10! = 3628800 permutations, already 0-indexed
        perms = [0, 362880, 999999, 1088640, 3628799]
        expected = ["0123456789", "1023456789", "2783915460", "3012456789", "9876543210"]
        for index, p in enumerate(perms):
            self.assertEqual(expected[index], lexicographic_perms(p, string))
            self.assertEqual(expected[index], lexicographic_perms_builtin(p, string))

    def test_speed_comparison(self):
        string = "0123456789"
        perm = 999999  # the millionth permutation
        builtin_sol_start = perf_counter()
        builtin_ans = lexicographic_perms_builtin(perm, string)
        builtin_sol_end = perf_counter()
        alt_sol_start = perf_counter()
        alt_ans = lexicographic_perms(perm, string)
        alt_sol_end = perf_counter()
        print(f"Builtin solution took: {builtin_sol_end - builtin_sol_start:0.4f}s\n" +
              f"Alt solution took: {alt_sol_end - alt_sol_start:0.4f}s")
        self.assertEqual(builtin_ans, alt_ans)


if __name__ == '__main__':
    unittest.main()
