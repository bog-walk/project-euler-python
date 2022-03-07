import unittest
from util.tests.reusable import get_test_resource
from solution.batch5.problem59 import xor_decryption, sum_of_decrypted_codes


class XORDecryption(unittest.TestCase):
    def test_HR_problem_only_letters(self):
        encryption = [
            32, 66, 50, 20, 11, 0, 42, 66, 33, 19, 13, 20, 47, 66, 37, 14, 58, 67,
            43, 23, 14, 17, 49, 67, 46, 20, 6, 51, 66, 55, 9, 39, 67, 45, 3, 25,
            56, 66, 39, 14, 37, 34, 65, 51, 22, 8, 1, 40, 65, 32, 17, 14, 21, 45,
            65, 36, 12, 57, 66, 41, 20, 15, 19, 50, 66, 44, 23, 7, 49, 65, 54, 11,
            36, 66, 47, 0, 24, 58, 65, 38, 12, 38
        ]
        expected = "abc"
        self.assertEqual(expected, xor_decryption(encryption))

    def test_HR_problem_letters_and_digits(self):
        encryption = [
            50, 9, 13, 21, 65, 13, 21, 65, 85, 70, 18, 5, 11, 17, 8, 3, 65, 9, 3,
            18, 23, 7, 6, 1, 70, 22, 13, 18, 9, 68, 87, 81, 68, 2, 8, 3, 15, 21, 23,
            70, 8, 10, 70, 8, 16, 46, 4, 22, 3, 65, 13, 21, 65, 87, 70, 0, 10, 2,
            65, 86, 95, 65, 5, 8, 5, 68, 82, 81, 84, 83, 65, 5, 8, 5, 68, 18, 9, 1,
            8, 65, 5, 70, 22, 12, 9, 13, 1, 70, 3, 17, 8, 2, 12, 70, 14, 2, 70, 22,
            11, 20, 5, 23, 70, 21, 11, 70, 7, 13, 10, 13, 68, 18, 9, 1, 70, 18,
            13, 28, 4, 68, 20, 4, 21, 19, 8, 22, 3, 12, 1, 8, 21
        ]
        expected = "fad"
        self.assertEqual(expected, xor_decryption(encryption))

    def test_HR_problem_letters_digits_punctuations_1(self):
        expected = "qzd"
        resource: list[list[int]] = get_test_resource(
            "../resources/xor_decryption_ldp_1.txt", ", \n", int, ", "
        )
        # flatmap nested lists
        encryption: list[int] = [code for line in resource for code in line]
        self.assertEqual(expected, xor_decryption(encryption))

    def test_HR_problem_letters_digits_punctuations_2(self):
        expected = "lse"
        resource: list[list[int]] = get_test_resource(
            "../resources/xor_decryption_ldp_2.txt", ", \n", int, ", "
        )
        # flatmap nested lists
        encryption: list[int] = [code for line in resource for code in line]
        self.assertEqual(expected, xor_decryption(encryption))

    def test_PE_problem(self):
        expected = 129_448
        resource: list[list[int]] = get_test_resource(
            "../resources/xor_decryption_pe.txt", ", \n", int, ","
        )
        # flatmap nested lists
        encryption: list[int] = [code for line in resource for code in line]
        self.assertEqual(expected, sum_of_decrypted_codes(encryption))


if __name__ == '__main__':
    unittest.main()
