import unittest
from solution.batch0.problem4 import largest_palindrome_product, \
    largest_palindrome_product_brute, largest_palindrome_product_brute_backwards, \
    largest_palindrome_product_alt
from util.tests.reusable import compare_speed


class LargestPalindromeProduct(unittest.TestCase):
    def test_lower_constraints(self):
        nums = [101_102, 101_110]
        expected = 101_101
        for n in nums:
            self.assertEquals(expected, largest_palindrome_product(n))
            self.assertEquals(expected, largest_palindrome_product_alt(n))
            self.assertEquals(expected, largest_palindrome_product_brute(n))
            self.assertEquals(
                expected, largest_palindrome_product_brute_backwards(n)
            )

    def test_mid_constraints(self):
        nums = [794_000, 650_001]
        expected = [793_397, 649_946]
        for i, n in enumerate(nums):
            self.assertEquals(expected[i], largest_palindrome_product(n))
            self.assertEquals(expected[i], largest_palindrome_product(n))
            self.assertEquals(expected[i], largest_palindrome_product_alt(n))
            self.assertEquals(expected[i], largest_palindrome_product_brute(n))
            self.assertEquals(
                expected[i], largest_palindrome_product_brute_backwards(n)
            )

    def test_n_is_palindrome(self):
        n = 332_233
        expected = 330_033
        self.assertEquals(expected, largest_palindrome_product(n))
        self.assertEquals(expected, largest_palindrome_product_alt(n))
        self.assertEquals(expected, largest_palindrome_product_brute(n))
        self.assertEquals(
            expected, largest_palindrome_product_brute_backwards(n)
        )

    def test_upper_constraints_speed(self):
        n = 1_000_000 - 1
        expected = 906_609
        solutions = {
            "Brute": [largest_palindrome_product_brute, n],
            "Brute Backwards": [largest_palindrome_product_brute_backwards, n],
            "Valid Palindrome": [largest_palindrome_product_alt, n],
            "Improved": [largest_palindrome_product, n]
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
