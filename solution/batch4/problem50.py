""" Problem 50: Consecutive Prime Sum

https://projecteuler.net/problem=50

Goal: Return the smallest prime <= N that can be represented as the sum of the
longest consecutive prime sequence.

Constraints: 2 <= N <= 1e12

e.g.: N = 100
      sum = 41 -> 2 + 3 + 5 + 7 + 11 + 13
      length = 6
"""
from util.maths.reusable import is_prime_mr, prime_numbers
from util.search.reusable import binary_search


def consecutive_prime_sum(n: int) -> (int, int):
    """
    Brute force solution shows that all valid sequences start at low primes, with
    only a few starting as high as the 4th, 8th or 12th prime.

    Note that sieve generation of prime numbers is limited by memory. If the sum
    of a sequence exceeds the given limit, the next sequence starting from a larger
    prime will be 1 prime longer from where it broke.

    SPEED (WORSE)
        23.50s for N = 1e10

    :returns: Tuple of the smallest valid prime to the length of the generating
        prime sequence.
    """

    limit = min(n, 10_000_000)
    primes = prime_numbers(limit)
    len_primes = len(primes)
    prime_sum, longest = 2, 1
    max_j = len_primes
    for i in range(min(len_primes, 12)):
        for j in range(i + longest, max_j):
            seq_sum = sum(primes[i:j])
            if seq_sum > n:
                max_j = j + 1
                break
            if (
                    seq_sum <= limit and binary_search(seq_sum, primes)
                    or is_prime_mr(seq_sum)
            ):
                length = j - i
                if length > longest:
                    prime_sum, longest = seq_sum, length
    return prime_sum, longest


def consecutive_prime_sum_improved(n: int) -> (int, int):
    """
    Solution optimised by generating a smaller list of cumulative sums of primes
    to loop through, of which only the last value can exceed the given limit.
    Nested loop starts backwards to get the longest sequence sum for each starting
    prime by subtracting cumulative sums, then breaking the internal loop if a
    valid sequence is found.

    SPEED (BETTER)
        1.98s for N = 1e10

    :returns: Tuple of the smallest valid prime to the length of the generating
        prime sequence.
    """

    limit = min(n, 10_000_000)
    primes = prime_numbers(limit)
    cumulative_sum = [0]
    for prime in primes:
        cumulative_sum.append(cumulative_sum[-1] + prime)
        if cumulative_sum[-1] > n:
            break
    size = len(cumulative_sum)
    prime_sum, longest = 2, 1
    for i in range(size):
        for j in range(size - 1, i + longest - 1, -1):
            seq_sum = cumulative_sum[j] - cumulative_sum[i]
            if seq_sum > n:
                continue
            length = j - i
            if (
                    length > longest and
                    (seq_sum <= limit and binary_search(seq_sum, primes)
                     or is_prime_mr(seq_sum))
            ):
                prime_sum, longest = seq_sum, length
                break
    return prime_sum, longest
