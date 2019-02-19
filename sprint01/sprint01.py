from datetime import datetime

def birth_before_death(indi): #us03
    res = True

    for i in indi:
        if "BIRT" in indi[i] and "DEAT" in indi[i]:
            birthday = datetime.strptime(indi[i]["BIRT"],'%d%b%Y')
            deathday = datetime.strptime(indi[i]['DEAT'],'%d%b%Y')
    
            if birthday > deathday:
                warnin = 'ERROR death of individual %s comes before birth.' %i
                print(warnin)
                #file.write(warnin)
                res = False

    return res





