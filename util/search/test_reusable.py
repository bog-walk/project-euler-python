import unittest
from util.tests.reusable import compare_speed_nano
from reusable import *


class SearchReusable(unittest.TestCase):
    def test_binary_search_empty(self):
        nums = []
        target = 1
        self.assertFalse(binary_search(target, nums))
        self.assertFalse(binary_search_recursive(target, nums, 0, len(nums) - 1))

    def test_binary_search_1_element(self):
        nums = [100]
        target = 100
        self.assertTrue(binary_search(target, nums))
        self.assertTrue(binary_search_recursive(target, nums, 0, len(nums) - 1))
        target = 1000
        self.assertFalse(binary_search(target, nums))
        self.assertFalse(binary_search_recursive(target, nums, 0, len(nums) - 1))

    def test_binary_search_all_true(self):
        nums = [n for n in range(1001)]
        targets = [0, 1000, 500, 43, 267, 681, 800]
        for target in targets:
            self.assertTrue(binary_search(target, nums))
            self.assertTrue(binary_search_recursive(target, nums, 0, len(nums) - 1))

    def test_binary_search_all_false(self):
        nums = [n for n in range(1000) if n % 2 == 0]
        targets = [-1, 1, 11, 33, 139, 431, 673, 805, 999, 2000]
        for target in targets:
            self.assertFalse(binary_search(target, nums))
            self.assertFalse(binary_search_recursive(target, nums, 0, len(nums) - 1))

    def test_binary_search_speed(self):
        nums = [n for n in range(1_000_000)]
        target = 1
        solutions = {
            binary_search: ["Iterative", target, nums],
            binary_search_recursive: ["Recursive", target, nums, 0, len(nums) - 1]
        }
        outputs = compare_speed_nano(solutions)
        for output in outputs.values():
            self.assertTrue(output)


if __name__ == '__main__':
    unittest.main()
