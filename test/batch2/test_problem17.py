import unittest
from solution.batch2.problem17 import number_written, count_first_N_positives


class NumberToWords(unittest.TestCase):

    def test_number_written_pick_as_is(self):
        nums = [0, 1, 9, 12, 17, 60]
        expected = ["Zero", "One", "Nine", "Twelve", "Seventeen", "Sixty"]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], number_written(n))
            self.assertEqual(expected[i], number_written(n, include_and=False))

    def test_number_written_double_combo(self):
        nums = [21, 84, 200, 5000]
        expected = ["Twenty One", "Eighty Four", "Two Hundred", "Five Thousand"]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], number_written(n))
            self.assertEqual(expected[i], number_written(n, include_and=False))

    def test_number_written_triple_combo(self):
        nums = [243, 696]
        expected = ["Two Hundred Forty Three", "Six Hundred Ninety Six"]
        expected_and = [
            "Two Hundred And Forty Three", "Six Hundred And Ninety Six"
        ]
        for i, n in enumerate(nums):
            self.assertEqual(expected_and[i], number_written(n))
            self.assertEqual(expected[i], number_written(n, include_and=False))

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
        nums = [
            8_004_792, 10_000_000_010, 1_010_000_000, 1_000_010_000,
            101_100_000_011, 104_382_426_112
        ]
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
        for i, n in enumerate(nums):
            self.assertEqual(expected_and[i], number_written(n))
            self.assertEqual(expected[i], number_written(n, include_and=False))

    def test_count_first_N_positives(self):
        n = 1000
        expected = 21124
        self.assertEqual(expected, count_first_N_positives(n))


if __name__ == '__main__':
    unittest.main()
