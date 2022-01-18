import unittest
from solution.batch5.problem44 import *


class PentagonNumbers(unittest.TestCase):
    def test_HR_problem_lower_constraints(self):
        n = 10
        k_s = [1, 2, 3]
        expected = [{92}, {70}, {70}]
        for i, k in enumerate(k_s):
            self.assertSetEqual(expected[i], pentagon_numbers_HR(n, k))

    def test_HR_problem_normal_values(self):
        n = 1000
        k_s = [10, 20]
        expected = [
            {715, 1247, 1926, 7957, 8855, 69230, 92877, 173_230,
             199_655, 336_777, 1_078_232},
            {6305, 73151, 82720, 270_725, 373_252, 747_301}
        ]
        for i, k in enumerate(k_s):
            self.assertSetEqual(expected[i], pentagon_numbers_HR(n, k))

    def test_HR_problem_upper_constraints(self):
        n = 100_000
        k_s = [1000, 5000]
        expected = [
            {16_832_075, 34_485_640, 78_253_982, 215_310_551, 472_957_695,
             661_804_535, 937_412_502, 3_345_135_652, 5_174_142_370,
             7_562_742_551, 10_836_947_507},
            {323_114_155, 891_564_410, 1_141_136_295, 3_802_809_626}
        ]
        for i, k in enumerate(k_s):
            self.assertSetEqual(expected[i], pentagon_numbers_HR(n, k))

    def test_PE_problem(self):
        expected = 5_482_660
        self.assertEqual(expected, pentagon_numbers_PE())


if __name__ == '__main__':
    unittest.main()
