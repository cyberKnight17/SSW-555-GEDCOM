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
                print('ERROR: FAMILY: US13: %s: %s, %s: Birth dates of siblings should be more than 8 months apart '
                      'or less than 2 days apart' % (fam[f]['fam_rec'], key1, key2))
                res = False

    return res