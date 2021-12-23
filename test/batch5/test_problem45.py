import unittest
from solution.batch5.problem45 import common_numbers, next_triple_type


class TriPentHex(unittest.TestCase):
    def test_common_numbers_low(self):
        expected = [1]
        self.assertListEqual(expected, common_numbers(2, 3, 5))
        self.assertListEqual(expected, common_numbers(2, 5, 6))
        self.assertListEqual(expected, common_numbers(10, 3, 5))

    def test_common_numbers_mid(self):
        self.assertListEqual([1, 210], common_numbers(10_000, 3, 5))
        self.assertListEqual([1, 40755], common_numbers(100_000, 5, 6))

    def test_common_numbers_high(self):
        self.assertListEqual(
            [1, 210, 40755],
            common_numbers(1_000_000, 3, 5)
        )
        self.assertListEqual(
            [1, 40755],
            common_numbers(10_000_000, 5, 6)
        )

    def test_next_triple_type(self):
        expected = 1533776805
        self.assertEqual(expected, next_triple_type())


if __name__ == '__main__':
    unittest.main()
