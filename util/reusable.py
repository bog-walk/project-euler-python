from math import gcd, floor, sqrt


def least_common_multiple(x, y):
    if x == 0 or y == 0:
        raise ValueError("The LCM of 0 is undefined")
    return abs(x * y) // gcd(x, y)


def prime_numbers(n):
    """
    Uses Sieve of Eratosthenes method to output all prime numbers
    less than or equal to the upper bound provided.
    """
    boolean_mask = [not(i != 0 and i % 2 == 0) for i in range(n - 1)]
    for p in range(3, floor(sqrt(n)) + 1, 2):
        if boolean_mask[p - 2]:
            if p * p > n:
                break
            for m in range(p * p, n + 1, 2 * p):
                boolean_mask[m - 2] = False
    primes = []
    for i, isPrime in enumerate(boolean_mask):
        if isPrime:
            primes.append(i + 2)
    return primes


def gaussian_sum(n):
    return n * (n + 1) // 2
