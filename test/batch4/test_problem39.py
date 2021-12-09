import unittest
from solution.batch4.problem39 import get_triplet_solutions, best_triplet_perimeter


class IntegerRightTriangles(unittest.TestCase):
    def test_get_triplet_solutions(self):
        nums = [12, 60, 120, 840]
        expected = [
            [(3, 4, 5)],
            [(15, 20, 25), (10, 24, 26)],
            [(30, 40, 50), (20, 48, 52), (24, 45, 51)],
            [(210, 280, 350), (140, 336, 364), (168, 315, 357), (105, 360, 375),
             (240, 252, 348), (120, 350, 370), (56, 390, 394), (40, 399, 401)]
        ]
        for i, n in enumerate(nums):
            self.assertListEqual(expected[i], get_triplet_solutions(n))

    def test_best_triplet_perimeter(self):
        nums = [12, 80, 1000]
        expected = [12, 60, 840]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], best_triplet_perimeter(n))


if __name__ == '__main__':
    unittest.main()
