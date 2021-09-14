import unittest


def get_test_digits(filename):
    with open(filename) as digitsFile:
        digits = [line.strip() for line in digitsFile]
    return digits


class LargeSum(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.three_digits = ["123", "456", "789", "812", "234"]
        cls.ten_digits = ["6041184107", "5351558590", "1833324270"]
        cls.five_N = get_test_digits("../resources/large_sum_5N")
        cls.hundred_N = get_test_digits("../resources/large_sum_100N")

    def test_digits_setup(self):
        self.assertEqual(5, len(self.five_N))
        self.assertEqual(50, len(self.five_N[0]))
        self.assertEqual(100, len(self.hundred_N))


if __name__ == '__main__':
    unittest.main()
