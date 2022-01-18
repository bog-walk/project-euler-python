""" Problem 11: Largest Product in a Grid

https://projecteuler.net/problem=11

Goal: Find the largest product of 4 adjacent integers in the same direction
(up, down, left, right, diagonal) in an NxN grid.

Constraints: 0 <= integer <= 100, 4 <= N <= 20

e.g.: 1 1 1 1
      1 1 2 1
      1 1 3 1
      1 1 1 1
      column {1,2,3,1} = 6
"""
from math import prod

size = 4


def transpose_grid(grid: list[list[int]]) -> list[list[int]]:
    t_rows = len(grid[0])
    t_cols = len(grid)
    return [[grid[c][r] for c in range(t_cols)] for r in range(t_rows)]


def rotate_grid(grid: list[list[int]]) -> list[list[int]]:
    r_rows = len(grid[0])
    r_cols = len(grid)
    return [[grid[c][r_cols - r - 1] for c in range(r_cols)] for r in range(r_rows)]


def largest_row_product(grid: list[list[int]]) -> int:
    largest = 0
    for row in grid:
        for col in range(len(row) - size + 1):
            product = prod(row[col:col + size])
            largest = max(largest, product)
    return largest


def largest_col_product(grid: list[list[int]]) -> int:
    t_grid = transpose_grid(grid)
    return largest_row_product(t_grid)


def largest_leading_diagonal(grid: list[list[int]]) -> int:
    largest = 0
    for row in range(len(grid) - size + 1):
        for col in range(len(grid) - size + 1 - row):
            diagonal = [grid[row+i][col+i] for i in range(size)]
            product = prod(diagonal)
            largest = max(largest, product)
    return largest


def largest_counter_diagonal(grid: list[list[int]]) -> int:
    r_grid = rotate_grid(grid)
    return largest_leading_diagonal(r_grid)


def largest_diagonal_product(grid: list[list[int]]) -> int:
    t_grid = transpose_grid(grid)
    return max(
        largest_leading_diagonal(grid), largest_leading_diagonal(t_grid),
        largest_counter_diagonal(grid), largest_counter_diagonal(t_grid)
    )


def largest_product_in_grid_functional(grid: list[list[int]]) -> int:
    """ Finds the largest product by calling helper functions.

    SPEED (EQUAL)
        3.95ms for N = 20
    """

    return max(
        largest_row_product(grid),
        largest_col_product(grid),
        largest_diagonal_product(grid)
    )


def largest_product_in_grid(grid: list[list[int]]) -> int:
    """ Finds the largest product by processing all options at once.

    SPEED (EQUAL)
        3.15ms for N = 20
    """

    largest = 0
    right, down, leading_diag, counter_diag = 0, 0, 0, 0
    for row in range(len(grid)):
        for col in range(len(grid[0]) - size + 1):
            right = prod(grid[row][col:col + size])
            down = prod([grid[col+i][row] for i in range(size)])
            if row <= len(grid) - size:
                leading_diag = prod([grid[row+i][col+i] for i in range(size)])
                counter_diag = prod([grid[row+i][col + size - 1 - i] for i in range(size)])
            largest = max(largest, right, down, leading_diag, counter_diag)
    return largest
