""" Problem 52: Permuted Multiples 

https://projecteuler.net/problem=52

Goal: Find all positive integers, x <= N, such that all requested multiples
(x, 2x, ..., Kx) are a permutation of x.

Constraints: 125_875 <= N <= 2e6, 2 <= K <= 6

e.g.: N = 125_875, K = 2
      output = [[125_874, 251_748]]
"""


def is_permutation(original: str, other: str) -> bool:
    return sorted(list(original)) == sorted(list(other))


def permuted_multiples(n: int, k: int) -> list[list[int]]:
    """
    Solution optimised by limiting loops to between 10^m and 10^(m+1) // K, where
    m is the amount of digits at the time, as any higher starting integer will
    gain more digits when multiplied & not be a permutation.
    """

    results = []
    start = 125_874
    digits = 6
    while start <= n:
        end = min(n + 1, pow(10, digits) // k)
        for x in range(start, end):
            x_str = str(x)
            perms = [x]
            for m in range(2, k + 1):
                multiple = x * m
                if is_permutation(x_str, str(multiple)):
                    perms.append(multiple)
                else:
                    break
            else:
                results.append(perms)
        digits += 1
        start = pow(10, digits - 1)
    return results


def smallest_permuted_multiple() -> int:
    """
    Project Euler specific implementation that finds the smallest positive integer,
    x, such that 2x, ..., 6x are all permutations of x.
    """

    x = 125_875
    perms = 1
    while perms != 6:
        x += 1
        x_str = str(x)
        for m in range(2, 7):
            multiple = x * m
            if is_permutation(x_str, str(multiple)):
                perms += 1
            else:
                perms = 1
                break
    return x
