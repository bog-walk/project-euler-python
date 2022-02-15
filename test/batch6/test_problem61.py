import unittest
from solution.batch6.problem61 import cyclical_figurates


class CyclicalFigurateNumbers(unittest.TestCase):
    def test_cyclical_figurates_lower_constraints(self):
        polygons = {3, 4, 5}
        expected = [[2882, 8281, 8128]]
        self.assertListEqual(expected, cyclical_figurates(polygons))

    def test_cyclical_figurates_mid_constraints_1(self):
        polygons = {3, 4, 5, 6}
        expected = [[1653, 5370, 7021, 2116], [1770, 7021, 2116, 1617]]
        self.assertListEqual(expected, cyclical_figurates(polygons))

    def test_cyclical_figurates_mid_constraints_2(self):
        polygons = {4, 5, 6, 7}
        expected = [[1651, 5151, 5192, 9216]]
        self.assertListEqual(expected, cyclical_figurates(polygons))

    def test_cyclical_figurates_multiple_cycles(self):
        polygons = {3, 4, 6, 7}
        expected = [[2512, 1225, 2556, 5625], [2839, 3916, 1681, 8128]]
        self.assertListEqual(expected, cyclical_figurates(polygons))

    def test_cyclical_figurates_separate_polygonals(self):
        polygons = {3, 5, 7}
        expected = []
        self.assertListEqual(expected, cyclical_figurates(polygons))

    def test_cyclical_figurates_upper_constraints(self):
        polygons = {3, 4, 5, 6, 7, 8}
        expected = [[1281, 8128, 2882, 8256, 5625, 2512]]
        self.assertListEqual(expected, cyclical_figurates(polygons))


if __name__ == '__main__':
    unittest.main()
