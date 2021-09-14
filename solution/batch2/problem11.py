""" Problem 11: Largest Product in a Grid

https://projecteuler.net/problem=11

Goal: Find the largest product of 4 adjacent integers in the
same direction (up, down, left, right, diagonal) in an NxN grid.

Constraints: 0 <= integer <= 100, 4 <= N <= 20

e.g.: 1 1 1 1
      1 1 2 1
      1 1 3 1
      1 1 1 1
      column {1,2,3,1} = 6
"""
from math import prod


def transpose_grid(grid):
    t_rows = len(grid[0])
    t_cols = len(grid)
    return [[grid[c][r] for c in range(t_cols)] for r in range(t_rows)]


def rotate_grid(grid):
    t_rows = len(grid[0])
    t_cols = len(grid)
    return [[grid[c][t_cols - r - 1] for c in range(t_cols)] for r in range(t_rows)]


def largest_row_product(grid):
    largest = 0
    for row in grid:
        for col in range(len(row) - 3):
            product = prod(row[col:col + 4])
            if product > largest:
                largest = product
    return largest


def largest_col_product(grid):
    t_grid = transpose_grid(grid)
    return largest_row_product(t_grid)


def largest_diagonal_product(grid):
    t_grid = transpose_grid(grid)
    return max(
        largest_leading_diag(grid),
        largest_leading_diag(t_grid),
        largest_counter_diag(grid),
        largest_counter_diag(t_grid)
    )


def largest_leading_diag(grid):
    largest = 0
    for row in range(len(grid) - 3):
        for col in range(len(grid) - 3 - row):
            diag = [grid[row][col], grid[row + 1][col + 1], grid[row + 2][col + 2], grid[row + 3][col + 3]]
            product = prod(diag)
            if product > largest:
                largest = product
    return largest


def largest_counter_diag(grid):
    r_grid = rotate_grid(grid)
    return largest_leading_diag(r_grid)


def largest_product_in_grid(grid):
    return max(
        largest_row_product(grid),
        largest_col_product(grid),
        largest_diagonal_product(grid)
    )
