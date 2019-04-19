# List recent survivors
import datetime


def us37(fam, indi):
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
                        husid = fam[c]['HUSB']
                        wifeid = fam[c]['WIFE']
                        husname = indi[husid]['name']
                        wifename = indi[wifeid]['name']
                        namelist.append(husname)
                        namelist.append(wifename)
                        namelist.remove(name)
                        chilid = fam[c]['CHIL']
                        chilnamelist = []
                        for p in chilid:
                            chilname = indi[p]['name']
                            chilnamelist.append(chilname)
                        chilname = ','.join(chilnamelist)
                        print('US37:', name, 'died in the last 30 days, spouse:', ' '.join(namelist), ' descendant: ',
                              chilname)
                    except:
                        KeyError
                        print('US37:', name, 'died in the last 30 days, spouse:', ' '.join(namelist), ' descendant: ',
                              'no child')
