
def unique_id(indi,fam):
    """All individual id and family id should be unique"""
    flag = True
    indi_list =[]
    fam_list=[]

    for i in indi:
        if i in indi_list:
            error = '%s this individual id already exist'%i
            print(error)
            erro_loc = [i]
            flag = False

        else:
            indi_list.append(indi)

    for f in fam:
        if f in fam_list:
            error = '%s this family id already exist'%f
            print(error)
            erro_loc = [i]
            flag = False
        else:
            fam_list.append(f)

    return flag
