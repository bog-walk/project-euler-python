""" Problem 8: Largest Product in a Series

https://projecteuler.net/problem=8

Goal: Find the largest product of K adjacent digits in
an N-digit number.

Constraints: 1 <= K <= 13, K <= N <= 1000

e.g.: input = 3675356291; N = 10
      K = 5
      products LTR = {1890,3150,3150,900,1620,540}
      largest = 3150 -> {6*7*5*3*5} or {7*5*3*5*6}
"""
from math import prod


def string_product(string):
    digits = [int(char) for char in string]
    return prod(digits)


def digits_product(num):
    product = 1
    while num > 0:
        product *= (num % 10)
        num //= 10
    return product


def largest_series_product_recursive(string: str, digits: int, series_size: int) -> int:
    """
    RecursionError: max recursion depth exceeded for string lengths > 100.
    """
    if digits == 1:
        return int(string)
    elif series_size == 1:
        return max(int(char) for char in string)
    elif digits == series_size:
        return string_product(string)
    else:
        return max(
            largest_series_product_recursive(string[:series_size], series_size, series_size),
            largest_series_product_recursive(string[1:], digits - 1, series_size)
        )


def largest_series_product(string, digits, series_size):
    largest = 0
    if digits == 1:
        largest = int(string)
    elif digits == series_size:
        largest = string_product(string)
    else:
        for i in range(digits - series_size + 1):
            product = string_product(string[i:i+series_size])
            largest = max(largest, product)
    return largest
