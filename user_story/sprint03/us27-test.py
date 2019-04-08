import unittest
from datetime import datetime
from us27 import age_cal as us27


birthday1 = '14FEB2015'
birthday2 = '14NOV2000'
birthday3 = '14MAR2019'


class Test_US27(unittest.TestCase):
    def test_age_cal(self):
        self.assertEqual(us27(birthday1), 4)
        self.assertEqual(us27(birthday2), 18)
        self.assertEqual(us27(birthday3), 0)

if __name__ == '__main__':
    unittest.main()
