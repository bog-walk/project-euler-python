import unittest
from util.tests.reusable import get_test_resource
from solution.batch9.problem98 import find_largest_anagramic_square_by_words, \
    find_largest_anagramic_square_by_digits


class AnagramicSquares(unittest.TestCase):
    def test_HR_problem(self):
        expected = [961, 9216, 96100, 501_264, 9_610_000, 73_462_041, 923_187_456,
                    9_814_072_356, 98_310_467_025, 985_203_145_476,
                    9_831_140_766_225]

        for n in range(3, 14):
            self.assertEqual(expected[n - 3],
                             find_largest_anagramic_square_by_digits(n))

    def test_PE_problem(self):
        resource = get_test_resource("../resources/anagramic_squares.txt",
                                     line_strip=" \n\"")
        self.assertEqual(1, len(resource))

        expected = ("BOARD", "BROAD", 18769)
        words = resource[0].split("\",\"")
        output = find_largest_anagramic_square_by_words(words)
        self.assertTupleEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
