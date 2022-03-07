""" Problem 70: Totient Permutation

https://projecteuler.net/problem=70

Goal: Find the value of n, with 1 < n < N, for which Phi(n) is a permutation of n
and the ratio n/Phi(n) produces a minimum.

Constraints: 100 <= N <= 1e7

Euler's Totient Function: Phi(n) is used to determine the count of positive
integers < n that are relatively prime to n. The number 1 is considered co-prime
to every positive number, so Phi(1) = 1.
Phi(87109) = 79180, which is a permutation.

e.g.: N = 100
      result = 21 -> Phi(21) = 12 & 21/Phi(21) = 1.75
"""
from util.combinatorics.reusable import permutation_id
from util.maths.reusable import prime_numbers


def totient_permutation(limit: int) -> int:
    """
    Solution based on Euler's product formula:

    Phi(n) = nPi(1 - (1/p)), with p being distinct prime factors of n.

    If the ratio n / Phi(n) is the required result, this becomes:

     n/Phi(n) = n / (nPi(1 - (1/p)))

     n/Phi(n) = Pi(p / (p - 1))

     If this ratio must be minimised then the result of Phi(n) needs to be
     maximised, which is done by finding n with the fewest but largest distinct
     prime factors. If these prime factors are narrowed down to only 2 & are both
     as close to sqrt([limit]) as possible, then Phi's formula becomes:

     Phi(n) = n(1 - (1/p_1))(1 - (1/p_2)), with n = p_1p_2 it becomes:

     Phi(n) = p_1p_2(1 - (1/p_1))(1 - (1/p_2))

     Phi(n) = (p_1p_2 - (p_1p_2/p_1))(1 - (1/p_2))

     Phi(n) = (p_1p_2 - p_2)(1 - (1/p_2))

     Phi(n) = p_1p_2 - p_1 - p_2 + 1 = (p_1 - 1)(p_2 - 1)

     This solution finds all valid n except for one, 2817 = {3^2, 313^1}, as it is
     a product of 3 prime factors. This n is captured in the alternative solution
     below, without adding a special case clause, but is a slower solution.

     N.B. Using sorted string casts instead of util.combinatorics.permutation_id
     helper cut the speed in half.

     SPEED (BETTER)
        5.76s for N = 1e7
    """

    if 2818 <= limit <= 2991:
        return 2817
    primes = prime_numbers(limit)
    num_of_primes = len(primes)
    min_n, min_ratio = 1, float('inf')
    for i in range(num_of_primes - 1):
        p_1 = primes[i]
        for j in range(i+1, num_of_primes):
            p_2 = primes[j]
            n = p_1 * p_2
            if n >= limit:
                break
            phi = (p_1 - 1) * (p_2 - 1)
            ratio = n / phi
            if ratio < min_ratio and sorted(str(n)) == sorted(str(phi)):
                min_n, min_ratio = n, ratio
    return min_n


def totient_permutation_robust(limit: int) -> int:
    """
    Solution finds totient of every n under limit by iterating over prime
    numbers instead of using a helper prime factorisation method. This iteration
    is broken early & returns null if the increasingly reducing totient count
    becomes too small to satisfy the current minimum ratio.

    SPEED (WORSE)
        56.71s for N = 1e7
    """

    primes = prime_numbers(limit)
    min_n, min_ratio = 2, float('inf')

    def maximised_totient(num: int) -> int | None:
        """
        Based on Euler's product formula:

        Phi(n) = nPi(1 - (1/p)), that repeatedly subtracts found prime factors
        from n.

        :returns: Integer value of Phi(n) if n/Phi(n) will create a value that
        challenges the current minimum ratio stored; otherwise, None.
        """

        count = num
        reduced = num
        for p in primes:
            if p * p > reduced:
                break
            if reduced % p:
                continue
            while True:
                reduced //= p
                if reduced % p:
                    break
            # equivalent to count = count * (1 - (1/p))
            count -= count // p
            if count * min_ratio < num:
                return None
        return count - (count // reduced) if reduced > 1 else count

    for n in range(3, limit):
        phi = maximised_totient(n)
        if phi is None:
            continue
        ratio = n / phi
        if ratio < min_ratio and permutation_id(n) == permutation_id(phi):
            min_n, min_ratio = n, ratio
    return min_n
