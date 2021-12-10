import unittest
from solution.batch4.problem40 import foo


class ChampernownesConstant(unittest.TestCase):
    def test_something_low_digits(self):
        inputs = [
            [1, 2, 3, 4, 5, 6, 7],
            [8, 9, 10, 11, 12, 13, 14],
            [1, 5, 10, 15, 20, 25, 30]
        ]
        expected = [5040, 0, 140]
        for i, digits in enumerate(inputs):
            self.assertEqual(expected[i], foo(digits))


if __name__ == '__main__':
    unittest.main()
