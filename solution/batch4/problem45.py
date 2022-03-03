""" Problem 45: Triangular, Pentagonal, & Hexagonal

https://projecteuler.net/problem=45

Goal: Given a & b, find all numbers below N that are both types of numbers
queried (as below).

Constraints: 2 <= N <= 2e14
             a < b
             a,b in {3, 5, 6} -> {triangle, pentagonal, hexagonal}

Triangle Number: T_n = n (n + 1) / 2

Pentagonal Number: P_n = n(3n - 1) / 2

Hexagonal Number: H_n = n(2n - 1)

Some numbers can be all 3 types ->
e.g. T_1 = P_1 = H_1 = 1
     T_285 = P_165 = H_143 = 40755

e.g.: N = 10_000, a = 3, b = 5
      result = {1, 210}
      N = 100_000, a = 5, b = 6
      result = {1, 40755}
"""
from util.maths.reusable import is_hexagonal_number, is_triangular_number, \
    is_pentagonal_number


def common_numbers(n: int, a: int, b: int) -> list[int]:
    """
    HackerRank specific implementation will never request numbers that are both
    triangular and hexagonal.

    Solution is optimised by generating the fastest growing number type first.
    Hexagonal numbers jump to the limit faster than the other 2, and the pentagonal
    number sequence grows faster than triangular numbers.

    SPEED (WORSE)
        9.19s for N = 2e14, pentagonal-hexagonal combo
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

    x(x + 1) / 2 = y(3y - 1) / 2, after completing the square becomes:

    (6x - 1)^2 - 3(2y + 1)^2 = -2, a diophantine:

    36x^2 - 12x - 12y^2 - 12y, solved for 2 integer variables:

    T_(x+1) = -2T_x - P_y and

    P_(y+1) = -3T_x - 2P_y - 1

    For pentagonal-hexagonal combos, where P_x = H_y:

    x(3x - 1) / 2 = y(2y - 1), after completing the square becomes:

    (6x - 1)^2 - 3(4y - 1)^2 = -2, a diophantine:

    36x^2 - 12x - 48y^2 + 24y, solved for 2 integer variables:

    P_(x+1) = 97P_x + 112H_y - 44 and

    H_(y+1) = 84P_x + 97H_y - 38


    SPEED (BETTER)
        1.4e4ns for N = 2e14, pentagonal-hexagonal combo
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
    as T_(2n - 1) = H_n, based on completing the squares below:

    n(n + 1) / 2 = m(2m - 1)

    n^2 + n = 4m^2 - 2m

    (n + 0.5)^2 = 4(m - 0.25)^2

    n = 2m - 1

    So, this solution only needs to check for hexagonal numbers that are
    also pentagonal.
    """

    num = 40755
    while True:
        num += 1
        if (is_hexagonal_number(num) is not None
                and is_pentagonal_number(num) is not None):
            break
    return num
