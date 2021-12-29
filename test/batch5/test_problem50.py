import unittest
from solution.batch5.problem50 import consecutive_prime_sum


class ConsecutivePrimeSum(unittest.TestCase):
    def test_consecutive_prime_sum(self):
        nums = [
            2, 10, 50, 100, 1000, 10_000, 100_000, 1_000_000, 1_000_000_000_000
        ]
        expected = [
            (2, 1), (5, 2), (41, 6), (41, 6), (953, 21), (9521, 65),
            (92951, 183), (997651, 543), (37550402023, 78498)
        ]
        for i, n in enumerate(nums):
            self.assertTupleEqual(expected[i], consecutive_prime_sum(n))


if __name__ == '__main__':
    unittest.main()
