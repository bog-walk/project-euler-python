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
    SPEED (EQUAL): 0.01429s for N = 50 over 1000 iterations.
    """

    return prod(map(int, string))


def digits_product(num: int) -> int:
    """
    SPEED (EQUAL): 0.01716s for N = 50 over 1000 iterations.
    """

    product = 1
    while num > 0:
        product *= (num % 10)
        num //= 10
    return product


def largest_series_product_recursive(string: str, digits: int, k: int) -> int:
    """ Throws RecursionError for string lengths > 100 digits.

    SPEED (BETTER): 0.0007s for N = 100, K = 6.
    """

    if digits == 1:
        return int(string)
    elif k == 1:
        return max(int(char) for char in string)
    elif digits == k:
        return string_product(string)
    else:
        return max(
            largest_series_product_recursive(string[:k], k, k),
            largest_series_product_recursive(string[1:], digits - 1, k)
        )


def largest_series_product(string: str, digits: int, k: int) -> int:
    """
    SPEED (BETTER): 0.0004s for N = 100, K = 6.
    """

    largest = 0
    if digits == 1:
        largest = int(string)
    elif digits == k:
        largest = string_product(string)
    else:
        for i in range(digits - k + 1):
            product = string_product(string[i:i+k])
            largest = max(largest, product)
    return largest
