from datetime import datetime


def birth_before_marriage(indi):  # us02
    res = True

    for i in indi:
        if "BIRT" in indi[i] and "MARR" in indi[i]:
            birthday = datetime.strptime(indi[i]["BIRT"], '%d%b%Y')
            marriageday = datetime.strptime(indi[i]['MARR'], '%d%b%Y')

            if birthday > marriageday:
                warnin = 'ERROR marriage of individual %s comes before birth.' % i
                print(warnin)
                # file.write(warnin)
                res = False

    return res

