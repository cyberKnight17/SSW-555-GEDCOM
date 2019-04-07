def userStory21(result):
    """define a function to probe the wrong gender for the role in the family,
       print out any anamoly statement,
       store the problematic person in a list
    """
    indi,fam = result['indi'],result['fam']
    anamoly = list()

    for key in fam.keys():
        check_husb = fam[key]['HUSB']   # check the husband in the family
        check_wife = fam[key]['WIFE']   # check the wife in the family
        
        if indi[check_husb]['sex'] == 'F':   # find the problematic father
            if check_husb in anamoly:
                continue
            else:
                anamoly.append(check_husb)
                print("ERROR: INDIVIDUAL: US21:", check_husb, "should be a male.")
        
        if indi[check_wife]['sex'] == 'M':   # find the problematic mother
            if check_wife in anamoly:
                continue
            else:
                anamoly.append(check_wife)
                print("ERROR: INDIVIDUAL: US21:", check_wife, "should be a female.")
    
    return anamoly