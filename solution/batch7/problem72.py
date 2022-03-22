""" Problem 72: Counting Fractions

https://projecteuler.net/problem=72

Goal: Count the elements in a set of reduced proper fractions for d <= N,
i.e. order N.

Constraints: 2 <= N <= 1e6

Reduced Proper Fraction: A fraction n/d, where n & d are positive integers,
n < d, and gcd(n, d) == 1.

Farey Sequence: A sequence of completely reduced fractions, either between 0 and
1, or which when in reduced terms have denominators <= N, arranged in order of
increasing size.

    e.g. if d <= 8, the Farey sequence would be ->
         1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8,
         2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

e.g.: N = 8
      size = 21
"""
from math import isqrt


def farey_sequence_length_formula(order: int) -> int:
    """
    Solution based on the following Farey sequence properties:

    - The middle term of a sequence is always 1/2 for n > 1.

    - A sequence F(n) contains all elements of the previous sequence F(n-1) as
    well as an additional fraction for each number < n & co-prime to n.
    e.g. F(6) consists of F(5) as well as 1/6 & 5/6.

    Using Euler's totient (phi) function, the relationship between lengths becomes:

    F(n).length = F(n-1).length + phi(n)

    F(n).length = 0.5 * (3 + ({n}Sigma{d=1} mobius() * floor(n/d)^2))

    F(n).length = 0.5n(n + 3) - ({n}Sigma{d=2} F(n/d).length)

    N.B. This solution does not count left & right ancestors of F(1),
    namely {0/1, 1/0}, so these should be removed from the resulting length.

    SPEED (WORST)
        1.94s for N = 1e6
    """

    f_cache = [0]*(order + 1)
    f_cache[1] = 2

    def get_length(n: int) -> int:
        if not f_cache[n]:
            length = n * (n + 3) // 2
            for d in range(2, n + 1):
                next_term = n // d
                if f_cache[next_term]:
                    length -= f_cache[next_term]
                else:
                    new_length = get_length(next_term)
                    f_cache[next_term] = new_length
                    length -= new_length
            f_cache[n] = length
        return f_cache[n]

    return get_length(order) - 2


def farey_sequence_length_sieve(limit: int) -> int:
    """
    Solution uses Euler's product formula:

    Phi(n) = n * Pi(1 - (1/p)), with p being distinct prime factors of n.

    If prime factorisation means n = Pi(p_i^a_i), the above formula becomes:

    Phi(n) = Pi((p_i - 1) * p_i^(a_i - 1))

    if m = n/p, then Phi(n) = Phi(m)p, if p divides m, else, Phi(m)(p - 1)

    This quickly calculates totients by first sieving the smallest prime factors
    & checking if they are a multiple factor of n.

    Only odd numbers are included in the sieve, as all even numbers are handled
    together based on the following where k > 0 and n is odd:

    {m}Pi{k=0}(Phi(n2^k)) = (1 + {m}Pi{k=1}(2^(k-1))) * Phi(n) = 2^m * Phi(n)

    SPEED (BEST)
        483.37ms for N = 1e6
    """

    sieve_limit = (isqrt(limit) - 1) // 2
    max_i = (limit - 1) // 2
    cache = [0]*(max_i + 1)
    for n in range(1, sieve_limit + 1):  # sieve the smallest prime factors
        if not cache[n]:  # then 2n + 1 is prime
            p = 2 * n + 1
            for k in range(2 * n * (n + 1), max_i + 1, p):
                if not cache[k]:
                    cache[k] = p
    # find largest multiplier (m) where 2^m * n <= N, i.e. the largest power of 2
    multiplier = 1
    while multiplier <= limit:
        multiplier *= 2
    # num of reduced proper fractions whose denominator is power of 2
    multiplier //= 2
    count = multiplier - 1  # decrement to exclude fraction 1/1
    multiplier //= 2  # set to 2^(m-1)
    # the smallest index such that (2n + 1) * 2^(m-1) > N
    step_i = (limit // multiplier + 1) // 2
    for n in range(1, max_i + 1):
        if n == step_i:
            multiplier //= 2  # set to next smallest power of 2
            step_i = (limit // multiplier + 1) // 2
            # this maintains the invariant: (2n + 1)m <= N < (2n + 1)2m
        if not cache[n]:
            cache[n] = 2 * n
        else:
            p = cache[n]
            cofactor = (2 * n + 1) // p  # calculate Phi(2n+1)
            factor = p if cofactor % p == 0 else p - 1
            cache[n] = factor * cache[cofactor//2]
        # add sum of totients of all 2^k * (2n + 1) < N
        count += multiplier * cache[n]
    return count


def generate_all_farey_lengths(limit: int) -> list[int]:
    """
    Solution still uses a sieve, as in the above solution, but the sieve
    calculates the totient of all k multiples of primes <= [limit] based on the
    following:

    current Phi(p_k) = previous Phi(p_k) * (1 - (1/p))

    current Phi(p_k) = previous Phi(p_k) - previous Phi(p_k)/p

    Then the size of each sequence order is cached based on:

    F(n).length = F(n-1).length + phi(n)

    SPEED (BETTER)
        1.28s for N = 1e6

    :returns: List of Farey sequence lengths for every index = order N.
    """

    phi_cache = list(range(limit + 1))
    for n in range(2, limit + 1):
        if phi_cache[n] == n:  # n is prime
            # calculate Phi of all multiples of n
            for k in range(n, limit + 1, n):
                phi_cache[k] -= phi_cache[k] // n
    counts = [0]*(limit+1)
    # if returning only a single count instead of a generated list of counts, use
    # return sum(phi_cache[2:])
    for n in range(2, limit + 1):
        counts[n] = counts[n-1] + phi_cache[n]
    return counts
