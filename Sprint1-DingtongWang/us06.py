from datetime import datetime


def divorce_before_death(ind,fam):
    res = True
    for f in fam:
        hus_id = "0"
        wife_id = "0"

        if 'DIV' in fam[f] and 'HUSB' in fam[f] and 'WIFE' in fam[f]:
            hus_id = fam[f]['HUSB']
            wife_id = fam[f]['WIFE']
            div_date = datetime.strptime(fam[f]['DIV'],"%d%b%Y")

            if hus_id in ind:
                if 'DEAT' not in ind[hus_id]:
                    res = True
                else:
                    if div_date > datetime.strptime(ind[hus_id]['DEAT'],"%d%b%Y"):
                        print('ERROR:US06,%s:%s divorce date %s happened after death %s'%\
                             (fam[f]['DIV_rec'],ind[hus_id],ind[hus_id]['BIRT'],ind[hus_id]['DEAT']))
                        res = False

            if wife_id in ind:
                if 'DEAT' not in ind[wife_id]:
                    res = True
                else:
                    if div_date > datetime.strptime(ind[wife_id]['DEAT'],"%d%b%Y"):
                        print('ERROR:US06,%s:%s divorce date %s happened after death %s'%\
                             (fam[f]['DIV_rec'],ind[wife_id],ind[wife_id]['BIRT'],ind[wife_id]['DEAT']))
                        res = False

    return res

