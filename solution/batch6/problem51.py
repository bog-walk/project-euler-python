""" Problem 51: Prime Digit Replacements 

https://projecteuler.net/problem=51

Goal: Find the smallest N-digit prime which, by replacing
K digits of the number with the same digit, is part of an
L-prime value family at minimum. K digits are not necessarily
adjacent & leading zeroes should not be considered.

Constraints: 2 <= N <= 7, 1 <= K <= N, and
             1 <= L <= 8

Prime value family: A set of prime numbers generated by
replacing the same digits with a new digit.
e.g. Replacing the 3rd & 4th digits of 56**3 ->
     {56003, 56113, 56333, 56443, 56663, 56773, 56993}

e.g.: N = 2, K = 1, L = 3
      replace 1 digit in 1* -> {11, 13, 17, 19}
      smallest 3-prime value family = {11, 13, 17}
"""
from itertools import combinations
from util.maths.reusable import prime_numbers, is_prime
from util.search.reusable import binary_search


def get_replacements(prime: str, n: int, max_d: str, k: int) -> list[list[int]]:
    """
    Returned list will not include original prime.
    """
    replaced = []
    replacements = []
    for i in range(n):
        digit = prime[i]
        if digit <= max_d and prime.count(digit) >= k and digit not in replaced:
            replaced.append(digit)
            for perm in combinations([i for i, d in enumerate(prime) if d == digit], k):
                matches = []
                for d in range(int(digit) + 1, 10):
                    match = list(prime)
                    for index in perm:
                        match[index] = str(d)
                    matches.append(int("".join(match)))
                replacements.append(matches)
    return replacements


def smallest_prime_digit_repl(n, k, length):
    primes = prime_numbers(pow(10, n) - 1)
    max_d = str(9 - length + 1)
    smallest = []
    for prime in primes:
        if prime < pow(10, n - 1):
            continue
        p = str(prime)
        generated = list(filter(
            lambda family: len(family) >= length - 1,
            [
                list(filter(lambda num: binary_search(num, primes), replacements))
                for replacements in get_replacements(p, n, max_d, k)
            ]
        ))
        if len(generated):
            smallest = [prime] + min(generated)[:length - 1]
            break
    return smallest


def smallest_prime_digit_repl_old(n, k, length):
    """
    Solution optimised by generating all N-digit primes first. The only digits
    that are replaced are those of a value less than the maximum required
    to generate L primes.
    """
    primes = prime_numbers(pow(10, n) - 1)
    max_d = str(9 - length + 1)
    smallest = []
    for prime in primes:
        if prime < pow(10, n - 1):
            continue
        p = str(prime)
        if k == 1:
            # loop backwards to create smallest primes first
            for i in range(len(p) - 1, -1, -1):
                digit = p[i]
                if digit <= max_d:
                    generated = list(
                        filter(
                            lambda num: binary_search(num, primes),
                            [int(p[:i] + str(d) + p[i+1:]) for d in range(int(digit) + 1, 10)]
                        )
                    )
                    if len(generated) >= length - 1:
                        smallest = [prime] + generated[:length - 1]
                        break
        else:
            multiples = []  # avoid duplicate generations
            for digit in p:
                if digit <= max_d and p.count(digit) == k and digit not in multiples:
                    multiples.append(digit)
                    generated = list(
                        filter(
                            lambda num: binary_search(num, primes),
                            [int(p.replace(digit, str(d))) for d in range(int(digit) + 1, 10)]
                        )
                    )
                    if len(generated) >= length - 1:
                        smallest = [prime] + generated[:length - 1]
                        break
        if len(smallest):
            break
    return smallest


def smallest_8_prime_family():
    """
    Project Euler specific implementation that requires the smallest
    prime that is part of an 8-prime value family to be returned. The
    amount of digits replaced is not specified, so all values of K should
    be attempted for numbers greater than 56009 (the next prime after 56003,
    which is the smallest prime to be in a 7-prime value family). Optimised
    by only replacing digits in {0, 1, 2} as anything greater would not
    be able to generate 7 more primes of greater value.
    """
    n = 56009
    while True:
        if is_prime(n):
            # replace single digits only
            num = str(n)
            for i in range(len(num)):
                digit = num[i]
                if digit <= "2":
                    generated = list(
                        filter(
                            is_prime,
                            [int(num[:i] + str(d) + num[i+1:]) for d in range(int(digit) + 1, 10)]
                        )
                    )
                    if len(generated) == 7:
                        return n
            # replace multiple digits only
            multiples = []  # avoid duplicate generations
            for digit in num:
                if digit <= "2" and num.count(digit) > 1 and digit not in multiples:
                    multiples.append(digit)
                    generated = list(
                        filter(
                            is_prime,
                            [int(num.replace(digit, str(d))) for d in range(int(digit) + 1, 10)]
                        )
                    )
                    if len(generated) == 7:
                        return n
        n += 2
