import unittest
from solution.batch0.problem1 import sum_of_multiples_brute, sum_of_multiples
from util.tests.reusable import compare_speed


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
        n, k_1, k_2 = pow(10, 9), 3, 5
        expected = 233_333_333_166_666_668
        self.assertEqual(expected, sum_of_multiples(n, k_1, k_2))

    def test_sum_of_multiples_speed(self):
        n, k_1, k_2 = pow(10, 7), 20, 32
        expected = 3_749_995_000_000
        solutions = {
            "Brute": [sum_of_multiples_brute, n, k_1, k_2],
            "Arithmetic": [sum_of_multiples, n, k_1, k_2]
        }
        results = compare_speed(solutions, repeat=10)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
