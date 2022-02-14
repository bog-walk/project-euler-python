""" Problem 48: Self Powers

https://projecteuler.net/problem=48

Goal: Find the last 10 digits of the number generated by the series,
1^1 + 2^2 + 3^3 + .. + N^N, without leading zeroes.

Constraints: 1 <= N <= 2e6

e.g.: N = 10
      1^1 + 2^2 + 3^3 + .. + 10^10 = 10_405_071_317
      last 10 digits = 405_071_317 (leading zero omitted)
"""
modulus = 10_000_000_000


def self_powers_sum_modulo(n: int) -> int:
    """
    Solution based on the modular arithmetic rule that:

    (x + y) % z == ((x % z) + (y % z)) % z

    This same rule applies to multiplication with modulo:

    (x * y) % z == ((x % z) * (y % z)) % z

    The carried over number for each new self-power is thereby significantly
    reduced by performing modulo at every step.

    SPEED (WORSE)
        18.30s for N = 1e4
    """

    total = 0
    for d in range(1, n + 1):
        power = d
        for _ in range(d - 1):
            power *= d
            power %= modulus
        total += power
        total %= modulus
    return total


def self_powers_sum(n: int) -> int:
    """
    Solution optimised by using built-in pow(base, exp, mod).

    SPEED (BETTER)
        36.00ms for N = 1e4
    """

    total = 0
    for d in range(1, n + 1):
        total += pow(d, d, modulus)
    return total % modulus
