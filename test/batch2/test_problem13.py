import unittest
from util.tests.reusable import get_test_resource
from solution.batch2.problem13 import add_in_reverse


class LargeSum(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.three_digits = ["123", "456", "789", "812", "234"]
        cls.ten_digits = ["6041184107", "5351558590", "1833324270"]
        cls.five_N = get_test_resource("../resources/large_sum_5N")
        cls.hundred_N = get_test_resource("../resources/large_sum_100N")

    def test_setup(self):
        self.assertEqual(5, len(self.five_N))
        self.assertEqual(50, len(self.five_N[0]))
        self.assertEqual(100, len(self.hundred_N))

    def test_one_sum(self):
        digits = ["123456789123456789"]
        n = len(digits)
        expected = "1234567891"
        self.assertEqual(expected, add_in_reverse(n, digits))

    def test_small_sum(self):
        digits = self.three_digits
        n = len(digits)
        expected = str(sum(map(int, digits)))
        self.assertEqual(expected, add_in_reverse(n, digits))

    def test_mid_sum(self):
        digits = self.ten_digits
        n = len(digits)
        expected = str(sum(map(int, digits)))[:10]
        self.assertEqual(expected, add_in_reverse(n, digits))

    def test_large_sum(self):
        digits = self.five_N
        n = len(digits)
        expected = str(sum(map(int, digits)))[:10]
        self.assertEqual(expected, add_in_reverse(n, digits))

    def test_very_large_sum(self):
        digits = self.hundred_N
        n = len(digits)
        expected = str(sum(map(int, digits)))[:10]
        self.assertEqual(expected, add_in_reverse(n, digits))


if __name__ == '__main__':
    unittest.main()
