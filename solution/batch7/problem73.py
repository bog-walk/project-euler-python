""" Problem 73: Counting Fractions In A Range

https://projecteuler.net/problem=73

Goal:  Count the elements of a sorted set of reduced proper fractions of order D
(their denominator <= D) that lie between 1/A+1 and 1/A (both exclusive).

Constraints: 1 < D < 2e6, 1 < A <= 100

Reduced Proper Fraction: A fraction n/d, where n & d are positive integers,
n < d, and gcd(n, d) == 1.

Farey Sequence: A sequence of completely reduced fractions, either between 0 and
1, or which when in reduced terms have denominators <= N, arranged in order of
increasing size.

    e.g. if d <= 8, the Farey sequence would be ->
         1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8,
         2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

e.g.: D = 8, A = 2
      count between 1/3 and 1/2 = 3
"""
from util.maths.reusable import prime_numbers


def count_mediants(d: int, left: int, right: int) -> int:
    """
    Recursively counts all mediants between a lower and upper bound until the
    calculated denominator exceeds d. Each new mediant will replace both the
    lower and upper bounds in different recursive calls.
    """

    mediant_denom = left + right
    if mediant_denom > d:
        return 0
    count_a = count_mediants(d, left, mediant_denom)
    count_b = count_mediants(d, mediant_denom, right)
    return 1 + count_a + count_b


def farey_range_count_recursive(d: int, a: int) -> int:
    """
    Solution uses recursion to count mediants between neighbours based on:

    p/q = (a + n)/(b + d)

    This is a recursive implementation of the Stern-Brocot tree binary search
    algorithm.

    There is no need to reference the numerators of these bounding fractions,
    so each fraction is represented as its Integer denominator instead of a
    Tuple/Fraction as in previous problem sets.

    SPEED (WORST)
        27.39ms for D = 1e3, A = 2
    SPEED (BETTER)
        1.42ms for D = 1e4, A = 100
    Risk of RecursionError for D > 1e3 if A is low.
    """

    return count_mediants(d, a + 1, a)


def farey_range_count_iterative(d: int, a: int) -> int:
    """
    This an iterative implementation of the Stern-Brocot tree binary search
    algorithm above.

    SPEED (WORSE)
        23.35ms for D = 1e3, A = 2
    SPEED (WORSE)
        1.71ms for D = 1e4, A = 100
    SPEED (WORSE)
        13.53s for D = 1e6, A = 100
    Quadratic complexity O(N^2) makes it difficult to scale for D > 1e6.
    """

    count = 0
    left, right = a + 1, a
    stack = []
    while True:
        mediant_denom = left + right
        if mediant_denom > d:
            if len(stack) == 0:
                break
            left, right = right, stack.pop()
        else:
            count += 1
            stack.append(right)
            right = mediant_denom
    return count


def farey_sieve(d: int, a: int) -> int:
    """
    Finds number of reduced fractions p/q <= 1/a with q <= d.
    """

    # every denominator q is initialised to floor(1/a * q) == floor(q/a)
    cache = [q // a for q in range(d + 1)]
    for q in range(1, d + 1):
        # subtract each q's rank from all its multiples
        for m in range(2 * q, d + 1, q):
            cache[m] -= cache[q]
    return sum(cache)


def farey_range_count_sieve(d: int, a: int) -> int:
    """
    Solution finds the number of reduced fractions less than the greater fraction
    1/a, then subtracts the number of reduced fractions less than 1/(a+1) from
    the former. The result is further decremented to remove the count for the
    upper bound fraction itself.

    SPEED (BETTER)
        2.19ms for D = 1e3, A = 2
    SPEED (BETTER)
        9.83s for D = 1e6, A = 100
    SPEED (WORSE)
        19.28s for D = 2e6, A = 2
    """

    return farey_sieve(d, a) - farey_sieve(d, a + 1) - 1


def num_of_fractions_in_range(limit: int) -> int:
    """
    Counts the number of fractions between 1/3 and 1/2 based on the formula:

    F(N) = {N}Sigma{m=1}(R(floor(N/m)))

    This can be rewritten to assist finding R(N) in the calling function:

     F(m) = {m}Sigma{n=1}(floor((n-1)/2) - floor(n/3))

     F(m) = q(3q - 2 + r) + { if (r == 5) 1 else 0 }

     where m = 6q + r and r in [0, 6).

     This helper function has not been adapted to allow different values of A.
     Once the lcm of A and A+1 is found, the above F(m) equation needs to be
     solved for q and r to determine the coefficients for the final function. How
     to do so programmatically for any input A has not yet been achieved.
    """

    q, r = limit // 6, limit % 6
    f = q * (3 * q - 2 + r)
    if r == 5:
        f += 1
    return f


def farey_range_count_IE(d: int, a: int) -> int:
    """
    Solution based on the Inclusion-Exclusion principle.

    If F(N) is a Farey sequence and R(N) is a Farey sequence of reduced proper
    fractions, i.e. gcd(n, d) = 1), then the starting identity is:

    F(N) = {N}Sigma{m=1}(R(floor(N/m)))

    Using the Mobius inversion formula, this becomes:

    R(N) = {N}Sigma{m=1}(mobius(m) * F(floor(N/m)))

    If all Mobius function values were pre-generated, this would allow a O(N)
    loop. Instead, R(N) is calculated using primes and the inclusion-exclusion
    principle.

    N.B. This solution does not translate well if A != 2.

    SPEED (BEST)
        2.7e5ns for D = 1e3, A = 2
    SPEED (BETTER)
        583.42ms for D = 2e6, A = 2

    :raises ValueError: If the value of a is not 2.
    """

    if a != 2:
        raise ValueError("Solution does not work if a != 2")
    primes = prime_numbers(d)
    num_of_primes = len(primes)

    def inclusion_exclusion(limit: int, index: int) -> int:
        count = num_of_fractions_in_range(limit)
        while index < num_of_primes and 5 * primes[index] <= limit:
            new_limit = limit // primes[index]
            index += 1
            count -= inclusion_exclusion(new_limit, index)
        return count

    return inclusion_exclusion(d, 0)
