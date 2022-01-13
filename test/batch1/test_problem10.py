import unittest
from util.maths.reusable import prime_numbers_og
from solution.batch1.problem10 import sum_of_primes_quick_draw


class SummationOfPrimes(unittest.TestCase):
    def test_sum_of_primes(self):
        nums = [2, 3, 5, 10, 100, 5000, 300_000, 1_000_000]
        expected = [2, 5, 10, 17, 1060, 1_548_136, 3_709_507_114, 37_550_402_023]
        sum_of_primes = sum_of_primes_quick_draw(1_000_000)
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], sum(prime_numbers_og(n)))
            self.assertEqual(expected[i], sum_of_primes[n])


if __name__ == '__main__':
    unittest.main()
