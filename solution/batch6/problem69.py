""" Problem 69: Totient Maximum

https://projecteuler.net/problem=69

Goal: Find the smallest value of n < N for which n / Phi(n) is maximum.

Constraints: 3 <= N <= 1e18

Euler's Totient Function: Phi(n) is used to determine the count of positive
integers < n that are relatively prime to n. An integer k is relatively prime to
n (aka co-prime or its totative) if gcd(n, k) = 1, as the only positive integer
that is a divisor of both of them is 1.

    n = 2 -> {1}                -> Phi(n) = 1; n/Phi(n) = 2
    n = 3 -> {1, 2}             -> Phi(n) = 2; n/Phi(n) = 1.5
    n = 4 -> {1, 3}             -> Phi(n) = 2; n/Phi(n) = 2
    n = 5 -> {1, 2, 3, 4}       -> Phi(n) = 4; n/Phi(n) = 1.25
    n = 6 -> {1, 5}             -> Phi(n) = 2; n/Phi(n) = 3
    n = 7 -> {1, 2, 3, 4, 5, 6} -> Phi(n) = 6; n/Phi(n) = 1.1666...
    n = 8 -> {1, 3, 5, 7}       -> Phi(n) = 4; n/Phi(n) = 2
    n = 9 -> {1, 2, 4, 5, 7, 8} -> Phi(n) = 6; n/Phi(n) = 1.5
    n = 10 -> {1, 3, 7, 9}      -> Phi(n) = 4; n/Phi(n) = 2.5

e.g.: N = 3
      n = 2
      N = 10
      n = 6
"""
from util.maths.reusable import prime_factors, prime_numbers


def totient(n: int) -> int:
    """
    Based on Euler's product formula:

    Phi(n) = n * Pi(1 - (1/p)), with p being distinct prime factors of n.

    This is equivalent to the formula that doesn't use fractions:

    Phi(n) = p_1^(e_1 - 1)(p_1 - 1) * p_2^(e_2 - 1)(p_2 - 1)... p_r(e_r - 1)(p_r - 1)

    e.g. Phi(20) = Phi({2^2, 5^1}) = 2^1 * 1 * 5^0 * 4 = 8
    """

    count = 1
    for p, e in prime_factors(n).items():
        count *= pow(p, e - 1) * (p - 1)
    return count


def max_totient_ratio(limit: int) -> int:
    """
    Solution calculates the totient of each n under limit.

    SPEED (WORSE)
        38.54s for N = 1e6

    :returns: The first n under limit that achieves the maximum ratio.
    """

    max_n, max_ratio = 1, 1.0
    for n in range(2, limit + 1):
        current_phi = totient(n)
        current_ratio = n / current_phi
        if current_ratio > max_ratio:
            max_n, max_ratio = n, current_ratio
    return max_n


def max_totient_ratio_primorial(limit: int) -> int:
    """
    Solution optimised by taking Euler's product formula further:

    Phi(n) = n * Pi(1 - (1/p)), with p being distinct prime factors of n.

    If the ratio n / Phi(n) is the required result, this becomes:

    n/Phi(n) = n / (n * Pi(1 - (1/p)))

    n/Phi(n) = Pi(p / (p - 1))

    Among all numbers having exactly k-distinct prime factors, the quotient is
    maximised for those numbers divisible by the k-smallest primes. So if n_k is
    the product of the k-smallest primes, n_k/Phi(n_k) is maximised over all
    n/Phi(n) that occur for n < n_{k+1}.

    N.B. Upper constraints 1e18 will be reached by prime number 47.

    SPEED (BETTER)
        1.9e4ns for N = 1e6

    :returns: The first n under limit that achieves the maximum ratio.
    """

    max_n = 1
    for p in prime_numbers(50):
        if max_n * p >= limit:
            break
        max_n *= p
    return max_n
