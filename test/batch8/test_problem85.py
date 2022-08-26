import unittest
from solution.batch8.problem85 import find_closest_containing_area


class CountingRectangles(unittest.TestCase):
    def test_lower_constraints(self):
        targets = [2, 11, 18, 20, 25, 33, 49, 66]
        expected = [2, 4, 6, 6, 7, 9, 10, 11]
        for t, e in zip(targets, expected):
            self.assertEqual(e, find_closest_containing_area(t))

    def test_mid_constraints(self):
        targets = [100, 333, 1000]
        expected = [16, 30, 56]
        for t, e in zip(targets, expected):
            self.assertEqual(e, find_closest_containing_area(t))

    def test_upper_constraints(self):
        targets = [12000, 1_000_000, 2_000_000]
        expected = [178, 1632, 2772]
        for t, e in zip(targets, expected):
            self.assertEqual(e, find_closest_containing_area(t))


if __name__ == '__main__':
    unittest.main()
