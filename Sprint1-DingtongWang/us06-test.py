import unittest
from us06 import divorce_before_death as us06


fam1 = {'F23':
	{'fam': 'F23', 'DIV': '14FEB2015', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30'],'DEAT_rec': '1'}}
ind1 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23SEP1960', 'sex': 'F', 'family': 'F23', 'DEAT': '31DEC2013'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13FEB1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'}}

fam2 = {'F23':
	{'fam': 'F23', 'DIV': '14FEB1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30'],'DEAT_rec': '1'}}
ind2 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23SEP1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13FEB1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'}}

fam3 = {'F23':
	{'fam': 'F23', 'MARR': '14FEB1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30'],'DEAT_rec': '1'}}
ind3 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13FEB1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'}}

fam4 = {'F23':
	{'fam': 'F23', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30'],'DEAT_rec': '1'}}
ind4 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL1960', 'sex': 'M', 'family': 'F23'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23SEP1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13FEB1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'}}


class Test_US06(unittest.TestCase):
    def test_divorce_before_death(self):
        self.assertFalse(us06(ind1, fam1))
        self.assertTrue(us06(ind2, fam2))

    def test_no_divorce(self):
        self.assertTrue(us06(ind3, fam3))

    def test_no_death(self):
        self.assertTrue(us06(ind4, fam4))


if __name__ == '__main__':
    unittest.main()
