import unittest
from util.maths.reusable import prime_numbers_og
from util.tests.reusable import compare_speed_nano
from solution.batch1.problem10 import *


class SummationOfPrimes(unittest.TestCase):
    def test_quick_draw(self):
        nums = [2, 3, 5, 10, 100, 5000, 300_000, 1_000_000]
        expected = [2, 5, 10, 17, 1060, 1_548_136, 3_709_507_114, 37_550_402_023]
        sum_of_primes = sum_of_primes_quick_draw(1_000_000)
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], sum(prime_numbers_og(n)))
            self.assertEqual(expected[i], sum_of_primes[n])

    def test_speed(self):
        n = 1_000_000
        solutions = {
            "A": [sum_of_primes_quick_draw, n],
            "B": [sum_of_primes_quick_draw_2, n]
        }
        results = list(compare_speed_nano(solutions).values())
        self.assertListEqual(results[0], results[1])


if __name__ == '__main__':
    unittest.main()
