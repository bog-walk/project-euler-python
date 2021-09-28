import unittest
from solution.batch3.problem25 import n_digit_fib_terms


class NDigitFibonacciNumber(unittest.TestCase):
    def test_n_digit_fib_terms(self):
        all_terms = n_digit_fib_terms(5000)
        digits = [2, 3, 4, 9, 1000, 5000]
        expected = [7, 12, 17, 40, 4782, 23922]
        for index, digit in enumerate(digits):
            self.assertEqual(expected[index], all_terms[digit - 2])


if __name__ == '__main__':
    unittest.main()
