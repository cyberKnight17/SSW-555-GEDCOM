    
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
                table.add_row([person["id"], person["name"], person["DEAT"]])
                isThereRecentDeath = True
    print("Individuals dead in last 30 days.\n",table)
    return isThereRecentDeath #return a boolean value for test