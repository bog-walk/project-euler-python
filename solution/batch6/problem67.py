""" Problem 67: Maximum Path Sum 2

https://projecteuler.net/problem=67

Goal: Find the maximum sum from tree root to leaf node of an N-rowed tree, which
contains i integers on each ith row, by moving to an adjacent number on the row
below. This goal is identical to Problem 18, but the constraints have been
increased from N = 15 to N = 100.

Constraints: 1<= N <= 100, numbers in [0,100]

e.g.: N = 4
         3
        7 4
       2 4 6
      8 5 9 3
      max path -> 3 + 7 + 4 + 9
      output = 23
"""
from util.custom.pyramid_tree import PyramidTree


def max_path_sum(rows: int, elements: list[int]) -> int:
    """
    Generates a graph using custom PyramidTree class & finds the largest valued
    route using post-order traversal.

    While acceptable for Problem 18, this solution is impossible for pyramids
    with more than 25 rows, as shown by the 24x longer speed taken to find the
    solution when only 5 more rows were added to the same pyramid. A 100 row
    pyramid would have 2^99 possible routes and even if 1e12 routes could be
    assessed every second, it would take ~> 20e9 years to iterate through them all.

    SPEED (WORSE)
        782.00ms for N = 20
        18.57s for N = 25
    """

    pyramid = PyramidTree(rows, elements)
    return pyramid.max_sum_post_order_traversal(pyramid.root)


def max_path_sum_dynamic(rows: int, elements: list[list[int]]) -> int:
    """
    This solution is identical to the Problem 18 solution.

    Rather than create a custom tree, this solution starts from the bottom of the
    tree (last nested list), repeatedly finding the maximum of adjacent values and
    adding it to the parent value 1 row above, until the tree root is reached. This
    new root value is returned as the maximum path value.

    SPEED (BETTER)
        1.0e5ns for N = 20
        1.5e5ns for N = 25
        3.90ms for N = 100
    """

    for row in range(rows - 1, 0, -1):
        for col in range(row):
            elements[row-1][col] += max(elements[row][col], elements[row][col+1])
    return elements[0][0]
