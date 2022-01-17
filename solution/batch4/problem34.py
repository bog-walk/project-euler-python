""" Problem 34: Digit Factorials

https://projecteuler.net/problem=34

Goal: Find the sum of all numbers less than N that divide the sum of the factorial
of their digits (& therefore have minimum 2 digits).

Constraints: 10 <= N <= 1e5

Factorion: A natural number that equals the sum of the factorials of its digits.
The only non-single-digit factorions are: 145 and 40585.

e.g.: N = 20
      qualifying numbers = {19}
      as 1! + 9! = 362_881, which % 19 = 0
      e.g. 18 does not work as 1! + 8! = 40321, which % 19 > 0
      sum = 19
"""
from math import factorial

# pre-calculation of all digit factorials to increase performance
factorials = [factorial(x) for x in range(10)]


def sum_of_digit_factorials_HR(n: int) -> int:
    """
    HackerRank specific implementation that finds the sum of all numbers < n that
    are divisors of the sum of the factorials of their digits.
    """

    overall_total = 0
    for num in range(10, n):
        num_total = sum([factorials[int(ch)] for ch in str(num)])
        if num_total % num == 0:
            overall_total += num
    return overall_total


def sum_of_digit_factorials_PE() -> int:
    """
    Project Euler specific implementation that finds the sum of all numbers that
    are factorions.

    The numbers cannot have more than 7 digits, as 9! * 8 returns only a 7-digit
    number. 9! * 7 return 2_540_160, so the 1st digit of the 7-digit number cannot
    be greater than 2.
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
