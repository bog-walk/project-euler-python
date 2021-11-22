""" Problem 21: Amicable Numbers

https://projecteuler.net/problem=21

Goal: Return the sum of all amicable numbers less than N.

Constraints: 1 <= N <= 1e5

Proper Divisor: A number x that evenly divides N, where x != N.

Amicable Number: A number X that has a pair Y, where X != Y but
d(X) = Y && d(Y) = X, with d(N) = sum{proper divisors of N}.

e.g.: N = 300
      amicable pairs = [{220, 284}]; since
      d(220) = sum{1,2,4,5,10,11,20,22,44,55,110} = 284
      d(284) = sum{1,2,4,71,142} = 220
      sum = 220 + 284 = 504
"""
from util.reusable import sum_proper_divisors


def sum_amicable_pairs(n):
    amicable_nums = []
    for x in range(2, n):
        y = sum_proper_divisors(x)
        # The partner of a newly explored amicable number must be larger
        if y > x and sum_proper_divisors(y) == x:
            amicable_nums.append(x)
            # Account for possibility that only 1 of the amicable pair
            # may be under N
            if y < n:
                amicable_nums.append(y)
            else:
                break
    return sum(amicable_nums)
