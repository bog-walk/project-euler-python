import unittest
from util.tests.reusable import get_test_resource
from solution.batch7.problem79 import derive_passcode


class PasscodeDerivation(unittest.TestCase):
    def test_HR_problem_with_invalid_passcodes(self):
        logins = [["an0", "n/.", ".#a"], ["123", "231"]]
        for login in logins:
            self.assertIsNone(derive_passcode(login))

    def test_HR_problem_with_valid_passcodes(self):
        logins = [
            ["abc"], ["SMH", "TON", "RNG", "WRO", "THG"],
            ["@<!", "@!3", "<R3", "@!R", "<!3", "@R3"]
        ]
        expected = ["abc", "SMTHWRONG", "@<!R3"]
        for login, e in zip(logins, expected):
            self.assertEqual(e, derive_passcode(login))

    def test_PE_problem_with_50_login_attempts(self):
        # remove duplicate strings in test resource
        logins = list(set(get_test_resource("../resources/passcode_derivation.txt")))
        expected = "73162890"
        self.assertEqual(expected, derive_passcode(logins))


if __name__ == '__main__':
    unittest.main()
