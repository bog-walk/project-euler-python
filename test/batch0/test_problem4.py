import unittest
from solution.batch0.problem4 import largest_palindrome_product


class LargestPalindromeProduct(unittest.TestCase):
    def test_lower_constraints(self):
        nums = [101_102, 101_110]
        expected = 101101
        for n in nums:
            self.assertEquals(expected, largest_palindrome_product(n))

    def test_upper_constraints(self):
        n = 1_000_000 - 1
        expected = 906_609
        self.assertEquals(expected, largest_palindrome_product(n))

    def test_normal_n(self):
        nums = [794_000, 650_001]
        expected = [793_397, 649_946]
        for i, n in enumerate(nums):
            self.assertEquals(expected[i], largest_palindrome_product(n))

    def test_n_is_palindrome(self):
        n = 332_233
        expected = 330_033
        self.assertEquals(expected, largest_palindrome_product(n))


if __name__ == '__main__':
    unittest.main()
