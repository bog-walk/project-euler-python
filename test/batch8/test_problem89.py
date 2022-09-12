import unittest
from util.tests.reusable import get_test_resource
from solution.batch8.problem89 import get_roman_number, roman_chars_saved


class RomanNumerals(unittest.TestCase):
    def test_HR_problem_more_than_3_consecutive_not_M(self):
        inputs = ["IIIII", "MMMMMMMMMMMMMIIII", "MDCCCCII", "XXXXVIIII"]
        expected = ["V", "MMMMMMMMMMMMMIV", "MCMII", "XLIX"]
        for i, e in zip(inputs, expected):
            self.assertEqual(e, get_roman_number(i))

    def test_HR_problem_more_than_once_consecutive_VLD(self):
        inputs = ["VVVVVVVVV", "LLLXXXXX", "VVVI"]
        expected = ["XLV", "CC", "XVI"]
        for i, e in zip(inputs, expected):
            self.assertEqual(e, get_roman_number(i))

    def test_HR_problem_incorrect_subtraction(self):
        string = "IM"
        expected = "CMXCIX"
        self.assertEqual(expected, get_roman_number(string))

    def test_HR_problem_already_minimal_efficient(self):
        inputs = ["CCXX", "XIV", "CMXCIX", "MMMMDCLXXII", "LI"]
        expected = ["CCXX", "XIV", "CMXCIX", "MMMMDCLXXII", "LI"]
        for i, e in zip(inputs, expected):
            self.assertEqual(e, get_roman_number(i))

    def test_PE_problem(self):
        inputs = get_test_resource("../resources/roman_numerals.txt")
        expected = 743
        self.assertEqual(expected, roman_chars_saved(inputs))


if __name__ == '__main__':
    unittest.main()
