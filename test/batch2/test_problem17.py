import unittest
from solution.batch2.problem17 import *


class NumberToWords(unittest.TestCase):

    def test_number_written_pick_as_is(self):
        nums = [0, 1, 9, 12, 17, 60]
        expected = ["Zero", "One", "Nine", "Twelve", "Seventeen", "Sixty"]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], number_written(n))
            self.assertEqual(expected[index], number_written(n, include_and=False))

    def test_number_written_double_combo(self):
        nums = [21, 84, 200, 5000]
        expected = ["Twenty One", "Eighty Four", "Two Hundred", "Five Thousand"]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], number_written(n))
            self.assertEqual(expected[index], number_written(n, include_and=False))

    def test_number_written_triple_combo(self):
        nums = [243]
        expected = ["Two Hundred Forty Three"]
        expected_and = ["Two Hundred And Forty Three"]
        for index, n in enumerate(nums):
            self.assertEqual(expected_and[index], number_written(n))
            self.assertEqual(expected[index], number_written(n, include_and=False))

    def test_number_written_powers_of_ten(self):
        expected = [
            "Ten", "One Hundred", "One Thousand", "Ten Thousand", "One Hundred Thousand",
            "One Million", "Ten Million", "One Hundred Million", "One Billion"
        ]
        for e in range(8):
            n = 10 * (pow(10, e))
            self.assertEqual(expected[e], number_written(n))
            self.assertEqual(expected[e], number_written(n, include_and=False))

    def test_number_written_long_combo(self):
        nums = [8004792, 10000000010, 1010000000, 1000010000, 101100000011, 104382426112]
        expected = [
            "Eight Million Four Thousand Seven Hundred Ninety Two",
            "Ten Billion Ten", "One Billion Ten Million", "One Billion Ten Thousand",
            "One Hundred One Billion One Hundred Million Eleven",
            "One Hundred Four Billion Three Hundred Eighty Two Million Four Hundred Twenty "
            "Six Thousand One Hundred Twelve"
        ]
        expected_and = [
            "Eight Million Four Thousand Seven Hundred And Ninety Two",
            "Ten Billion Ten", "One Billion Ten Million", "One Billion Ten Thousand",
            "One Hundred And One Billion One Hundred Million Eleven",
            "One Hundred And Four Billion Three Hundred And Eighty Two Million Four Hundred And Twenty "
            "Six Thousand One Hundred And Twelve"
        ]
        for index, n in enumerate(nums):
            self.assertEqual(expected_and[index], number_written(n))
            self.assertEqual(expected[index], number_written(n, include_and=False))

    def test_count_letters(self):
        numbers = ["Four", "One Hundred And Fifteen", "Three Hundred And Forty-Two"]
        expected = [4, 20, 23]
        for index, number in enumerate(numbers):
            self.assertEqual(expected[index], count_letters(number))

    def test_count_first_N_positives(self):
        self.assertEqual(21124, count_first_N_positives(1000))


if __name__ == '__main__':
    unittest.main()
