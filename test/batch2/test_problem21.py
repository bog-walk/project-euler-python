import unittest
from solution.batch2.problem21 import sum_amicable_pairs


class AmicableNumbers(unittest.TestCase):
    def test_sum_amicable_pairs(self):
        nums = [1, 100, 300, 2000, 5000, 10000, 40000, 100_000]
        expected = [0, 0, 504, 2898, 8442, 31626, 115_818, 852_810]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], sum_amicable_pairs(n))


if __name__ == '__main__':
    unittest.main()
