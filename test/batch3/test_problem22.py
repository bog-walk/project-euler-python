import unittest
from solution.batch3.problem22 import *


def get_long_list(filename):
    with open(filename) as listFile:
        # Could use readlines() but extra whitespace would affect output
        long_list = [row.strip() for row in listFile]
    return long_list


class NamesScores(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.small_list = ["ALEX", "LUIS", "JAMES", "BRIAN", "PAMELA"]
        cls.medium_list = [
            "OLIVIA", "ALEX", "MIA", "LUIS", "LEO", "JAMES", "BRIAN", "NOAH", "PAMELA",
            "AIDEN", "BENJAMIN", "HARPER", "MUHAMMAD", "PENELOPE", "RILEY", "JACOB",
            "SEBASTIAN", "LILY", "ELI", "IVY", "STELLA", "HANNAH", "VIOLET"
        ]
        cls.long_list_location = "../resources/names_scores"

    def test_name_score(self):
        names = [(4, "PAMELA"), (937, "COLIN"), (0, "A"), (5199, "ZZZZZZZZZZ")]
        expected = [240, 49714, 1, 1352000]
        for index, name in enumerate(names):
            self.assertEqual(expected[index], name_score(name[0], name[1]))

    def test_name_score_small_list(self):
        sorted_list = sorted(self.small_list)
        expected = [42, 244, 144, 88, 240]
        for index, name in enumerate(self.small_list):
            position = sorted_list.index(name)
            self.assertEqual(expected[index], name_score(position, name))

    def test_name_score_medium_list(self):
        sorted_list = sorted(self.medium_list)
        self.assertEqual(130, name_score(sorted_list.index("ELI"), "ELI"))
        self.assertEqual(608, name_score(sorted_list.index("NOAH"), "NOAH"))

    def test_sum_of_name_scores_small_list(self):
        self.assertEqual(758, sum_of_name_scores(self.small_list))

    def test_sum_of_name_scores_large_list(self):
        long_list = get_long_list(self.long_list_location)
        self.assertEqual(871198282, sum_of_name_scores(long_list))


if __name__ == '__main__':
    unittest.main()
