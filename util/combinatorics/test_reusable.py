import unittest
from reusable import *


class CombinatoricsReusable(unittest.TestCase):
    def test_permutation_id_less_than_9_duplicates(self):
        nums = [1487, 2214, 999, 15, 148_748_178_147, 1_000_000_000]
        ids = [
            (0, 1, 0, 0, 1, 0, 0, 1, 1), (0, 1, 2, 0, 1),
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 3), (0, 1, 0, 0, 0, 1),
            (0, 3, 0, 0, 3, 0, 0, 3, 3), (9, 1)
        ]
        for i, n in enumerate(nums):
            self.assertEqual(ids[i], permutation_id(n))

    def test_permutation_id_more_than_9_duplicates(self):
        nums = [1_000_000_000_000, 31_111_111_111, 999_999_999_999]
        ids = [(12, 1), (0, 10, 0, 1), (0, 0, 0, 0, 0, 0, 0, 0, 0, 12)]
        for i, n in enumerate(nums):
            self.assertEqual(ids[i], permutation_id(n))

    def test_permutation_id_same_permutation(self):
        nums = [1487, 4871, 8714, 7814, 1748]
        expected = (0, 1, 0, 0, 1, 0, 0, 1, 1)
        for n in nums:
            self.assertEqual(expected, permutation_id(n))


if __name__ == '__main__':
    unittest.main()
