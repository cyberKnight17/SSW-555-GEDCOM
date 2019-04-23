import unittest
from us42 import dateVerify, userStory42
from main import parse_file


class UserStory42Test(unittest.TestCase):
    def test_userStory42(self):
        r = parse_file('us40-test.ged')
        expect = []
        self.assertEqual(expect, userStory42(r))

    def test_dateVerify(self):
        self.assertTrue(dateVerify('1JAN2015'))
        self.assertTrue(dateVerify('31MAR2017'))
        self.assertTrue(dateVerify('29FEB2016'))
        self.assertFalse(dateVerify('30FEB2018'))
        self.assertFalse(dateVerify('31APR2014'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
