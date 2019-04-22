# List upcoming anniversaries
import datetime


def us39(fam, indi):
    # get married fam
    huslist = []
    wifelist = []
    couple = []
    for i in fam:
        if 'DIV' not in fam[i] and 'MARR' in fam[i]:
            marrydate = datetime.datetime.strptime(fam[i]['MARR'], '%d%b%Y')
            # print(marrydate)
            for x in range(30):
                comingday = (datetime.datetime.now() + datetime.timedelta(days=x))
                couplelist = []
                if comingday.month == marrydate.month and comingday.day == marrydate.day:
                    huslist.append(fam[i]['HUSB'])
                    wifelist.append(fam[i]['WIFE'])
                    couplelist.append(fam[i]['HUSB'])
                    couplelist.append(fam[i]['WIFE'])
                    couple.append(couplelist)

    for m in couple:
        for n in m:
            if 'DEAT' in indi[n]:
                couple.remove(m)
    ########list1 used to test#######
    list1 = []
    for v in couple:
        coupleidname = []
        for c in v:
            name = indi[c]['name']
            id = indi[c]['id']
            idname = id + ' ' + name
            coupleidname.append(idname)
        print('US39:', ' '.join(coupleidname),'are living couple whose marriage anniversaries occur in the next 30 days')
        list1.append(' '.join(coupleidname))
    return list1
