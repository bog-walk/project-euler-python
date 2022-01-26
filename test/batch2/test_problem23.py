import unittest
from solution.batch2.problem23 import *


class NonAbundantSums(unittest.TestCase):
    def test_is_abundant_all_true(self):
        nums = [12, 18, 20, 24, 70, 104, 120, 945]
        for n in nums:
            self.assertTrue(is_abundant(n))

    def test_is_abundant_all_false(self):
        nums = [6, 9, 21, 43, 86, 115]
        for n in nums:
            self.assertFalse(is_abundant(n))

    def test_is_sum_of_abundants_all_true(self):
        nums = [24, 110, 158, 234, 957, 20162, 28122, 28123, 28124, 100_000]
        for n in nums:
            self.assertTrue(is_sum_of_abundants(n))

    def test_is_sum_of_abundants_all_false(self):
        nums = [0, 10, 12, 13, 27, 49, 121, 20161]
        for n in nums:
            self.assertFalse(is_sum_of_abundants(n))

    def test_sum_of_all_non_abundants(self):
        expected = 4_179_871
        self.assertEqual(expected, sum_of_all_non_abundants())

    def test_all_integers_expressed(self):
        cannot_be_expressed = []
        for n in range(20162, 28124):
            if not is_sum_of_abundants(n):
                cannot_be_expressed.append(n)
        # in Python, 0 is False, so this checks that list is empty
        self.assertFalse(len(cannot_be_expressed))


if __name__ == '__main__':
    unittest.main()
