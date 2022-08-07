from math import floor, gcd, isqrt, log2, sqrt

from util.tests.reusable import compare_speed


def gauss_sum(n: int) -> int:
    """ Calculates the sum of the first n natural numbers, based on the formula:

    {n}Sigma{k=1} k = n * (n + 1) / 2

    Conversion of very large floats to integers in this formula can lead to large
    rounding losses, so division by 2 & int cast is replaced with a single bitwise
    right shift, as n >> 1 = n / 2^1.
    """

    return n * (n + 1) >> 1


def is_coprime(x: int, y: int) -> bool:
    """
    Two integers are co-prime (relatively/mutually prime) if the only positive
    integer that is a divisor of both of them is 1.
    """

    return gcd(x, y) == 1


def is_hexagonal_number(h_n: int) -> int | None:
    """
    Derivation solution is based on the formula:

    n(2n - 1) = h_n, in quadratic form becomes:

    0 = 2n^2 - n - h_n, with a, b, c = 2, -1, -h_n

    putting these values in the quadratic formula becomes:

    n = (1 +/- sqrt(1 + 8h_n)) / 4

    so the inverse function, positive solution becomes:

    n = (1 + sqrt(1 + 8h_n)) / 4

    :returns: h_n's corresponding term if hexagonal, or None.
    """

    n = 0.25 * (1 + sqrt(1 + 8 * h_n))
    return int(n) if n == floor(n) else None


def is_pentagonal_number(p_n: int) -> int | None:
    """
    Derivation solution is based on the formula:

    n(3n - 1) / 2 = p_n, in quadratic form becomes:

    0 = 3n^2 - n - 2p_n, with a, b, c = 3, -1, -2p_n

    putting these values in the quadratic formula becomes:

    n = (1 +/- sqrt(1 + 24p_n)) / 6

    so the inverse function, positive solution becomes:

    n = (1 + sqrt(1 + 24p_n)) / 6

    :returns: p_n's corresponding term if pentagonal, or None.
    """

    n = (1 + sqrt(1 + 24 * p_n)) / 6
    return int(n) if n == floor(n) else None


def is_prime(n: int) -> bool:
    """ Checks if n is prime.

    This version will be used preferentially, unless the argument is expected to
    frequently exceed 1e5.

    SPEED (WORSE for N > 1e15)
        1.86s for a 15-digit prime
    SPEED (WORSE for N > 1e10)
        5.01ms for a 10-digit prime
    SPEED (WORSE for N > 1e5)
        6.6e4ns for a 6-digit prime
    SPEED (BETTER for N < 1e5)
        1.7e4ns for a 5-digit prime
    SPEED (BETTER for N < 1e3)
        7700ns for a 3-digit prime
    """

    if n < 2:
        return False
    elif n < 4:  # 2 and 3 are primes
        return True
    elif not n % 2:  # 2 is the only even prime
        return False
    elif n < 9:  # 4, 6, and 8 already excluded
        return True
    elif not n % 3:
        # primes > 3 are of the form 6k(+/-1)
        # i.e. they are never multiples of 3
        return False
    else:
        # n can only have 1 prime factor > sqrt(n): n itself!
        max_p = isqrt(n)
        step = 5  # as multiples of prime 5 not yet assessed
        # 11, 13, 17, 19, and 23 will all bypass this loop
        while step <= max_p:
            if not n % step or not n % (step + 2):
                return False
            step += 6
        return True


def is_prime_mr(num: int, k_rounds: list[int] | None = None) -> bool:
    """ Miller-Rabin probabilistic algorithm determines if a large number is
    likely to be prime.

    This version will only be used if the argument is expected to frequently
    exceed 1e5.

    -   The number received, once determined to be odd, is expressed as
        n = (2^r)s + 1, with s being odd.
    -   A random integer, a, is chosen k times (higher k means higher accuracy),
        with 0 < a < num.
    -   Calculate a^s % n. If this equals 1 or this plus 1 equals n while s has
        the powers of 2 previously factored out returned, then n passes as a
        strong probable prime.
    -   n should pass for all generated a.

    The algorithm's complexity is O(k*log^3*n). This algorithm uses a list of
    the first 5 primes instead of randomly generated a, as this has been proven
    valid for numbers up to 2.1e12. Providing a list of the first 7 primes gives
    test validity for numbers up to 3.4e14.

    SPEED (BETTER for N > 1e15)
        1.5e5ns for a 15-digit prime
    SPEED (BETTER for N > 1e10)
        7.6e4ns for a 10-digit prime
    SPEED (BETTER for N > 1e5)
        5.6e4ns for a 6-digit prime
    SPEED (WORSE for N < 1e5)
        4.2e4ns for a 5-digit prime
    SPEED (WORSE for N < 1e3)
        3.9e4ns for a 3-digit prime
    """

    if k_rounds is None:
        k_rounds = [2, 3, 5, 7, 11]
    if 2 <= num <= 3:
        return True
    if num < 2 or num % 2 == 0:
        return False

    def miller_rabin(a: int, s: int, r: int, n: int) -> bool:
        # calculate a^s % n
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(r):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False

    # write num as 2^r * s + 1 by first getting r, the largest power of 2
    # that divides (num - 1), by getting the index of the right-most one bit
    n_r = int(log2((num - 1) & -(num - 1)))
    # x * 2^y == x << y
    n_s = (num - 1) // (2 << (n_r - 1))
    for k in k_rounds:
        if k > num - 2:
            break
        if not miller_rabin(k, n_s, n_r, num):
            return False
    return True


def is_triangular_number(t_n: int) -> int | None:
    """
    Derivation solution is based on the formula:

    n(n + 1) / 2 = t_n, in quadratic form becomes:

    0 = n^2 + n - 2t_n, with a, b, c = 1, 1, -2t_n

    putting these values in the quadratic formula becomes:

    n = (-1 +/- sqrt(1 + 8t_n)) / 2

    so the inverse function, positive solution becomes:

    n = (sqrt(1 + 8t_n) - 1) / 2

    :returns: t_n's corresponding term if triangular, or None.
    """

    n = 0.5 * (sqrt(1 + 8 * t_n) - 1)
    return int(n) if n == floor(n) else None


def power_digit_sum(base: int, exponent: int) -> int:
    """ Calculates the sum of the digits of the number, base^exponent. """

    return sum(map(int, str(pow(base, exponent))))


def prime_factors_og(n: int) -> dict[int, int]:
    """ Prime decomposition repeatedly divides out all prime factors using an
    optimised Direct Search Factorisation algorithm.

    Every prime number after 2 will be odd and there can be at most 1 prime factor
    greater than sqrt(n), which would be n itself if n is a prime. This is based
    on all cofactors having been already tested following the formula:

    n / floor(sqrt(n) + 1) < sqrt(n)

    e.g. N = 12 returns {2=2, 3=1} -> 2^2 * 3^1 = 12

    SPEED (WORSE for N with large factors)
        55.88s for N = 600_851_475_143
    SPEED (WORSE for N with small factors)
        74.70ms for N = 1e12

    :returns: Dict of prime factors (keys) and their exponents (values).
    :raises ValueError: If argument is not greater than 1.
    """

    if n <= 1:
        raise ValueError("Must provide a natural number greater than 1")
    primes = dict()
    factors = [2]
    factors.extend(range(3, isqrt(n) + 1, 2))
    for factor in factors:
        while n % factor == 0:
            if factor in primes:
                primes[factor] += 1
            else:
                primes[factor] = 1
            n //= factor
    if n > 2:
        primes[n] = primes[n] + 1 if n in primes else 1
    return primes


def prime_factors(n: int) -> dict[int, int]:
    """ Prime decomposition repeatedly divides out all prime factors using a
    Direct Search Factorisation algorithm without any optimisation.

    e.g. N = 12 returns {2=2, 3=1} -> 2^2 * 3^1 = 12

    This version will be used in future solutions.

    SPEED (BETTER for N with large factors)
        2.9e+05ns for N = 600_851_475_143
    SPEED (BETTER for N with small factors)
        8590ns for N = 1e12

    :returns: Dict of prime factors (keys) and their exponents (values).
    :raises ValueError: If argument is not greater than 1.
    """

    if n <= 1:
        raise ValueError("Must provide a natural number greater than 1")
    primes = dict()
    factor = 2
    while factor * factor <= n:
        while n % factor == 0 and n != factor:
            if factor in primes:
                primes[factor] += 1
            else:
                primes[factor] = 1
            n //= factor
        factor += 1
    if n > 1:
        primes[n] = primes[n] + 1 if n in primes else 1
    return primes


def prime_numbers_og(n: int) -> list[int]:
    """
    Sieve of Eratosthenes algorithm outputs all prime numbers less than or equal
    to the upper bound provided.

    SPEED (WORSE)
        23.04ms for N = 1e5
    """

    # create mask representing [2, max], with all even numbers except 2 (index 0)
    # marked false
    boolean_mask = [not (i != 0 and i % 2 == 0) for i in range(n - 1)]
    for p in range(3, isqrt(n) + 1, 2):
        if boolean_mask[p - 2]:
            if p * p > n:
                break
            # mark all multiples (composites of the divisors) that are >= p squared
            # as false
            for m in range(p * p, n + 1, 2 * p):
                boolean_mask[m - 2] = False
    primes = []
    for i, isPrime in enumerate(boolean_mask):
        if isPrime:
            primes.append(i + 2)
    return primes


def prime_numbers(n: int) -> list[int]:
    """
    Still uses Sieve of Eratosthenes method to output all prime numbers less than
    or equal to the upper bound provided, but cuts processing time in half by only
    allocating mask memory to odd numbers and by only looping through multiples of
    odd numbers.

    This version will be used in future solutions.

    SPEED (BETTER)
        14.99ms for N = 1e5
    """

    if n < 2:
        return []
    odd_sieve = (n - 1) // 2
    upper_limit = isqrt(n) // 2
    # create mask representing [2, 3..n step 2]
    boolean_mask = [True] * (odd_sieve + 1)
    # boolean_mask[0] corresponds to prime 2 & is skipped
    for i in range(1, upper_limit + 1):
        if boolean_mask[i]:
            # j = next index at which multiple of odd prime exists
            j = i * 2 * (i + 1)
            while j <= odd_sieve:
                boolean_mask[j] = False
                j += 2 * i + 1
    primes = []
    for i, isPrime in enumerate(boolean_mask):
        if i == 0:
            primes.append(2)
            continue
        if isPrime:
            primes.append(2 * i + 1)
    return primes


def pythagorean_triplet(m: int, n: int, d: int) -> tuple[int, int, int]:
    """
    Euclid's formula generates all Pythagorean triplets from 2 numbers, m and n.

    All triplets originate from a primitive one by multiplying them by
    d = gcd(a, b, c).

    :raises ValueError: If arguments do not follow m > n > 0, or if both are odd,
        or if they are not co-prime, i.e. gcd(m, n) != 1.
    """

    if n < 1 or m < n:
        raise ValueError("Positive integers assumed to be m > n > 0")
    if m % 2 == 1 and n % 2 == 1:
        raise ValueError("Both integers cannot be odd")
    if not is_coprime(m, n):
        raise ValueError("Positive integers must be co-prime")
    a = (m * m - n * n) * d
    b = 2 * m * n * d
    c = (m * m + n * n) * d
    return min(a, b), max(a, b), c


def sum_proper_divisors_og(n: int) -> int:
    """ Calculates the sum of all divisors of n, not inclusive of n.

    Solution optimised based on the following:

    -   N == 1 has no proper divisor but 1 is a proper divisor of all other naturals.

    -   A perfect square would duplicate divisors if included in the loop range.

    -   Loop range differs for odd numbers as they cannot have even divisors.

    SPEED (WORSE)
        8.8e4ns for N = 1e6 - 1
    """

    if n < 2:
        return 0
    total = 1
    max_divisor = isqrt(n)
    if max_divisor * max_divisor == n:
        total += max_divisor
        max_divisor -= 1
    divisor_range = range(3, max_divisor + 1, 2) if n % 2 != 0 \
        else range(2, max_divisor + 1)
    for d in divisor_range:
        if n % d == 0:
            total += d + n // d
    return total


def sum_proper_divisors(num: int) -> int:
    """ Calculates the sum of all divisors of num, not inclusive of num.

    Solution above is further optimised by using prime factorisation to
    out-perform the original method.

    This version will be used in future solutions.

    SPEED (BETTER)
        1.5e4ns for N = 1e6 - 1
    """

    if num < 2:
        return 0
    n = num
    total = 1
    p = 2
    while p * p <= num and n > 1:
        if n % p == 0:
            j = p * p
            n //= p
            while n % p == 0:
                j *= p
                n //= p
            total *= (j - 1)
            total //= (p - 1)
        if p == 2:
            p += 1
        else:
            p += 2
    if n > 1:
        total *= (n + 1)
    return total - num
