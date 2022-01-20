""" Problem 55: Lychrel Numbers

https://projecteuler.net/problem=55

Goal: Given N, find the palindrome to which the maximum positive numbers <= N
converge if non-Lychrel and return both the palindrome and the max_count.

Constraints: 100 <= N <= 1e5

Lychrel Number: A number that, theoretically, never produces a palindrome through
the reverse and add process shown below.
e.g. 349 + 943 = 1292
     1292 + 2921 = 4213
     4213 + 3124 = 7337, a palindrome in 3 iterations.

So far, 10677 is the 1st number shown to require over 50 iterations to produce a
palindrome (in 53 iterations it produces a 28-digit palindrome). All numbers less
than 10677 will either become a palindrome in under 50 iterations or have not been
proven to not be Lychrel, e.g. 196.

Note that palindromic numbers can themselves be Lychrel numbers, e.g. 4994,
but, for this problem, it is assumed that palindromes are non-Lychrel in the 0th
iteration.

e.g.: N = 130
      palindrome = 121
      18 numbers <= 121 converge -> [19, 28, 29, 37, 38, 46, 47, 56, 64, 65, 73,
      74, 82, 83, 91, 92, 110, 121]
"""
from util.strings.reusable import is_palindrome


def max_palindrome_convergence(n: int) -> (int, int):
    palindromes = dict()
    visited = set()
    limit = 50 if n < 10677 else 60
    for i in range(1, n + 1):
        num = i
        if num in visited:
            continue
        iteration = 0
        nums = set()
        while iteration < limit:
            if num <= n:
                nums.add(num)
            if is_palindrome(str(num)):
                visited = visited.union(nums)
                if num in palindromes.keys():
                    palindromes[num] = palindromes[num].union(nums)
                else:
                    palindromes[num] = nums
                break
            iteration += 1
            reverse_num = str(num)[::-1]
            if reverse_num[0] > "0" and int(reverse_num) <= n:
                nums.add(int(reverse_num))
            num += int(reverse_num)
    palindrome = max(palindromes.keys(), key=lambda k: len(palindromes[k]))
    return palindrome, len(palindromes[palindrome])


def count_lychrel_numbers() -> int:
    """
    Project Euler specific implementation that counts Lychrel numbers < 1e5.

    Storing visited numbers in a set that is checked before cycling through
    iterations prevents unnecessary steps. e.g. If 19 converges to a palindrome,
    so will 91.
    """

    count = 0
    visited = set()
    for n in range(1, 10_000):
        num = n
        if num in visited:
            continue
        iteration = 0
        is_lychrel = True
        nums = set()
        while iteration < 50:
            nums.add(num)
            reverse_num = str(num)[::-1]
            if reverse_num[0] > "0":
                nums.add(int(reverse_num))
            num += int(reverse_num)
            if is_palindrome(str(num)):
                is_lychrel = False
                visited = visited.union(nums)
                break
            iteration += 1
        count += is_lychrel
    return count


if __name__ == '__main__':
    print(max_palindrome_convergence(130))
