import unittest
from reusable import *


class StringsReusable(unittest.TestCase):
    def test_is_palindrome_all_true(self):
        nums = ["5", "22", "303", "9119"]
        for n in nums:
            self.assertTrue(is_palindrome_recursive(n))
            self.assertTrue(is_palindrome_number(n))
            self.assertTrue(is_palindrome_manual(n))
            self.assertTrue(is_palindrome(n))

    def test_is_palindrome_all_false(self):
        nums = ["10", "523", "8018", "124521"]
        for n in nums:
            self.assertFalse(is_palindrome_recursive(n))
            self.assertFalse(is_palindrome_number(n))
            self.assertFalse(is_palindrome_manual(n))
            self.assertFalse(is_palindrome(n))

    def test_is_pandigital_all_true(self):
        strings = ["1", "231", "54321", "564731982", "1234560789"]
        digits = [1, 3, 5, 9, 10]
        for i, s in enumerate(strings):
            self.assertTrue(is_pandigital(s, digits[i]))

    def test_is_pandigital_all_false(self):
        strings = ["", "1", "85018", "810"]
        digits = [10, 4, 5, 3]
        for i, s in enumerate(strings):
            self.assertFalse(is_pandigital(s, digits[i]))


if __name__ == '__main__':
    unittest.main()
