import unittest
from sprint01 import birth_before_death as us03
ind1 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL2015', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013'},
		'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23SEP1960', 'sex': 'F', 'family': 'F23', 'DEAT': '31DEC2013'},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1999','sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013'}
}

ind2={'I01': 
{'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013'}
}

ind3 ={'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1998', 'sex': 'F', 'family': 'F23'},
		'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 2000', 'sex': 'F', 'family': 'F12'},
		'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 2010','sex': 'M', 'family': 'F12'},
		'I43': {'id': 'I43', 'name': 'Extra /Person/', 'BIRT': '13 FEB 1997','sex': 'M', 'family': 'F23'},
		'I44': {'id': 'I44', 'name': 'Extra /Person2/', 'BIRT': '13 FEB 2005','sex': 'F', 'family': 'F16'},
		'I45': {'id': 'I44', 'name': 'Extra /Person3/', 'BIRT': '13 FEB 2003','sex': 'M', 'family': 'F16'}
        }
ind4 ={'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F23'},
		'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
		'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F12'},
		'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F12'},
		'I43': {'id': 'I43', 'name': 'Extra /Person/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F23'},
		'I44': {'id': 'I44', 'name': 'Extra /Person2/', 'BIRT': '13 FEB 1981','sex': 'F', 'family': 'F16'},
		'I45': {'id': 'I44', 'name': 'Extra /Person3/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F16'}}

ind5 ={'I01': 
{'id': 'I01', 'name': 'Joe /Smith/', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013'}
}
class Test_US03(unittest.TestCase):
    def test_birth_before_death(self):
        self.assertFalse(us03(ind1))
        self.assertTrue(us03(ind2))

    def no_death(self):
        self.assertTrue(ind3)
        self.assertTrue(ind4)

    def no_birth(self):
        self.assertTrue(ind5)


if __name__ == '__main__':
    unittest.main()