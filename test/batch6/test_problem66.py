import unittest
from solution.batch6.problem66 import largest_diophantine_x


class DiophantineEquation(unittest.TestCase):
    def test_lower_constraints(self):
        nums = [7, 13, 15, 23, 50]
        expected = [5, 13, 13, 13, 46]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], largest_diophantine_x(n))

    def test_mid_constraints(self):
        nums = [100, 128]
        expected = [61, 109]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], largest_diophantine_x(n))

    def test_upper_constraints(self):
        nums = [1000, 3000, 10_000]
        expected = [661, 2389, 9949]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], largest_diophantine_x(n))


if __name__ == '__main__':
    unittest.main()
