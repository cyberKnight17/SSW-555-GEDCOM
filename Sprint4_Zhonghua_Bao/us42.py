def userStory42(result):
    indi,fam = result['indi'],result['fam']
    mess = list()

    for id in fam.keys():
        if 'MARR' in fam[id]:
            if dateVerify(fam[id]['MARR']) == False:
                print("ERROR: FAMILY: US42:",fam[id]['MARR_rec'],":",fam[id]['MARR'],"marriage date is invalid")
                mess.append(fam[id]['MARR'])

        if 'DIV' in fam[id]:
            if dateVerify(fam[id]['DIV']) == False:
                print("ERROR: FAMILY: US42:",fam[id]['DIV_rec'],":",fam[id]['DIV'],"divorce date is invalid")
                mess.append(fam[id]['DIV'])
    
    for id in indi.keys():
        if 'BIRT' in indi[id]:
            if dateVerify(indi[id]['BIRT']) == False:
                print("ERROR: INDIVIDUAL: US42:",indi[id]['BIRT_rec'],":",indi[id]['BIRT'],"birth date is invalid")
                mess.append(indi[id]['BIRT'])
        
        if 'DEAT' in indi[id]:
            if dateVerify(indi[id]['DEAT']) == False:
                print("ERROR: INDIVIDUAL: US42:",indi[id]['DEAT_rec'],":",indi[id]['DEAT'],"death date is invalid")
                mess.append(indi[id]['DEAT'])
    
    return mess

def dateVerify(checkdate):
    day = ('01','02','03','04','05','06','07','08','09','10',
            '11','12','13','14','15','16','17','18','19','20',
            '21','22','23','24','25','26','27','28','29','30','31')
    month = ('JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC')
    res = True

    if type(checkdate) != str:
         res = False
    
    if checkdate[1].isalpha():
        checkdate = '0' + checkdate
    
    date = list()
    date.append(checkdate[0:2])
    date.append(checkdate[2:5])
    date.append(checkdate[5:])
    print(date)

    if date[0] not in day or date[1] not in month:
        res = False
    if date[2].isdecimal() == False: # year should be an integer
        res = False
    if date[0] == '31' and date[1] not in ('JAN','MAR','MAY','JUL','AUG','OCT','DEC'):
        res = False
    if date[0] == '30' and date[1] == 'FEB':
        res = False
    if date[0] == '29' and date[1] == 'FEB' and int(date[2]) % 4 != 0 or ((int(date[2]) % 100 == 0 and int(date[2]) % 400 != 0)):
        res = False
    
    return res
