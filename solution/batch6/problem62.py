""" Problem 62: Cubic Permutations

https://projecteuler.net/problem=62

Goal: Given N, find the smallest cubes for which exactly K permutations of its
digits are the cube of some number < N.

Constraints: 1e3 <= N <= 1e6, 3 <= K <= 49

e.g.: N = 1000, K = 3
      smallest cube = 41_063_625 (345^3)
      permutations -> 56_623_104 (384^3), 66_430_125 (405^3)
"""


def cubic_permutations(n: int, k: int) -> list[list[int]]:
    """
    Solution stores all cubes in a dictionary with their permutation id as the key,
    thereby creating value lists of cubic permutations. The dictionary is then
    filtered for lists of K size.

    Original solution was adjusted in 3 locations to increase speed at upper
    constraints from 7.95s to 3.89s, as specified in the code.

    :returns: List of all K-sized lists of permutations that are cubes. These will
        already be sorted by the first (smallest) element of each list.
    """

    cube_perms: dict[str, list[int]] = {}
    for num in range(345, n):
        cube = num * num * num  # og: pow(n, 3)
        cube_id = "".join(sorted(str(cube)))  # og: permutation_id(cube)
        cube_perms[cube_id] = cube_perms.setdefault(cube_id, []) + [cube]
    # og: list(filter(lambda perms: len(perms) == k, cube_perms.values()))
    results = []
    for value in cube_perms.values():
        if len(value) == k:
            results.append(value)
    return results


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

    cube_perms: dict[str, list[int]] = {}
    longest_id = 0
    num = 345
    max_digits = 100
    current_digits = 0
    while current_digits <= max_digits:
        cube = pow(num, 3)
        cube_id = "".join(sorted(str(cube)))
        cube_perms[cube_id] = cube_perms.setdefault(cube_id, []) + [cube]
        if longest_id == 0 and len(cube_perms[cube_id]) == 5:
            longest_id = cube_id
            max_digits = len(cube_id)
        num += 1
        current_digits = len(cube_id)
    return cube_perms[longest_id]
