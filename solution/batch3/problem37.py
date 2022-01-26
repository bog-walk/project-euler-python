""" Problem 37: Truncatable Primes

https://projecteuler.net/problem=37

Goal: Find the sum of all primes less than N that are truncatable both from left
to right and from right to left (single-digit primes are not considered).

Constraints: 100 <= N <= 1e6

Truncatable Prime: A prime that remains prime as digits are continuously removed
from LTR or RTL.
e.g. 3797 -> 797 -> 97 -> 7 and 3797 -> 379 -> 37 -> 3

e.g.: N = 50
      truncatable primes = {23, 37}
      sum = 60
"""
from util.maths.reusable import prime_numbers
from util.search.reusable import binary_search


def sum_of_trunc_primes(n: int) -> int:
    """
    Solution speed optimised based on the following:

    -   There are only 11 such qualifying numbers.

    -   A number must start and end with a single-digit prime.

    -   No point in considering double-digit primes less than 23.

    -   Above 100, pattern shows that qualifying numbers must start and end in a 3
        or 7.

    -   Above 1000, pattern shows that qualifying numbers must have their first &
        last 3 digits be a prime number.
    
    -   No need to check first & last digits again in final loop.

    -   A binary search algorithm is used to check the primes list.
    """

    primes = prime_numbers(n - 1)
    singles_a = "2357"
    singles_b = "37"
    total = 0
    count = 0
    for prime in primes[8:]:
        p = str(prime)
        digits = len(p)
        if digits == 2:
            if p[:1] not in singles_a or p[-1:] not in singles_a:
                continue
        else:
            if p[:1] not in singles_b or p[-1:] not in singles_b:
                continue
            if digits >= 4:
                if not binary_search(int(p[:3]), primes) or \
                        not binary_search(int(p[-3:]), primes):
                    continue
        valid = True
        if digits > 2:
            for i in range(2, digits):
                if not binary_search(int(p[:i]), primes) or \
                        not binary_search(int(p[-i:]), primes):
                    valid = False
                    break
        if valid:
            total += prime
            count += 1
        if count == 11:
            break
    return total
