import unittest
from us06 import divorce_before_death as us02


# I reused my teammate's testcase
ind1 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL2015', 'sex': 'M', 'family': 'F23',
				'DEAT': '31DEC2013', 'DIV': '31DEC2014'},
		'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23SEP1960', 'sex': 'F', 'family': 'F23',
				'DEAT': '31JAN2013', 'DIV': '31DEC2013'},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1999','sex': 'M', 'family': 'F23',
				'DEAT': '30DEC2013', 'DIV': '31DEC2013'}}

ind2 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL2015', 'sex': 'M', 'family': 'F23',
				'DEAT': '31DEC2013', 'DIV': '31DEC2000'},
		'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23SEP1960', 'sex': 'F', 'family': 'F23',
				'DEAT': '31JAN2013', 'DIV': '31DEC2013'},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1999','sex': 'M', 'family': 'F23',
				'DEAT': '30DEC2013', 'DIV': '31DEC2013'}}

ind3 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL2015', 'sex': 'M', 'family': 'F23',
				'DEAT': '31DEC2013', 'DIV': '31DEC2000'},
		'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23SEP1960', 'sex': 'F', 'family': 'F23',
				'DEAT': '30NOV2013', 'DIV': '30JAN2013'},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1999','sex': 'M', 'family': 'F23',
				'DEAT': '30DEC2013', 'DIV': '1DEC2013'}}

ind4 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL2015', 'sex': 'M', 'family': 'F23',
				'DIV': '31DEC2000'},
		'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23SEP1960', 'sex': 'F', 'family': 'F23',
				'DIV': '30JAN2013'},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1999','sex': 'M', 'family': 'F23',
				'DIV': '1DEC2013'}}

ind5 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL2015', 'sex': 'M', 'family': 'F23',
				'DEAT': '31DEC2013'},
		'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23SEP1960', 'sex': 'F', 'family': 'F23',
				'DEAT': '30NOV2013'},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1999','sex': 'M', 'family': 'F23',
				'DEAT': '30DEC2013'}}



class Test_US06(unittest.TestCase):
    def test_birth_before_death(self):
        self.assertFalse(us02(ind1))
        self.assertFalse(us02(ind2))
        self.assertTrue(us02(ind3))

    def no_death(self):
        self.assertTrue(ind4)

    def no_birth(self):
        self.assertTrue(ind5)


if __name__ == '__main__':
    unittest.main()
