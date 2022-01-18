""" Problem 45: Triangular, Pentagonal, & Hexagonal

https://projecteuler.net/problem=45

Goal: Given a & b, find all numbers below N that are both types of numbers
queried (as below).

Constraints: 2 <= N <= 2e14
             a < b
             a,b in {3, 5, 6} -> {triangle, pentagonal, hexagonal}

Triangular Number: T_n = n * (n + 1) / 2
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


def is_hexagonal_number(h_n: int) -> int | None:
    """
    Derivation solution is based on the formula:
    n * (2 * n - 1) = h_n, in quadratic form becomes:
    0 = 2 * n^2 - n - h_n, with a, b, c = 2, -1, -h_n
    putting these values in the quadratic formula becomes:
    n = 1 +/- sqrt(1 + 8 * h_n) / 4
    so the inverse function, positive solution becomes:
    n = 0.25 * (1 + sqrt(1 + (8 * h_n)))

    :returns: h_n's corresponding term if hexagonal, or None.
    """

    n = 0.25 * (1 + sqrt(1 + 8 * h_n))
    return int(n) if n == floor(n) else None


def common_numbers(n: int, a: int, b: int) -> list[int]:
    """
    HackerRank specific implementation will never request numbers that are both
    triangular and hexagonal.

    Solution is optimised by generating the fastest growing number type first.
    Hexagonal numbers jump to the limit faster than the other 2, and the pentagonal
    number sequence grows faster than triangular numbers.

    SPEED (WORSE): 8.5s for N = 2e14, pentagonal-hexagonal combo.
    """

    common = [1]
    i = 2
    if a == 3 and b == 5:
        while True:
            pentagonal = i * (3 * i - 1) // 2
            if pentagonal >= n:
                break
            if is_triangular_number(pentagonal):
                common.append(pentagonal)
            i += 1
    else:  # a == 5 and b == 6
        while True:
            hexagonal = i * (2 * i - 1)
            if hexagonal >= n:
                break
            if is_pentagonal_number(hexagonal):
                common.append(hexagonal)
            i += 1
    return common


def common_numbers_formula(n: int, a: int, b: int) -> list[int]:
    """
    For triangular-pentagonal combos, where T_x = P_y:

    x * (x + 1) / 2 = y * (3 * y - 1) / 2, after completing the square becomes:
    (6 * x - 1)^2 - 3 * (2 * y + 1)^2 = -2, a diophantine:
    36 * x^2 - 12 * x - 12 * y^2 - 12 * y, solved for 2 integer variables:
    T_x+1 = -2 * T_x - P_y and
    P_y+1 = -3 * T_x - 2 * P_y - 1

    For pentagonal-hexagonal combos, where P_x = H_y:

    x * (3 * x - 1) / 2 = y * (2 * y - 1), after completing the square becomes:
    (6 * x - 1)^2 - 3 * (4 * y - 1)^2 = -2, a diophantine:
    36 * x^2 - 12 * x - 48 * y^2 + 24 * y, solved for 2 integer variables:
    P_x+1 = 97 * P_x + 112 * H_y - 44 and
    H_y+1 = 84 * P_x + 97 * H_y - 38


    SPEED (BETTER): 14400ns for N = 2e14, pentagonal-hexagonal combo.
    """

    x, y, num = 1, 1, 1  # P_1 = H_1 = 1
    common = []
    if a == 3 and b == 5:
        while num < n:
            # negative terms signify non-integer solutions of the diophantine
            if x > 0 and y > 0:
                common.append(num)
            next_x = -2 * x - y
            next_y = -3 * x - 2 * y - 1
            x, y = next_x, next_y
            # could insert term into either triangular or pentagonal formula
            num = y * (y + 1) // 2
    else:  # a == 5 and b == 6
        while num < n:
            if x > 0 and y > 0:
                common.append(num)
            next_x = 97 * x + 112 * y - 44
            next_y = 84 * x + 97 * y - 38
            x, y = next_x, next_y
            num = y * (2 * y - 1)
    return common


def next_triple_type() -> int:
    """
    Project Euler specific implementation that finds the next number, after
    {1, 40755} that is triangular, pentagonal, and hexagonal.

    All hexagonal numbers are a subset of triangular numbers made from an odd n,
    as T_(2n - 1) == H_n, based on completing the squares below:
    (n * (n + 1)) / 2 = m * (2 * m - 1)
    n^2 + n = 4 * m^2 - 2 * m
    (n + 0.5)^2 = 4 * (m - 0.25)^2
    n = 2 * m - 1

    So, this solution only needs to check for hexagonal numbers that are
    also pentagonal.
    """

    num = 40755
    while True:
        num += 1
        if is_hexagonal_number(num) is not None and \
                is_pentagonal_number(num) is not None:
            break
    return num
