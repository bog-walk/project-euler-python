import unittest
from util.maths.reusable import prime_numbers_og
from util.tests.reusable import compare_speed
from solution.batch0.problem10 import *


class SummationOfPrimes(unittest.TestCase):
    def test_quick_draw(self):
        nums = [2, 3, 5, 10, 100, 5000, 300_000, 1_000_000]
        expected = [2, 5, 10, 17, 1060, 1_548_136, 3_709_507_114, 37_550_402_023]
        sum_of_primes = sum_of_primes_quick_draw(1_000_000)
        sum_of_primes_opt = sum_of_primes_quick_draw_optimised(1_000_000)
        for n, e in zip(nums, expected):
            self.assertEqual(e, sum(prime_numbers_og(n)))
            self.assertEqual(e, sum_of_primes[n])
            self.assertEqual(e, sum_of_primes_opt[n])

    def test_speed(self):
        n = 1_000_000
        solutions = {
            "Original": [sum_of_primes_quick_draw, n],
            "Optimised": [sum_of_primes_quick_draw_optimised, n]
        }
        results = list(compare_speed(solutions).values())
        self.assertListEqual(results[0], results[1])


if __name__ == '__main__':
    unittest.main()
