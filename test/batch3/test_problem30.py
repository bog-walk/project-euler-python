import unittest
from solution.batch3.problem30 import *


class DigitFifthPowers(unittest.TestCase):
    def test_digit_nth_powers(self):
        expected = [
            [153, 370, 371, 407],
            [1634, 8208, 9474],
            [4150, 4151, 54748, 92727, 93084, 194979],
            [548834]
        ]
        for n in range(3, 7):
            self.assertListEqual(expected[n - 3], digit_nth_powers_brute(n))


if __name__ == '__main__':
    unittest.main()
