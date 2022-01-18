""" Problem 28: Number Spiral Diagonals

https://projecteuler.net/problem=28

Goal: Return the sum (mod 1e9 + 7) of the diagonal numbers in a NxN grid that is
generated using a spiral pattern.

Constraints: 1 <= N <= 1e18, with N always odd

Spiral Pattern: start with 1 & move to the right in a clockwise direction,
incrementing the numbers.

e.g.: N = 5
      grid = 21  22  23  24  25
             20  7   8   9   10
             19  6   1   2   11
             18  5   4   3   12
             17  16  15  14  13
      diagonals = {1, 3, 5, 7, 9, 13, 17, 21, 25}
      sum = 101
"""
from math import ceil

modulus = 1_000_000_007


def spiral_diag_sum_brute(n: int) -> int:
    """
    SPEED (WORST)
        555.78ms at N = 1e6 + 1
    """

    total = 1
    num = 1
    for step in range(2, n, 2):
        for _ in range(4):
            num += step
            total += num
    return total % modulus


def spiral_diag_sum_formula_brute(num: int) -> int:
    """
    Solution based on the formula:

    f(n) = 4 * (2 * n + 1)^2 - 12 * n + f(n - 1),

    with n as the centre ring number, and

    f(0) = 1, as it is the only element, and

    f(1) = 25, as the first ring creates a 3x3 grid.

    So the side of a ring is odd at 2 * N + 1 wide with the upper right corner
    being (2n + 1)^2 or the area. So provided n would need to be divided by 2.

    SPEED (BETTER)
        460.31ms at N = 1e6 + 1
    """

    f_n = 1
    for n in range(1, int(ceil(num / 2))):
        f_n += 4 * pow(2 * n + 1, 2) - 12 * n
    return f_n % modulus


def spiral_diag_sum_formula_derived(n: int) -> int:
    """
    Solution optimised based on the same formula as above, but reduced to:

    f(n) = 16 * n^2 + 4 * n + 4 + f(n - 1)

    Third order polynomial function required as the 3rd delta between consecutive
    f(n) gives a constant, such that ->

    a*x^3 + b*x^2 + c*x + d

    Solving for f(0) to f(3) derives the closed-form formula:

    f(n) = (16 * n^3 + 30 * n^2 + 26 * n + 3) // 3

    SPEED (BEST)
        9300ns at N = 1e6 + 1
    """

    n = (n - 1) // 2
    f_n = (16 * pow(n, 3) + 30 * pow(n, 2) + 26 * n + 3) // 3
    return f_n % modulus
