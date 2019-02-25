from datetime import datetime
from Homework04_Zhonghua_Bao import dateVerify

def userStory01(result):
    """implement user story 01, dates (birth, marriage, divorce, death) should not be after the current date,
       verify the date checked validity, return none if date is invalid, and then compare with current date,
       if it is not later than current date, return true, else return false
    """
    indi,fam = result['indi'],result['fam']   # get the summary of the test ged

    for key in indi.keys():
        if 'BIRT' in indi[key]:   # if indi has birthday, compare with the current date
            if dateVerify(indi[key]['BIRT']) == False:
                birthday = datetime.strptime(indi[key]['BIRT'],'%d%b%Y')
                birth_str = birthday.strftime('%Y-%m-%d')
                print("ERROR: INDIVIDUAL: US01:",indi[key]['BIRT_rec'],":",indi[key]['id'],": Birthday",birth_str,"occurs in the future")
        
        if 'DEAT' in indi[key]:   # if indi has death date, compare with the current date
            if dateVerify(indi[key]['DEAT']) == False:
                death = datetime.strptime(indi[key]['DEAT'],'%d%b%Y')
                death_str = death.strftime('%Y-%m-%d')
                print("ERROR: INDIVIDUAL: US01:",indi[key]['DEAT_rec'],":",indi[key]['id'],": Death",death_str,"occurs in the future")
    
    for key in fam.keys():
        if 'MARR' in fam[key]:   # if fam has marriage date, compare with the current date
            if dateVerify(fam[key]['MARR']) == False:
                marr = datetime.strptime(fam[key]['MARR'],'%d%b%Y')
                marr_str = marr.strftime('%Y-%m-%d')
                print("ERROR: FAMILY: US01:",fam[key]['MARR_rec'],":",fam[key]['fam'],": Marriage",marr_str,"occurs in the future")
        
        if 'DIV' in fam[key]:   # if fam has divorce date, compare with the current date
            if dateVerify(fam[key]['DIV']) == False:
                div = datetime.strptime(fam[key]['DIV'],'%d%b%Y')
                div_str = div.strftime('%Y-%m-%d')
                print("ERROR: FAMILY: US01:",fam[key]['DIV_rec'],":",fam[key]['fam'],": Divorce",div_str,"occurs in the future")
