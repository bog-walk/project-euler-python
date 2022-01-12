import unittest
from solution.batch1.problem1 import sum_of_multiples_brute, sum_of_multiples


class MultiplesOf3Or5(unittest.TestCase):
    def test_lower_constraints(self):
        n, k_1, k_2 = 1, 1, 1
        for expected in range(2):
            self.assertEqual(expected, sum_of_multiples_brute(n, k_1, k_2))
            self.assertEqual(expected, sum_of_multiples(n, k_1, k_2))
            n += 1
            k_2 += 1

    def test_same_factors(self):
        n, k_1, k_2 = 10, 3, 3
        expected = 18
        self.assertEqual(expected, sum_of_multiples_brute(n, k_1, k_2))
        self.assertEqual(expected, sum_of_multiples(n, k_1, k_2))

    def test_different_factors_1(self):
        n, k_1, k_2 = 10, 3, 5
        expected = [23, 233_168]
        for e in expected:
            self.assertEqual(e, sum_of_multiples_brute(n, k_1, k_2))
            self.assertEqual(e, sum_of_multiples(n, k_1, k_2))
            n = 1000

    def test_different_factors_2(self):
        n, k_1, k_2 = 23000, 8, 21
        expected = 44_087_172
        self.assertEqual(expected, sum_of_multiples_brute(n, k_1, k_2))
        self.assertEqual(expected, sum_of_multiples(n, k_1, k_2))

    def test_upper_constraints(self):
        n = [pow(10, 7), pow(10, 9)]
        k_1 = [20, 3]
        k_2 = [32, 5]
        expected = [3_749_995_000_000, 233_333_333_166_666_668]
        for i, e in enumerate(expected):
            if i == 0:
                self.assertEqual(e, sum_of_multiples_brute(n[i], k_1[i], k_2[i]))
                self.assertEqual(e, sum_of_multiples(n[i], k_1[i], k_2[i]))
            else:
                self.assertEqual(e, sum_of_multiples(n[i], k_1[i], k_2[i]))


if __name__ == '__main__':
    unittest.main()
