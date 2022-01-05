import unittest
from util.strings.reusable import *


class StringsReusable(unittest.TestCase):
    def test_is_palindrome_all_true(self):
        test_n = ["5", "22", "303", "9119"]
        for n in test_n:
            self.assertTrue(is_palindrome(n))
            self.assertTrue(is_palindrome_recursive(n))
            self.assertTrue(is_palindrome_number(n))

    def test_is_palindrome_all_false(self):
        test_n = ["10", "523", "8018", "124521"]
        for n in test_n:
            self.assertFalse(is_palindrome(n))
            self.assertFalse(is_palindrome_recursive(n))
            self.assertFalse(is_palindrome_number(n))


if __name__ == '__main__':
    unittest.main()
