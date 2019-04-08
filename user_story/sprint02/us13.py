from datetime import datetime


def siblings_spacing(ind, fam):
    """us13 Birth dates of siblings should be more than 8 months apart or less than 2 days apart
        (twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)"""
    child_birth_dict = {}
    res = True

    for f in fam:

        if 'HUSB' in fam[f] and 'WIFE' in fam[f] and 'CHIL' in fam[f]:
            hus_id = fam[f]['HUSB']
            wife_id = fam[f]['WIFE']

            if hus_id in ind and wife_id in ind:

                for child_id in fam[f]['CHIL']:

                    if child_id in ind:
                        child_birth = datetime.strptime(ind[child_id]['BIRT'],"%d%b%Y")
                        child_birth_dict[child_id] = child_birth

    for key1 in child_birth_dict.keys():
        for key2 in child_birth_dict.keys():
            interval = child_birth_dict[key1] - child_birth_dict[key2]
            if interval.days/30 < 8 and interval.days > 2:
                print('ERROR:US13, %s, %s: Birth dates of siblings should be more than 8 months apart '
                      'or less than 2 days apart' % (key1, key2))
                res = False

    return res

fam2 = {'F23':
	{'fam': 'F23', 'MARR': '14FEB1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30'],'MARR_rec': '1'}}
ind2 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL1700', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23SEP1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '25FEB1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13FEB1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13FEB1981', 'sex': 'F', 'family': 'F23'}}

siblings_spacing(ind2, fam2)