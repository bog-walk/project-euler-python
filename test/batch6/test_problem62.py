import unittest
from solution.batch6.problem62 import *


class CubicPermutations(unittest.TestCase):
    def test_cubic_perms_lower_constraints(self):
        n, k = 1000, 3
        expected = [[41_063_625, 56_623_104, 66_430_125]]
        self.assertListEqual(expected, cubic_permutations(n, k))

    def test_cubic_perms_mid_constraints(self):
        n, k = 100_000, 10
        expected_size = 3
        expected_smallests = [
            109_867_826_442_375, 150_178_532_496_264, 238_604_875_149_824
        ]
        actual = cubic_permutations(n, k)
        self.assertEqual(expected_size, len(actual))
        self.assertListEqual(expected_smallests, [a[0] for a in actual])

    def test_cubic_perms_upper_constraints(self):
        n, k = 1_000_000, 49
        expected_size = 1
        expected_smallest = 101_740_954_697_838_253
        actual = cubic_permutations(n, k)
        self.assertEqual(expected_size, len(actual))
        self.assertEqual(expected_smallest, actual[0][0])

    def test_PE_problem(self):
        expected = [
            127_035_954_683, 352_045_367_981, 373_559_126_408,
            569_310_543_872, 589_323_567_104
        ]
        self.assertListEqual(expected, smallest_5_cube_perm())


if __name__ == '__main__':
    unittest.main()
