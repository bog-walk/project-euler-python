import unittest
from time import perf_counter_ns, perf_counter
from solution.batch1.problem4 import *


class LargestPalindromeProduct(unittest.TestCase):
    def test_is_palindrome_all_true(self):
        test_n = [5, 22, 303, 9119]
        for n in test_n:
            self.assertTrue(is_palindrome(n))
            self.assertTrue(is_palindrome_recursive(n))
            self.assertTrue(is_palindrome_no_cast(n))

    def test_is_palindrome_all_false(self):
        test_n = [10, 523, 8018, 124521]
        for n in test_n:
            self.assertFalse(is_palindrome(n))
            self.assertFalse(is_palindrome_recursive(n))
            self.assertFalse(is_palindrome_no_cast(n))

    def test_is_palindrome_speed_comparison(self):
        n = 987654321123456789
        solutions = [
            is_palindrome, is_palindrome_recursive, is_palindrome_no_cast
        ]
        starts = []
        stops = []
        for solution in solutions:
            ans = False
            starts.append(perf_counter())
            for _ in range(1000):
                ans = solution(n)
            stops.append(perf_counter())
            self.assertTrue(ans)
        print(f"String in-built solution took: {stops[0] - starts[0]:0.4f}s\n"
              f"String recursive solution took: {stops[1] - starts[1]:0.4f}s\n"
              f"Maths only solution took: {stops[2] - starts[2]:0.4f}s\n")

    def test_largest_palindrome_product_lower_constraints(self):
        test_n = [101102, 101110]
        expected = 101101
        for n in test_n:
            self.assertEquals(expected, largest_palindrome_product(n))

    def test_largest_palindrome_product_upper_constraints(self):
        self.assertEquals(906609, largest_palindrome_product(1000000))

    def test_largest_palindrome_product_normals(self):
        test_n = [794000, 650001]
        expected = [793397, 649946]
        for index, n in enumerate(test_n):
            self.assertEquals(expected[index], largest_palindrome_product(n))

    def test_largest_palindrome_product_n_is_palindrome(self):
        self.assertEquals(330033, largest_palindrome_product(332233))


if __name__ == '__main__':
    unittest.main()
