    
import unittest
from prettytable import PrettyTable
from datetime import datetime, timedelta

def us36(indi):
    """" US36 Print deaths in the last 30 days in pretty table
        """
    isThereRecentDeath =False
    table = PrettyTable(["ID", "Name", "Deathdate"])

    for person_id in indi:
        person = indi[person_id]
        recent_date = datetime.today() - timedelta(days=30)

        if "DEAT" in person:
            death_date = datetime.strptime(person["DEAT"], '%d%b%Y') 
            if recent_date < death_date and death_date < datetime.now():
                table.add_row([person["id"], person["name"], death_date])
                isThereRecentDeath = True
    print("Individuals dead in last 30 days.\n",table)
    return isThereRecentDeath #return a boolean value for test

ind = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL1960', 'sex': 'M', 'family': 'F23', 'DEAT': '18APR2019'},
        'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23SEP1960', 'sex': 'F', 'family': 'F23'},
        'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1981','sex': 'M', 'family': 'F23'},
        'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'},
        'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F12'},
        'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13FEB1981','sex': 'M', 'family': 'F12'},
        'I43': {'id': 'I43', 'name': 'Extra /Person/', 'BIRT': '13FEB1981','sex': 'M', 'family': 'F23'},
        'I44': {'id': 'I44', 'name': 'Extra /Person2/', 'BIRT': '13FEB1981','sex': 'F', 'family': 'F16'},
        'I45': {'id': 'I44', 'name': 'Extra /Person3/', 'BIRT': '13FEB1981','sex': 'M', 'family': 'F16'}}

class MyTest(unittest.TestCase):
    def test(self):

        self.assertTrue(us36(ind))
    
if __name__ == '__main__':
    unittest.main()