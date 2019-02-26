from datetime import datetime

def check_birth_death(indi): #us03 
    res = True

    for i in indi:
        if "BIRT" in indi[i] and "DEAT" in indi[i]:
            birthday = datetime.strptime(indi[i]["BIRT"],'%d%b%Y')
            deathday = datetime.strptime(indi[i]['DEAT'],'%d%b%Y')
            #marri_date = datetime.strptime(indi[i]['MARR'],'%d%b%Y')
    
            if birthday > deathday:
                warnin = ('ERROR:US03,%s:%s death date %d happened beofore birthdate %d'%\
                         (indi[i]['DEAT_rec'],indi[i],indi[i]['DEAT'],indi['BIRT']))
                print(warnin)
                #file.write(warnin)
                res = False
        
    return res

#ind1 = {'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13FEB1998', 'sex': 'F', 'family': 'F23','DEAT': '31DEC2013','MARR':'15MAR2016'},}

#s= check_birth_death_marri(ind1)




def marrige_before_death(ind,fam):
    res = True
    for f in fam:
        hus_id = "0"
        wife_id = "0"
        if 'MARR' in fam[f] and 'HUSB' in fam[f] and 'WIFE' in fam[f]:
            hus_id = fam[f]['HUSB']
            wife_id = fam[f]['WIFE']
            marr_date = datetime.strptime(fam[f]['MARR'],"%d%b%Y")
        if hus_id in ind:
            if 'DEAT' not in ind[hus_id]:
                print('%s is alive and married!\n'%hus_id)
            else:
                if marr_date > datetime.strptime(ind[hus_id]['DEAT'],"%d%b%Y"):
                    print('ERROR:US05,%s:%s death date %d happened beofore marrige %d'%\
                         (fam[f]['MARR_rec'],ind[hus_id],ind[hus_id]['DEAT'],ind[hus_id]['MARR']))
                    res=False 
        if wife_id in ind:
            if 'DEAT' not in ind[wife_id]:
                print('%s is alive and married!\n'%wife_id)
            else:
                if marr_date > datetime.strptime(ind[wife_id]['DEAT'],"%d%b%Y"):
                    print('ERROR:US05,%s:%s death date %d happened beofore marrige %d'%\
                         (fam[f]['MARR_rec'],ind[wife_id],ind[wife_id]['DEAT'],ind[wife_id]['MARR']))
                    res=False
    return res
