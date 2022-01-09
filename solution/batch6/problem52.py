""" Problem 52: Permuted Multiples 

https://projecteuler.net/problem=52

Goal: Find all positive integers, x <= N, such that
all requested multiples (x, 2x, ..., Kx) are a permutation
of x.

Constraints: 125875 <= N <= 2e6, 2 <= K <= 6

e.g.: N = 125875, K = 2
      output = [[125874, 251748]]
"""


def is_permutation(original: str, other: str):
    return sorted(list(original)) == sorted(list(other))


def permuted_multiples(n, k):
    """
    Solution optimised by limiting loops to between 10^m and
    10^(m+1) // K, as any higher starting integer will gain more
    digits when multiplied & not be a permutation.
    """
    results = []
    start = 125874
    digits = 6
    while start <= n:
        end = min(n + 1, pow(10, digits) // k)
        for x in range(start, end):
            x_str = str(x)
            perms = [x]
            valid = True
            for m in range(2, k + 1):
                multiple = x * m
                if is_permutation(x_str, str(multiple)):
                    perms.append(multiple)
                else:
                    valid = False
                    break
            if valid:
                results.append(perms)
        digits += 1
        start = pow(10, digits - 1)
    return results


def smallest_permuted_multiple():
    """
    Project Euler specific implementation that finds the smallest positive
    integer, x, such that 2x, ..., 6x are all permutations of x.
    """
    x = 125875
    perms = 1
    multiples = []
    while perms != 6:
        x += 1
        x_str = str(x)
        for m in range(2, 7):
            multiple = x * m
            if is_permutation(x_str, str(multiple)):
                perms += 1
                multiples.append(multiple)
            else:
                perms = 1
                multiples = []
                break
    print(multiples)
    return x
