""" Problem 13: Large Sum

https://projecteuler.net/problem=13

Goal: Find the first 10 digits of the sum of N 50-digit numbers.

Constraints: 1 <= N <= 1e3

e.g.: N.B. This is a scaled-down example (first 2 digits of N 5-digit numbers)
      N = 3
      34827, 93726, 90165
      sum = 218718
      1st 2 digits = 21
"""


def first_10_digits(string):
    return string[:10]


def add_in_reverse(n, digits):
    if n == 1:
        return digits[0]
    for i in range(len(digits[0]), -1, -1):
        pass