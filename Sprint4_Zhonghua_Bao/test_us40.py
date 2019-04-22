import unittest
from US40 import parse_file

class UserStory40Test(unittest.TestCase):
    def test_userStory40(self):
        r = parse_file('us40-test.ged')
        expect = {'fam': {'F1': {'fam': 'F1', 'fam_rec': 24, 'CHIL': {'I1'}}}, 
                  'indi': {'I1': {'id': 'I1', 'indi_rec': 15, 'name': 'Sam/Smith/', 'name_rec': 16, 'sex': 'M', 'sex_rec': 20, 'BIRT': '9JAN1980', 'BIRT_rec': 22, 'FAMC': {'F1'}}}
                 }
        self.assertEqual(r,expect)

if __name__ == '__main__':
    unittest.main(verbosity=2) 