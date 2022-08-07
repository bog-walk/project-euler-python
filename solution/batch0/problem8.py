""" Problem 8: Largest Product in a Series

https://projecteuler.net/problem=8

Goal: Find the largest product of K adjacent digits in an N-digit number.

Constraints: 1 <= K <= 13, K <= N <= 1000

e.g.: N = 10 with input = "367535629", K = 5
      products LTR = {1890, 3150, 3150, 900, 1620, 540}
      largest = 3150 -> (6*7*5*3*5) or (7*5*3*5*6)
"""
from math import prod


def string_product(string: str) -> int:
    """
    SPEED (BETTER)
        9619ns for N = 50
    """

    return prod(map(int, string))


def string_product_alt(string: str) -> int:
    """
    SPEED (WORSE)
        1.1e+04ns for N = 50
    """

    product = 1
    for ch in string:
        product *= int(ch)
        if not product:
            break
    return product


def largest_series_product_recursive(string: str, digits: int, k: int) -> int:
    """
    SPEED (WORSE)
        2.4e5ns for N = 100, K = 6

    :raises RecursionError: For string lengths > 100 digits.
    """

    if digits == 1:
        return int(string)
    elif k == 1:
        return max(int(char) for char in string)
    elif digits == k:
        return string_product(string)
    else:
        return max(
            string_product(string[:k]),
            largest_series_product_recursive(string[1:], digits - 1, k)
        )


def largest_series_product(string: str, digits: int, k: int) -> int:
    """
    SPEED (BETTER)
        1.6e5ns for N = 100, K = 6
    """

    largest = 0
    if digits == 1:
        largest = int(string)
    elif k == 1:
        largest = max(int(char) for char in string)
    elif digits == k:
        largest = string_product(string)
    else:
        for i in range(digits - k + 1):
            largest = max(largest, string_product(string[i:i+k]))
    return largest
