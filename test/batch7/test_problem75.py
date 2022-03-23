import unittest
from solution.batch7.problem75 import singularTriplets


class SingularIntegerRightTriangles(unittest.TestCase):
    def test_lower_constraints(self):
        limits = [12, 13, 15, 30, 41, 50, 99]
        expected = [1, 1, 1, 3, 5, 6, 11]
        for n, e in zip(limits, expected):
            self.assertEqual(e, singularTriplets(n))

    def test_mid_constraints(self):
        limits = [800, 9999, 60_000, 1_500_000]
        expected = [87, 1119, 6619, 161667]
        for n, e in zip(limits, expected):
            self.assertEqual(e, singularTriplets(n))

    def test_upper_constraints(self):
        limits = [3_146_789, 5_000_000]
        expected = [336_929, 534_136]
        for n, e in zip(limits, expected):
            self.assertEqual(e, singularTriplets(n))


if __name__ == '__main__':
    unittest.main()
