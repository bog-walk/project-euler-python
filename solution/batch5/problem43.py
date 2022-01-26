""" Problem 43: Substring Divisibility

https://projecteuler.net/problem=43

Goal: Find the sum of all 0 to N pandigital numbers that have their 3-digit
substrings, starting from d_2, being divisible by sequential primes.

Constraints: 3 <= N <= 9

Substring Divisibility: The 0 to 9 pandigital, 1_406_357_289 ->
d_2 .. d_4 = 406 % 2 == 0
d_3 .. d_5 = 063 % 3 == 0
d_4 .. d_6 = 635 % 5 == 0
d_5 .. d_7 = 357 % 7 == 0
d_6 .. d_8 = 572 % 11 == 0
d_7 .. d_9 = 728 % 13 == 0
d_8 .. d_10 = 289 % 17 == 0

e.g.: N = 3
      sum = 22212
"""
from itertools import permutations

primes = [0, 2, 3, 5, 7, 11, 13, 17]


def sum_of_pandigital_substrings(n: int) -> int:
    """
    SPEED (WORSE)
        6.212s for N = 9
    """

    total = 0
    digits = "0123456789"[:n + 1]
    for tup in permutations(digits):
        perm = "".join(tup)
        for i in range(1, n - 1):
            sub = int(perm[i:i+3])
            if sub % primes[i] != 0:
                break
        else:
            total += int(perm)
    return total


def is_permutation_invalid(perm: (str, ...)) -> bool:
    """
    Filters pandigital permutations based on the following:

    -   [d_2, d_4] must be divisible by 2 so d_4 must be an even number.

    -   [d_4, d_6] must be divisible by 5 so d_6 must be '0' or '5', which is
        narrowed down to '5' as [d_6, d_8] must be divisible by 11 and '0' would not
        allow pandigital options.

    -   [d_3, d_5] must be divisible by 3, so sum([d_3, d_5]) must be also so.

    -   If eligible numbers are narrowed down manually, it is proven that d_1 and
        d_2 are either '1' or '4' and d_10 is either '7' or '9'.
    """

    return (
            perm[0] not in "14" or perm[-1] not in "79" or
            int(perm[3]) % 2 != 0 or perm[5] != "5" or
            sum([int(d) for d in perm[2:5]]) % 3 != 0
    )


def sum_of_9_pandigital_substrings() -> int:
    """
    Project Euler specific implementation that only requires the sum of all
    0 to 9 pandigital numbers that have substring divisibility.

    Filtering the generated permutations allowed the performance speed to be
    improved compared to the previous solution above.

    SPEED (BETTER)
        1.201s for N = 9
    """

    digits = "0123456789"
    total = 0
    for tup in permutations(digits):
        if is_permutation_invalid(tup):
            continue
        perm = "".join(tup)
        for i in range(1, 8):
            sub = int(perm[i:i+3])
            if sub % primes[i] != 0:
                break
        else:
            total += int(perm)
    return total
