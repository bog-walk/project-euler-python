import unittest
from sudoku_game import SudokuGame


class SudokuGameTest(unittest.TestCase):
    # The order in which the various tests will be run is determined by sorting
    # the test method names with respect to the built-in ordering for strings.

    @classmethod
    def setUpClass(cls):
        cls.solution = ["247913568", "195687342", "863254197", "312479685",
                        "958162734", "674538219", "526891473", "439726851",
                        "781345926"]
        cls.puzzle = SudokuGame(["207013068", "000680340", "803050000",
                                 "310470085", "000162004", "600008209",
                                 "020091000", "439020800", "700300006"])

    def test_01_puzzle_setup(self):
        initial_state = self.puzzle.get_grid()
        self.assertEqual("207013068", initial_state[0])
        self.assertEqual("700300006", initial_state[-1])

    def test_02_incorrect_input_caught(self):
        self.assertRaises(ValueError, SudokuGame, "207013068")
        self.assertRaises(ValueError, SudokuGame, ["1234" for _ in range(9)])
        self.assertRaises(ValueError, SudokuGame, ["1234a6789" for _ in range(9)])

    def test_03_puzzle_solved_correctly(self):
        self.puzzle.solve()
        self.assertListEqual(self.solution, self.puzzle.get_grid())


if __name__ == '__main__':
    unittest.main()
