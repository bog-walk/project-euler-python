""" Problem 91: Right Triangles with Integer Coordinates

https://projecteuler.net/problem=91

Goal: Given that 0 <= x_1, y_1, x_2, y_2 <= N, count how many right triangles can
be formed that fulfill the requirements detailed below.

Constraints: 2 <= N <= 2500

A right-angled triangle is formed with a point at origin O (0,0), and 2 others:
P (x_1, y_1) and Q (x_2, y_2). Both points are plotted at integer coordinates.

e.g.: N = 2
      count = 14
      4 triangles with right angle at O
      4 triangles with right angle on x-axis
      4 triangles with right angle on y-axis
      2 triangles with right angle internal (along center bisecting line)
"""
from math import gcd


def count_right_triangles(n: int) -> int:
    """
    Accumulates count based on a pattern of 5 positions observed for the
    right-angles:
            - at origin (0,0)
            - on the x-axis
            - on the y-axis
            - mirrored on both sides of the line y=x that bisects the [n]x[n] grid
            along the centre
            - mirrored between line y=x and each axis (pattern not yet finalised)

    Note that the line y=x creates right-angled triangles with the following
    pyramidal sequence of counts:
            2 -> 1
            3 -> 1 1
            4 -> 1 2 1
            5 -> 1 2 2 1
            6 -> 1 2 3 2 1
            7 -> 1 2 3 3 2 1
            8 -> 1 2 3 4 3 2 1
    The equation used in the code below is Gauss's summation method
    (provided[n]/2) multiplied by 4 and then adjusted based on [n]'s parity to
    mimic this sequence.
    """

    # right angles at origin and on both axes
    count = (n * n) * 3
    # right angles along centre line y = x
    count += 2 * (n // 2) * (n // 2)
    if n % 2:
        count += 2 * (n // 2)

    # internal right angles between x-axis and centre line y = x
    for p_x in range(2, n + 1):
        for p_y in range(1, p_x):
            factor = gcd(p_x, p_y)
            delta_x, delta_y = p_x // factor, p_y // factor
            # most Q occur to the left of point P
            q_x = p_x - delta_y
            q_y = p_y + delta_x
            while q_x >= 0 and q_y <= n:
                count += 2
                q_x -= delta_y
                q_y += delta_x
            # Q occasionally occurs to the right of P
            q_x = p_x + delta_y
            q_y = p_y - delta_x
            while q_y >= 0 and q_x <= n:
                count += 2
                q_x += delta_y
                q_y -= delta_x

    return count
