""" Problem 83: Path Sum 4 Ways

https://projecteuler.net/problem=83

Goal: Find the minimum path sum for an NxN grid, starting at (0,0) and ending
at (n,n), by moving left, right, up, or down with each step.

Constraints: 1 <= N <= 1000, numbers in [1, 1e9]

e.g.: N = 3
      grid = 2 0 3 5
             8 0 9 9
             0 3 9 9
             0 1 1 1
      minimum = 8: {2 -> R -> D -> D -> L -> D -> R -> R -> 1}
"""
from heapq import heappop, heappush


def min_path_sum_dijkstra(rows: int, grid: list[list[int]]) -> int:
    """
    Solution is identical to the Dijkstra solution used in Problem 81,
    except extra steps (left & up) are added to the heap queue, instead of using
    an adjacency matrix.

    SPEED (WORSE)
        101.13ms for N = 80
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
        if col - 1 >= 0:
            heappush(sums, (weight + grid[row][col-1], row, col - 1))
        if row - 1 >= 0:
            heappush(sums, (weight + grid[row-1][col], row - 1, col))
        if col + 1 < rows:
            heappush(sums, (weight + grid[row][col+1], row, col + 1))
        if row + 1 < rows:
            heappush(sums, (weight + grid[row+1][col], row + 1, col))


def make_adjacency_matrix(
        rows: int,
        grid: list[list[int]]
) -> list[list[list[tuple[int, int, int]]]]:
    # step up, left, down, right
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    matrix = []
    for row in range(rows):
        row_adj = []
        for col in range(rows):
            adjacents = []
            for x, y in directions:
                adj_r, adj_c = row + x, col + y
                if 0 <= adj_r < rows and 0 <= adj_c < rows:
                    adjacents.append((grid[adj_r][adj_c], adj_r, adj_c))
            row_adj.append(adjacents)
        matrix.append(row_adj)
    return matrix


def min_path_sum_dijkstra_improved(rows: int, grid: list[list[int]]) -> int:
    """
    Dijkstra's algorithm for finding the shortest paths between nodes in a graph
    involves using 2 lists to store the distance from the source (sum in this case)
    for each vertex & whether each vertex has been processed. Using a heap queue
    (priority queue implementation module) is faster than storing the sums &
    writing a function that finds the matrix element with the smallest sum so far.

    Since only the smallest sum path between the source and the target is
    required, regardless of the length of the path (how many steps it takes),
    the loop can be broken once the target element is reached.

    An adjacency matrix is initially created to link all neighbour vertices,
    instead of relying on conditional branches to generate the heap queue.

    SPEED (BETTER)
        74.14ms for N = 80
    """

    adjacents = make_adjacency_matrix(rows, grid)
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
        for adj_w, adj_r, adj_c in adjacents[row][col]:
            if not visited[adj_r][adj_c]:
                heappush(sums, (weight + adj_w, adj_r, adj_c))
