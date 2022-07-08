""" Problem 6: Sum Square Difference

https://projecteuler.net/problem=6

Goal: Find the absolute difference between the sum of the squares & the square
of the sum of the first N natural numbers.

Constraints: 1 <= N <= 1e4

e.g.: N = 3 -> [1,2,3]
      sum of squares = [1,4,9] = 14
      square of sum = 6^2 = 36
      diff = |14 - 36| = 22
"""
from functools import reduce
from util.maths.reusable import gauss_sum


def sum_square_diff_brute(n: int) -> int:
    """
    SPEED (WORSE)
        5.02ms for N = 1e4
    """

    sum_of_range, sum_of_squares = reduce(
        lambda acc, num: (acc[0] + num, acc[1] + num * num),
        range(2, n+1),
        (1, 1)
    )
    return sum_of_range ** 2 - sum_of_squares


def sum_square_diff(n: int) -> int:
    """
    The sum of the 1st N natural numbers (triangular numbers) is found using
    the gauss summation method.

    The sum of the sequence's squares is based on the assumption that:

    f(n) = an^3 + bn^2 + cn + d, with

    f(0) = 0, f(1) = 1, f(2) = 5, f(3) = 14

    The formula (square pyramidal numbers) can then be solved as:

    f(n) = (2n^3 + 3n^2 + n) / 6

    f(n) = (n(2n + 1)(n + 1)) / 6

    SPEED (BETTER)
        6900ns for N = 1e4
    """

    sum_of_squares = n * (2 * n + 1) * (n + 1) // 6
    square_of_sum = gauss_sum(n) ** 2
    return square_of_sum - sum_of_squares
