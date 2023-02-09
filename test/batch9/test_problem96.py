import unittest
from util.tests.reusable import get_test_resource
from solution.batch9.problem96 import solve_all_sudoku
from util.custom.sudoku_game import SudokuGame


class SuDoku(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.super_easy_puzzle = ["123456780", "456780123", "780123456",
                                 "234567801", "567801234", "801234567",
                                 "345678012", "678012345", "012345678"]
        cls.easy_puzzle = ["610000803", "047080500", "000900006", "000300014",
                           "324016058", "560498072", "036509000", "000067005",
                           "700000400"]
        cls.medium_puzzle = ["050000079", "003008100", "290064500", "506400013",
                             "020905607", "000003000", "000000340", "000009720",
                             "400200001"]
        cls.hard_puzzle = ["000000640", "540000807", "000080001", "900060070",
                           "063400105", "000078000", "004100000", "306005018",
                           "100002090"]
        resource: list[str] = get_test_resource("../resources/sudoku.txt")
        cls.all_puzzles = [SudokuGame(resource[i*10+1:i*10+10]) for i in range(50)]

    def test_01_setUp_handles_resources(self):
        self.assertEqual(50, len(self.all_puzzles))
        self.assertEqual("003020600", self.all_puzzles[0].get_grid()[0])
        self.assertEqual("300200000", self.all_puzzles[-1].get_grid()[0])

    def test_02_SuDoku_class_solves_individual_puzzles(self):
        puzzles = [self.super_easy_puzzle, self.easy_puzzle, self.medium_puzzle,
                   self.hard_puzzle]
        solutions = [
            ["123456789", "456789123", "789123456", "234567891", "567891234",
             "891234567", "345678912", "678912345", "912345678"],
            ["615274893", "947683521", "283951746", "879325614", "324716958",
                "561498372", "136549287", "492867135", "758132469"],
            ["658132479", "743598162", "291764538", "586427913", "324915687",
                "179683254", "962871345", "815349726", "437256891"],
            ["831257649", "549613827", "672984531", "928561374", "763429185",
                "415378962", "284196753", "396745218", "157832496"]
        ]
        for single, solution in zip(puzzles, solutions):
            puzzle = SudokuGame(single)
            puzzle.solve()
            self.assertListEqual(solution, puzzle.get_grid())

    def test_03_PE_solution_correct(self):
        self.assertEqual(24702, solve_all_sudoku(self.all_puzzles))


if __name__ == '__main__':
    unittest.main()
