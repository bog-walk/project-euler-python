import unittest
from solution.batch6.problem51 import smallest_prime_digit_repl, \
    smallest_8_prime_family


class PrimeDigitReplacements(unittest.TestCase):
    def test_smallest_prime_digit_repl_a(self):
        n, k, length = 2, 1, 3
        expected = [11, 13, 17]
        self.assertListEqual(
            expected,
            smallest_prime_digit_repl(n, k, length)
        )

    def test_smallest_prime_digit_repl_b(self):
        n, k, length = 2, 1, 6
        expected = [13, 23, 43, 53, 73, 83]
        self.assertListEqual(
            expected,
            smallest_prime_digit_repl(n, k, length)
        )

    def test_smallest_prime_digit_repl_c(self):
        n, k, length = 5, 2, 7
        expected = [56003, 56113, 56333, 56443, 56663, 56773, 56993]
        self.assertListEqual(
            expected,
            smallest_prime_digit_repl(n, k, length)
        )

    def test_smallest_prime_digit_repl_d(self):
        n, k, length = 6, 3, 8
        expected = [
            121313, 222323, 323333, 424343, 525353, 626363, 828383, 929393
        ]
        self.assertListEqual(
            expected,
            smallest_prime_digit_repl(n, k, length)
        )

    def test_smallest_prime_digit_repl_e(self):
        n, k, length = 5, 1, 2
        expected = [10007, 10009]
        self.assertListEqual(
            expected,
            smallest_prime_digit_repl(n, k, length)
        )

    def test_smallest_prime_digit_repl_f(self):
        n, k, length = 3, 2, 1
        expected = [101]
        self.assertListEqual(
            expected,
            smallest_prime_digit_repl(n, k, length)
        )

    def test_smallest_prime_digit_repl_g(self):
        n, k, length = 7, 4, 6
        expected = [
            2422027, 3433037, 5455057, 6466067, 8488087, 9499097
        ]
        self.assertListEqual(
            expected,
            smallest_prime_digit_repl(n, k, length)
        )

    def test_smallest_8_prime_family(self):
        expected = 121313
        self.assertEqual(expected, smallest_8_prime_family())


if __name__ == '__main__':
    unittest.main()
