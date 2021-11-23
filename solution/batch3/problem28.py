""" Problem 28: Number Spiral Diagonals

https://projecteuler.net/problem=28

Goal: Return the sum (mod 1e9 + 7) of the diagonal numbers
in a N x N grid that was generated using a spiral pattern.

Constraints: 1 <= N <= 1e18, with N always odd

Spiral Pattern: start with 1 & move to the right in a
clockwise direction, incrementing the numbers.

e.g.: N = 5
      grid = 21  22  23  24  25
             20  7   8   9   10
             19  6   1   2   11
             18  5   4   3   12
             17  16  15  14  13
      diagonals = {1,3,5,7,9,13,17,21,25}
      sum = 101
"""
from math import ceil


def spiral_diag_sum_brute(n):
    """
    SPEED: ~4.1e8ns at N = 1e6 + 1
    """
    total = 1
    num = 1
    for step in range(2, n, 2):
        for _ in range(4):
            num += step
            total += num
    return total % 1000000007


def spiral_diag_sum_formula_brute(num):
    """
    Based on the formula:
    f(n) = 4 * (2 * n + 1)^2 - 12 * n + f(n - 1)
    This assumes n is the ring number, with f(0) = 1 & f(1) = 25
    as the first ring creates a 3x3 grid. So the side of a ring is
    2N + 1 wide with the upper right corner being (2n + 1)^2 or the area.
    So provided n would need to be divided by 2.

    SPEED: ~3.7e8ns at N = 1e6 + 1
    """
    f_n = 1
    prev = f_n
    for n in range(1, int(ceil(num / 2))):
        f_n = 4 * pow(2 * n + 1, 2) - 12 * n + prev
        prev = f_n
    return f_n % 1000000007


def spiral_diag_sum_formula_derived(n):
    """
    Based on the formula:
    f(n) = 4 * (2 * n + 1)^2 - 12 * n + f(n - 1)
    Third order polynomial function required as the 3rd delta between consecutive
    f(n) gives a constant -> a*x^3 + b*x^2 + c*x + d.
    Solving for f(0) to f(3) derives the formula:
    f(n) = (16 * x^3 + 30 * x^2 + 26 * x + 3) // 3

    SPEED (BEST): 4800ns at N = 1e6 + 1
    """
    n = (n - 1) // 2
    f_n = (16 * pow(n, 3) + 30 * pow(n, 2) + 26 * n + 3) // 3
    return f_n % 1000000007
