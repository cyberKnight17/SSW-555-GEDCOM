from datetime import datetime


def parents_not_too_old(ind, fam):
    """us12 Mother should be less than 60 years older than her children and father should be less than 80 years older
       than his children"""
    res = True
    for f in fam:

        if 'HUSB' in fam[f] and 'WIFE' in fam[f] and 'CHIL' in fam[f]:
            hus_id = fam[f]['HUSB']
            wife_id = fam[f]['WIFE']

            if hus_id in ind and wife_id in ind:

                for child_id in fam[f]['CHIL']:

                    if child_id in ind:
                        child_birth = datetime.strptime(ind[child_id]['BIRT'],"%d%b%Y")
                        hus_birth = datetime.strptime(ind[hus_id]['BIRT'],"%d%b%Y")
                        wife_birth = datetime.strptime(ind[wife_id]['BIRT'],"%d%b%Y")
                        interval_hus_child = child_birth - hus_birth
                        interval_wife_child = child_birth - wife_birth

                        if interval_hus_child.days/365 > 80:
                            res = False
                            print('ERROR:US12, %s, %s: %s is more than 80 years older then his child %s' %
                                  (hus_id, child_id, hus_id, child_id))

                        if interval_wife_child.days/365 > 60:
                            res = False
                            print('ERROR:US12, %s, %s: %s is more than 60 years older then his child %s'%
                                  (wife_id, child_id, wife_id, child_id))

    return res