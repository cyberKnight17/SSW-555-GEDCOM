from datetime import datetime


def mutible_birth(ind, fam):
    """No more than five siblings should be born at the same time"""
    child_birth_dict = {}
    res = True

    for f in fam:
        if 'CHIL' in fam[f]:
            for child_id in fam[f]['CHIL']:
                if child_id in ind:
                    child_birth = datetime.strptime(ind[child_id]['BIRT'],"%d%b%Y")
                    child_birth_dict[child_id] = child_birth

    child_birth_list = list(child_birth_dict.values())
    child_birth_set = set(child_birth_list)

    if len(child_birth_list) - len(child_birth_set) > 3:
        res = False
        print('Error: US14: FAMILY %s have 5 or more children born at the same time'%fam[f]['fam'])

    return res
