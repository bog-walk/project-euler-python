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

    :returns: List of the cumulative sums of prime numbers <= index.
    """
    if n % 2:
        n += 1
    boolean_mask = [i > 2 and i % 2 != 0 or i == 2 for i in range(n + 1)]
    sums = [0]*(n + 1)
    sums[2] = 2
    for i in range(3, n + 1, 2):
        if boolean_mask[i]:
            sums[i] = sums[i - 1] + i
            if i * i < n:
                for j in range(i * i, n + 1, 2 * i):
                    boolean_mask[j] = False
        else:
            sums[i] = sums[i - 1]
        # even number cumulative sum will not have changed
        sums[i + 1] = sums[i]
    return sums
