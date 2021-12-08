import unittest
from time import perf_counter
from solution.batch4.problem36 import sum_of_palindromes_brute, sum_of_palindromes


class DoubleBasePalindromes(unittest.TestCase):
    def test_sum_of_palindromes_low_N(self):
        n = 10
        expected = [25, 11, 22, 37]
        e = 0
        for k in range(2, 10, 2):
            self.assertEqual(expected[e], sum_of_palindromes_brute(n, k))
            self.assertEqual(expected[e], sum_of_palindromes(n, k))
            e += 1

    def test_sum_of_palindromes_mid_N(self):
        n = 1000
        expected = [2638, 1940, 855]
        e = 0
        for k in range(3, 9, 2):
            self.assertEqual(expected[e], sum_of_palindromes_brute(n, k))
            self.assertEqual(expected[e], sum_of_palindromes(n, k))
            e += 1

    def test_sum_of_palindromes_high_N(self):
        n = 1_000_000
        expected = [872187, 782868]
        e = 0
        for k in range(2, 10, 7):
            self.assertEqual(expected[e], sum_of_palindromes_brute(n, k))
            self.assertEqual(expected[e], sum_of_palindromes(n, k))
            e += 1

    def test_sum_of_palindromes_speed_comparison(self):
        n, k = 1_000_000_000, 2
        solutions = [sum_of_palindromes_brute, sum_of_palindromes]
        answers = []
        starts = []
        stops = []
        for solution in solutions:
            starts.append(perf_counter())
            answers.append(solution(n, k))
            stops.append(perf_counter())
        print(f"Brute solution took: {stops[0] - starts[0]:0.4f}s\n"
              f"Improved solution took: {stops[1] - starts[1]:0.4f}s\n")
        self.assertEqual(answers[0], answers[1])


if __name__ == '__main__':
    unittest.main()
