""" Problem 6: Sum Square Difference

https://projecteuler.net/problem=6

Goal: Find the absolute difference between the sum of the squares of &
the square of the sum of the first N natural numbers.

Constraints: 1 <= N <= 1e4

e.g.: N = 3 -> {1,2,3}
      sum of squares = {1,4,9} = 14
      square of sum = 6^2 = 36
      diff = |14 - 36| = 22
"""
from util.reusable import gaussian_sum


def sum_square_diff(n):
    """
    Sum of squares is based on the assumption that:
    f(n) = an^3 + bn^2 + cn + d, with
    f(0) = 0, f(1) = 1, f(2) = 5, f(3) = 14; then
    f(n) = 1/6(2n^3 + 3n^2 + n),
    f(n) = n/6(2n + 1)(n + 1)
    """
    sum_of_squares = n * (2 * n + 1) * (n + 1) // 6
    square_of_sum = gaussian_sum(n) ** 2
    return square_of_sum - sum_of_squares
