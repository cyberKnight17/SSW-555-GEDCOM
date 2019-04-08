import unittest
import os,sys
s = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(s)
from pair_programming import us09,us22

fam = {'F23':
  {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
   'F23': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
 'I01': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}

fam1 = {
    'F23':{'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
    'F24': {'fam': 'F23', 'MARR': '12 DEC 2007'},
    'F25':{'fam':'F23'},
    'F26':{'fam':'F23'}}

ind1 = {
'I02': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'}, 
'I03': {'id': 'I01', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
'I04': {'id': 'I01', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
'I01': {'id': 'I01', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
'I01': {'id': 'I01', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
'I01': {'id': 'I01', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
'I01': {'id': 'I01', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}
  }
class Testus22us09(unittest.TestCase):
    def test_same_id(self):
        self.assertTrue(us22.unique_id(ind,fam))
        self.assertEqual(us22.unique_id(ind,fam),True)
        self.assertEqual(us22.unique_id(ind1,fam1),False)

    def test_birth_after_pdeath(self):
        self.assertEqual(us09.birth_before_parents_death("Ralph /Doe/", "I01", "20JUN1993", "20JUL1985",True),\
            "ERROR Us09: Birthday of child I01 Ralph /Doe/ is after their mother's death.\n")
        self.assertEqual(us09.birth_before_parents_death("Ralph /Doe/", "I01", "20JUN1993", "20JUL2030", False), None)






if __name__ == '__main__':
    unittest.main()