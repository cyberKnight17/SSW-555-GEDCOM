#list living single
def us31(fam,indi):
    marriedlist=[]
    allpeoplelist=[]
    singlelist=[]
    print('person living and single')
    for i in fam:
        if 'DIV' not in fam[i]:
            marriedlist.append(fam[i]['HUSB'])
            marriedlist.append(fam[i]['WIFE'])
    #get married couple id

    for m in indi:
        allpeoplelist.append(indi[m]['id'])
        singlelist=[item for item in allpeoplelist if item not in marriedlist]
    #get single id
    for x in singlelist:
        print(indi[x]['name'])


