""" Problem 15: Lattice Paths

https://projecteuler.net/problem=15

Goal: Find the number of routes through a N x M grid, starting at (0,0)
& ending at (n,m), while only being able to move right or down.

Constraints: 1 <= N <= 500, 1 <= M <= 500

e.g.: N = 2, M = 2
      routes = 6 -> {RRDD, RDRD, RDDR, DRRD, DRDR, DDRR}
"""
from math import factorial


def lattice_path_routes(n, m):
    """
    Calculates permutations with identical items, based on the formula:
    x! / Pi(i!); where x is the number of items to be combined & i represents
    the groups of indistinguishable items to undergo product notation.
    The new formula becomes:
    (n + m)! / n! * m!; since grid dimensions determine the number of steps
    taken & a deterministic proportion of R vs D steps.

    :return number of routes scaled down to modulo (1e9 + 7)
    """
    routes = factorial(n + m) // (factorial(n) * factorial(m))
    return routes % 1_000_000_007
