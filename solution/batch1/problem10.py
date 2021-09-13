""" Problem 10: Summation of Primes

https://projecteuler.net/problem=10

Goal: Find the sum of all prime numbers <= N.

Constraints: 1 <= N <= 1e6

e.g. N = 5
     primes = {2, 3, 5}
     sum = 10
"""


def sum_of_primes_quick_draw(n):
    """
    This optimisation use the Sieve of Eratosthenes algorithm to discriminate
    against even numbers entirely, using only half of memory & fewer
    iterations, for multiple draws.

    Returns:
        array of sums of prime numbers <= index.
    """
    if n % 2 != 0:
        n += 1
    boolean_mask = [i > 2 and i % 2 != 0 or i == 2 for i in range(n + 1)]
    sums = [0] * (n + 1)
    sums[2] = 2
    for i in range(3, n + 1, 2):
        if boolean_mask[i]:
            sums[i] = sums[i - 1] + i
            if i * i < n:
                for j in range(i * i, n + 1, 2 * i):
                    boolean_mask[j] = False
        else:
            sums[i] = sums[i - 1]
        sums[i + 1] = sums[i]
    return sums
