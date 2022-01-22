from math import floor, gcd, isqrt, sqrt


def gaussian_sum(n: int) -> int:
    """ Calculates the sum of the first n natural numbers.

    Conversion of very large floats to integers in this formula can lead to large
    rounding losses, so division by 2 & int cast is replaced with a single bitwise
    right shift, as :math:`n >> 1 = n / 2^1`.
    """

    return n * (n + 1) >> 1


def is_pentagonal_number(p_n: int) -> int | None:
    """
    Derivation solution is based on the formula:

    :math:`n(3n - 1) / 2 = p_n`, in quadratic form becomes:

    :math:`0 = 3n^2 - n - 2p_n`, with :math:`a, b, c = 3, -1, (-2p_n)`

    putting these values in the quadratic formula becomes:

    :math:`n = (1 \\pm \\sqrt{1 + 24p_n}) / 6`

    so the inverse function, positive solution becomes:

    :math:`n = (1 + \\sqrt{1 + 24p_n}) / 6`

    :returns: p_n's corresponding term if pentagonal, or None.
    """

    n = (1 + sqrt(1 + 24 * p_n)) / 6
    return int(n) if n == floor(n) else None


def is_prime(n: int) -> bool:
    """ Checks if n is prime.

    This version will be used preferentially, unless the argument is expected to
    frequently exceed 1e6.

    SPEED (WORSE for N > 1e7)
        1.96s for a 15-digit prime
    SPEED (EQUAL for N == 1e6 || N == 1e7)
        20000ns for 7-digit prime
    SPEED (BETTER for N < 1e6)
        11200ns for 3-digit prime
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
        # primes > (k=3) are of the form 6k(+/-1)
        # i.e. they are never multiples of 3
        return False
    else:
        # N can only have 1 prime factor > sqrt(N): N itself!
        # max_p = floor(sqrt(n))
        max_p = isqrt(n)
        step = 5  # multiples of prime 5 not yet assessed
        # 11, 13, 17, 19, and 23 will all bypass N loop
        while step <= max_p:
            if not n % step or not n % (step + 2):
                return False
            step += 6
        return True


def is_prime_mr(num: int, k_rounds: list[int] = None) -> bool:
    """ Miller-Rabin probabilistic algorithm determines if a large number is
    likely to be prime.

    This version will only be used if the argument is expected to frequently
    exceed 1e6.

    -   The number received, once determined to be odd, is expressed as :math:`n =
        2^rs + 1`, with s being odd.
    -   A random integer, a, is chosen k times (higher k means higher accuracy),
        with 0 < a < num.
    -   Calculate :math:`a^s \\% n`. If this equals 1 or n - 1 while s has the
        powers of 2 previously factored out returned, then n passes as a strong
        probable prime.
    -   n should pass for all generated a.

    This algorithm uses a list of the first 5 primes instead of randomly generated a,
    as this has been proven valid for numbers up to 2.1e12. Providing a list of
    the first 7 primes gives test validity for numbers up to 3.4e14.

    SPEED (BETTER for N > 1e7)
        1.4e5ns for a 15-digit prime
    SPEED (EQUAL for N == 1e6 || N == 1e7)
        23700ns for 7-digit prime
    SPEED (WORSE for N < 1e6)
        28100ns for 3-digit prime
    """

    if k_rounds is None:
        k_rounds = [2, 3, 5, 7, 11]
    if 2 <= num <= 3:
        return True
    if num < 2 or num % 2 == 0:
        return False

    def miller_rabin(a: int, s: int, n: int) -> bool:
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            return True
        while s != n - 1:
            x = x * x % n
            s *= 2
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False

    # write num as 2^r * s + 1 by factoring out powers of 2
    # from num - 1 (even) until s is odd
    n_s = num - 1
    while n_s % 2 == 0:
        n_s //= 2
    for k in k_rounds:
        if k > num - 2:
            break
        if not miller_rabin(k, n_s, num):
            return False
    return True


def is_triangular_number(t_n: int) -> int | None:
    """
    Derivation solution is based on the formula:

    :math:`n(n + 1) / 2 = t_n`, in quadratic form becomes:

    :math:`0 = n^2 + n - 2t_n`, with `a, b, c = 1, 1, -2t_n`

    putting these values in the quadratic formula becomes:

    :math:`n = (-1 \\pm \\sqrt{1 + 8t_n}) / 2`

    so the inverse function, positive solution becomes:

    :math:`n = (\\sqrt{1 + 8t_n} - 1) / 2`

    :returns: t_n's corresponding term if triangular, or None.
    """

    n = 0.5 * (sqrt(1 + 8 * t_n) - 1)
    return int(n) if n == floor(n) else None


def power_digit_sum(base: int, exponent: int) -> int:
    """ Calculates the sum of the digits of the number :math:`base^exponent`. """

    return sum(map(int, str(pow(base, exponent))))


def prime_factors(n: int) -> dict[int, int]:
    """ Prime decomposition using Sieve of Eratosthenes algorithm.

    Every prime number after 2 will be odd and there can be at most 1 prime factor
    greater than sqrt(n), which would be n itself if n is a prime.

    :returns: Dict of prime factors (keys) and their exponents (values).
    """

    primes = dict()
    if n < 2:
        return primes
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
        primes[n] = 1
    return primes


def prime_numbers_og(n: int) -> list[int]:
    """
    Sieve of Eratosthenes algorithm outputs all prime numbers less than or equal
    to the upper bound provided.

    SPEED (WORSE)
        39.80ms for N = 1e5
    """

    boolean_mask = [not (i != 0 and i % 2 == 0) for i in range(n - 1)]
    for p in range(3, isqrt(n) + 1, 2):
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


def prime_numbers(n: int) -> list[int]:
    """
    Still uses Sieve of Eratosthenes method to output all prime numbers less than
    or equal to the upper bound provided, but cuts processing time in half by only
    allocating mask memory to odd numbers and by only looping through multiples of
    odd numbers. This version will be used in future solutions.

    SPEED (BETTER)
        16.71ms for N = 1e5
    """

    odd_sieve = (n - 1) // 2
    upper_limit = isqrt(n) // 2
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


def pythagorean_triplet(m: int, n: int, d: int) -> (int, int, int):
    """
    Euclid's formula generates all Pythagorean triplets from 2 numbers, m and n.

    All triplets originate from a primitive one by multiplying them by
    d = gcd(a, b, c).

    :raises ValueError: If arguments do not follow m > n > 0, or if both are odd,
        or if they are not co-prime, i.e. gcd(m, n) != 1.
    """

    if n < 1 or m < n:
        raise ValueError("Positive integers assumed to be m > n > 0")
    if n % 2 != 0 and m % 2 != 0:
        raise ValueError("Both integers cannot be odd")
    if gcd(m, n) != 1:
        raise ValueError("Positive integers must be co-prime")
    a = (m * m - n * n) * d
    b = 2 * m * n * d
    c = (m * m + n * n) * d
    return min(a, b), max(a, b), c


def sum_proper_divisors_og(n: int) -> int:
    """ Calculates the sum of all divisors of n.

    Solution optimised based on the following:

    -   N == 1 has no proper divisor but 1 is a proper divisor of all other naturals.

    -   A perfect square would duplicate divisors if included in the loop range.

    -   Loop range differs for odd numbers as they cannot have even divisors.

    SPEED (WORSE)
        4.2e4ns for N = 1e6 - 1
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
    """ Calculates the sum of all divisors of n.

    Solution above is further optimised by using prime factorisation to
    out-perform the original method. This version will be used in future solutions.

    SPEED (BETTER)
        7.8e3ns for N = 1e6 - 1
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
