from datetime import datetime


def fewer_than_15_siblings(fam):
    """There should be fewer than 15 siblings in a family"""
    res = True

    for f in fam:

        if 'CHIL' in fam[f]:
            if len(fam[f]['CHIL']) > 15:
                print('ERROR: FAMILY: US15: %s: There are more than 15 siblings in family %s' % (fam[f]['fam_rec'],f))
                res = False

    return res
