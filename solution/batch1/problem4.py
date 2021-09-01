""" Problem 4: Largest Palindrome Product

https://projecteuler.net/problem=4

Goal: Find the largest palindrome less than N that is made from the
product of two 3-digit numbers.

Constraints: 101101 < N < 1000000

e.g.: N = 800000
      869 * 913 = 793397
"""


def is_palindrome(n):
    num = str(n)
    return num == num[::-1]


def is_palindrome_recursive(n):
    num = str(n)
    digits = len(num)
    if digits < 2:
        return True
    elif num[0] == num[digits - 1]:
        return is_palindrome_recursive(num[1:digits - 1])
    else:
        return False


def is_palindrome_no_cast(n):
    num = n
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return num == rev


def largest_palindrome_product(num):
    """ Tries all product combos that involve 1 of the integers being a multiple of 11.

    A palindrome of the product of two 3-digit integers must be 6-digits long &
    one of the integers must have a factor of 11, based on the following algebra:
    Palindrome = 100000x + 10000y + 1000z + 100z + 100y + x;
    Palindrome = 11 * (9091x + 910y + 100z).
    """
    largest = 0
    x = 999
    while x > 100:
        y = 999 if x % 11 == 0 else 990
        delta_y = 1 if x % 11 == 0 else 11
        while y >= x:
            product = y * x
            if product <= largest:
                # Combo will be too small to pursue
                break
            if product < num and is_palindrome(product):
                largest = product
            y -= delta_y
        x -= 1
    return largest
