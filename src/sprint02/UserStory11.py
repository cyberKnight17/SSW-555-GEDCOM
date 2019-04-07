import os,sys
p = os.path.dirname(__file__)
sys.path.append(p)
from Homework05_Zhonghua_Bao import periodCompare

def userStory11(result):
    """define a function to find out all the bigamy individual in the gem document,
       get all the people who marrys more than one time, and compare the marr and div date in each marriage,
       print the people when bigamy happened
    """
    indi,fam = result['indi'],result['fam']

    for key in indi.keys():
        if 'FAMS' in indi[key]:
            if len(indi[key]['FAMS']) > 1:   # find people who marrys more than one time
                marr_exp = list(indi[key]['FAMS'])  # change to list variarion
                
                for i in range(len(marr_exp)-1):
                    for j in range(i+1,len(marr_exp)):

                        # get any two marriage's marry and divorce date, then find whether is there any overlap
                        if 'MARR' in fam[marr_exp[i]]:
                            dt1 = fam[marr_exp[i]]['MARR']
                        else:
                            dt1 = None
                        
                        if 'DIV' in fam[marr_exp[i]]:
                            dt2 = fam[marr_exp[i]]['DIV']
                        else:
                            dt2 = None
                        
                        if 'MARR' in fam[marr_exp[j]]:
                            dt3 = fam[marr_exp[j]]['MARR']
                        else:
                            dt3 = None
                        
                        if 'DIV' in fam[marr_exp[j]]:
                            dt4 = fam[marr_exp[j]]['DIV']
                        else:
                            dt4 = None
                        
                        if periodCompare(dt1,dt2,dt3,dt4) == False:
                            print("ERROR: INDIVIDUAL: US11:",indi[key]['id'],": marrys to other people at the same time.")