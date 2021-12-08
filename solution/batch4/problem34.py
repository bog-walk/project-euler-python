""" Problem 34: Digit Factorials

https://projecteuler.net/problem=34

Goal: Find the sum of all numbers less than N that divide the sum of
the factorial of their digits (& therefore have minimum 2 digits).

Constraints: 10 <= N <= 1e5

e.g.: N = 20
      qualifying numbers = {19}
      as 1! + 9! = 362881, which % 19 = 0
      e.g. 18 does not work as 1! + 8! = 40321, which % 19 > 0
      sum = 19
"""
from math import factorial


# pre-calculation of all digits to increase performance
factorials = [factorial(x) for x in range(10)]


def sum_of_digit_factorials_HR(n):
    """
    Increase this solution's efficiency by creating an array of upper constraint
    size (plus 1) & looping once through all numbers then caching the result plus the
    previously calculated sum, if it matches the necessary requirements.
    """
    overall_total = 0
    for num in range(10, n):
        num_total = sum([factorials[int(ch)] for ch in str(num)])
        if num_total % num == 0:
            overall_total += num
    return overall_total


def sum_of_digit_factorials_PE():
    """
    Project Euler specific implementation that finds the sum of all numbers
    that are equal to the sum of the factorial of their digits.
    Search limit based on double-digit need and that a 7-digit number of only
    9! would sum to 2_540_160, so the 1st digit of the 7-digit number cannot
    be greater than 2. An 8-digit number is not possible as 8 * 9! still
    results in a 7-digit sum.
    The only 2 numbers are: 145 and 40585.
    """
    overall_total = 0
    for n in range(10, 2_000_000):
        digits = [int(ch) for ch in str(n)]
        n_total = 0
        for digit in digits:
            n_total += factorials[digit]
            # prevents further unnecessary calculation
            if n_total > n:
                break
        if n_total == n:
            overall_total += n_total
    return overall_total
