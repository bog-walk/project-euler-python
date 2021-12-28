import unittest
from solution.batch5.problem49 import prime_perm_sequence


class PrimePermutations(unittest.TestCase):
    def test_prime_perm_seq_4_digit(self):
        n = 10_000
        expected = ['148748178147', '296962999629']
        self.assertListEqual(expected, prime_perm_sequence(n, k=3))
        self.assertListEqual([], prime_perm_sequence(n, k=4))

    def test_prime_perm_seq_5_digit_low(self):
        n = 20_000
        expected = [
            '148748178147', '296962999629', '114831481318143', '114974171971941',
            '127131321713721', '127391723921739', '127571725721757', '127991729921799',
            '148214812181421', '148313148148131', '148974718979481', '185035180385103',
            '185935189385193', '195433549151439'
        ]
        self.assertListEqual(expected, prime_perm_sequence(n, k=3))
        self.assertListEqual([], prime_perm_sequence(n, k=4))

    def test_prime_perm_seq_5_digit_high(self):
        n = 100_000
        self.assertEqual(55, len(prime_perm_sequence(n, k=3)))
        expected = ['83987889379388798837']
        self.assertListEqual(expected, prime_perm_sequence(n, k=4))

    def test_prime_perm_seq_6_digit(self):
        n = 1_000_000
        self.assertEqual(15, len(prime_perm_sequence(n, k=4)))


if __name__ == '__main__':
    unittest.main()
