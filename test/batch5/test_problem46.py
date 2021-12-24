import unittest
from solution.batch5.problem46 import smallest_failing_num, goldbach_repr


class GoldbachsOtherConjecture(unittest.TestCase):
    def test_goldbach_repr_low(self):
        odds = [9, 15, 21, 25, 27, 33]
        expected = [1, 2, 3, 3, 1, 1]
        for i, odd in enumerate(odds):
            self.assertEqual(expected[i], goldbach_repr(odd))

    def test_goldbach_repr_mid(self):
        odds = [403, 695, 1599, 3393]
        expected = [5, 2, 12, 10]
        for i, odd in enumerate(odds):
            self.assertEqual(expected[i], goldbach_repr(odd))

    def test_goldbach_repr_high(self):
        odds = [23851, 499999]
        expected = [53, 156]
        for i, odd in enumerate(odds):
            self.assertEqual(expected[i], goldbach_repr(odd))

    def test_smallest_failing_num(self):
        expected = 5777
        self.assertEqual(expected, smallest_failing_num())

    def test_goldbach_repr_no_rep(self):
        expected = 0
        self.assertEqual(expected, goldbach_repr(5777))


if __name__ == '__main__':
    unittest.main()
