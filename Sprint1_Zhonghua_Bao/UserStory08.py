from datetime import datetime
from datetime import timedelta
from Homework04_Zhonghua_Bao import dateVerify,dateCompare

def userStory08(result):
    """implementing user story 08, the child birthday should not be earlier the parent's marriage date, and not be later than 9 months after the parent's divorce date if applicable
       only apply to those clear date, not to any 'NA'
       get this two date from the summary of ged, if wrong, print error statement
    """
    indi,fam = result['indi'],result['fam']

    for key in fam.keys():
        if 'CHIL' in fam[key]:   # only applicable to family has child, or it will raise keyerror
            for item in fam[key]['CHIL']:   # get the kid iterately    
                if 'BIRT' not in indi[item]:
                    continue
                else:
                    if 'MARR' not in fam[key]:
                        continue
                    else:
                        if dateCompare(indi[item]['BIRT'],fam[key]['MARR']) == False:   # child birthday earlier than parent's marriage date
                            birth = datetime.strptime(indi[item]['BIRT'],'%d%b%Y')
                            birth_str = birth.strftime('%Y-%m-%d')
                            marr = datetime.strptime(fam[key]['MARR'],'%d%b%Y')
                            marr_str = marr.strftime('%Y-%m-%d')
                            print("ANOMALY:FAMILY: US08:",fam[key]['MARR_rec'],":",key,": Child",indi[item]['id'],"born",birth_str,"before marriage on",marr_str)
                    
                    if 'DIV' not in fam[key]:
                        continue
                    else:
                        div = datetime.strptime(fam[key]['DIV'],'%d%b%Y')
                        expire = div + timedelta(days=272)   # add 9 months to divorce date
                        expire_day = expire.strftime('%d%b%Y').upper()
                        
                        if expire_day.startswith('0'):   # string use 01 for 1, for later comparison without error, skip 0
                            expire_day = expire_day[1:]
                                               
                        if dateCompare(indi[item]['BIRT'],expire_day) == True:
                            birth = datetime.strptime(indi[item]['BIRT'],'%d%b%Y')
                            birth_str = birth.strftime('%Y-%m-%d')
                            div_str = div.strftime('%Y-%m-%d')
                            print("ANOMALY:FAMILY: US08:",fam[key]['DIV_rec'],":",key,": Child",indi[item]['id'],"born",birth_str,"after divorce on",div_str)
                