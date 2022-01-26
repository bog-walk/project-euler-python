import unittest
from util.tests.reusable import get_test_resource
from solution.batch2.problem22 import *


class NamesScores(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.small_list = ["ALEX", "LUIS", "JAMES", "BRIAN", "PAMELA"]
        cls.medium_list = [
            "OLIVIA", "ALEX", "MIA", "LUIS", "LEO", "JAMES", "BRIAN", "NOAH",
            "PAMELA", "AIDEN", "BENJAMIN", "HARPER", "MUHAMMAD", "PENELOPE",
            "RILEY", "JACOB","SEBASTIAN", "LILY", "ELI", "IVY", "STELLA", "HANNAH",
            "VIOLET"
        ]
        cls.long_list_location = "../resources/names_scores"

    def test_name_score(self):
        names = [(4, "PAMELA"), (937, "COLIN"), (0, "A"), (5199, "ZZZZZZZZZZ")]
        expected = [240, 49714, 1, 1_352_000]
        for i, name in enumerate(names):
            self.assertEqual(expected[i], name_score(name[0], name[1]))

    def test_name_score_small_list(self):
        sorted_list = sorted(self.small_list)
        expected = [42, 244, 144, 88, 240]
        for i, name in enumerate(self.small_list):
            position = sorted_list.index(name)
            self.assertEqual(expected[i], name_score(position, name))

    def test_name_score_medium_list(self):
        sorted_list = sorted(self.medium_list)
        names = ["ELI", "NOAH"]
        expected = [130, 608]
        for i, name in enumerate(names):
            self.assertEqual(expected[i], name_score(sorted_list.index(name), name))

    def test_sum_of_name_scores_small_list(self):
        expected = 758
        self.assertEqual(expected, sum_of_name_scores(self.small_list))

    def test_sum_of_name_scores_large_list(self):
        expected = 871_198_282
        long_list = get_test_resource(self.long_list_location)
        self.assertEqual(expected, sum_of_name_scores(long_list))


if __name__ == '__main__':
    unittest.main()
