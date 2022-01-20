import unittest
from util.tests.reusable import compare_speed_seconds
from solution.batch6.problem55 import *


class LychrelNumbers(unittest.TestCase):
    def test_PE_problem(self):
        expected = 249
        self.assertEqual(expected, count_lychrel_numbers())

    def test_speed(self):
        n = 10_000
        solutions = {
            "OG": [max_palindrome_convergence, n],
            # FIX THIS
            "BS": [max_palindrome_convergence, n]
        }
        results = list(compare_speed_seconds(solutions).values())
        self.assertTupleEqual(results[0], results[1])


if __name__ == '__main__':
    unittest.main()
