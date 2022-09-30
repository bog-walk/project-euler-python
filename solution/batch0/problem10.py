""" Problem 10: Summation of Primes

https://projecteuler.net/problem=10

Goal: Find the sum of all prime numbers <= N.

Constraints: 1 <= N <= 1e6

e.g. N = 5
     primes = {2, 3, 5}
     sum = 10
"""


def sum_of_primes_quick_draw(n: int) -> list[int]:
    """
    Stores the cumulative sum of prime numbers to allow quick access to the
    answers for multiple N <= n.

    Solution mimics original Sieve of Eratosthenes algorithm that iterates over
    only odd numbers & their multiples, but uses boolean mask to alter a list of
    cumulative sums instead of returning a list of prime numbers.

    SPEED (WORSE)
        400.56ms for N = 1e6

    :returns: List of the cumulative sums of prime numbers <= index.
    """

    if n % 2:
        n += 1
    boolean_mask = [i > 2 and i % 2 != 0 or i == 2 for i in range(n + 1)]
    sums = [0]*(n + 1)
    sums[2] = 2
    for i in range(3, n + 1, 2):
        prev_sum = sums[i - 1]
        if boolean_mask[i]:
            # change next even number as well as current odd
            sums[i:i+2] = [prev_sum + i, prev_sum + i]
            if i * i < n:
                for j in range(i * i, n + 1, 2 * i):
                    boolean_mask[j] = False
        else:
            sums[i:i+2] = [prev_sum, prev_sum]
    return sums


def sum_of_primes_quick_draw_optimised(n: int) -> list[int]:
    """
    Similar to the above solution in that it stores the cumulative sum of prime
    numbers to allow future quick access; however, it replaces the typical boolean
    mask from the Sieve of Eratosthenes algorithm with this cumulative cache.

    An unaltered element == 0 indicates a prime, with future multiples of that
    prime marked with a -1, before the former, and its even successor, are replaced
    by the total so far.

    SPEED (BETTER)
        282.85ms for N = 1e6

    :returns: List of the cumulative sums of prime numbers <= index.
    """

    if n % 2:
        n += 1
    sums = [0]*(n + 1)
    total = 2
    sums[2] = total
    for i in range(3, n + 1, 2):
        if sums[i] == 0:
            total += i
            # mark all multiples of prime using slice assignment with step
            # which, unlike other assignments, requires an exact size match
            sums[i*i::2*i] = [-1]*((n-i*i)//(2*i)+1)
        # change next even number as well as current odd using slice assignment
        sums[i:i+2] = [total]*2
    return sums
