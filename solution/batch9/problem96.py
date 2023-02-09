""" Problem 96: Su Doku

https://projecteuler.net/problem=96

Goal: Given an unsolved representation of a Su Doku puzzle that has a unique
solution, output the solved puzzle with all empty spaces ('0') replaced with the
correct digit.

Constraints: Standard Su Doku 9x9 grid, split into 9 3x3 boxes, with each row,
column, and 3x3 box expected to contain the set of digits [1, 9].
"""
from util.custom.sudoku_game import SudokuGame


def solve_all_sudoku(puzzles: list[SudokuGame]) -> int:
    total = 0

    for i, puzzle in enumerate(puzzles):
        if puzzle.solve():
            solution = puzzle.get_grid()
            if any('0' in sol for sol in solution):
                print(f"Puzzle {i + 1} has empty cell in it")
            if any(len(set(sol)) != 9 for sol in solution):
                print(f"Puzzle {i + 1} has invalid repeats")
            total += int(solution[0][:3])
        else:
            print(f"Puzzle {i + 1} failed")

    return total
