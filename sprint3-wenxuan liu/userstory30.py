#list living married
def us30(fam,indi):
    print('person living and married')
    marriedlist=[]
    for i in fam:
        if 'DIV' not in fam[i]:
            marriedlist.append(fam[i]['HUSB'])
            marriedlist.append(fam[i]['WIFE'])
    #get married couple id
    for m in marriedlist:
        if 'DEAT' not in indi[m]:
            print(indi[m]['name'])



