import unittest
from userstory04 import *
from datetime import datetime

# fam=parse_file('C:\\Users\\woshi\\PycharmProjects\\untitled1\Teamproject\My-Family-27-Jan-2019-230.ged')
# print(fam)
# fam1={'F1': {'fam': 'F1', 'HUSB': 'I2', 'WIFE': 'I3', 'CHIL': ['I1']}}
# fam2={'F2': {'fam': 'F2', 'HUSB': 'I4', 'WIFE': 'I5', 'CHIL': ['I2', 'I6', 'I8']}}
# fam3={'F3': {'fam': 'F3', 'HUSB': 'I6', 'WIFE': 'I7', 'MARR': '14AUG1985'}}
# fam4={'F4': {'fam': 'F4', 'HUSB': 'I13', 'WIFE': 'I7', 'MARR': '15SEP2005'}}
# fam5={'F5': {'fam': 'F5', 'HUSB': 'I8', 'WIFE': 'I10', 'CHIL': ['I11'], 'MARR': '7AUG2008'}}
# fam6={'F6': {'fam': 'F6', 'HUSB': 'I8', 'WIFE': 'I9', 'CHIL': ['I12'], 'MARR': '8JUL1994', 'DIV': '14NOV2001'}}

FAM = {'fam': {'F1': {'fam': 'F1', 'HUSB': 'I2', 'WIFE': 'I3', 'CHIL': ['I1']},
               'F2': {'fam': 'F2', 'HUSB': 'I4', 'WIFE': 'I5', 'CHIL': ['I2', 'I6', 'I8']},
               'F3': {'fam': 'F3', 'HUSB': 'I6', 'WIFE': 'I7', 'MARR': '14AUG1985'},
               'F4': {'fam': 'F4', 'HUSB': 'I13', 'WIFE': 'I7', 'MARR': '15SEP2005'},
               'F5': {'fam': 'F5', 'HUSB': 'I8', 'WIFE': 'I10', 'CHIL': ['I11'], 'MARR': '7AUG2008'},
               'F6': {'fam': 'F6', 'HUSB': 'I8', 'WIFE': 'I9', 'CHIL': ['I12'], 'MARR': '8JUL1994',
                      'DIV': '14NOV2001'}},
       'indi': {'I1': {'id': 'I1', 'name': 'Sam/Smith/', 'sex': 'M', 'BIRT': '9JAN1980', 'family': 'F1'},
                'I2': {'id': 'I2', 'name': 'Mike/Smith/', 'sex': 'M', 'BIRT': '7OCT1965', 'family': 'F2'},
                'I3': {'id': 'I3', 'name': 'Mary/Smith/', 'sex': 'F', 'BIRT': '13JUL1966', 'family': 'F1'},
                'I4': {'id': 'I4', 'name': 'Jordan/Smith/', 'sex': 'M', 'BIRT': '28SEP1939', 'family': 'F2'},
                'I5': {'id': 'I5', 'name': 'Alice/Smith/', 'sex': 'F', 'BIRT': '15JUN1943', 'DEAT': '7SEP2009',
                       'family': 'F2'},
                'I6': {'id': 'I6', 'name': 'Will/Smith/', 'sex': 'M', 'BIRT': '7OCT1963', 'DEAT': '11APR2002',
                       'family': 'F2'},
                'I7': {'id': 'I7', 'name': 'Jane/Forrest/', 'sex': 'F', 'BIRT': '24JAN1963', 'family': 'F4'},
                'I8': {'id': 'I8', 'name': 'Chris/Smith/', 'sex': 'M', 'BIRT': '19JUN1970', 'family': 'F2'},
                'I9': {'id': 'I9', 'name': 'Julie/Swift/', 'sex': 'F', 'BIRT': '25MAR1972', 'family': 'F6'},
                'I10': {'id': 'I10', 'name': 'Fiona/Gibson/', 'sex': 'F', 'BIRT': '24MAY1974', 'family': 'F5'},
                'I11': {'id': 'I11', 'name': 'Curry/Smith/', 'sex': 'M', 'BIRT': '12OCT2010', 'family': 'F5'},
                'I12': {'id': 'I12', 'name': 'Brown/Smith/', 'sex': 'M', 'BIRT': '8SEP1997', 'family': 'F6'},
                'I13': {'id': 'I13', 'name': 'Paul/Pierce/', 'sex': 'M', 'BIRT': '24NOV1960', 'family': 'F4'}}}
MARR_date = {'MARR': {'14AUG1985', '15SEP2005', '7AUG2008', '8JUL1994'}}
DIV_date = {'DIV': {'14NOV2001'}}


class US04_Function(unittest.TestCase):
    # test porject03.py

    def test_Validation_check04(self):
        self.assertTrue(Marrige_before_Divorce(FAM))
        self.assertEqual(True,Marrige_before_Divorce(FAM))
        self.assertNotEqual(False,Marrige_before_Divorce(FAM))

    def test_marrigedateget(self):
        self.assertEqual(datetime(1985, 8, 14).date(), Marrige_date_get(FAM))

    def test_divorcedateget(self):
       self.assertEqual(datetime(2001, 11, 14).date(), Divorce_date_get(FAM))


if __name__ == '__main__':
    unittest.main(verbosity=1)
