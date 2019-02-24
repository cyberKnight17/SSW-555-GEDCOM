from datetime import datetime

def check_birth_death_marri(indi): #us03 and us05
    res = True

    for i in indi:
        if "BIRT" in indi[i] and "DEAT" in indi[i]:
            birthday = datetime.strptime(indi[i]["BIRT"],'%d%b%Y')
            deathday = datetime.strptime(indi[i]['DEAT'],'%d%b%Y')
            #marri_date = datetime.strptime(indi[i]['MARR'],'%d%b%Y')
    
            if birthday > deathday:
                warnin = 'ERROR death of individual %s comes before birth.' %i
                print(warnin)
                #file.write(warnin)
                res = False
        if "DEAT" in indi[i] and "MARR" in indi[i]:
            deathday = datetime.strptime(indi[i]['DEAT'],'%d%b%Y')
            marri_date = datetime.strptime(indi[i]['MARR'],'%d%b%Y')
            if marri_date > deathday:
                warnin = 'ERROR death of individual %s comes before marrige.' %i
                res = False
                print(warnin)

    return res

#ind1 = {'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13FEB1998', 'sex': 'F', 'family': 'F23','DEAT': '31DEC2013','MARR':'15MAR2016'},}

#s= check_birth_death_marri(ind1)




