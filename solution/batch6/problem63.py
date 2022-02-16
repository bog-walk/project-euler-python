""" Problem 63: Powerful Digit Counts

https://projecteuler.net/problem=63

Goal: Given N, find all N-digit positive integers that are also a Nth power.

Constraints: 1 <= N <= 19

e.g. the 5-digit number, 16807 = 7^5
     the 9-digit number, 134_217_728 = 8^9

e.g.: N = 2
      output = [16, 25, 36, 49, 64, 81]
"""
from math import log10


def n_digit_nth_powers(n: int) -> list[int]:
    """
    Solution optimised by searching backwards from 9^N, as 10^N produces a number
    with (N + 1) digits, and breaking the loop as soon as the power's digits drop
    below N.

    :returns: List of all N-digit integers that are a Nth power, in ascending order.
    """

    results = []
    for x in range(9, 0, -1):
        power = pow(x, n)
        digits = int(log10(power)) + 1
        if digits == n:
            results.append(int(power))
        else:
            break
    return results[::-1]


def all_n_digit_nth_powers_brute() -> int:
    """
    Project Euler specific implementation that requests a count of all N-digit
    positive integers that are also a Nth power.

    N.B. The last 9-digit number to also be a 9th power occurs at N = 21.

    SPEED (WORSE)
        5.5e4ns to count all valid numbers
    """

    total = 0
    n = 1
    while True:
        count = 0
        for x in range(9, 0, -1):
            power = pow(x, n)
            digits = int(log10(power)) + 1
            if digits == n:
                count += 1
            else:
                break
        if count == 0:  # if 9^N has less than N digits, no future integers exist
            break
        total += count
        n += 1
    return total


def all_n_digit_nth_powers_formula() -> int:
    """
    Project Euler specific implementation that requests a count of all N-digit
    positive integers that are also a Nth power.

    Solution is based on the following formula:

    10^(n-1) <= x^n < 10^n, so find where the lower bounds meets x^n

    10^(n-1) = x^n, using the quotient rule of exponentiation becomes

    10^n / 10^1 = x^n

    log(10)n / log(10) = log(x)n, using the quotient rule of logarithms becomes

    log(10)n - log(10) = log(x)n

    n = log(10) / (log(10) - log(x)) -> 1 / (1 - log(x))

    SPEED (BETTER)
        6900ns to count all valid numbers
    """

    return sum(int(1 / (1 - log10(n))) for n in range(1, 10))
