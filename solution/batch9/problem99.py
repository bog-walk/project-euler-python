""" Problem 99: Largest Exponential

https://projecteuler.net/problem=99

Goal: Compare 2 base (B) /exponent (E) pairs whose numbers contain a very large
amount of digits, then use this comparison to either find the Kth smallest
exponential or the greatest value exponential from a list of N pairs.

Constraints: 1 <= N <= 1e5, 1 <= K <= N, 1 <= B <= 1e9, 1 <= E <= 1e9

e.g.: N = 3, K = 2, list -> [4 7, 3 7, 2 11]
      sorted -> [2 11, 3 7, 4 7]
      output = 3 7
"""
from functools import cmp_to_key
from math import log10


def compare_exponentials(a: [int, int, int], b: [int, int, int]) -> int:
    """
    Solution avoids using large numbers for comparison by reducing both values
    using the root of the object with the smaller exponent, based on the following:

            (a^x)^(1/x) == x_root(a^x) == a
            then the object with the larger exponent becomes:
            (b^y)^(1/x) == b^(y/x)

    Based on the large values of the exponents, this provides a more manageable
    comparison.

    N.B. An alternative calculates the gcd of the exponents and depends on the
    following:

            a^(x * y) == (a^x)^y

    e.g. 2^350 and 5^150 == (2^7)^50 and (5^3)^50; 2^7 (128) > 5^3 (125), so 2^350
    has the greater value. This only works if the gcd is assured to be greater
    than 1.
    """

    smaller_exp = min(a[1], b[1])
    if a[1] == smaller_exp:
        reduced_a = float(a[0])
        reduced_exp = b[1] / smaller_exp
        reduced_b = pow(b[0], reduced_exp)
    else:
        reduced_b = float(b[0])
        reduced_exp = a[1] / smaller_exp
        reduced_a = pow(a[0], reduced_exp)

    return 1 if reduced_a > reduced_b else -1


def largest_exponential(inputs: list[str]) -> [int, int, int]:
    """
    Project Euler specific implementation that requires the line number of the
    base/exponent pair that has the greatest numerical value, from a 1000-line
    test file.
    """

    largest = ()

    for i, input_val in enumerate(inputs):
        base, exponent = map(int, input_val.split(","))
        exponential = (base, exponent, i + 1)
        if not len(largest) or compare_exponentials(largest, exponential) == -1:
            largest = exponential

    return largest


def k_smallest_exponential(inputs: list[str], k: int) -> tuple[int, int]:
    """
    HackerRank specific implementation that requires the kth smallest
    exponential from a list of base/exponent pairs.

    compare_exponentials() is used to sort the input values (plugged in using
    functools.cmp_to_key(func) to allow a more readable comparator), then the
    (k-1)th value is accessed.

    SPEED (WORSE/WORST/BETTER/BEST)
            #s for PE test list.
    """

    exponentials: list[tuple[int, int, int]] = []
    for i, input_val in enumerate(inputs):
        base, exponent = map(int, input_val.split(" "))
        exponentials.append((base, exponent, i + 1))

    k_smallest = sorted(exponentials, key=cmp_to_key(compare_exponentials))[k - 1]

    return k_smallest[:2]


def k_smallest_exponential_alt(inputs: list[str], k: int) -> tuple[int, int]:
    """
    Solution optimised by not relying on a tuple comparator and instead sorting
    base/exponent pairs solely based on their logarithm calculation, based on the
    following:

            a^x > b^y -> log_10(a^x) > log_10(b^y) -> x * log_10(a) > y * log_10(b)

    SPEED (WORSE/WORST/BETTER/BEST)
            #s for PE test list.
    """

    exponentials: list[tuple[int, int, float]] = []
    for input_val in inputs:
        base, exponent = map(int, input_val.split(" "))
        exponentials.append((base, exponent, exponent * log10(base)))

    k_smallest = sorted(exponentials, key=lambda e: e[2])[k - 1]

    return k_smallest[:2]
