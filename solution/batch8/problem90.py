""" Problem 90: Cube Digit Pairs

https://projecteuler.net/problem=90

Goal: Count the distinct arrangements of M cubes that allow for all square numbers
[1, N^2] to be displayed.

Constraints: 1 <= M <= 3, 1 <= N < 10^(M/2)

The 6 faces of each cube has a different digit [0, 9]] on it. Placing the cubes
side-by-side in any order creates a variety of M-digit square numbers <= N^2. For
example, when 2 cubes are used, the arrangement {0, 5, 6, 7, 8, 9} and {1, 2, 3,
4, 6, 7} allows all squares <= 81; Note that "09" is achievable because '6' can be
flipped to represent '9'.

Arrangements are considered distinct if the combined cubes have different numbers,
regardless of differing order. Note that cubes can share the same numbers as long
as they still are able to display all expected squares.

e.g.: M = 1, N = 3
      Cube must have {1, 4, 6} or {1, 4, 9} at minimum
      Of all possible digit combinations, 55 match this requirement
"""
from itertools import combinations


def get_squares(max_n: int, cubes: int) -> [str]:
    """
    Generates a list of square numbers with all '9' represented by '6' and
    appropriately padded with leading zeroes.

    Note that certain squares have been removed to avoid redundancy:
        8^2 = 64 = 46
        10^2 = 100 = 001
        14^2 = 196 = 31^2 = 961 = 166
        20^2 = 400 = 004
        21^2 = 441 = 144
        23^2 = 529 = 25^2 = 625 = 256
        30^2 = 900 = 006
    """

    squares = []

    for i in range(1, max_n + 1):
        if i in [8, 10, 14, 20, 21, 23, 25, 30, 31]:
            continue
        square = str(i * i).replace('9', '6').zfill(cubes)
        squares.append(square)

    return squares


def is_valid_triple(sq: str, cube_1: tuple, cube_2: tuple, cube_3: tuple) -> bool:
    return (sq[0] in cube_1 and sq[1] in cube_2 and sq[2] in cube_3 or
            sq[0] in cube_1 and sq[1] in cube_3 and sq[2] in cube_2 or
            sq[0] in cube_2 and sq[1] in cube_1 and sq[2] in cube_3 or
            sq[0] in cube_2 and sq[1] in cube_3 and sq[2] in cube_1 or
            sq[0] in cube_3 and sq[1] in cube_2 and sq[2] in cube_1 or
            sq[0] in cube_3 and sq[1] in cube_1 and sq[2] in cube_2)


def count_valid_cubes(max_square: int, cubes: int) -> int:
    squares = get_squares(max_square, cubes)
    count = 0

    # '9' is represented by '6' for ease of validity check within block
    all_cubes = list(combinations("0123456786", 6))
    size = len(all_cubes)
    # avoid duplicate arrangements by limiting iteration to only larger cubes
    for i, cube_1 in enumerate(all_cubes):
        if cubes > 1:
            # must include equivalent cubes for cases when N is lower
            for j in range(i, size):
                cube_2 = all_cubes[j]
                # at least 1 cube must have '0' by now, regardless of N value
                # any further combos will be larger and not include '0'
                if cube_1[0] != '0' and cube_2[0] != '0':
                    break
                if cubes > 2:
                    for k in range(j, size):
                        cube_3 = all_cubes[k]
                        # both smaller cubes must have '0' as cube_3 will be larger
                        if (cube_1[0] == '0') ^ (cube_2[0] == '0'):
                            break
                        if all(
                                is_valid_triple(sq, cube_1, cube_2, cube_3)
                                for sq in squares
                        ):
                            count += 1
                else:
                    # 2 cubes cannot be equivalent when expected to show
                    # squares >= 36 as amount of necessary digits will exceed 6
                    if max_square > 5 and cube_1 == cube_2:
                        continue
                    # 2 cubes cannot display > 9^2
                    if all(
                            sq[0] in cube_1 and sq[1] in cube_2 or
                            sq[0] in cube_2 and sq[1] in cube_1
                            for sq in squares
                    ):
                        count += 1
        else:
            # one cube cannot display > 3^2
            if all(sq[0] in cube_1 for sq in squares):
                count += 1

    return count
