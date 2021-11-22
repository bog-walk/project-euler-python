import unittest
from solution.batch3.problem21 import sum_amicable_pairs


class AmicableNumbers(unittest.TestCase):
    def test_sum_amicable_pairs(self):
        """
        First amicable pair: 220, 284
        Second amicable pair: 1184, 1210
        Third amicable pair: 2620, 2924
        """
        nums = [1, 100, 300, 2000, 5000, 10000, 40000, 100000]
        expected = [0, 0, 504, 2898, 8442, 31626, 115818, 852810]
        for index, n in enumerate(nums):
            self.assertEqual(expected[index], sum_amicable_pairs(n))


if __name__ == '__main__':
    unittest.main()
