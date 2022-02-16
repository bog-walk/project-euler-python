""" Problem 62: Cubic Permutations

https://projecteuler.net/problem=62

Goal: Given N, find the smallest cubes for which exactly K permutations of its
digits are the cube of some number < N.

Constraints: 1e3 <= N <= 1e6, 3 <= K <= 49

e.g.: N = 1000, K = 3
      smallest cube = 41_063_625 (345^3)
      permutations -> 56_623_104 (384^3), 66_430_125 (405^3)
"""
from math import log10

from solution.batch4.problem49 import perm_id


def cubic_permutations(n: int, k: int) -> list[list[int]]:
    cube_perms: dict[int, list[int]] = {}
    for num in range(345, n):
        cube = pow(num, 3)
        cube_id = perm_id(cube)
        cube_perms[cube_id] = cube_perms.setdefault(cube_id, []) + [cube]
    return list(filter(lambda perms: len(perms) == k, cube_perms.values()))


def smallest_5_cube_perm() -> list[int]:
    """
    Project Euler specific implementation that requests the smallest cube for
    which exactly 5 permutations of its digits are cube.

    Since exactly 5 permutations are required, without setting a limit, once the
    first permutations are found, the loop has to continue until the generated
    cubes no longer have the same amount of digits as the smallest cube in the
    permutation list. This ensures the list is not caught early.

    N.B. The permutations occur between 5027^3 and 8384^3.
    """

    cube_perms: dict[int, list[int]] = {}
    longest_id = 0
    num = 345
    max_digits = 100
    current_digits = 0
    while current_digits <= max_digits:
        cube = pow(num, 3)
        cube_id = perm_id(cube)
        cube_perms[cube_id] = cube_perms.setdefault(cube_id, []) + [cube]
        if longest_id == 0 and len(cube_perms[cube_id]) == 5:
            longest_id = cube_id
            max_digits = int(log10(cube)) + 1
        num += 1
        current_digits = int(log10(cube)) + 1
    return cube_perms[longest_id]


if __name__ == '__main__':
    print(cubic_permutations(1_000_000, 49))
