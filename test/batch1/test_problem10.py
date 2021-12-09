import unittest
from util.reusable import prime_numbers_og
from solution.batch1.problem10 import sum_of_primes_quick_draw


class SummationOfPrimes(unittest.TestCase):
    def test_sum_of_primes(self):
        nums = [2, 3, 5, 10, 100, 5000, 300000, 1000000]
        expected = [2, 5, 10, 17, 1060, 1548136, 3709507114, 37550402023]
        all_primes = sum_of_primes_quick_draw(1000000)
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], sum(prime_numbers_og(n)))
            self.assertEqual(expected[index], all_primes[n])


if __name__ == '__main__':
    unittest.main()
