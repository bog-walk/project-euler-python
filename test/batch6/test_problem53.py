import unittest
from util.tests.reusable import compare_speed_seconds
from solution.batch6.problem53 import *


class CombinatoricSelections(unittest.TestCase):
    def test_def(self):
        n = 1
        expected = 1
        self.assertEqual(expected, n)


if __name__ == '__main__':
    unittest.main()
