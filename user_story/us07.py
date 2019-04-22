from datetime import datetime


def less_than_150_years_old(ind):
    """Death should be less than 150 years after birth for dead people, and current date should be less than 150 years
        after birth for all living people"""
    res = True
    for id in ind.keys() :
        current = datetime.today()
        if 'BIRT' in ind[id]:
            birth = datetime.strptime(ind[id]['BIRT'],"%d%b%Y")
            age = (current - birth).days/365
            if 'DEAT' in ind[id]:
                death = datetime.strptime(ind[id]['DEAT'],"%d%b%Y")
                age = (death - birth).days/365
            if age > 150:
                res = False
                print('Error: INDIVIDUAL: US07：%s: %s is more than 150 years old'% (ind[id]['indi_rec'],ind[id]['id']))

    return res