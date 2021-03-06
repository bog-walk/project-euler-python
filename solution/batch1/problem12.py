""" Problem 12: Highly Divisible Triangular Number

https://projecteuler.net/problem=12

Goal: Find the value of the first triangle number to have more than N divisors.

Constraints: 1 <= N <= 1000

Triangle Number: A number generated by adding all natural numbers prior to &
including itself.

e.g.: N = 5
      1st = 1 from [1] -> {1}
      2nd = 3 from [1+2] -> {1,3}
      3rd = 6 from [1+2+3] -> {1,2,3,6}
      4th = 10 from [1+2+3+4] -> {1,2,5,10}
      5th = 15 from [1+2+3+4+5] -> {1,3,5,15}
      6th = 21 from [1+2+3+4+5+6] -> {1,3,7,21}
      7th = 28 from [1+2+3+4+5+6+7] -> {1,2,4,7,14,28}
      result = 28
"""
from math import prod
from util.maths.reusable import gauss_sum, prime_factors, prime_numbers_og


def count_divisors(n: int) -> int:
    """ Counts unique divisors of n using n's prime decomposition.

    e.g. 28 = 2^2 * 7^1, therefore

        num_of_divisors = (2 + 1) * (1 + 1) = 6 -> {1,2,4,7,14,28}
    """

    return prod([v + 1 for _, v in prime_factors(n).items()])


def first_triangle_over_N(n: int) -> int:
    """
    Returns the found triangle number generated as a Gaussian sum that has had its
    divisors counted using prime decomposition.

    Since the components of a Gaussian sum (n & n+1) are co-prime (i.e. they can
    have neither a common prime factor nor a common divisor), the amount of
    divisors can be assessed based on the cycling formulae:

    - t represents Gaussian sum = n(n + 1) / 2

    - [even n] D(t) = D(n/2) * D(n+1)
    D(n+1) becomes D(n) for the next number, which will be odd.

    - [odd n] D(t) = D(n) * D((n+1)/2)

    SPEED (WORSE)
        583.69ms for N = 1000
    """

    if n == 1:
        return 3
    t = 2  # D(2) = D(1) * D(3)
    d_n_1 = 2  # D(3) = 2
    count = 2
    while count <= n:
        t += 1
        d_n_2 = count_divisors(t + 1) if t % 2 == 0 else count_divisors((t + 1) // 2)
        count = d_n_1 * d_n_2
        d_n_1 = d_n_2
    return gauss_sum(t)


def first_triangle_over_N_improved(n: int) -> int:
    """ Generates primes to count number of divisors based on prime factorisation.

    SPEED (BETTER)
        229.81ms for N = 1000
    """

    if n == 1:
        return 3
    all_primes = prime_numbers_og(n * 2)
    all_primes_size = len(all_primes)
    prime = 3
    divisors_of_n = 2  # min num of divisors of any prime
    count = 0
    while count <= n:
        prime += 1
        n_1 = prime
        if n_1 % 2 == 0:
            n_1 //= 2
        divisors_of_n1 = 1
        for i in range(all_primes_size):
            # when the prime divisor would be greater than the residual n_1,
            # that residual n_1 is the last prime factor with an exponent==1,
            # so no need to identify it.
            if all_primes[i] * all_primes[i] > n_1:
                divisors_of_n1 *= 2
                break
            exponent = 1
            while n_1 % all_primes[i] == 0:
                exponent += 1
                n_1 //= all_primes[i]
            if exponent > 1:
                divisors_of_n1 *= exponent
            if n_1 == 1:
                break
        count = divisors_of_n * divisors_of_n1
        divisors_of_n = divisors_of_n1
    return prime * (prime - 1) // 2


def first_triangle_over_N_optimised(limit: int) -> int:
    """
    Similar to first function that exploits co-prime property of Gaussian sum
    but stores cumulative divisor counts in a list for quick access instead of
    calculating the count for every new n. Dual cyclic formulae use (n - 1) instead
    of (n + 1) to match the index used in the cached list.

    Note that n_max was found by exhausting all solutions for n = [1, 1000] &
    finding the maximum of the ratios of t:n. At n = 1000, the valid triangle number
    is the 41041st term.

    SPEED (BEST)
        71.81ms for N = 1000
    """

    n_max = min(limit * 53, 41100)
    divisor_count = [0]*n_max
    n, d_t = 0, 0
    while d_t <= limit:
        n += 1
        for i in range(n, n_max, n):
            divisor_count[i] += 1
        if n % 2 == 0:
            d_t = divisor_count[n//2] * divisor_count[n-1]
        else:
            d_t = divisor_count[n] * divisor_count[(n-1)//2]
    return n * (n - 1) // 2
