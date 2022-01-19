""" Problem 15: Lattice Paths

https://projecteuler.net/problem=15

Goal: Find the number of routes through an NxM grid, starting at (0, 0) & ending
at (n, m), while only being able to move right or down.

Constraints: 1 <= N <= 500, 1 <= M <= 500

e.g.: N = 2, M = 2
      routes = 6 -> {RRDD, RDRD, RDDR, DRRD, DRDR, DDRR}
"""
from math import factorial


def lattice_path_routes(n: int, m: int) -> int:
    """ Calculates distinct permutations with identical items.

    Solution is based on the formula:

    :math:`x! / \\prod i!`

    where x is the number of items to be combined & i represents the groups of
    indistinguishable items to undergo product notation.

    Note that, if the lattice was assured to be square, the number of routes would
    be equal to the central binomial coefficient C(2*n, n) found as the midline
    number in the (2*n)th row of Pascal's triangle.

    The formula for a rectangular grid with C(n+m, n) becomes:

    :math:`(n + m)! / n!m!`

    since grid dimensions determine the number of steps
    taken & there is a deterministic proportion of R vs D steps.

    :returns: Number of valid routes scaled down to modulo (1e9 + 7).
    """

    routes = factorial(n + m) // (factorial(n) * factorial(m))
    return routes % 1_000_000_007
