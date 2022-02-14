import unittest
from util.tests.reusable import compare_speed
from solution.batch2.problem24 import *


class LexicographicPermutations(unittest.TestCase):
    def test_lexico_perms_short_string(self):
        string = "abc"
        expected = ["abc", "acb", "bac", "bca", "cab", "cba"]
        for n in range(6):
            self.assertEqual(expected[n], nth_lexicographic_perm(n, string))
            self.assertEqual(expected[n], nth_lexicographic_perm_improved(n, string))
            self.assertEqual(expected[n], nth_lexicographic_perm_builtin(n, string))

    def test_lexico_perms_long_string(self):
        string = "0123456789"
        # 10! = 3_628_800 permutations, already 0-indexed
        perms = [0, 362_880, 1_088_640, 3_628_799]
        expected = [
            "0123456789", "1023456789", "3012456789", "9876543210"
        ]
        for i, p in enumerate(perms):
            self.assertEqual(expected[i], nth_lexicographic_perm(p, string))
            self.assertEqual(expected[i], nth_lexicographic_perm_improved(p, string))
            self.assertEqual(expected[i], nth_lexicographic_perm_builtin(p, string))

    def test_lexico_perms_speed(self):
        string = "0123456789"
        perm = 999_999  # the millionth permutation
        expected = "2783915460"
        solutions = {
            "Builtin": [nth_lexicographic_perm_builtin, perm, string],
            "Original": [nth_lexicographic_perm, perm, string],
            "Improved": [nth_lexicographic_perm_improved, perm, string]
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
