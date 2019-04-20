# List recent survivors
import datetime


def us37(fam, indi):
    ######used to test #### list1 used to test spouse
    list1 = []
    #################
    for i in indi:
        # find dead peole
        if 'DEAT' in indi[i]:
            deathdate = indi[i]['DEAT']
            now = datetime.datetime.now()
            flag = now - datetime.datetime.strptime(deathdate, '%d%b%Y')
            if flag <= datetime.timedelta(days=30):
                name = indi[i]['name']

                family = indi[i]['FAMS']
                for c in family:
                    try:
                        namelist = []
                        hus_id = fam[c]['HUSB']
                        wife_id = fam[c]['WIFE']
                        husname = indi[hus_id]['name']
                        wifename = indi[wife_id]['name']
                        namelist.append(husname)
                        namelist.append(wifename)
                        namelist.remove(name)
                        list1.append(' '.join(namelist))
                        chilid = fam[c]['CHIL']

                        chilnamelist = []
                        for p in chilid:
                            chilname = indi[p]['name']

                            chilnamelist.append(chilname)
                        chilname = ','.join(chilnamelist)
                        print('US37:', name, 'died in the last 30 days, spouse:', ' '.join(namelist), ' descendant: ',
                              chilname)
                    except KeyError:

                        print('US37:', name, 'died in the last 30 days, spouse:', ' '.join(namelist), ' descendant: ',
                              'no child')
    return list1

