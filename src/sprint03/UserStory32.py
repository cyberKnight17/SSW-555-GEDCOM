def userStory32(result):
    """define a function to probe the multiple birth in the family,
       print out any anamoly statement,
       store the problematic family in a list
    """
    indi,fam = result['indi'],result['fam']
    anamoly = list()

    for key in fam.keys():
        tmp = set()
        
        if 'CHIL' in fam[key]:   # only read the family has children
            
            for person in fam[key]['CHIL']:
                birth = indi[person]['BIRT']
                
                if birth in tmp:   # find out the family whose kid has the same birthday
                    print("ANAMOLY: FAMILY: US32:",fam[key]['fam'],"has multiple birth")
                    anamoly.append(fam[key]['fam'])
                    break
                else:
                    tmp.add(birth)
    
    return anamoly