import unittest
from solution.batch8.problem90 import count_valid_cubes


class CubeDigitPairs(unittest.TestCase):
    def test_with_1_cube(self):
        cubes = 1
        expected = [126, 70, 55]
        for n in range(1, 4):
            self.assertEqual(expected[n-1], count_valid_cubes(n, cubes))

    def test_with_2_cubes(self):
        cubes = 2
        expected = [9450, 8630, 8150, 3946, 2579, 2365]
        for n in range(2, 8):
            self.assertEqual(expected[n-2], count_valid_cubes(n, cubes))

    def test_with_3_cubes(self):
        cubes = 3
        squares = [3, 4, 10, 20, 30]
        expected = [519_805, 518_050, 294_197, 28954, 9600]
        for n, e in zip(squares, expected):
            self.assertEqual(e, count_valid_cubes(n, cubes))


if __name__ == '__main__':
    unittest.main()
