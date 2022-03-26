""" Problem 81: Path Sum 2 Ways

https://projecteuler.net/problem=81

Goal: Find the minimum path sum for an NxN grid, starting at (0,0) and ending at
(n,n), while only being able to move to the right or down with each step.

Constraints: 1 <= N <= 1000, numbers in [1, 1e9]

e.g.: N = 3
      grid = 1 0 5
             1 0 0
             1 1 1
      minimum = 2: {1 -> R -> D -> R -> D -> 1}
"""
from heapq import heappop, heappush


def min_path_sum(rows: int, grid: list[list[int]]) -> int:
    """
    Solution starts at top-left corner & works downwards replacing each grid
    value with the smallest cumulative sum so far.

    The first row is treated specially in that sums can only be achieved by adding
    the value from the previous column. The first column is also special in that
    sums can only be achieved by adding the value from the previous row.

    N.B. The nested lists have to be copied, otherwise they will reference and
    alter the original list, causing errors when testing a single grid with
    multiple solutions.

    SPEED (BETTER)
        6.51ms for N = 80
    """

    elements = [row.copy() for row in grid]
    for row in range(rows):
        for col in range(rows):
            if row == 0:
                if col == 0:  # no need to alter starter
                    continue
                elements[0][col] += elements[0][col-1]
            else:
                elements[row][col] += elements[row-1][0] if col == 0 else min(
                    elements[row-1][col], elements[row][col-1]
                )
    return elements[-1][-1]


def min_path_sum_dijkstra(rows: int, grid: list[list[int]]) -> int:
    """
    Solution uses Dijkstra's algorithm for finding the shortest paths between
    nodes in a graph, via the priority queue implementation from the heapq
    module, that intrinsically stores the smallest weighted grid element
    encountered at its head. A step is taken to the right and down, if either are
    possible, on each smallest polled element until the bottom-right corner is found.

    This heap queue stores its elements as a tuple with the grid element's
    weight placed first in the tuple so that it will be used to sort elements. This
    means that equivalent grid elements will then be sorted naturally by their
    rows & column values, which will not cause errors in the end, but may cause
    unnecessary processing.

    e.g. When using the 3X3 grid in the test suite, after grid[1][2] is
    encountered & grid[2][2] is added to the queue, the next smallest & valid
    element should be grid[2][2], but its value is identical with the sum at
    grid[1][0], which is prioritised as being lesser because it's row value
    is smaller. This could be avoided by storing the heap elements with their row
    & column values negated (& therefore multiplied by -1 once popped),
    which would cause equivalently weighted ties to be broken by the element with
    the (originally) larger row/column values. Implementing this actually
    increased the execution time from 13.73ms to 18.70ms.

    SPEED (WORSE)
        13.73ms for N = 80
    """

    visited = [[False]*rows for _ in range(rows)]
    sums = []
    heappush(sums, (grid[0][0], 0, 0))
    while len(sums):
        weight, row, col = heappop(sums)
        if visited[row][col]:
            continue
        if row == rows - 1 and col == rows - 1:
            return weight
        visited[row][col] = True
        if col + 1 < rows:
            heappush(sums, (weight + grid[row][col+1], row, (col + 1)))
        if row + 1 < rows:
            heappush(sums, (weight + grid[row+1][col], (row + 1), col))
