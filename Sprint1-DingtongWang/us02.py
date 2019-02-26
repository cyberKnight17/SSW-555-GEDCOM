from datetime import datetime


def birth_before_marriage(ind, fam):  # us02
    res = True
    for f in fam:
        hus_id = "0"
        wife_id = "0"
        if 'MARR' in fam[f] and 'HUSB' in fam[f] and 'WIFE' in fam[f]:
            hus_id = fam[f]['HUSB']
            wife_id = fam[f]['WIFE']
            marr_date = datetime.strptime(fam[f]['MARR'],"%d%b%Y")
        if hus_id in ind:
            if marr_date < datetime.strptime(ind[hus_id]['BIRT'],"%d%b%Y"):
                print('ERROR:US02,%s:%s birth date %d happened after marrige %d'%\
                     (fam[f]['MARR_REC'],ind[hus_id],ind[hus_id]['BIRT'],ind[hus_id]['MARR']))
                res=False
        if wife_id in ind:
            if marr_date < datetime.strptime(ind[wife_id]['BIRT'],"%d%b%Y"):
                print('ERROR:US02,%s:%s birth date %d happened beofore marrige %d'%\
                     (fam[f]['MARR_REC'],ind[wife_id],ind[wife_id]['BIRT'],ind[wife_id]['MARR']))
                res=False
    return res

