""" Problem 20: Factorial Digit Sum

https://projecteuler.net/problem=20

Goal: Find the sum of the digits of N!

Constraints: 0 <= N <= 1000

e.g.: N = 10
      10! = 10 * 9 * ... * 2 * 1 = 3_628_800
      sum  = 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
"""
from math import factorial


def factorial_digit_sum_iterative(n: int) -> int:
    """
    SPEED (WORSE)
        93.12ms for N = 1000 over 100 iterations
    """

    return sum(int(digit) for digit in str(factorial(n)))


def factorial_digit_sum_builtin(n: int) -> int:
    """
    SPEED (BETTER)
        60.50ms for N = 1000 over 100 iterations
    """

    return sum(map(int, str(factorial(n))))
