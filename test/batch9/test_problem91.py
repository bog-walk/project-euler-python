import unittest
from solution.batch9.problem91 import count_right_triangles


class RightTrianglesWithIntegerCoordinates(unittest.TestCase):
    def test_lower_constraints(self):
        expected = [14, 33, 62, 101, 148, 207]
        for n in range(2, 8):
            self.assertEqual(expected[n-2], count_right_triangles(n))

    def test_mid_constraints(self):
        inputs = [30, 50, 100, 333]
        expected = [4764, 14234, 62848, 812_759]
        for i, e in zip(inputs, expected):
            self.assertEqual(e, count_right_triangles(i))

    def test_upper_constraints(self):
        inputs = [1000, 1999, 2500]
        expected = [8_318_030, 35_734_575, 57_183_752]
        for i, e in zip(inputs, expected):
            self.assertEqual(e, count_right_triangles(i))


if __name__ == '__main__':
    unittest.main()
