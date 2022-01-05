import unittest
from solution.batch1.problem4 import *


class LargestPalindromeProduct(unittest.TestCase):

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
