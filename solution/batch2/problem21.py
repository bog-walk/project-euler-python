""" Problem 21: Amicable Numbers

https://projecteuler.net/problem=21

Goal: Return the sum of all amicable numbers less than N.

Constraints: 1 <= N <= 1e5

Proper Divisor: A number x that evenly divides N, where x != N.

Amicable Number: A number X that has a pair Y, where X != Y but
d(X) = Y && d(Y) = X, with d(N) = sum(proper divisors of N).
First amicable pairs = {(220, 284), (1184, 1210), (2620, 2924)}

e.g.: N = 300
      amicable pairs = [{220, 284}]; since
      d(220) = sum{1,2,4,5,10,11,20,22,44,55,110} = 284
      d(284) = sum{1,2,4,71,142} = 220
      sum = 220 + 284 = 504
"""
from util.maths.reusable import sum_proper_divisors_og


def sum_amicable_pairs(n: int) -> int:
    """ Sums amicable numbers < n even if larger pair-member is >= n. """

    amicable_nums = []
    for x in range(2, n):
        y = sum_proper_divisors_og(x)
        # the partner of a newly explored amicable number must be larger
        if y > x and sum_proper_divisors_og(y) == x:
            amicable_nums.append(x)
            # account for possibility that only 1 of the amicable pair
            # may be under N
            if y < n:
                amicable_nums.append(y)
            else:
                # future pairs will be > N
                break
    return sum(amicable_nums)
