import unittest
from solution.batch4.problem40 import champernownes_product, get_constant


class ChampernownesConstant(unittest.TestCase):
    def test_get_constant(self):
        position = [1, 10, 33, 65, 90, 145, 200, 298]
        expected = [1, 1, 1, 7, 5, 7, 0, 1]
        for i, pos in enumerate(position):
            self.assertEqual(expected[i], get_constant(pos))

    def test_champernownes_product_low(self):
        inputs = [
            [1, 2, 3, 4, 5, 6, 7],
            [8, 9, 10, 11, 12, 13, 14],
            [1, 5, 10, 15, 20, 25, 30]
        ]
        expected = [5040, 0, 140]
        for i, digits in enumerate(inputs):
            self.assertEqual(expected[i], champernownes_product(digits))

    def test_champernownes_product_mid(self):
        inputs = [
            [10, 20, 30, 40, 50, 60, 70],
            [11, 21, 31, 41, 51, 61, 71],
            [1, 2, 4, 8, 16, 32, 64, 128]
        ]
        expected = [144, 0, 2304]
        for i, digits in enumerate(inputs):
            self.assertEqual(expected[i], champernownes_product(digits))

    def test_champernownes_product_high(self):
        digits = [1, 10, 100, 1000, 10000, 100000, 1000000]
        expected = 210
        self.assertEqual(expected, champernownes_product(digits))


if __name__ == '__main__':
    unittest.main()