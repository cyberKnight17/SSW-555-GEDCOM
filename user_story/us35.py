import unittest
#from prettytable import PrettyTable 
#import re
from datetime import datetime, timedelta

def print_recent_births(ind):
    """" US35 Print births in the last 30 days in pretty table(optional)
    """
    people = ind #<-- this is just ind
    #table = PrettyTable(["ID", "Name", "Birthdate"])
    isThereRecentBirth = False

    for person_id in ind:
        person = ind[person_id] 
        recent_date = datetime.today() - timedelta(days=30)
        
        if "BIRT" in person:
            birth_date = datetime.strptime(person["BIRT"], '%d%b%Y')
            if recent_date < birth_date and birth_date < datetime.now():
               #table.add_row([person["id"], person["name"], person["BIRT"]]) 
               isThereRecentBirth = True 
               result = f'At line {person["BIRT_rec"]}:US35:The individual {person["id"]} was recently born.'
               print(result)

    return isThereRecentBirth

ind = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL1960','BIRT_rec':'1222', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013'},
        'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '21MAR2019','BIRT_rec':'12', 'sex': 'F', 'family': 'F23'},
        'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1981','sex': 'M', 'family': 'F23','BIRT_rec':'1422'},
        'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13FEB1981','BIRT_rec':'15', 'sex': 'F', 'family': 'F23'},
        'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13FEB1981', 'BIRT_rec':'1222','sex': 'F', 'family': 'F12'},
        'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13FEB1981','BIRT_rec':'1222','sex': 'M', 'family': 'F12'},
        'I43': {'id': 'I43', 'name': 'Extra /Person/', 'BIRT': '13FEB1981','sex': 'M','BIRT_rec':'1222', 'family': 'F23'},
        'I44': {'id': 'I44', 'name': 'Extra /Person2/', 'BIRT': '13FEB1981','sex': 'F', 'BIRT_rec':'1222','family': 'F16'},
        'I45': {'id': 'I44', 'name': 'Extra /Person3/', 'BIRT': '13FEB1981','sex': 'M', 'BIRT_rec':'1222','family': 'F16'}}
fam = {'F23': {'fam': 'F23', 'MARR': '14FEB1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30', 'I32', 'I43']},
         'F16': {'fam': 'F16', 'MARR': '12DEC2007','HUSB': 'I45', 'WIFE': 'I44'},
         'F12': {'fam': 'F12', 'MARR': '12DEC2008','DIV':'12DEC2001','HUSB': 'I32', 'WIFE': 'I30'}}


class MyTest(unittest.TestCase):
    def test(self):
        self.assertTrue(print_recent_births(ind))

if __name__ == '__main__':
    unittest.main()
