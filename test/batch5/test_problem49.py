import unittest
from util.tests.reusable import compare_speed_seconds
from solution.batch5.problem49 import concat_prime_perms


class PrimePermutations(unittest.TestCase):
    def test_concat_prime_perms_4_digit(self):
        n = 10_000
        expected = ['148748178147', '296962999629']
        self.assertListEqual(expected, concat_prime_perms(n, k=3, improved=False))
        self.assertListEqual([], concat_prime_perms(n, k=4, improved=False))
        self.assertListEqual(expected, concat_prime_perms(n, k=3, improved=True))
        self.assertListEqual([], concat_prime_perms(n, k=4, improved=True))

    def test_concat_prime_perms_5_digit_low(self):
        n = 20_000
        expected = [
            '148748178147', '296962999629', '114831481318143', '114974171971941',
            '127131321713721', '127391723921739', '127571725721757', '127991729921799',
            '148214812181421', '148313148148131', '148974718979481', '185035180385103',
            '185935189385193', '195433549151439'
        ]
        self.assertListEqual(expected, concat_prime_perms(n, k=3, improved=False))
        self.assertListEqual(expected, concat_prime_perms(n, k=3, improved=True))
        self.assertListEqual([], concat_prime_perms(n, k=4, improved=False))
        self.assertListEqual([], concat_prime_perms(n, k=4, improved=True))

    def test_concat_prime_perms_5_digit_high(self):
        n = 100_000
        self.assertEqual(55, len(concat_prime_perms(n, k=3, improved=False)))
        self.assertEqual(55, len(concat_prime_perms(n, k=3, improved=True)))
        expected = ['83987889379388798837']
        self.assertListEqual(expected, concat_prime_perms(n, k=4, improved=False))
        self.assertListEqual(expected, concat_prime_perms(n, k=4, improved=True))

    def test_concat_prime_perms_speed(self):
        n, k = 1_000_000, 3
        solutions = {
            "Built-in": [concat_prime_perms, n, k, False],
            "Improved": [concat_prime_perms, n, k, True]
        }
        results = list(compare_speed_seconds(solutions, precision=2).values())
        self.assertListEqual(results[0], results[1])


if __name__ == '__main__':
    unittest.main()
