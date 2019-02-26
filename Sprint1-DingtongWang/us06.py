from datetime import datetime


def divorce_before_death(ind,fam):
    res = True
    for f in fam:
        hus_id = "0"
        wife_id = "0"
        if 'DIV' in fam[f] and 'HUSB' in fam[f] and 'WIFE' in fam[f]:
            hus_id = fam[f]['HUSB']
            wife_id = fam[f]['WIFE']
            divorce_date = datetime.strptime(fam[f]['DIV'],"%d%b%Y")
        if hus_id in ind:
            if 'DEAT' not in ind[hus_id]:
                print('%s is alive and divorced!\n'%hus_id)
            else:
                if divorce_date > datetime.strptime(ind[hus_id]['DEAT'],"%d%b%Y"):
                    print('ERROR:US06,%s:%s death date %d happened beofore divorce %d'%\
                         (fam[f]['DIV_REC'],ind[hus_id],ind[hus_id]['DEAT'],ind[hus_id]['DIV']))
                    res=False
        if wife_id in ind:
            if 'DEAT' not in ind[wife_id]:
                print('%s is alive and divorced!\n'%wife_id)
            else:
                if divorce_date > datetime.strptime(ind[wife_id]['DEAT'],"%d%b%Y"):
                    print('ERROR:US06,%s:%s death date %d happened beofore divorce %d'%\
                         (fam[f]['DIV_REC'],ind[wife_id],ind[wife_id]['DEAT'],ind[wife_id]['DIV']))
                    res=False
    return res

