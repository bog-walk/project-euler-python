import unittest
from util.tests.reusable import get_test_resource
from solution.batch5.problem42 import *


class CodedTriangleNumbers(unittest.TestCase):
    def test_triangle_term_all_false(self):
        nums = [2, 5, 26, 54, 218]
        for n in nums:
            self.assertEqual(-1, triangle_term(n))
            self.assertEqual(-1, triangle_term_improved(n))

    def test_triangle_term_all_true(self):
        nums = [1, 3, 6, 10, 55, 210, 5050, 500_500, 4_999_999_950_000_000]
        expected = [1, 2, 3, 4, 10, 20, 100, 1000, 99_999_999]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], triangle_term(n))
            self.assertEqual(expected[i], triangle_term_improved(n))

    def test_count_triangle_words(self):
        input_file = "../resources/coded_triangle_numbers"
        words = get_test_resource(input_file)
        expected = 162
        self.assertEqual(expected, count_triangle_words(words))


if __name__ == '__main__':
    unittest.main()
