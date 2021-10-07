import unittest
from time import perf_counter
from solution.batch3.problem26 import *


class ReciprocalCycles(unittest.TestCase):
    def test_longest_repetend_denominator(self):
        nums = [5, 10, 14, 19, 25, 46, 50, 70, 1000, 10000]
        expected = [3, 7, 7, 17, 23, 29, 47, 61, 983, 9967]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], longest_repetend_denominator_primes(n))
            self.assertEqual(expected[index], longest_repetend_denominator(n))

    def test_speed_comparison(self):
        n = 10000
        prime_sol_start = perf_counter()
        prime_ans = longest_repetend_denominator_primes(n)
        prime_sol_end = perf_counter()
        division_sol_start = perf_counter()
        division_ans = longest_repetend_denominator(n)
        division_sol_end = perf_counter()
        print(f"Prime solution took: {prime_sol_end - prime_sol_start:0.4f}s\n" +
              f"Alt solution took: {division_sol_end - division_sol_start:0.4f}s")
        self.assertEqual(prime_ans, division_ans)


if __name__ == '__main__':
    unittest.main()
