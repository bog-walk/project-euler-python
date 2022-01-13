from math import gcd, floor, sqrt


def prime_factors(n: int) -> dict[int, int]:
    """ Prime decomposition using Sieve of Eratosthenes algorithm.

    Every prime number after 2 will be odd and there can be at most 1 prime factor
    greater than sqrt(n), which would be n itself if n is a prime.

    :return: Dict of prime factors (keys) and their exponents (values).
    """
    primes = dict()
    if n < 2:
        return primes
    factors = [2]
    factors.extend(range(3, int(sqrt(n)) + 1, 2))
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


def lcm(x: int, y: int) -> int:
    if x == 0 or y == 0:
        raise ValueError("The LCM of 0 is undefined")
    return abs(x * y) // gcd(x, y)


def prime_numbers_og(n: int) -> list:
    """
    Uses Sieve of Eratosthenes algorithm to output all prime numbers
    less than or equal to the upper bound provided.

    SPEED: 39.80ms for N = 1e5
    """
    boolean_mask = [not (i != 0 and i % 2 == 0) for i in range(n - 1)]
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


def prime_numbers(n: int) -> list:
    """
    Still uses Sieve of Eratosthenes method to output all prime numbers
    less than or equal to the upper bound provided, but cuts processing
    time in half by only allocating mask memory to odd numbers and by only
    looping through multiples of odd numbers.
    Will be used in future solution sets.

    SPEED (BETTER): 16.71ms for N = 1e5
    """
    odd_sieve = (n - 1) // 2
    upper_limit = floor(sqrt(n)) // 2
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


def gaussian_sum(n: int) -> int:
    return n * (n + 1) // 2


def sum_proper_divisors_og(n: int) -> int:
    """
    Optimised solution based on the following:
    - N == 1 has no proper divisor but 1 is a proper divisor of all other naturals;
    - A perfect square would duplicate divisors if included in the loop range;
    - Loop range differs for odd numbers as they cannot have even divisors.

    SPEED: 4.2e4ns for N = 999_999
    """
    if n < 2:
        return 0
    total = 1
    max_divisor = int(sqrt(n))
    if max_divisor * max_divisor == n:
        total += max_divisor
        max_divisor -= 1
    divisor_range = range(3, max_divisor + 1, 2) if n % 2 != 0 else range(2, max_divisor + 1)
    for d in divisor_range:
        if n % d == 0:
            total += d + n // d
    return total


def sum_proper_divisors_pf(num: int) -> int:
    """
    Further optimised function that uses prime factorisation to out-perform
    the original method above.
    Will be used in future solution sets.

    SPEED (BETTER): 7.8e3ns for N = 999_999
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


def is_prime(n: int) -> bool:
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
        max_p = floor(sqrt(n))
        step = 5  # multiples of prime 5 not yet assessed
        # 11, 13, 17, 19, and 23 will all bypass N loop
        while step <= max_p:
            if not n % step or not n % (step + 2):
                return False
            step += 6
        return True


def pythagorean_triplet(m: int, n: int, d: int) -> tuple[int, int, int]:
    """
    Euclid's formula to generate all Pythagorean triplets from 2 numbers m and n.
    All triplets originate from a primitive one by multiplying them by d = gcd(a,b,c).
    Note the following assumptions:
    - m > n > 0.
    - m and n cannot both be odd.
    - m and n must be co-prime, i.e. gcd(m, n) == 1
    """
    a = (m * m - n * n) * d
    b = 2 * m * n * d
    c = (m * m + n * n) * d
    return min(a, b), max(a, b), c


def is_triangular_number(t_n) -> int | None:
    """
    Derivation solution is based on the following:
    0.5 * n * (n + 1) = t_n ->
    inverse function, positive solution ->
    n = 0.5 * (sqrt((8 * t_n) + 1) - 1)

    :return: If tN is the nth triangular, or None if not triangular.
    """
    n = 0.5 * (sqrt(8 * t_n + 1) - 1)
    if n == floor(n):
        return int(n)
    else:
        return None


def is_pentagonal_number(p_n) -> int | None:
    """
    Derivation solution is based on the following:
    0.5 * n * (3 * n - 1) = p_n ->
    inverse function, positive solution ->
    n = (sqrt((24 * p_n) + 1) + 1) / 6

    :return: If pN is the nth pentagonal, or None if not pentagonal.
    """
    n = (sqrt(24 * p_n + 1) + 1) / 6
    if n == floor(n):
        return int(n)
    else:
        return None
