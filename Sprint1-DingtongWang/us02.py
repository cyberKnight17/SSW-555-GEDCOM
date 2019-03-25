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
                if 'BIRT' not in ind[hus_id]:
                    res = True
                else:
                    if marr_date < datetime.strptime(ind[hus_id]['BIRT'],"%d%b%Y"):
                        print('ERROR:US02,%s:%s birth date %s happened after marriage %s'%\
                             (fam[f]['MARR_rec'],ind[hus_id],ind[hus_id]['BIRT'],fam[f]['MARR']))
                        res = False

            if wife_id in ind:
                if 'BIRT' not in ind[wife_id]:
                    res = True
                else:
                    if marr_date < datetime.strptime(ind[wife_id]['BIRT'],"%d%b%Y"):
                        print('ERROR:US02,%s:%s birth date %s happened before marriage %s'%\
                             (fam[f]['MARR_rec'],ind[wife_id],ind[wife_id]['BIRT'],fam[f]['MARR']))
                        res = False

    return res