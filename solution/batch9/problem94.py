""" Problem 94: Almost Equilateral Triangles

https://projecteuler.net/problem=94

Goal: Find the sum of the perimeters of all almost equilateral triangles with
integral side lengths and integral areas and whose perimeters do not exceed N.

Constraints: 15 <= N <= 1e18

Almost Equilateral Triangle: A triangle that has 2 equal sides, with the third
unique side differing by no more than 1 unit.

e.g.: N = 16
      sum = 16 -> {(5, 5, 6)}
      N = 51
      sum = 66 -> {(5, 5, 6), (17, 17, 16)}
"""
from decimal import *
from math import modf


def perimeter_sum_of_almost_equilaterals(n: int) -> int:
    """
    Solution takes advantage of the observed pattern that all almost equilateral
    triangles alternate in having the unique side being 1 unit greater or less than
    the equal sides.

    Area of an almost equilateral triangles found using Heron's formula:

    sp = (a + b + c) / 2
    area = sqrt(sp * (sp - a) * (sp - b) * (sp - c))

    substitute a for all sides, e.g. if distinct side expected to be 1 unit greater:
    sp = (3a + 1) / 2
    area = sqrt(sp * (sp - a)^2 * (sp - a - 1))

    Note that Decimal is necessary to handle floating-point issues when N > 1e6.

    SPEED (WORSE)
            6.84s for N = 1e6
            52.74s for N = 1e7
    """

    total = 0
    side = 5  # smallest valid triangle (5, 5, 6)
    valid_perimeter = 16
    toggle = -1  # side 5 used +1
    getcontext().prec = 20
    getcontext().rounding = ROUND_HALF_UP

    while valid_perimeter <= n:
        total += valid_perimeter
        side += 1
        perimeter = 3 * side + toggle
        semi_p = Decimal(perimeter) / Decimal(2)
        inner = semi_p * (semi_p - side)**Decimal(2) * (semi_p - (side + toggle))
        area = inner.sqrt()
        if modf(area)[1] == area:
            valid_perimeter = perimeter
            toggle *= -1
        else:
            valid_perimeter = 0

    return total


def perimeter_sum_of_sequence(n: int) -> int:
    """
    Solution uses the observed pattern as above, as well as a sequential pattern
    that forms the next term based on the previous 2 valid triangle sides:

    {(5, +1), (17, -1), (65, +1), (241, -1), ...}
    when next unique side expected to be greater ->
    side_i = 4 * side_{i-1} - side_{i-2} + 2
    when next unique side expected to be smaller ->
    side_i = 4 * side_{i-1} - side_{i-2} - 2

    SPEED (BETTER)
            8500ns for N = 1e6
            1.2e+04ns for N = 1e7
    """

    total = 0
    side_a, side_b = 1, 5  # smallest almost equilateral triangle (5, 5, 6)
    valid_perimeter = 16
    toggle = -1  # first triangle was +1

    while valid_perimeter <= n:
        total += valid_perimeter
        next_valid = 4 * side_b - side_a + (toggle * 2)
        valid_perimeter = 3 * next_valid + toggle
        toggle *= -1
        side_a, side_b = side_b, next_valid

    return total
