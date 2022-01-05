""" Problem 45: Triangular, Pentagonal, & Hexagonal

https://projecteuler.net/problem=45

Goal: Given a & b, find all numbers below N that are
both types of numbers queried (as below).

Constraints: 2 <= N <= 2e14
             a < b
             a,b in {3, 5, 6} -> {triangle, pentagonal, hexagonal}

Triangle Number: T_n = n * (n + 1) / 2
Pentagonal Number: P_n = n * (3 * n - 1) / 2
Hexagonal Number: H_n = n * (2 * n - 1)
Some numbers can be all 3 type ->
e.g. T_1 = P_1 = H_1 = 1
     T_285 = P_165 = H_143 = 40755

e.g.: N = 10000, a = 3, b = 5
      result = {1, 210}
      N = 100000, a = 5, b = 6
      result = {1, 40755}
"""
from math import sqrt, floor
from util.maths.reusable import is_triangular_number, is_pentagonal_number


def is_hexagonal_number(h_n):
    """
    Derivation solution is based on the following:
    n * (2 * n - 1) = h_n ->
    inverse function, positive solution ->
    n = 0.25 * (sqrt((8 * h_n) + 1) + 1)

    :return: If hN is the nth hexagonal, or None if not hexagonal.
    """
    n = 0.25 * (sqrt(8 * h_n + 1) + 1)
    return n == floor(n)


def common_numbers(n, a, b):
    """
    HackerRank specific implementation will never request numbers
    that are both triangular and hexagonal. The solution is optimised
    by generating the fastest growing number type first (e.g. hexagonal
    numbers jump to the limit faster than the other 2) & checking if
    it matches the other requested type.
    """
    common = [1]
    if a == 3 and b == 5:
        i = 2
        while True:
            pentagonal = i * (3 * i - 1) // 2
            if pentagonal >= n:
                break
            if is_triangular_number(pentagonal):
                common.append(pentagonal)
            i += 1
    if a == 5 and b == 6:
        i = 2
        while True:
            hexagonal = i * (2 * i - 1)
            if hexagonal >= n:
                break
            if is_pentagonal_number(hexagonal):
                common.append(hexagonal)
            i += 1
    return common


def next_triple_type():
    """
    Project Euler specific implementation that finds the next number,
    after {1, 40755} that is triangular, pentagonal, and hexagonal.
    All hexagonal numbers are a subset of triangular numbers made from
    odd n, as T_(2n - 1) == H_n, based on completing the squares below:
    (n * (n + 1)) / 2 = m * (2 * m - 1) ->
    n^2 + n = 4 * m^2 - 2 * m ->
    (n + 0.5)^2 = 4 * (m - 0.25)^2 ->
    n = 2 * m - 1
    So this solution only needs to check for hexagonal numbers that are
    also pentagonal.
    """
    num = 40755
    while True:
        num += 1
        if is_hexagonal_number(num) and is_pentagonal_number(num) is not None:
            break
    return num
