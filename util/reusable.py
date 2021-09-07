from math import gcd


def least_common_multiple(x, y):
    if x == 0 or y == 0:
        raise ValueError("The LCM of 0 is undefined")
    return abs(x * y) // gcd(x, y)
