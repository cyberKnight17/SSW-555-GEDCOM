import unittest
from us07 import less_than_150_years_old as us07

ind1 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23SEP1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13FEB1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'}}

ind2 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL1700', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23SEP1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13FEB1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'}}


class Test_US07(unittest.TestCase):
    def test_less_than_150_years_old(self):
        self.assertTrue(us07(ind1))
        self.assertFalse(us07(ind2))


if __name__ == '__main__':
    unittest.main()
