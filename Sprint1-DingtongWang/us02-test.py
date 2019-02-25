import unittest
from us02 import birth_before_marriage as us02


ind1 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'sex': 'M', 'family': 'F23',
				'BIRT': '31DEC2013', 'MARR': '31DEC2014'},
		'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23SEP1960', 'sex': 'F', 'family': 'F23',
				'BIRT': '31JAN2013', 'MARR': '31DEC2013'},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1999','sex': 'M', 'family': 'F23',
				'BIRT': '30DEC2013', 'MARR': '31DEC2013'}}

ind2 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'sex': 'M', 'family': 'F23',
				'BIRT': '31DEC2013', 'MARR': '31DEC2000'},
		'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'sex': 'F', 'family': 'F23',
				'BIRT': '31JAN2013', 'MARR': '31DEC2013'},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/','sex': 'M', 'family': 'F23',
				'BIRT': '30DEC2013', 'MARR': '31DEC2013'}}

ind3 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'sex': 'M', 'family': 'F23',
				'BIRT': '31DEC2013', 'MARR': '31DEC2000'},
		'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'sex': 'F', 'family': 'F23',
				'BIRT': '30NOV2013', 'MARR': '30JAN2013'},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/','sex': 'M', 'family': 'F23',
				'BIRT': '30DEC2013', 'MARR': '1DEC2013'}}

ind4 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'sex': 'M', 'family': 'F23',
				'MARR': '31DEC2000'},
		'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'sex': 'F', 'family': 'F23',
				'MARR': '30JAN2013'},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/','sex': 'M', 'family': 'F23',
				'MARR': '1DEC2013'}}

ind5 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'sex': 'M', 'family': 'F23',
				'BIRT': '31DEC2013'},
		'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'sex': 'F', 'family': 'F23',
				'BIRT': '30NOV2013'},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/','sex': 'M', 'family': 'F23',
				'BIRT': '30DEC2013'}}



class Test_US02(unittest.TestCase):
    def birth_before_marriage(self):
        self.assertFalse(us02(ind1))
        self.assertFalse(us02(ind2))
        self.assertTrue(us02(ind3))

    def no_birth(self):
        self.assertTrue(ind4)

    def no_marriage(self):
        self.assertTrue(ind5)


if __name__ == '__main__':
    unittest.main()
