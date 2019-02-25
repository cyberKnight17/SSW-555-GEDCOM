from datetime import datetime


def divorce_before_death(indi):  # us06
    res = True

    for i in indi:
        if "DIV" in indi[i] and "DEAT" in indi[i]:
            divorceday = datetime.strptime(indi[i]["DIV"], '%d%b%Y')
            deathday = datetime.strptime(indi[i]['DEAT'], '%d%b%Y')

            if divorceday > deathday:
                warnin = 'ERROR death of individual %s comes before divorcing.' % i
                print(warnin)
                # file.write(warnin)
                res = False

    return res

