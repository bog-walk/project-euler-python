import unittest
from solution.batch5.problem44 import pentagon_numbers_HR, pentagon_numbers_PE


class PentagonNumbers(unittest.TestCase):
    def test_pentagon_numbers_HR_low(self):
        n = 10
        k_s = [1, 2, 3]
        expected = [{92}, {70}, {70}]
        for i, k in enumerate(k_s):
            self.assertSetEqual(expected[i], pentagon_numbers_HR(n, k))

    def test_pentagon_numbers_HR_mid(self):
        n = 1000
        k_s = [10, 20]
        expected = [
            {715, 1247, 1926, 7957, 8855, 69230, 92877, 173230,
             199655, 336777, 1078232},
            {6305, 73151, 82720, 270725, 373252, 747301}
        ]
        for i, k in enumerate(k_s):
            self.assertSetEqual(expected[i], pentagon_numbers_HR(n, k))

    def test_pentagon_numbers_HR_high(self):
        n = 100000
        k_s = [1000, 5000]
        expected = [
            {16832075, 34485640, 78253982, 215310551, 472957695, 661804535,
             937412502, 3345135652, 5174142370, 7562742551, 10836947507},
            {323114155, 891564410, 1141136295, 3802809626}
        ]
        for i, k in enumerate(k_s):
            self.assertSetEqual(expected[i], pentagon_numbers_HR(n, k))

    def test_pentagon_numbers_PE(self):
        expected = 5482660
        self.assertEqual(expected, pentagon_numbers_PE())


if __name__ == '__main__':
    unittest.main()
