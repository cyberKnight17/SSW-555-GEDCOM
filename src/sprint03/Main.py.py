from datetime import datetime
from prettytable import PrettyTable as pt
import os,sys
#from UserStory08 import userStory08
from sprint01 import us05us03,user0108,user04,user10,us02,us06
#from us05us03 import marrige_before_death
from sprint02 import us12,us13,us09,us22,UserStory11 as us11,UserStory17 as us17,userstory23 as us23,userstory25 as us25
from sprint03 import us35,us24,us15,us27,userstory30,userstory31,UserStory21,UserStory32

valid = {
    '0':(['INDI','FAM'],'HEAD','TRLR','NOTE'),
    '1':('NAME','SEX','BIRT','DEAT','FAMC','FAMS','MARR','HUSB','WIFE','CHIL','DIV'),
    '2':('DATE'),
} # dictionary stores valid tags


def age_cal(indi,birthday): # calculate individual's age = us27
    birthdate = datetime.strptime(birthday, '%d%b%Y')
    current = datetime.today()
    for i in indi:
        if 'DEAT'not in indi[i]:
            return current.year - birthdate.year - ((current.month, current.day) < (birthdate.month, birthdate.day))
        else:
            deathdate = datetime.strptime(indi[i]['DEAT'],'%d%b%Y')
            return deathdate.year - birthdate.year -((deathdate.month, deathdate.day) <(birthdate.month, birthdate.day))


def parse_file(path,encode = 'utf-8'):
    """read the file from the path, based on level and tag scratch the information line by line and store in the dictionary,
       print the summary of individuals and families
    """
    with open(path,'r',encoding=encode) as ged_file:
        isValid = 'N'
        IsIND = True
        indi = {}
        fam = {}
        currentDate = ''
        currentInd = ''
        currentFam = ''
        num = 0

        for line in ged_file:
            num += 1    
            word_list = line.strip().split()
            arguments = ''.join(word_list[2:])
            tag = 'NA'
            level = 'NA'

            # verify each line's validity
            if len(word_list) == 1:
                level = word_list[0]
            elif len(word_list) > 1:
                level = word_list[0]
                tag = word_list[1]

            if len(word_list) == 3 and word_list[0] == '0' and word_list[2] in ('INDI', 'FAM'):
                isValid = 'Y'
                tag = word_list[2]
            elif len(word_list) > 1 and level in valid and tag in valid[level]:
                isValid = 'Y'
            
            if isValid == 'Y':   # only read the valid line
                if level== '0' and tag == 'INDI':
                    currentInd = word_list[1]
                    IsIND = True
                    indi[currentInd] = {'id':word_list[1]}   # key for each individual

                if IsIND:    # information about the individual if true
                    if level == '1' and tag == 'NAME':
                        indi[currentInd]['name'] = arguments   # store name
                    if level == '1' and tag == 'BIRT' or tag == 'DEAT':
                        currentDate = tag 
                    if level == '2' and currentDate != '' and tag == 'DATE':   # store birth date or death date
                        indi[currentInd][currentDate] = arguments
                        indi[currentInd][currentDate+'_rec'] = num   

                    if level == '1' and tag == 'SEX':   # store sex
                        indi[currentInd]['sex'] = arguments   
                    if level == '1' and tag in ('FAMC','FAMS'):   # store family information: child in the family, or spouse in the family
                        if tag in indi[currentInd]:
                            indi[currentInd][tag].add(arguments)
                        else:
                            indi[currentInd][tag] = {arguments}  
   
                if level=='0' and tag == 'FAM':   #  change to information about the family, info for individual is over at here
                    IsIND = False
                    currentFam = word_list[1]
                    fam[currentFam] = {'fam':currentFam}   # store key for the family dictionary
                    
                if IsIND == False:
                    if level == '1' and word_list[1] == 'MARR' or word_list[1] == 'DIV':   # store marriage date and divorce date
                        currentDate = tag
                    if level == '2' and tag == 'DATE':
                        fam[currentFam][currentDate] =arguments
                        fam[currentFam][currentDate+'_rec'] = num
                    if level == '1' and tag in ('HUSB','WIFE'):   # store role in the family, husband or wife
                        fam[currentFam][tag] = arguments
                    if level == '1' and tag == 'CHIL':   # store children in the family
                        if tag in fam[currentFam]:
                            fam[currentFam][tag].add(arguments)
                        else:
                            fam[currentFam][tag] = {arguments}

        # define the schema to print individual table
        indiTable = pt(["ID", "NAME", "Gender", "BDay", "Age", "Death", "Child", "Spouse"])
        for key in indi.keys():
            birth = datetime.strptime(indi[key]['BIRT'],'%d%b%Y')  # print birth date
            birth_str = birth.strftime('%Y-%m-%d')
            
            if 'DEAT' in indi[key]:   # print death date
                death = datetime.strptime(indi[key]['DEAT'],'%d%b%Y')
                death_str = death.strftime('%Y-%m-%d')
            else:
                death_str ='NA'

            if 'FAMC' in indi[key]:
                child = indi[key]['FAMC']
            else:
                child = None
            
            if 'FAMS' in indi[key]:
                spouse = indi[key]['FAMS']
            else:
                spouse = 'NA'

            age = age_cal(indi,indi[key]['BIRT'])
            indiTable.add_row([indi[key]['id'],indi[key]['name'],indi[key]['sex'], birth_str, age, death_str, child, spouse])

        # define the schema to print family table
        famTable =pt(['ID','Married','Divorced','Husband ID','Husband Name','Wife ID','Wife name','Children'])
        for key in fam.keys():
            if 'DIV' in fam[key]:   # print divorce date
                div = datetime.strptime(fam[key]['DIV'],'%d%b%Y')
                div_str = div.strftime('%Y-%m-%d')

            else: 
                div_str = "NA"

            if "HUSB" in fam[key]:   # print husband ID and his name
                hubID = fam[key]['HUSB']
                hubName = indi[hubID]['name']
            else:
                hubID = "NA"
                hubName = "NA"

            if "WIFE" in fam[key]:   # print wife ID and her name
                wifeID = fam[key]['WIFE']
                wifeName = indi[wifeID]['name']
            else:
                wifeID = "NA"
                wifeName = "NA"

            if 'CHIL' in fam[key] :   # print set for children in the family
                chil = fam[key]['CHIL']
            else:
                chil = "NA"

            if 'MARR' in fam[key]:   # print marriage date
                marr = datetime.strptime(fam[key]['MARR'],'%d%b%Y')
                marr_str = marr.strftime('%Y-%m-%d')
            else:
                marr_str = "NA"

            if div_str != 'NA' and marr_str!='NA':
                user04.us04(marr,div,hubName,wifeName)

            #us09
            cnt=0
            if chil != 'NA':
                for i in fam[key]['CHIL']:
                    if 'DEAT' in indi[fam[key]['WIFE']] and indi[fam[key]["WIFE"]]["DEAT"] != 'NA':
                        us09.birth_before_parents_death(indi[i]['name'],i,indi[i]['BIRT'],\
                            indi[fam[key]['WIFE']]['DEAT'],True)
                    elif 'DEAT' in indi[fam[key]['HUSB']] and indi[fam[key]["HUSB"]]["DEAT"]  != 'NA':
                        us09.birth_before_parents_death(indi[i]['name'],i,indi[i]['BIRT'],\
                           indi[fam[key]['HUSB']]['DEAT'],False)
                        indi[fam[key]["HUSB"]]["DEAT"]
                    cnt += 1


            famTable.add_row([key, marr_str, div_str, hubID, hubName, wifeID, wifeName, chil])
        
        #print(indiTable)
        #print(famTable)
        us02.birth_before_marriage(indi,fam)
        us06.divorce_before_death(indi,fam)
        us05us03.check_birth_death(indi)                    
        us05us03.marrige_before_death(indi,fam)
        user10.marrAfter14(fam,indi)
        user04.us04(marr_str,div_str,hubName,wifeName)
        us12.parents_not_too_old(indi,fam)
        us13.siblings_spacing(indi,fam) 
        us23.usstory23(indi)
        us25.usstory25(fam,indi)    
        us35.print_recent_births(indi)
        us24.unique_families_by_spouses(indi,fam)
        us15.fewer_than_15_siblings(fam)
        userstory30.us30(fam,indi)
        userstory31.us31(fam,indi)

    return {'fam':fam,'indi':indi}


if __name__ == '__main__':
    r = parse_file('D:\workspace\sprint02\sprint2-GEDCOM-Input-file')
    #r1 =parse_file('D:\workspace\sprint02\My-Family-27-Jan-2019-230.ged')
    #r2=parse_file('D:\workspace\sprint02\Project03-TestFile.ged')
    #r3=parse_file(r'D:\workspace\GED_file\test.ged\sprint01.ged')
    user0108.userStory01(r)   
    user0108.userStory08(r)
    us11.userStory11(r)
    us17.userStory17(r)
    us22.unique_id(r)
    UserStory21.userStory21(r)
    UserStory32.userStory32(r)


       
