import unittest
from solution.batch5.problem51 import smallest_prime_digit_repl, \
    smallest_8_prime_family


class PrimeDigitReplacements(unittest.TestCase):
    def test_HR_problem(self):
        arguments = [
            (2, 1, 3), (2, 1, 6), (5, 2, 7), (6, 3, 8), (5, 1, 2),
            (3, 2, 1), (7, 4, 6)
        ]
        expected = [
            [11, 13, 17], [13, 23, 43, 53, 73, 83],
            [56003, 56113, 56333, 56443, 56663, 56773, 56993],
            [12_1313, 222_323, 323_333, 424_343, 525_353, 626_363, 828_383, 929_393],
            [10007, 10009], [101],
            [2_422_027, 3_433_037, 5_455_057, 6_466_067, 8_488_087, 9_499_097]
        ]
        for i, (n, k, length) in enumerate(arguments):
            self.assertListEqual(
                expected[i],
                smallest_prime_digit_repl(n, k, length)
            )

    def test_PE_problem(self):
        expected = 121_313
        self.assertEqual(expected, smallest_8_prime_family())


if __name__ == '__main__':
    unittest.main()
