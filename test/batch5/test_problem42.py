import unittest
from solution.batch5.problem42 import *


def get_long_list(filename):
    with open(filename) as listFile:
        # Could use readlines() but extra whitespace would affect output
        long_list = [row.strip() for row in listFile]
    return long_list


class CodedTriangleNumbers(unittest.TestCase):
    def test_triangle_term_all_false(self):
        test_n = [2, 5, 26, 54, 218]
        for n in test_n:
            self.assertEqual(-1, triangle_term(n))
            self.assertEqual(-1, triangle_term_improved(n))

    def test_triangle_term_all_true(self):
        test_n = [1, 3, 6, 10, 55, 210, 5050, 500500, 4999999950000000]
        expected = [1, 2, 3, 4, 10, 20, 100, 1000, 99999999]
        for i, n in enumerate(test_n):
            self.assertEqual(expected[i], triangle_term(n))
            self.assertEqual(expected[i], triangle_term_improved(n))

    def test_count_triangle_words(self):
        input_file = "../resources/coded_triangle_numbers"
        words = get_long_list(input_file)
        expected = 162
        self.assertEqual(expected, count_triangle_words(words))


if __name__ == '__main__':
    unittest.main()