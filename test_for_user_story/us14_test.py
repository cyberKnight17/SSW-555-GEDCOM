import unittest
from us14 import mutible_birth as us14


fam1 = {'F23':{'fam': 'F23', 'DIV': '14FEB2015', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30', 'I1', 'I2', 'I3'
        'I4','I5', 'I6', 'I7', 'I8', 'I9','I10', 'I11', 'I12', '13', '14', '15'],'DEAT_rec': '1'}}
ind1 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013'},
 'I19': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '15JUL1960', 'sex': 'F', 'family': 'F23', 'DEAT': '31DEC2013'},
 'I26': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '15JUL1960', 'sex': 'M', 'family': 'F23'},
  'I30': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '15JUL1960', 'sex': 'F', 'family': 'F23'},
  'I1': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '15JUL1960', 'sex': 'F', 'family': 'F23'},
  'I2': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '15JUL1960', 'sex': 'M', 'family': 'F23'},
  'I3': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '15JUL1960', 'sex': 'F', 'family': 'F23'},
'I4': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '15JUL1960', 'sex': 'F', 'family': 'F23'},
'I5': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '15JUL1960', 'sex': 'F', 'family': 'F23'},
'I6': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '15JUL1960', 'sex': 'F', 'family': 'F23'},
'I7': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '15JUL1960', 'sex': 'F', 'family': 'F23'},}

fam2 = {'F23':
	{'fam': 'F23', 'DIV': '14FEB1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30'],'DEAT_rec': '1'}}
ind2 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23SEP1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13FEB1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'}}


class Test_US14(unittest.TestCase):
    def test_mutible_birth(self):
        self.assertFalse(us14(ind1, fam1))
        self.assertTrue(us14(ind2, fam2))

if __name__ == '__main__':
    unittest.main()
