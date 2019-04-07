def userStory17(result):
    """define a function to find out any people who marry to their parents,
       print the info when the people is found
    """
    indi,fam = result['indi'],result['fam']

    for key in indi.keys():
        check = str()   # storing the checked people's parent
        
        # look for the individual whose famc and fams are both valid.
        if 'FAMC' in indi[key] and 'FAMS' in indi[key]:
            for item in list(indi[key]['FAMS']):
                if indi[key]['sex'] == 'M':
                    for c in indi[key]['FAMC']:
                        check = fam[c]['WIFE']   # get his mother
                        if fam[item]['WIFE'] == check:   # determine whether his mother is his wife
                            print("ERROR: INDIVIDUAL: US17:",indi[key]['id'],"marrys to his mother")
                
                elif indi[key]['sex'] == 'F':
                    for c in indi[key]['FAMC']:
                        check = fam[c]['HUSB']   # get his father
                        if fam[item]['HUSB'] == check:   # determine whether his father is his wife
                            print("ERROR: INDIVIDUAL: US17:",indi[key]['id'],"marrys to her father")