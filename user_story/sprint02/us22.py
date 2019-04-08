
def unique_id(result):
    """All individual id and family id should be unique"""
    flag = True
    indi_list =[]
    fam_list=[]
    indi,fam = result['indi'],result['fam']
    for i in indi.keys():
        if indi[i]['id'] in indi_list:
            error = 'ERROR:US22 %s this individual id already exist'%i
            print(error)
            erro_loc = [i]
            flag = False

        else:
            indi_list.append(indi[i]['id'])

    for f in fam.keys():
        if fam[f]['fam'] in fam_list:
            error = 'ERROR:US22 %s this family id already exist'%f
            print(error)
            erro_loc = [i]
            flag = False
        else:
            fam_list.append(fam[f]['fam'])
            

    return flag
#fam1 = {
#    'F23':{'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
#    'F24': {'fam': 'F23', 'MARR': '12 DEC 2007'},
#    'F25':{'fam':'F23'},
#    'F26':{'fam':'F23'}}
#
#ind1 = {
#'I02': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'}, 
#'I03': {'id': 'I01', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
#'I04': {'id': 'I01', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
#'I01': {'id': 'I01', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
#'I01': {'id': 'I01', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
#'I01': {'id': 'I01', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
#'I01': {'id': 'I01', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}
#  }

