""" Problem 82: Path Sum 3 Ways

https://projecteuler.net/problem=82

Goal: Find the minimum path sum for an NxN grid, by starting at any cell in the
leftmost column and ending at any cell in the rightmost column, while only being
able to move up, down or right with each step.

Constraints: 1 <= N <= 1000, numbers in [1, 1e9]

e.g.: N = 3
      grid = 1 0 5
             1 0 0
             1 1 1
      minimum = 1: {1 -> R -> D -> R -> 1 || 1 -> R -> R -> 1}
"""
from heapq import heapify, heappop, heappush


def min_path_sum(rows: int, grid: list[list[int]]) -> int:
    """
    Solution isolates the final column of the grid & each of this list's elements
    iteratively becomes the sum bubbled up by the minimal path encountered moving
    backwards through the columns.

    N.B. The nested lists have to be copied, otherwise they will reference and
    alter the original list, causing errors when testing a single grid with
    multiple solutions.

    SPEED (BETTER)
        4.88ms for N = 80
    """

    sums = [row.copy()[-1] for row in grid]
    for i in range(rows - 2, -1, -1):
        sums[0] += grid[0][i]
        for j in range(1, rows):
            # i.e. between the right or down
            sums[j] = min(sums[j], sums[j-1]) + grid[j][i]
        for j in range(rows - 2, -1, -1):
            # bubble up the minimal last sums with the rightmost element
            sums[j] = min(sums[j], sums[j+1] + grid[j][i])
    return min(sums)


def min_path_sum_dijkstra(rows: int, grid: list[list[int]]) -> int:
    """
    Solution is identical to the Dijkstra solution used in Problem 81, except for
    the following changes:

    - All leftmost column elements are added to the heap queue as starters.

    - The loop is broken when any cell in the rightmost column is reached.

    - An extra upwards step is added to the queue, if possible.

    SPEED (WORSE)
        23.03ms for N = 80
    """

    visited = [[False]*rows for _ in range(rows)]
    sums = [(grid[i][0], i, 0) for i in range(rows)]
    heapify(sums)
    while len(sums):
        weight, row, col = heappop(sums)
        if visited[row][col]:
            continue
        if col == rows - 1:
            return weight
        visited[row][col] = True
        if row - 1 >= 0:
            heappush(sums, (weight + grid[row-1][col], row - 1, col))
        if col + 1 < rows:
            heappush(sums, (weight + grid[row][col+1], row, col + 1))
        if row + 1 < rows:
            heappush(sums, (weight + grid[row+1][col], row + 1, col))
